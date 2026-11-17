# SDEV 1001 - Game Leaderboard Exercise

## Why is this important?

You'll often get data from a file and need to show it to someone. Printing data in neat columns by hand is fiddly: you have to work out widths, pad every value and draw the lines yourself. Someone has already solved this. [`tabulate`](https://pypi.org/project/tabulate/) is a popular package that turns a list of rows into a tidy text table in one function call.

The skill is the same as last time: **create a virtual environment, install the package, read its docs, and use it**.

## Best Practices

- Follow the PEP-8 Style guide for writing Python code https://peps.python.org/pep-0008/
- Name the files and functions exactly as described in the exercise.
- Never commit your `venv` folder. The `.gitignore` in this repo already ignores it.

## Instructions

### Part 1: Set up your environment

1. Open this folder in VS Code and open a terminal.
2. Create a virtual environment called `venv`, then activate it. You should see `(venv)` at the start of your prompt.
3. Install the `tabulate` package with pip.
4. Save your dependencies to `requirements.txt` with `pip freeze`.
   - Check that `requirements.txt` only has one or two lines. If it has a long list of packages, your venv wasn't active when you ran `pip freeze`.
5. Run `git status` and make sure `venv` is **not** listed, then commit.

---

### Part 2: Load the scores from a CSV file

The game scores are in `game_scores.csv`:

```text
Title,Platform,Score
Elden Ring,PC,95
No Man's Sky,PC,90
...
```

Edit `leaderboard.py`:

1. Complete `load_scores(file_name)` so it opens the CSV file and **returns** a list of rows, where each row is a list.
   - Use the `csv` module (it's already imported at the top of the file). Check your notes from the CSV lesson.
   - Keep the header row as the first row: `["Title", "Platform", "Score"]`.
   - Every value in a CSV file comes in as text. Convert each game's **Score** to an `int` so `"95"` becomes `95`.

When you're done, `load_scores("game_scores.csv")` should return:

```python
[
    ["Title", "Platform", "Score"],
    ["Elden Ring", "PC", 95],
    ["No Man's Sky", "PC", 90],
    ...
]
```

Run the Part 2 tests, then commit.

---

### Part 3: Make a table

Open the [tabulate page on PyPI](https://pypi.org/project/tabulate/) and read the **Usage** and **Table format** sections. You need to find the function that builds a table, how to give it headers, and how to pick a table style.

1. Import `tabulate` at the top of the file.

2. Complete `make_table(rows, headers, style)` so it **returns** (not prints) a table of `rows`, with `headers` as the column names, in the given `style`.

3. Complete `main()` so it:
- loads the scores from `GAME_SCORES_FILE` using `load_scores()`
- splits them into the headers (the first row) and the game rows (everything after it). Hint: list slicing.
- asks the user `Pick a table style (grid, github, simple, fancy_grid): `
- prints the game rows as a table in the style they picked, using `make_table()`

4. Run `python leaderboard.py` from this folder, try a few styles, then commit.

#### Sample desired output

```text
Pick a table style (grid, github, simple, fancy_grid): grid
+----------------+------------+---------+
| Title          | Platform   |   Score |
+================+============+=========+
| Elden Ring     | PC         |      95 |
+----------------+------------+---------+
| No Man's Sky   | PC         |      90 |
+----------------+------------+---------+
| Stardew Valley | Switch     |      89 |
+----------------+------------+---------+
| Hades          | Switch     |      88 |
+----------------+------------+---------+
| Cyberpunk 2077 | PS5        |      82 |
+----------------+------------+---------+
| Gollum         | PS5        |      43 |
+----------------+------------+---------+
```

Notice that `tabulate` lines the numbers up on the right for you.

---

### Part 4: Number the rows

A leaderboard needs a rank. `tabulate` can add a column of row numbers for you, so you don't have to put the numbers in your data. Look in the docs for the option that shows a row index.

1. Complete `make_leaderboard(rows, headers)` so it **returns** a table in the `github` style with the rows numbered **starting at 1** (not 0).
   - Hint: by default the numbering starts at 0. The docs show that you can give it your own list of numbers. `range()` can help here.

2. At the end of `main()`, print a blank line and then the leaderboard for the game rows.

3. Run `python leaderboard.py` again, then commit.

#### Sample desired output (after the first table)

```text
|    | Title          | Platform   |   Score |
|----|----------------|------------|---------|
|  1 | Elden Ring     | PC         |      95 |
|  2 | No Man's Sky   | PC         |      90 |
|  3 | Stardew Valley | Switch     |      89 |
|  4 | Hades          | Switch     |      88 |
|  5 | Cyberpunk 2077 | PS5        |      82 |
|  6 | Gollum         | PS5        |      43 |
```

---

### Stretch (optional)

- Type a style that doesn't exist, like `turkey`. `tabulate` doesn't crash: it quietly uses the `simple` style instead. Find the list of every style name in the docs, then check the user's choice against it. If it isn't on the list, print `Style not found, using simple` before the table.
- Add a few of your own favourite games to the bottom of `game_scores.csv`. Then sort the rows by score (highest first) before printing the leaderboard, so it stays in the right order no matter how the file is ordered. This is why you converted Score to an `int`: try sorting the scores as text and see what goes wrong with a score like `100`.

When you're done working, run `deactivate`.

---

## Checking your work

This exercise isn't graded. The tests are there to give you feedback.

After you push, click the ✓ or ✗ next to your latest commit on GitHub (or open the **Actions** tab) to see which parts pass. Click a failing part to read its error message.

## Running the Automated Tests Locally

- Make sure your venv is active, then type this command (exclude the .py from the filename):
```bash
python -m automated-tests-do-not-touch.<name_of_test_file>
```
- So if you wanted to execute the part_one.py file, run this command:
```bash
python -m automated-tests-do-not-touch.part_one
```
- Your current working directory must be the top folder of this repo.
- GitHub installs packages from **your** `requirements.txt` before running the tests. If `tabulate` isn't in it, Parts 3 and 4 will fail on GitHub even if they work on your computer.

## What the tests check

| Part | What the tests check |
| --- | --- |
| Part 1 | `requirements.txt` lists `tabulate` |
| Part 2 | `load_scores()` returns the header row plus one list per game, with Score as an `int` (tested on a different CSV file too) |
| Part 3 | `make_table()` returns the right table, and `main()` prints the games from `game_scores.csv` in the chosen style |
| Part 4 | `make_leaderboard()` returns a `github` table numbered from 1, and `main()` prints it |
