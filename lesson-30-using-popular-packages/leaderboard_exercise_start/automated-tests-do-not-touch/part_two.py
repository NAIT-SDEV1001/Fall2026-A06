from .helpers import load_module, read_csv_rows

TEST_FILE = "automated-tests-do-not-touch/testing_game_scores.csv"


def test_load_scores():
    module = load_module("leaderboard.py")
    result = module["load_scores"](TEST_FILE)
    expected = read_csv_rows(TEST_FILE)
    assert result is not None, (
        "load_scores should return the rows, not print them"
    )
    assert len(result) == len(expected), (
        f"load_scores should return {len(expected)} rows "
        "(the header row plus one row per game)"
    )
    assert result[0] == expected[0], (
        "The first row should be the header row: ['Title', 'Platform', 'Score']"
    )
    for row in result[1:]:
        assert isinstance(row[2], int), (
            "The Score in each game row should be converted to an int"
        )
    assert result == expected, (
        "load_scores didn't return the rows from the file. "
        "Check that each row is a list like ['Tetris', 'Game Boy', 89]"
    )


def test_load_scores_uses_file_name():
    module = load_module("leaderboard.py")
    result = module["load_scores"]("game_scores.csv")
    assert result == read_csv_rows("game_scores.csv"), (
        "load_scores should read whichever file name it's given"
    )


if __name__ == "__main__":
    test_load_scores()
    test_load_scores_uses_file_name()
    # if the above fail they will make the output not successful and throw an error.
    print("successful output")
