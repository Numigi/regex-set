# © 2020 - today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

import pytest

from odoo_regex_set import task


@pytest.mark.parametrize(
    "input_,expected",
    [
        ("TA#6789", ["6789"]),
        ("TA#1234 TA#4567", ["1234", "4567"]),
        ("TA#1234 TA#4567 ta0987", ["0987", "1234", "4567"]),
        ("(TA#6890 TA#4567)", ["4567", "6890"]),
        (
                """
        TA#1234
        TA#4567
        ta0987
        """,
                ["0987", "1234", "4567"]
        )  # multilines,
    ]
)
def test_find_ids_found(input_, expected):
    """ Test the function accepts any numbers of tags"""
    assert task.find_ids(input_) == expected


@pytest.mark.parametrize(
    "input_",
    [
        "",  # empty string
    ]
)
def test_find_ids_empty(input_):
    assert not task.find_ids(input_)


