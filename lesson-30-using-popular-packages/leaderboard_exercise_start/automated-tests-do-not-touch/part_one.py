import os
from .helpers import read_text_file


def test_requirements_has_tabulate():
    assert os.path.exists("requirements.txt"), (
        "requirements.txt not found. Run: pip freeze > requirements.txt"
    )
    lines = read_text_file("requirements.txt").lower().splitlines()
    package_names = [line.split("==")[0].strip() for line in lines]
    assert "tabulate" in package_names, (
        "tabulate is missing from requirements.txt. "
        "Activate your venv, install it, then run pip freeze again"
    )


if __name__ == "__main__":
    test_requirements_has_tabulate()
    # if the above fail they will make the output not successful and throw an error.
    print("successful output")
