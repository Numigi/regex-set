# © 2020 - today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from typing import List
import re

task_number_from_tag_regex = re.compile(r"(^|\s+)(?P<task_tag>[Tt][Aa]#?(?P<id>\d+))(\s+|$)")


def task_numbers_from_tag(text: str, ids=None) -> List[str]:
    ids = ids or []
    no_parentheses = re.sub(r"([()])", " ", text)
    res = re.search(task_number_from_tag_regex, no_parentheses)
    # I can't find a way to make it work with findall or finditer
    # so here is a recursive way.
    if res:
        group_dict = res.groupdict()
        ids.append(group_dict["id"])
        task = group_dict["task_tag"]
        sub_text = re.sub(task, " ", text)
        ids = task_numbers_from_tag(sub_text, ids)
    return ids
