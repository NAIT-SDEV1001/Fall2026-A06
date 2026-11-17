from tabulate import tabulate
from .helpers import load_module, read_csv_rows, run_file_with_patches

ROWS = [["Tetris", "Game Boy", 89], ["Pong", "Arcade", 70]]
HEADERS = ["Title", "Platform", "Score"]


def test_make_table():
    module = load_module("leaderboard.py")
    result = module["make_table"](ROWS, HEADERS, "grid")
    expected = tabulate(ROWS, headers=HEADERS, tablefmt="grid")
    assert result is not None, (
        "make_table should return the table, not print it"
    )
    assert result == expected, (
        "make_table(rows, headers, 'grid') didn't match tabulate's grid "
        "table. Check that you're passing the headers and the style"
    )


def test_main_prints_table():
    output = run_file_with_patches("leaderboard.py", ["fancy_grid"])
    scores = read_csv_rows("game_scores.csv")
    expected = tabulate(scores[1:], headers=scores[0], tablefmt="fancy_grid")
    for line in expected.splitlines():
        assert line.rstrip() in output, (
            "main() should print the games from game_scores.csv as a table "
            "in the style the user picked"
        )


if __name__ == "__main__":
    test_make_table()
    test_main_prints_table()
    # if the above fail they will make the output not successful and throw an error.
    print("successful output")
