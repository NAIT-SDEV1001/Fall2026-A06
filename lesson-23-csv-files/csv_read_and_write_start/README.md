# Reading and Writing CSV Files

## Why is this important?

CSV (Comma-Separated Values) files are everywhere in data science, analytics, and day-to-day programming. They store tabular data in a simple text format that almost every program can read — Excel, Google Sheets, databases, and of course Python. Being able to read, transform, and write CSV files is a fundamental skill for any programmer who works with data.

CSV files are structured in a row/column format, similar to the structure of spreadsheets. The first row is known as the "header row" that contains the name of all of the columns. Each row after that is an actual record of our data. Each column is distinguised by using commas to separate them.

## What are we going to do?

We're going to build a small data analysis app around a fictional dataset of music artists. The CSV contains 10 bands with columns for `band_name`, `members`, `year_formed`, `biggest_hit`, and `monthly_listeners`.

Along the way we'll:
- Read a CSV file into a list of dictionaries
- Filter rows using a list comprehension
- Sort the data by any column (numeric or text)
- Write results to a new CSV file
- Update the original CSV with a calculated column

> **Heads up:** In the previous lesson we learned how to use `pathlib` to build file paths that anchor to the script's location instead of the current working directory. We'll use the same `Path(__file__).parent / ...` pattern from the start of this lesson so the program runs correctly no matter where you launch it from.

## Steps

### 1. Let's open the music artists CSV and read the contents.

CSV files are easy to work with in Python thanks to the built-in `csv` module. 

Let's create a `read_artists` function that opens the file and reads each row into a dictionary, then returns the full list.

```python
import csv


def read_artists(file_path):
    """Read the music artists data from a CSV file."""
    all_artists = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for artist in reader:
                all_artists.append(artist)
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
    return all_artists
```

Let's break down the code:
- We import the built-in `csv` module.
- We use `with open(...)` to open the file in read mode (`'r'`) with `encoding='utf-8'` — the same UTF-8 encoding pattern we learned in the previous lesson.
- We wrap the read in a `try`/`except FileNotFoundError` so the program prints a friendly message instead of crashing if the file is missing.
- `csv.DictReader(file)` reads each row as a dictionary, using the column headers as the keys. So instead of getting `['The Velvet Echoes', '4', '2008', ...]` for each row, we get `{'band_name': 'The Velvet Echoes', 'members': '4', 'year_formed': '2008', ...}` — much easier to work with.
- We loop through the reader and append each row to our `all_artists` list, then return it.

> **Important:** `DictReader` reads every value as a **string**, even numeric columns like `members` and `monthly_listeners`. We'll need to convert those to integers later when we want to sort or do math with them.

### 2. Let's create the `main` function and run it.

Now we'll add a `main()` function that reads the CSV and prints all the artists using `pprint` (which formats dictionaries in a much more readable way than `print`).

```python
import csv
from pathlib import Path
from pprint import pprint


# ... read_artists function ...


def main():
    data_dir = Path(__file__).parent / 'data'
    file_path = data_dir / 'music_artists.csv'
    artists = read_artists(file_path)
    print(f"All artists from {file_path.name}:\n")
    pprint(artists)


if __name__ == "__main__":
    main()
```

We build `data_dir` once (anchored to the script's location) and then derive `file_path` from it. We'll reuse `data_dir` later when we write our own CSV files into the same folder. The `print` uses `file_path.name` so the header shows just the filename rather than the full absolute path.

Run the script with `python music_analysis_app.py` and you should see all 10 artists printed as a list of dictionaries:

```
All artists from music_artists.csv:

[{'band_name': 'The Velvet Echoes',
  'biggest_hit': 'Midnight Drive',
  'members': '4',
  'monthly_listeners': '12500000',
  'year_formed': '2008'},
 {'band_name': 'Crimson Tide Theory',
  'biggest_hit': 'Burning Skies',
  'members': '3',
  'monthly_listeners': '8200000',
  'year_formed': '2015'},
 ...
]
```

Notice that every value is a string — even the numbers. That's the trade-off `DictReader` makes for simplicity. We'll handle the conversion as needed in the next few steps.

### 3. Let's filter the data using a list comprehension.

Often we don't want every row — we want a subset. A **list comprehension** is a compact way to build a new list from an existing one, optionally filtered by a condition.

Let's write a function that returns only the artists with at least a certain number of monthly listeners.

```python
def filter_by_min_listeners(artists, minimum):
    """Return only the artists with at least `minimum` monthly listeners."""
    return [
        artist
        for artist in artists
        if int(artist['monthly_listeners']) >= minimum
    ]
```

Let's break this down:
- The square brackets `[...]` mean we're building a new list.
- `for artist in artists` loops through every artist (the same as a regular `for` loop).
- `if int(artist['monthly_listeners']) >= minimum` is the filter — we keep only the artists whose listener count meets the threshold.
- We call `int(...)` because `monthly_listeners` is a string when it comes out of the CSV; comparing strings to numbers wouldn't work the way we expect.

Now update `main()` to print how many artists meet a threshold:

```python
def main():
    data_dir = Path(__file__).parent / 'data'
    file_path = data_dir / 'music_artists.csv'
    artists = read_artists(file_path)
    print(f"All artists from {file_path.name}:\n")
    pprint(artists)

    popular = filter_by_min_listeners(artists, 10_000_000)
    print(f"\n{len(popular)} artists have over 10,000,000 monthly listeners.")
```

> Python lets you write large numbers with underscores like `10_000_000` to make them easier to read. It's the same as `10000000`.

Run the script and you should see:

```
5 artists have over 10,000,000 monthly listeners.
```

### 4. Let's sort the data by a column.

Python's built-in `sorted()` function can sort a list of dictionaries if we tell it which value to sort by. We do that with a **key function** — a function that takes one item from the list and returns the value to sort on.

There's a subtlety though: some of our columns are numbers (`members`, `year_formed`, `monthly_listeners`) and some are text (`band_name`, `biggest_hit`). Since `DictReader` returns everything as strings, we need to convert the numeric columns to integers before sorting — otherwise `'9300000'` would sort *after* `'12500000'` because string comparison goes character by character.

Let's keep a list of which columns are numeric at the top of the file, then write a sort function that uses it:

```python
NUMERIC_COLUMNS = ['members', 'year_formed', 'monthly_listeners']


def sort_artists_by(artists, column, reverse=True, top_n=5):
    """Sort the artists by a column and return the top N."""

    def get_value(artist):
        if column in NUMERIC_COLUMNS:
            return int(artist[column])
        else:
            return artist[column]

    sorted_artists = sorted(artists, key=get_value, reverse=reverse)
    return sorted_artists[:top_n]
```

Let's break it down:
- `NUMERIC_COLUMNS` is a constant (uppercase by convention) listing the columns that should be treated as numbers.
- `get_value` is a helper function defined *inside* `sort_artists_by`. It takes one artist (a dictionary) and returns the value to sort by — converted to `int` if the column is numeric, or left as a string otherwise.
- `sorted(artists, key=get_value, reverse=reverse)` does the actual sorting. The `key` parameter tells `sorted()` how to extract the sort value from each item; `reverse=True` sorts highest-to-lowest.
- Finally, we slice off the top N results with `sorted_artists[:top_n]`.

Update `main()` to print the top 5 artists by `monthly_listeners`:

```python
def main():
    data_dir = Path(__file__).parent / 'data'
    file_path = data_dir / 'music_artists.csv'
    artists = read_artists(file_path)

    column = 'monthly_listeners'
    top_artists = sort_artists_by(artists, column)
    print(f"Top 5 artists by {column}:\n")
    for index, artist in enumerate(top_artists):
        rank = index + 1
        print(f"{rank}. {artist['band_name']} - {artist[column]}")
```

Run the script:

```
Top 5 artists by monthly_listeners:

1. Neon Foxes - 22750000
2. Glass Harbor - 18400000
3. Iron Compass - 15900000
4. The Velvet Echoes - 12500000
5. Static Bloom - 11200000
```

### 5. Let's simplify the sort with a `lambda`.

Defining a whole `get_value` function just to grab one value feels heavy. Python has a feature called a **`lambda` function** — a tiny anonymous function you can write inline. It's perfect for short throwaway functions like our sort key.

Here's the same `sort_artists_by` function using a `lambda`:

```python
def sort_artists_by(artists, column, reverse=True, top_n=5):
    """Sort the artists by a column and return the top N."""
    if column in NUMERIC_COLUMNS:
        key = lambda artist: int(artist[column])
    else:
        key = lambda artist: artist[column]

    sorted_artists = sorted(artists, key=key, reverse=reverse)
    return sorted_artists[:top_n]
```

So we replaced this:

```python
    def get_value(artist):
        if column in NUMERIC_COLUMNS:
            return int(artist[column])
        else:
            return artist[column]
```

with two one-line lambdas:

```python
    if column in NUMERIC_COLUMNS:
        key = lambda artist: int(artist[column])
    else:
        key = lambda artist: artist[column]
```

A `lambda` is just a function without a name. It takes any arguments (here, `artist`) and returns the result of a single expression (here, `int(artist[column])` or `artist[column]`). Lambdas are common in Python whenever you need to pass a small "how do I get this value" function to something like `sorted()`, `filter()`, or `map()`.

### 6. Let's make the program interactive.

Right now we've hardcoded the column to sort by. Let's let the user pick one at runtime by listing the available columns and reading their choice with `input()`.

```python
def main():
    data_dir = Path(__file__).parent / 'data'
    file_path = data_dir / 'music_artists.csv'
    artists = read_artists(file_path)

    print(f"All artists from {file_path.name}:\n")
    pprint(artists)

    # Let the user choose which column to sort by
    columns = list(artists[0].keys())
    print("\nAvailable columns to sort by:")
    for index, column in enumerate(columns):
        print(f"{index + 1}. {column}")

    choice = int(input("Enter the number of the column you want to sort by: ")) - 1
    selected_column = columns[choice]

    top_artists = sort_artists_by(artists, selected_column)
    print(f"\nTop 5 artists by {selected_column}:\n")
    for index, artist in enumerate(top_artists):
        rank = index + 1
        print(f"{rank}. {artist['band_name']} - {artist[selected_column]}")
```

We grab the column names from the keys of the first artist (`artists[0].keys()`), print them with a number, and ask the user to pick. We subtract `1` from their choice because lists are zero-indexed but humans count from 1.

Now you can sort by any column — try `1` for `band_name` (alphabetical), `3` for `year_formed`, or `5` for `monthly_listeners`.

### 7. Let's write our results to a new CSV file.

So far we've only *read* CSV files. To write one, we use `csv.DictWriter` — the writing counterpart to `DictReader`.

```python
def write_top_artists(file_path, artists):
    """Write a list of artist dictionaries to a CSV file."""
    fieldnames = list(artists[0].keys())
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for artist in artists:
            writer.writerow(artist)
```

Let's break this down:
- We pull the `fieldnames` (column headers) from the keys of the first artist. `DictWriter` needs to know the order of the columns.
- We open the file in write mode (`'w'`) with `encoding='utf-8'` — same as before.
- **`newline=''` is required when writing CSV files in Python.** Without it, you'll get extra blank rows between every record on Windows. Always pass it when writing CSVs.
- `csv.DictWriter(file, fieldnames=fieldnames)` creates the writer. The `fieldnames` argument tells it which columns to write and in what order.
- `writer.writeheader()` writes the header row (`band_name,members,year_formed,...`).
- `writer.writerow(artist)` writes one row for each dictionary in our list.

Now add a call at the end of `main()` to export the user's top artists. We reuse `data_dir` from earlier so the new file lands in the same `data/` folder as the source CSV:

```python
    write_top_artists(data_dir / 'top_artists.csv', top_artists)
    print("\nSaved the top artists to data/top_artists.csv")
```

Run the program, pick a column, and then open `data/top_artists.csv` in a text editor or Excel — you should see your top 5 artists saved out.

### 8. Let's update the original CSV by adding a calculated column.

A common pattern is **read–modify–write**: load a CSV, change something, then save it back. Let's add a `listeners_per_member` column that divides each band's monthly listeners by their member count.

```python
def add_listeners_per_member(file_path):
    """Read the CSV, add a listeners_per_member column, and write it back."""
    artists = read_artists(file_path)
    for artist in artists:
        listeners = int(artist['monthly_listeners'])
        members = int(artist['members'])
        artist['listeners_per_member'] = round(listeners / members)
    write_top_artists(file_path, artists)
```

Let's break it down:
- We read the file into a list of dictionaries (reusing our `read_artists` function).
- We loop through each artist and add a new key `listeners_per_member` to the dictionary, calculated from the two existing columns.
- We call `write_top_artists(file_path, artists)` to write everything back — including the new column — to the **same** file path. This **overwrites** the original CSV.

Since `DictWriter` uses `artists[0].keys()` for the field names, the new `listeners_per_member` column automatically becomes part of the output header. Running this function is also idempotent — if you run it twice, the second run just recomputes the same value and overwrites with the same result.

Add this to the end of `main()`:

```python
    add_listeners_per_member(file_path)
    print("Added a listeners_per_member column to data/music_artists.csv")
```

Run the program once, then open `data/music_artists.csv` — you'll see a new column at the end:

```
band_name,members,year_formed,biggest_hit,monthly_listeners,listeners_per_member
The Velvet Echoes,4,2008,Midnight Drive,12500000,3125000
Crimson Tide Theory,3,2015,Burning Skies,8200000,2733333
...
```

## Challenge

1. Add a new function called `oldest_artists(artists, top_n=3)` that returns the `top_n` bands with the earliest `year_formed` (use your existing `sort_artists_by` function with `reverse=False`).
2. Add a filter function called `filter_by_members(artists, exact_count)` that returns only the artists with exactly that many band members.
3. Combine the two: filter the data to only 3-member bands, then export them to `data/three_member_bands.csv` using `write_top_artists`.

## Conclusion

Reading and writing CSV files is a fundamental skill in data analysis and programming. In this lesson we read a CSV with `csv.DictReader`, filtered rows with a list comprehension, sorted by any column using `sorted()` (with a key function and then a `lambda`), and wrote results back out with `csv.DictWriter`. We also covered the read–modify–write pattern for updating an existing CSV in place. These same building blocks scale up to much larger datasets — the only thing that changes is the data.

