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
pyDatalog.create_terms('P1, P2, grandparent, grandchild, uncle, aunt, cousin, GP, GC, U, A, C, '
                       'full_sibling, half_sibling, brother, sister, '
                       'grandfather, grandmother, great_grandparent, ancestor, descendant, '
                       'first_cousin, second_cousin, cousin_degree, '
                       'mother_in_law, father_in_law, brother_in_law, sister_in_law, '
                       'son_in_law, daughter_in_law, sibling_in_law, niece_in_law, nephew_in_law, '
                       'step_parent, step_child, step_sibling, step_grandparent, '
                       'adoptive_parent, biological_parent, multiple_marriages, half_uncle, step_cousin, '
                       'adoptive_father, adoptive_mother, '
                       'D, Z, S, SP, M, F, G, A, B, C_node, D1, D2, P_spouse, P_child, P_parent, P_step, P_adoptive, P_biological, P_multiple, P_half_uncle, P_step_cousin, '
                       'M1, M2, F1, F2, M_X, M_Y, F_X, F_Y, shares_father, shares_mother, M_of_X, M_of_Y, F_of_X, F_of_Y') # Added M_of_X, M_of_Y, F_of_X, F_of_Y

# Terms are created globally by src.facts when it's imported.
# We import them directly from src.facts.
from src.facts import X, Y, P, father, mother, parent, child, son, daughter, is_male, is_female, spouse, sibling, adoptive_father, adoptive_mother, M1, M2, F1, F2, M_X, M_Y, F_X, F_Y, shares_father, shares_mother, M_of_X, M_of_Y, F_of_X, F_of_Y

def define_family_rules() -> None:
    """
    Declares PyDatalog terms and defines logical rules for family relationships.
    """
    # Q1.2 Base rule: parent(X, Y) <= father(X, Y) | mother(X, Y) | adoptive_father(X, Y) | adoptive_mother(X, Y)
    parent(X, Y) <= father(X, Y)
    parent(X, Y) <= mother(X, Y)
    parent(X, Y) <= adoptive_father(X, Y)
    parent(X, Y) <= adoptive_mother(X, Y)

    # Q2.1 Derived rules for child, son, daughter
    child(X, Y) <= parent(Y, X)
    son(X, Y) <= child(X, Y) & is_male(X)
    daughter(X, Y) <= child(X, Y) & is_female(X)

    # Q3.1 Sibling Logic
    # Basic sibling rule: sibling(X, Y) <= (parent(P, X) & parent(P, Y) & (X != Y))
    sibling(X, Y) <= (parent(P, X) & parent(P, Y) & (X != Y))

    # Helper rules for sharing parents
    shares_mother(X, Y) <= mother(M_of_X, X) & mother(M_of_Y, Y) & (M_of_X == M_of_Y) & (X != Y)
    shares_father(X, Y) <= father(F_of_X, X) & father(F_of_Y, Y) & (F_of_X == F_of_Y) & (X != Y)

    full_sibling(X, Y) <= shares_father(X, Y) & shares_mother(X, Y)
    # Half-siblings share one parent but not both
    half_sibling(X, Y) <= shares_father(X, Y) & ~shares_mother(X, Y)
    half_sibling(X, Y) <= shares_mother(X, Y) & ~shares_father(X, Y)
    brother(X, Y) <= sibling(X, Y) & is_male(X)
    sister(X, Y) <= sibling(X, Y) & is_female(X)

    # Q4.1 Ancestry and Descendants
    grandparent(X, Y) <= parent(X, P) & parent(P, Y)
    grandchild(X, Y) <= grandparent(Y, X) # Added for direct grandchild query
    grandfather(X, Y) <= grandparent(X, Y) & is_male(X)
    grandmother(X, Y) <= grandparent(X, Y) & is_female(X)
    great_grandparent(X, Y) <= grandparent(X, P) & parent(P, Y) # X is grandparent of P, P is parent of Y
    ancestor(X, Y) <= parent(X, Y)
    ancestor(X, Y) <= parent(X, P) & ancestor(P, Y)
    descendant(X, Y) <= ancestor(Y, X)

    # Q5.1 Extended Family rules
    uncle(X, Y) <= sibling(X, P) & parent(P, Y) & is_male(X)
    aunt(X, Y) <= sibling(X, P) & parent(P, Y) & is_female(X)
    first_cousin(X, Y) <= parent(P1, X) & parent(P2, Y) & sibling(P1, P2) & (X != Y)
    second_cousin(X, Y) <= parent(P1, X) & parent(P2, Y) & first_cousin(P1, P2) & (X != Y)

    # General cousin relationship (recursive)
    cousin(X, Y) <= first_cousin(X, Y)
    cousin(X, Y) <= parent(P1, X) & parent(P2, Y) & cousin(P1, P2) & (X != Y)

    # Cousin degree (needs more complex logic, will simplify for now)
    # For now, we will skip cousin_degree as it requires more advanced PyDatalog features or a different approach.

    # Q6.2 Spouse and In-law Logic
    mother_in_law(X, Y) <= spouse(Y, P) & mother(X, P)
    father_in_law(X, Y) <= spouse(Y, P) & father(X, P)
    brother_in_law(X, Y) <= spouse(Y, P) & brother(X, P)
    brother_in_law(X, Y) <= sibling(X, P) & spouse(P, Y) & is_male(X)
    sister_in_law(X, Y) <= spouse(Y, P) & sister(X, P)
    sister_in_law(X, Y) <= sibling(X, P) & spouse(P, Y) & is_female(X)
    son_in_law(X, Y) <= spouse(X, P) & child(P, Y) & is_male(X)
    daughter_in_law(X, Y) <= spouse(X, P) & child(P, Y) & is_female(X)
    sibling_in_law(X, Y) <= brother_in_law(X, Y)
    sibling_in_law(X, Y) <= sister_in_law(X, Y)
    niece_in_law(X, Y) <= sibling_in_law(P, Y) & child(X, P) & is_female(X)
    nephew_in_law(X, Y) <= sibling_in_law(P, Y) & child(X, P) & is_male(X)

    # Q7.1 Step Relationships
    step_parent(X, Y) <= spouse(X, P) & parent(P, Y) & ~parent(X, Y)
    step_child(X, Y) <= step_parent(Y, X)
    step_sibling(X, Y) <= parent(P1, X) & parent(P2, Y) & spouse(P1, P2) & ~sibling(X, Y) & (X != Y)
    step_grandparent(X, Y) <= step_parent(X, P) & parent(P, Y)
    step_grandparent(X, Y) <= grandparent(X, P) & step_parent(P, Y)

    # Q8.1 Blended and Complex Relationships
    adoptive_parent(X, Y) <= adoptive_father(X, Y)
    adoptive_parent(X, Y) <= adoptive_mother(X, Y)
    biological_parent(X, Y) <= father(X, Y)
    biological_parent(X, Y) <= mother(X, Y)
    multiple_marriages(X) <= spouse(X, Y) & spouse(X, Z) & (Y != Z)
    half_uncle(X, Y) <= half_sibling(X, P) & parent(P, Y) & is_male(X)
    step_cousin(X, Y) <= parent(P1, X) & parent(P2, Y) & step_sibling(P1, P2) & (X != Y)
    step_cousin(X, Y) <= parent(P1, X) & step_parent(P2, Y) & sibling(P1, P2) & (X != Y)

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
