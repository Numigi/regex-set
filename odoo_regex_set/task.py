# © 2020 - today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from typing import List

from odoo_regex_set import task_tools


def find_ids(text: str, ids=None) -> List[str]:
    ids = ids or set([])
    id_, task_tag = task_tools.find_task_details(text)

    if id_:
        ids.add(id_)
        cleaned_text = task_tools.remove_task_from_text(text, task_tag)
        ids = find_ids(cleaned_text, ids)

    return sorted(list(ids))
