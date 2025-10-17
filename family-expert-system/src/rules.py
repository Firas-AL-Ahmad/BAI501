import sys
import os

# Add the project root to sys.path for direct execution
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

"""
This module defines the logical rules for family relationships using PyDatalog.
It includes base rules for parent-child relationships and a basic sibling rule.
"""
from typing import List, Tuple, Dict
from pyDatalog import pyDatalog

# Declare terms specific to rules defined in this module
pyDatalog.create_terms('P1, P2, grandparent, grandchild, uncle, aunt, cousin, GP, GC, U, A, C')

# Terms are created globally by src.facts when it's imported.
# We import them directly from src.facts.
from src.facts import X, Y, P, father, mother, parent, child, son, daughter, is_male, is_female, sibling

def define_family_rules() -> None:
    """
    Declares PyDatalog terms and defines logical rules for family relationships.
    """
    # Base rule: parent(X, Y) <= father(X, Y) | mother(X, Y)
    parent(X, Y) <= father(X, Y)
    parent(X, Y) <= mother(X, Y)

    # Derived rules for child, son, daughter
    child(X, Y) <= parent(Y, X)
    son(X, Y) <= child(X, Y) & is_male(X)
    daughter(X, Y) <= child(X, Y) & is_female(X)

    # Basic sibling rule: sibling(X, Y) <= (parent(P, X) & parent(P, Y) & (X != Y))
    sibling(X, Y) <= (parent(P, X) & parent(P, Y) & (X != Y))

    # Extended family rules
    grandparent(X, Y) <= parent(X, P) & parent(P, Y)
    grandchild(X, Y) <= grandparent(Y, X)
    uncle(X, Y) <= sibling(X, P) & parent(P, Y) & is_male(X)
    aunt(X, Y) <= sibling(X, P) & parent(P, Y) & is_female(X)
    cousin(X, Y) <= parent(P1, X) & parent(P2, Y) & sibling(P1, P2) & (X != Y)

def sample_queries() -> Dict[str, List]:
    """
    Runs a few example queries on the PyDatalog knowledge base.
    Assumes facts have already been registered.

    Returns:
        A dictionary containing results of sample queries as sorted lists/tuples.
    """
    # Query for children of John
    children_of_john_results = pyDatalog.ask('child(X, "John")')
    children_of_john = sorted(set([str(r[0]) for r in children_of_john_results.answers])) if children_of_john_results else []

    # Query for all sons (son, parent) tuples
    all_sons_results = pyDatalog.ask('son(X, Y)')
    all_sons = sorted(list(set([(str(r[0]), str(r[1])) for r in all_sons_results.answers]))) if all_sons_results else []

    # Query for all daughters (daughter, parent) tuples
    all_daughters_results = pyDatalog.ask('daughter(X, Y)')
    all_daughters = sorted(list(set([(str(r[0]), str(r[1])) for r in all_daughters_results.answers]))) if all_daughters_results else []

    # Query for all grandchildren of John
    all_grandchildren_of_john_results = pyDatalog.ask('grandchild(X, "John")')
    all_grandchildren_of_john = sorted(set([str(r[0]) for r in all_grandchildren_of_john_results.answers])) if all_grandchildren_of_john_results else []

    # Query for all uncles of Kevin
    all_uncles_of_kevin_results = pyDatalog.ask('uncle(X, "Kevin")')
    all_uncles_of_kevin = sorted(set([str(r[0]) for r in all_uncles_of_kevin_results.answers])) if all_uncles_of_kevin_results else []

    # Query for all aunts of Kevin
    all_aunts_of_kevin_results = pyDatalog.ask('aunt(X, "Kevin")')
    all_aunts_of_kevin = sorted(set([str(r[0]) for r in all_aunts_of_kevin_results.answers])) if all_aunts_of_kevin_results else []

    # Query for all cousins of Sarah
    all_cousins_of_sarah_results = pyDatalog.ask('cousin(X, "Sarah")')
    all_cousins_of_sarah = sorted(set([str(r[0]) for r in all_cousins_of_sarah_results.answers])) if all_cousins_of_sarah_results else []

    return {
        "children_of_john": children_of_john,
        "all_sons": all_sons,
        "all_daughters": all_daughters,
        "all_grandchildren_of_john": all_grandchildren_of_john,
        "all_uncles_of_kevin": all_uncles_of_kevin,
        "all_aunts_of_kevin": all_aunts_of_kevin,
        "all_cousins_of_sarah": all_cousins_of_sarah,
    }

if __name__ == "__main__":
    from src.facts import load_facts_into_pydatalog, CSV_FILEPATH

    print(f"Loading facts from: {CSV_FILEPATH}")
    load_facts_into_pydatalog(CSV_FILEPATH)

    print("\nDefining family rules...")
    define_family_rules()

    print("\nRunning sample queries:")
    results = sample_queries()

    print("\nChildren of John:")
    for c in results["children_of_john"]:
        print(f"- {c}")

    print("\nAll Sons (Son, Parent):")
    for s, p in results["all_sons"]:
        print(f"- {s} is son of {p}")

    print("\nAll Daughters (Daughter, Parent):")
    for d, p in results["all_daughters"]:
        print(f"- {d} is daughter of {p}")

    print("\nAll Grandchildren of John:")
    for gc in results["all_grandchildren_of_john"]:
        print(f"- {gc}")

    print("\nAll Uncles of Kevin:")
    for u in results["all_uncles_of_kevin"]:
        print(f"- {u}")

    print("\nAll Aunts of Kevin:")
    for a in results["all_aunts_of_kevin"]:
        print(f"- {a}")

    print("\nAll Cousins of Sarah:")
    for c in results["all_cousins_of_sarah"]:
        print(f"- {c}")
