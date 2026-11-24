# FastAPI Models and Validation

## Why is this important?

At the end of the last lesson we had a POST endpoint that looked like this:

```python
@app.post("/add_research_station", status_code=201)
def add_research_station(
    name: str = Body(...),
    location: str = Body(...),
) -> dict:
    if not name or not location:
        raise HTTPException(status_code=400, detail="Name and location are required")
    ...
```

This works for two fields, but it doesn't scale. Every new field means another `Body(...)` parameter, and any validation rule beyond "is it present?" turns into more hand-written `if` statements.

In this lesson we'll see how **Pydantic models** let us:

- Describe the shape of a request body once, in a single class.
- Get **automatic validation** (required fields, types, length constraints, and more) without writing any `if` statements.
- Make the auto-generated `/docs` page significantly more useful — it now shows the exact schema clients are expected to send.

## What are we going to do?

We're going to refactor the `/add_research_station` endpoint to use a Pydantic model called `ResearchStation`, then add field constraints and an optional field.

[Pydantic Docs](https://docs.pydantic.dev/latest/) — the library FastAPI uses under the hood

## Steps

### 1. Recap: virtual environment, install, and run

1. Create the virtual environment, and activate it:
```bash
python -m venv ./venv
.\venv\Scripts\activate # Or source ./venv/bin/activate on macOS/Linux
```
2. Install FastAPI with the standard extras:
```bash
pip install "fastapi[standard]"
```
3. Save the dependencies to a requirements file:
```bash
pip freeze > requirements.txt
```
4. Run the application:
```bash
fastapi dev ufo_app.py
```

### 2. Define your first Pydantic model

**Pydantic** is a Python library for describing data with classes and automatically validating that real data matches the description. FastAPI uses it under the hood for everything related to request and response bodies.

> **Note:** Pydantic is already installed — it comes with `fastapi[standard]` as a dependency, so there's no separate install needed.

A Pydantic model is just a Python class that inherits from `BaseModel`. Each class attribute becomes a field in the model, with a type hint that says what kind of value it accepts.

1. Add a new import at the top of `ufo_app.py`:
```python
from pydantic import BaseModel
```

2. Define a `ResearchStation` model class. Add this near the top of the file, after your imports and `app = FastAPI()`:
```python
class ResearchStation(BaseModel):
    name: str
    location: str
```

This is a Pydantic model. It says: "a research station has a `name` (string) and a `location` (string)." We haven't used it yet; that's the next step.

### 3. Use the model in the POST endpoint

Right now, our POST endpoint declares each body field as its own parameter:
```python
@app.post("/add_research_station", status_code=201)
def add_research_station(
    name: str = Body(...),
    location: str = Body(...),
) -> dict:
    if not name or not location:
        raise HTTPException(status_code=400, detail="Name and location are required")
    ...
```

We can replace all of that with a single parameter typed as our new model. We can also remove the `if` validation because Pydantic handles that for us.

```python
@app.post("/add_research_station", status_code=201)
def add_research_station(station: ResearchStation) -> dict:
    with open("data/research_stations.csv", mode="a", newline="", encoding="utf-8") as file:
        fieldnames = ["name", "location"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({"name": station.name, "location": station.location})
    return {"message": "Research station added successfully"}
```

Some things to notice:

- Our parameter `station` had been typed with the Pydantic Model `ResearchSation`. FastAPI sees the Pydantic model as the type hint and knows this parameter is the entire request body.
- The `name` and `location` fields are now accessed as attributes on the model using `station.name` and `station.location`. They behave just like any other Python attribute.
- The manual `if not name or not location:` check is gone. Pydantic enforces that `name` and `location` are present and are strings — if they're missing or the wrong type, the request is rejected automatically before our function even runs.

Because Pydantic now handles validation, we can remove the imports we no longer need. Update your `fastapi` import to drop `Body` and `HTTPException`:
```python
from fastapi import FastAPI
```

### 4. See what we gained

Restart your server (or let `fastapi dev` reload) and visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

Click `POST /add_research_station`, then **Try it out**. Notice that the request body editor now shows the full schema:
```json
{
  "name": "string",
  "location": "string"
}
```

The `/docs` page knows the shape of the body because Pydantic told it.

<!-- TODO: add screenshot of /docs with Pydantic schema → images/docs_pydantic_schema.png -->

Try a few requests and see what Pydantic catches for free:

1. **Missing field** — send `{"name": "Test Lab"}` (no `location`). Pydantic returns a `422 Unprocessable Entity` with a body like:
   ```json
   {
     "detail": [
       {
         "loc": ["body", "location"],
         "msg": "Field required",
         "type": "missing"
       }
     ]
   }
   ```
2. **Wrong type** — send `{"name": 123, "location": "Earth"}`. Pydantic rejects it because `name` isn't a string.

Compare this to lesson 2: we were writing `if not name or not location:` checks by hand. Pydantic now does this based purely on the type hints on the model.

### 5. Stronger validation with `Field(...)` and optional fields

The model so far accepts any non-empty string for `name` and `location`. Let's tighten it up by:

- Requiring `name` and `location` to be at least 2 characters long.
- Adding an **optional** `notes` field for free-form text.

1. Update the import to bring in `Field`:
```python
from pydantic import BaseModel, Field
```

2. Update the model:
```python
class ResearchStation(BaseModel):
    name: str = Field(..., min_length=2)
    location: str = Field(..., min_length=2)
    notes: str | None = None
```

Unpacking the new bits:

- **`Field(..., min_length=2)`** — the `...` (literal three dots, called *Ellipsis* in Python) marks the field as required. `min_length=2` adds a constraint Pydantic will check on every request. There are many more constraints available — see the [Body - Fields docs](https://fastapi.tiangolo.com/tutorial/body-fields/) for the full list.
- **`notes: str | None = None`** — this is the standard Python way of saying "this is optional." The type is "either a string or `None`," and the default is `None`. Since the field has a default value, clients can omit it entirely.

3. We're now collecting a third field, so update `data/research_stations.csv` to include a `notes` column. The file should now look like this (existing rows have an empty `notes` value):
```csv
name,location,notes
Aerial Phenomena Research Lab,Nevada USA,
Deep Space Materials Institute,Alberta Canada,
Dan's alien research lab,Alberta Canada,
```

4. Update the POST endpoint to write the `notes` field too:
```python
@app.post("/add_research_station", status_code=201)
def add_research_station(station: ResearchStation) -> dict:
    with open("data/research_stations.csv", mode="a", newline="", encoding="utf-8") as file:
        fieldnames = ["name", "location", "notes"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({
            "name": station.name,
            "location": station.location,
            "notes": station.notes or "",
        })
    return {"message": "Research station added successfully"}
```
- `station.notes or ""` writes an empty string when the client omits `notes` (so every row in the CSV has the same shape).

5. Test it from the `/docs` page:

   - Send `{"name": "x", "location": "Mars"}` — rejected, because `name` fails the `min_length=2` rule. Pydantic's error message tells you exactly which field and why.
   - Send `{"name": "Mars Base Alpha", "location": "Mars"}` — accepted, with `notes` defaulting to `None`/empty string in the CSV.
   - Send `{"name": "Mars Base Alpha", "location": "Mars", "notes": "Established 2042"}` — accepted, with the notes written to the CSV.

## Exercises

1. Add a required `country` field to `ResearchStation` (with `min_length=2`) and write it to a new column in `data/research_stations.csv`.
2. Define a separate Pydantic model called `Message` with a single `message: str` field, and use it as the **return type** of `add_research_station`. (Hint: the return value already matches that shape.)
3. Apply Pydantic models to the `/space_organizations` POST endpoint from the previous lesson's exercises.

## Summary

In this lesson you learned how to:

- Define a Pydantic model with `BaseModel` to describe the shape of a request body.
- Replace multiple `Body(...)` parameters with a single typed model parameter.
- Let Pydantic handle required fields and type checking — no more hand-written `if` statements.
- Add field constraints (`min_length`, etc.) with `Field(...)`.
- Declare optional fields using `str | None = None`.
- See the resulting schema show up automatically in the `/docs` page.

Pydantic models are the foundation of every serious FastAPI application — once you start describing your data with classes, almost everything else (validation, docs, IDE auto-complete) follows from it.
