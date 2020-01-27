# © 2020 - today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
import re

task_details_from_tag_regex = re.compile(
    r"(^|\s+)(?P<task_tag>[Tt][Aa]#?(?P<id>\d+))(\s+|$)"
)


def find_task_details(text: str) -> (str, str):
    no_parentheses = re.sub(r"([()])", " ", text)
    res = re.search(task_details_from_tag_regex, no_parentheses)

    if res:
        group_dict = res.groupdict()
        return group_dict["id"], group_dict["task_tag"]

    return "", ""


def remove_task_from_text(text: str, task_tag: str) -> str:
    return re.sub(task_tag, "", text)
