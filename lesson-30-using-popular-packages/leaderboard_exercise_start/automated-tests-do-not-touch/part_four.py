from tabulate import tabulate
from .helpers import load_module, read_csv_rows, run_file_with_patches

ROWS = [["Tetris", "Game Boy", 89], ["Pong", "Arcade", 70], ["Myst", "PC", 65]]
HEADERS = ["Title", "Platform", "Score"]


def test_make_leaderboard():
    module = load_module("leaderboard.py")
    result = module["make_leaderboard"](ROWS, HEADERS)
    expected = tabulate(
        ROWS, headers=HEADERS, tablefmt="github", showindex=[1, 2, 3]
    )
    assert result is not None, (
        "make_leaderboard should return the table, not print it"
    )
    assert result == expected, (
        "make_leaderboard didn't match. It should use the 'github' style and "
        "number the rows starting at 1 (look for showindex in the docs)"
    )


def test_main_prints_leaderboard():
    output = run_file_with_patches("leaderboard.py", ["simple"])
    scores = read_csv_rows("game_scores.csv")
    rows = scores[1:]
    expected = tabulate(
        rows,
        headers=scores[0],
        tablefmt="github",
        showindex=range(1, len(rows) + 1),
    )
    for line in expected.splitlines():
        assert line.rstrip() in output, (
            "main() should also print the leaderboard after the first table"
        )


if __name__ == "__main__":
    test_make_leaderboard()
    test_main_prints_leaderboard()
    # if the above fail they will make the output not successful and throw an error.
    print("successful output")
