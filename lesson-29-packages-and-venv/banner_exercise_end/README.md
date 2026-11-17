# SDEV 1001 - Banner Maker Exercise

## Why is this important?

You'll often need a package you've never seen before. The skill is the same every time: **create a virtual environment, install the package, read its docs, and use it**. In this exercise you'll do that on your own with a package we haven't used in class: [`pyfiglet`](https://pypi.org/project/pyfiglet/), which turns text into big ASCII art banners.

## Best Practices

- Follow the PEP-8 Style guide for writing Python code https://peps.python.org/pep-0008/
- Name the files and functions exactly as described in the exercise.
- Never commit your `venv` folder. The `.gitignore` in this repo already ignores it.

## Instructions

### Part 1: Set up your environment

1. Open this folder in VS Code and open a terminal.
2. Create a virtual environment called `venv`, then activate it. Check your notes from class if you've forgotten the commands. You should see `(venv)` at the start of your prompt.
3. Install the `pyfiglet` package with pip.
4. Save your dependencies to `requirements.txt` with `pip freeze`.
5. Run `git status` and make sure `venv` is **not** listed, then commit.

---

### Part 2: Make a banner

Open the [pyfiglet page on PyPI](https://pypi.org/project/pyfiglet/) and read the usage section. You need to find the function that turns text into a banner, and how to pick a font.

Edit `banner.py`:

1. Import `pyfiglet` at the top of the file.

2. Complete `make_banner(text, font)` so it **returns** (not prints) the banner for `text` in the given `font`.

3. Complete `main()` so it:
- asks the user `What's your name? `
- asks the user `Pick a font (slant, banner, bubble, digital): `
- prints a banner that says `Hi <name>` in the font they picked, using `make_banner()`

4. Run `python banner.py`, try a few fonts, then commit.

#### Sample desired output

```text
What's your name? Sam
Pick a font (slant, banner, bubble, digital): slant
    __  ___    _____
   / / / (_)  / ___/____ _____ ___
  / /_/ / /   \__ \/ __ `/ __ `__ \
 / __  / /   ___/ / /_/ / / / / / /
/_/ /_/_/   /____/\__,_/_/ /_/ /_/
```

---

### Stretch (optional)

- pyfiglet comes with over 500 fonts. Find out how to list them all in the docs, and print the list when the program starts.
- Type a font that doesn't exist, like `turkey`. Your program crashes with a `FontNotFound` error. Use `try`/`except` to print `Font not found, using standard` and show the banner in the `standard` font instead.

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
- GitHub installs packages from **your** `requirements.txt` before running the tests. If `pyfiglet` isn't in it, Part 2 will fail on GitHub even if it works on your computer.

## What the tests check

| Part | What the tests check |
| --- | --- |
| Part 1 | `requirements.txt` lists `pyfiglet` |
| Part 2 | `make_banner()` returns the right banner, and `main()` prints `Hi <name>` in the chosen font |
