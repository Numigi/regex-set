# © 2020 - today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

import pytest
from src.odoo import task


@pytest.mark.parametrize(
    "input_,expected",
    [
        ("TA#6789", ["6789"]),
        ("TA#1234 TA#4567", ["1234", "4567"]),
        ("TA#1234 TA#4567 ta0987", ["1234", "4567", "0987"]),
        ("ta#6752", ["6752"]),
        ("TA6785", ["6785"]),
        ("ta6751", ["6751"]),
        ("Some text TA#6787 followed by some text", ["6787"]),
        ("(TA#6752)", ["6752"]),
        ("(TA#6890 TA#4567)", ["6890", "4567"]),
        ("Une phrase avec le tag suivi par un point TA#6754", ["6754"])
    ]
)
def test_task_numbers_from_tag(input_, expected):
    assert task.task_numbers_from_tag(input_) == expected


@pytest.mark.parametrize(
    "input_",
    [
        "⁣TA#6789⁣",  # invisble spaces
        "6TA#5678",  # a number before the tag
        "tt#5678",  # not the correct tag
        "sometextnospaceTA#5678nospace",  # the tag with some text around without any spaces
        "TA#4567nospace",  # the tag followed by some text without space
        "34567TA4567nospace",  # some numbers a tag and some text after
        "3456TA#3456",  # some numbers then a tag
        "56789-TA#4567-45678",  # tag surrounded by -
        "4567-TA#4567$sometext"  # tag surrounded by special characters
        "^⁣TA#5647"  # tag with a special character before
    ]
)
def test_task_numbers_from_tag_wrong(input_):
    assert not task.task_numbers_from_tag(input_)
