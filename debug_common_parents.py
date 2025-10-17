import sys
import os
from pyDatalog import pyDatalog

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "family-expert-system"))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.facts import load_facts_into_pydatalog, CSV_FILEPATH, has_common_mother, has_common_father, X, Y, P, F, M
from src.rules import define_family_rules, half_sibling, full_sibling, parent, father, mother

pyDatalog.clear()
load_facts_into_pydatalog(CSV_FILEPATH)
define_family_rules()

print("\n--- Debugging common parents for Tom and Michael ---")

# Check has_common_father
result_common_father = pyDatalog.ask('has_common_father("Tom", "Michael")')
print(f"has_common_father(Tom, Michael): {result_common_father}")

# Check has_common_mother
result_common_mother = pyDatalog.ask('has_common_mother("Tom", "Michael")')
print(f"has_common_mother(Tom, Michael): {result_common_mother}")

# Check full_sibling
result_full_sibling = pyDatalog.ask('full_sibling("Tom", "Michael")')
print(f"full_sibling(Tom, Michael): {result_full_sibling}")

# Check half_sibling
result_half_sibling = pyDatalog.ask('half_sibling("Tom", "Michael")')
print(f"half_sibling(Tom, Michael): {result_half_sibling}")

print("\n--- Debugging half_uncle('Tom', 'Kevin') ---")
result_half_uncle = pyDatalog.ask('half_uncle("Tom", "Kevin")')
print(f"half_uncle(Tom, Kevin): {result_half_uncle}")
