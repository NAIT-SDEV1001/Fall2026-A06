from io import StringIO
from unittest.mock import patch
import csv
import runpy
import sys


def read_text_file(file_name):
    with open(file_name, "rb") as file:
        raw = file.read()
    if raw.startswith((b"\xff\xfe", b"\xfe\xff")):
        return raw.decode("utf-16")
    return raw.decode("utf-8-sig")


def read_csv_rows(file_name):
    with open(file_name, "r", newline="") as file:
        rows = list(csv.reader(file))
    header = rows[0]
    games = [[title, platform, int(score)] for title, platform, score in rows[1:]]
    return [header] + games


def load_module(file_name):
    return runpy.run_path(file_name, run_name="student_module")


def run_file_with_patches(file_name, user_input_patches=None):
    if user_input_patches is None:
        user_input_patches = []
    captured_output = StringIO()
    sys.stdout = captured_output
    try:
        with patch("builtins.input", side_effect=user_input_patches):
            runpy.run_path(file_name, run_name="__main__")
    finally:
        sys.stdout = sys.__stdout__
    return captured_output.getvalue()
