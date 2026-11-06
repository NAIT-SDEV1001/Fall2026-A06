import pyfiglet
from .helpers import load_module, run_file_with_patches


def test_make_banner():
    module = load_module("banner.py")
    result = module["make_banner"]("Hi", "slant")
    expected = pyfiglet.figlet_format("Hi", font="slant")
    assert result is not None, "make_banner should return the banner, not print it"
    assert result == expected, (
        "make_banner('Hi', 'slant') didn't match pyfiglet's slant banner. "
        "Check that you're using the font argument"
    )


def test_main_prints_banner():
    output = run_file_with_patches("banner.py", ["Sam", "banner"])
    expected = pyfiglet.figlet_format("Hi Sam", font="banner")
    for line in expected.splitlines():
        if line.strip():
            assert line.rstrip() in output, (
                "main() should print a banner of 'Hi <name>' in the chosen font"
            )


if __name__ == "__main__":
    test_make_banner()
    test_main_prints_banner()
    # if the above fail they will make the output not successful and throw an error.
    print("successful output")
