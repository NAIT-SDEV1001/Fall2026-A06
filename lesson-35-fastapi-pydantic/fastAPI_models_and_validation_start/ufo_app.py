import csv
from fastapi import FastAPI, Body, HTTPException
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def home() -> str:
    return """
    <html>
        <head>
            <title>UFO Sightings</title>
        </head>
        <body>
            <h1>Welcome to the UFO Sightings API</h1>
            <p>Use the /sightings route to get UFO sighting data.</p>
        </body>
    </html>
    """


def load_ufo_data(filepath: str) -> list[dict]:
    sightings = []
    with open(filepath, mode="r", encoding="utf-8") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            sightings.append(row)
    return sightings


@app.get("/ufo_sightings")
def get_sightings(
    country: str = "",
    page: int = 1,
    per_page: int = 10,
) -> list[dict]:
    sightings = load_ufo_data("data/scrubbed.csv")
    if country:
        sightings = [s for s in sightings if s["country"].lower() == country.lower()]
    start = (page - 1) * per_page
    end = start + per_page
    return sightings[start:end]


@app.get("/research_stations")
def get_research_stations() -> list[dict]:
    stations = []
    with open("data/research_stations.csv", mode="r", encoding="utf-8") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            stations.append(row)
    return stations


@app.post("/add_research_station", status_code=201)
def add_research_station(
    name: str = Body(...),
    location: str = Body(...),
) -> dict:
    if not name or not location:
        raise HTTPException(status_code=400, detail="Name and location are required")
    with open("data/research_stations.csv", mode="a", newline="", encoding="utf-8") as file:
        fieldnames = ["name", "location"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({"name": name, "location": location})
    return {"message": "Research station added successfully"}
