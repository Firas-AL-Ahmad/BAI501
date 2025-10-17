import sys
import os
from typing import List, Tuple, Dict, Any

# Add the project root to sys.path for direct execution
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from pyDatalog import pyDatalog
from src.facts import load_facts_into_pydatalog, load_facts_dataframe, CSV_FILEPATH
from src.rules import define_family_rules

# Import all terms that might be used in queries
pyDatalog.create_terms('X, Y, P, P1, P2, F, M, D, Z, S, SP, '
                       'father, mother, parent, child, son, daughter, is_male, is_female, spouse, sibling, '
                       'full_sibling, half_sibling, brother, sister, '
                       'grandparent, grandfather, grandmother, great_grandparent, ancestor, descendant, '
                       'uncle, aunt, first_cousin, second_cousin, cousin, cousin_degree, '
                       'mother_in_law, father_in_law, brother_in_law, sister_in_law, '
                       'son_in_law, daughter_in_law, sibling_in_law, niece_in_law, nephew_in_law, '
                       'step_parent, step_child, step_sibling, step_grandparent, '
                       'adoptive_parent, biological_parent, multiple_marriages, half_uncle, step_cousin, '
                       'adoptive_father, adoptive_mother, '
                       'M_of_X, M_of_Y, F_of_X, F_of_Y, shares_father, shares_mother') # Added new terms

def run_all_queries() -> Dict[str, Any]:
    """
    Loads facts, defines rules, and runs all specified queries.

    Returns:
        A dictionary containing results of all queries.
    """
    pyDatalog.clear()
    load_facts_into_pydatalog(CSV_FILEPATH)
    define_family_rules()

    results = {}

    # Q2.2 Query: List all sons and daughters of any individual.
    # This is already covered by sample_queries in rules.py, but we'll include it here for completeness.
    all_sons_results = pyDatalog.ask('son(X, Y)')
    results['all_sons'] = sorted(list(set([(str(r[0]), str(r[1])) for r in all_sons_results.answers]))) if all_sons_results else []

    all_daughters_results = pyDatalog.ask('daughter(X, Y)')
    results['all_daughters'] = sorted(list(set([(str(r[0]), str(r[1])) for r in all_daughters_results.answers]))) if all_daughters_results else []

    # Q2.2 Query: Who are the children of John?
    children_of_john_results = pyDatalog.ask('child(X, "John")')
    results['children_of_john'] = sorted(set([str(r[0]) for r in children_of_john_results.answers])) if children_of_john_results else []

    # Q3.2 Query: All siblings of Alice
    siblings_of_alice_results = pyDatalog.ask('sibling(X, "Alice")')
    results['siblings_of_alice'] = sorted(set([str(r[0]) for r in siblings_of_alice_results.answers])) if siblings_of_alice_results else []

    # Q3.2 Query: All half-siblings of Michael
    half_siblings_of_michael_results = pyDatalog.ask('half_sibling(X, "Michael")')
    results['half_siblings_of_michael'] = sorted(set([str(r[0]) for r in half_siblings_of_michael_results.answers])) if half_siblings_of_michael_results else []

    # Q3.2 Query: List all sibling pairs
    all_sibling_pairs_results = pyDatalog.ask('sibling(X, Y)')
    results['all_sibling_pairs'] = sorted(list(set([tuple(sorted((str(r[0]), str(r[1])))) for r in all_sibling_pairs_results.answers if str(r[0]) != str(r[1])]))) if all_sibling_pairs_results else []

    # Q4.2 Query: All ancestors of Liam
    ancestors_of_liam_results = pyDatalog.ask('ancestor(X, "Liam")')
    results['ancestors_of_liam'] = sorted(set([str(r[0]) for r in ancestors_of_liam_results.answers])) if ancestors_of_liam_results else []

    # Q4.2 Query: Who are the great-grandparents of Sophia?
    great_grandparents_of_sophia_results = pyDatalog.ask('great_grandparent(X, "Sophia")')
    results['great_grandparents_of_sophia'] = sorted(set([str(r[0]) for r in great_grandparents_of_sophia_results.answers])) if great_grandparents_of_sophia_results else []

    # Q4.2 Query: List all descendants of Emma
    descendants_of_emma_results = pyDatalog.ask('descendant(X, "Emma")')
    results['descendants_of_emma'] = sorted(set([str(r[0]) for r in descendants_of_emma_results.answers])) if descendants_of_emma_results else []

    # Q5.2 Query: Who are the cousins of Noah?
    cousins_of_noah_results = pyDatalog.ask('cousin(X, "Noah")')
    results['cousins_of_noah'] = sorted(set([str(r[0]) for r in cousins_of_noah_results.answers])) if cousins_of_noah_results else []

    # Q5.2 Query: Find all uncles and aunts of Emily
    uncles_of_emily_results = pyDatalog.ask('uncle(X, "Emily")')
    results['uncles_of_emily'] = sorted(set([str(r[0]) for r in uncles_of_emily_results.answers])) if uncles_of_emily_results else []

    aunts_of_emily_results = pyDatalog.ask('aunt(X, "Emily")')
    results['aunts_of_emily'] = sorted(set([str(r[0]) for r in aunts_of_emily_results.answers])) if aunts_of_emily_results else []

    # Q5.2 Query: List second cousins of James
    second_cousins_of_james_results = pyDatalog.ask('second_cousin(X, "James")')
    results['second_cousins_of_james'] = sorted(set([str(r[0]) for r in second_cousins_of_james_results.answers])) if second_cousins_of_james_results else []

    # Q6.3 Query: Who is the mother-in-law of Amir?
    mother_in_law_of_amir_results = pyDatalog.ask('mother_in_law(X, "Amir")')
    results['mother_in_law_of_amir'] = sorted(set([str(r[0]) for r in mother_in_law_of_amir_results.answers])) if mother_in_law_of_amir_results else []

    # Q6.3 Query: List all siblings-in-law of Fatima
    siblings_in_law_of_fatima_results = pyDatalog.ask('sibling_in_law(X, "Fatima")')
    results['siblings_in_law_of_fatima'] = sorted(set([str(r[0]) for r in siblings_in_law_of_fatima_results.answers])) if siblings_in_law_of_fatima_results else []

    # Q7.2 Query: All step-siblings of Oliver
    step_siblings_of_oliver_results = pyDatalog.ask('step_sibling(X, "Oliver")')
    results['step_siblings_of_oliver'] = sorted(set([str(r[0]) for r in step_siblings_of_oliver_results.answers])) if step_siblings_of_oliver_results else []

    # Q7.2 Query: Who is the stepfather of Sophia?
    stepfather_of_sophia_results = pyDatalog.ask('step_parent(X, "Sophia") & is_male(X)')
    results['stepfather_of_sophia'] = sorted(set([str(r[0]) for r in stepfather_of_sophia_results.answers])) if stepfather_of_sophia_results else []

    # Q8.2 Query: Who are the adoptive parents of Daniel?
    adoptive_parents_of_daniel_results = pyDatalog.ask('adoptive_parent(X, "Daniel")')
    results['adoptive_parents_of_daniel'] = sorted(set([str(r[0]) for r in adoptive_parents_of_daniel_results.answers])) if adoptive_parents_of_daniel_results else []

    # Q8.2 Query: List children of parents with multiple spouses
    children_of_multiple_spouses_results = pyDatalog.ask('multiple_marriages(P) & child(X, P)')
    results['children_of_multiple_spouses'] = sorted(set([str(r[0]) for r in children_of_multiple_spouses_results.answers])) if children_of_multiple_spouses_results else []

    # Q8.2 Query: Who are the step-cousins of Grace?
    step_cousins_of_grace_results = pyDatalog.ask('step_cousin(X, "Grace")')
    results['step_cousins_of_grace'] = sorted(set([str(r[0]) for r in step_cousins_of_grace_results.answers])) if step_cousins_of_grace_results else []

    return results

# Helper to ensure PyDatalog KB is loaded
def _ensure_kb_loaded():
    """
    Ensures PyDatalog facts and rules are loaded.
    This function clears the knowledge base, loads facts, and defines rules
    every time it's called to ensure a clean state for each query/test.
    """
    pyDatalog.clear()
    load_facts_into_pydatalog(CSV_FILEPATH)
    define_family_rules()

def relatives_within_generations(person: str, generations: int) -> set[str]:
    """
    Returns the set of distinct relatives reachable from person within 'generations'
    upwards (ancestors), downwards (descendants), and sideways (siblings, spouses, in-laws).
    """
    _ensure_kb_loaded()
    
    # Declare terms for local use in this function
    pyDatalog.create_terms('CurrentPerson, Relative, Depth, Path, RelativesSet')

    # Initialize with the person at depth 0
    # We'll use a BFS-like approach to explore relationships
    # (Person, Depth)
    to_explore = {(person, 0)}
    all_relatives = set()
    
    # Keep track of visited nodes to avoid infinite loops and redundant processing
    visited = {person}

    current_generation = 0
    while current_generation <= generations:
        next_to_explore = set()
        
        for current_person, depth in to_explore:
            if depth > current_generation:
                continue # Already processed for this generation

            # Find parents
            parents_results = pyDatalog.ask(f'parent(P, "{current_person}")')
            if parents_results:
                for p_res in parents_results.answers:
                    p_name = str(p_res[0])
                    if p_name not in visited:
                        all_relatives.add(p_name)
                        next_to_explore.add((p_name, depth + 1))
                        visited.add(p_name)

            # Find children
            children_results = pyDatalog.ask(f'child(C, "{current_person}")')
            if children_results:
                for c_res in children_results.answers:
                    c_name = str(c_res[0])
                    if c_name not in visited:
                        all_relatives.add(c_name)
                        next_to_explore.add((c_name, depth + 1))
                        visited.add(c_name)
            
            # Find siblings (only for current_person, not for newly found parents/children in this iteration)
            if depth <= generations: # Siblings are at the same generation level
                siblings_results = pyDatalog.ask(f'sibling(S, "{current_person}")')
                if siblings_results:
                    for s_res in siblings_results.answers:
                        s_name = str(s_res[0])
                        if s_name not in visited:
                            all_relatives.add(s_name)
                            # Siblings are at the same generation depth as current_person
                            next_to_explore.add((s_name, depth)) # Add to explore for their spouses/children
                            visited.add(s_name)

            # Find spouses (only for current_person, not for newly found parents/children in this iteration)
            if depth <= generations: # Spouses are at the same generation level
                spouses_results = pyDatalog.ask(f'spouse(SP, "{current_person}")')
                if spouses_results:
                    for sp_res in spouses_results.answers:
                        sp_name = str(sp_res[0])
                        if sp_name not in visited:
                            all_relatives.add(sp_name)
                            # Spouses are at the same generation depth as current_person
                            next_to_explore.add((sp_name, depth)) # Add to explore for their children/parents
                            visited.add(sp_name)
        
        # Prepare for next generation's exploration
        # Filter next_to_explore to only include those within the current generation limit
        to_explore = {(p, d) for p, d in next_to_explore if d <= generations}
        current_generation += 1

    # Ensure the input person is not included in the result
    if person in all_relatives:
        all_relatives.remove(person)
    
    return all_relatives

def unrelated_individuals() -> set[str]:
    """
    Returns the set of individuals in the dataset that have no family relationship
    (no path via parent/child/spouse) to any other individual.
    This is defined as individuals who are in components of size 1 (isolated individuals).
    """
    _ensure_kb_loaded()

    all_individuals = set()
    
    # Get all individuals who are parents
    parents_results = pyDatalog.ask('parent(X, Y)')
    if parents_results:
        for r in parents_results.answers:
            all_individuals.add(str(r[0]))
            all_individuals.add(str(r[1]))

    # Get all individuals who are spouses
    spouses_results = pyDatalog.ask('spouse(X, Y)')
    if spouses_results:
        for r in spouses_results.answers:
            all_individuals.add(str(r[0]))
            all_individuals.add(str(r[1]))
            
    # Get all individuals who are children (already covered by parent(X,Y) if Y is a child)
    # We can also get all names from the original DataFrame if needed, but this is more robust
    # to only consider individuals explicitly mentioned in facts.

    isolated_individuals = set()
    for person in all_individuals:
        # Check if the person has any parent, child, or spouse
        has_parent = pyDatalog.ask(f'parent(P, "{person}")')
        has_child = pyDatalog.ask(f'child(C, "{person}")')
        has_spouse = pyDatalog.ask(f'spouse(S, "{person}")')

        if not has_parent and not has_child and not has_spouse:
            isolated_individuals.add(person)
            
    # To be truly isolated, they shouldn't even be a parent/child/spouse of anyone else.
    # The above logic checks if 'person' is a child, parent, or spouse.
    # We need to ensure that 'person' is not a parent of anyone, child of anyone, or spouse of anyone.
    # The current logic for `all_individuals` already collects all names that appear in any relationship.
    # If a person is in `all_individuals` but has no relationships, they are isolated.
    
    # Re-evaluate: The definition of isolated is "component of size 1".
    # This means no parent, no child, no spouse.
    # The current check `if not has_parent and not has_child and not has_spouse:` correctly identifies this.
    
    # However, we need to ensure `all_individuals` contains *all* people in the dataset,
    # not just those involved in some relationship.
    # Let's get all names from the CSV directly for a complete list.
    df = load_facts_dataframe(CSV_FILEPATH) # Use the helper from facts.py
    all_names_in_dataset = set(df['Name'].tolist())

    isolated_individuals_from_dataset = set()
    for person_name in all_names_in_dataset:
        has_parent_fact = pyDatalog.ask(f'parent(P, "{person_name}")')
        is_parent_fact = pyDatalog.ask(f'parent("{person_name}", C)')
        has_spouse_fact = pyDatalog.ask(f'spouse(S, "{person_name}")')

        if not has_parent_fact and not is_parent_fact and not has_spouse_fact:
            isolated_individuals_from_dataset.add(person_name)

    return isolated_individuals_from_dataset


def is_direct_line_of_descent(descendant: str, ancestor: str) -> bool:
    """
    True if descendant is in a direct line of descent from ancestor
    (i.e., ancestor is an ancestor of descendant, possibly many generations).
    """
    _ensure_kb_loaded()
    result = pyDatalog.ask(f'ancestor("{ancestor}", "{descendant}")')
    return bool(result)

def is_aunt_or_uncle(x: str, y: str) -> Tuple[bool, str]:
    """
    Returns a tuple (True, "aunt") / (True, "uncle") if x is an aunt or uncle of y.
    If neither, returns (False, "").
    """
    _ensure_kb_loaded()
    
    is_aunt_result = pyDatalog.ask(f'aunt("{x}", "{y}")')
    if is_aunt_result:
        return True, "aunt"
    
    is_uncle_result = pyDatalog.ask(f'uncle("{x}", "{y}")')
    if is_uncle_result:
        return True, "uncle"
        
    return False, ""

def is_cousin_within_n(x: str, y: str, n: int) -> bool:
    """
    Determine whether x is a cousin of y within n generations.
    Their nearest common ancestor is at most n generations above each of them.
    """
    _ensure_kb_loaded()

    # Helper to get ancestors with their depth from the person
    def get_ancestors_with_depth(person_name: str, max_depth: int) -> Dict[str, int]:
        ancestors_with_depth = {}
        
        # Use a queue for BFS-like traversal
        queue = [(person_name, 0)] # (current_person, current_depth)
        visited_nodes = {person_name} # To prevent cycles and redundant processing

        while queue:
            current_node, current_depth = queue.pop(0)

            if current_depth > max_depth:
                continue

            # Add to ancestors_with_depth if it's an actual ancestor (depth > 0)
            if current_depth > 0:
                ancestors_with_depth[current_node] = current_depth

            # Find parents of current_node
            parents_results = pyDatalog.ask(f'parent(P, "{current_node}")')
            if parents_results:
                for p_res in parents_results.answers:
                    parent_name = str(p_res[0])
                    if parent_name not in visited_nodes:
                        visited_nodes.add(parent_name)
                        queue.append((parent_name, current_depth + 1))
        return ancestors_with_depth

    ancestors_x = get_ancestors_with_depth(x, n)
    ancestors_y = get_ancestors_with_depth(y, n)

    # Find common ancestors
    common_ancestors = set(ancestors_x.keys()) & set(ancestors_y.keys())

    for ancestor_name in common_ancestors:
        depth_x_to_ancestor = ancestors_x[ancestor_name]
        depth_y_to_ancestor = ancestors_y[ancestor_name]

        # Check if the common ancestor is within n generations for both
        # and that they are indeed cousins (i.e., not the same person, and not parent/child)
        # The definition of cousin implies they are not direct ancestors/descendants of each other.
        # The ancestor rule already handles depth >= 1.
        if depth_x_to_ancestor >= 1 and depth_y_to_ancestor >= 1 and \
           depth_x_to_ancestor == depth_y_to_ancestor and \
           depth_x_to_ancestor <= n:
            
            # Ensure X and Y are not the same person, and not siblings.
            # The problem states "cousin of Y", implying X != Y.
            # Also, cousins are not siblings.
            if x != y and not pyDatalog.ask(f'sibling("{x}", "{y}")'):
                return True
    return False


if __name__ == "__main__":
    print("Running all queries...")
    all_results = run_all_queries()

    for query_name, query_results in all_results.items():
        print(f"\n--- {query_name.replace('_', ' ').title()} ---")
        if query_results:
            for res in query_results:
                if isinstance(res, tuple):
                    print(f"- {res[0]} is {query_name.split('_of_')[0].replace('_', ' ')} of {res[1]}")
                else:
                    print(f"- {res}")
        else:
            print("- No results found.")

    print("\n--- Q9.1 Test Inference ---")
    # Q9.1 Test inference: Who are all relatives of Adam within 2 generations?
    adam_relatives = relatives_within_generations('Adam', 2)
    print(f"\nRelatives of Adam within 2 generations: {sorted(list(adam_relatives))}")

    # Q9.1 Test inference: Identify unrelated individuals in the system
    unrelated = unrelated_individuals()
    print(f"\nUnrelated individuals: {sorted(list(unrelated))}")

    # Q9.1 Test inference: Write a query to find if X is in a direct line of descent from Y
    is_adam_descendant_of_paul = is_direct_line_of_descent('Adam', 'Paul')
    print(f"\nIs Adam in direct line of descent from Paul? {is_adam_descendant_of_paul}")
    is_paul_descendant_of_adam = is_direct_line_of_descent('Paul', 'Adam')
    print(f"\nIs Paul in direct line of descent from Adam? {is_paul_descendant_of_adam}")

    print("\n--- Q6.3 Queries ---")
    print(f"\nMother-in-law of Amir: {all_results['mother_in_law_of_amir']}")
    print(f"\nSiblings-in-law of Fatima: {all_results['siblings_in_law_of_fatima']}")

    print("\n--- Q7.2 Queries ---")
    print(f"\nStep-siblings of Oliver: {all_results['step_siblings_of_oliver']}")
    print(f"\nStepfather of Sophia: {all_results['stepfather_of_sophia']}")

    print("\n--- Q8.2 Queries ---")
    print(f"\nAdoptive parents of Daniel: {all_results['adoptive_parents_of_daniel']}")
    print(f"\nChildren of parents with multiple spouses: {all_results['children_of_multiple_spouses']}")
    print(f"\nStep-cousins of Grace: {all_results['step_cousins_of_grace']}")

    print("\n--- Q9.1 Test Inference ---")
    # Q9.1 Test inference: Who are all relatives of Adam within 2 generations?
    adam_relatives = relatives_within_generations('Adam', 2)
    print(f"\nRelatives of Adam within 2 generations: {sorted(list(adam_relatives))}")

    # Q9.1 Test inference: Identify unrelated individuals in the system
    unrelated = unrelated_individuals()
    print(f"\nUnrelated individuals: {sorted(list(unrelated))}")

    # Q9.1 Test inference: Write a query to find if X is in a direct line of descent from Y
    is_adam_descendant_of_paul = is_direct_line_of_descent('Adam', 'Paul')
    print(f"\nIs Adam in direct line of descent from Paul? {is_adam_descendant_of_paul}")
    is_paul_descendant_of_adam = is_direct_line_of_descent('Paul', 'Adam')
    print(f"\nIs Paul in direct line of descent from Adam? {is_paul_descendant_of_adam}")

    print("\n--- Q9.2 Write a query ---")
    # Q9.2 Write a query: Is X the aunt or uncle of Y?
    olivia_kevin_aunt_uncle = is_aunt_or_uncle('Olivia', 'Kevin')
    print(f"\nIs Olivia aunt or uncle of Kevin? {olivia_kevin_aunt_uncle}")
    john_david_aunt_uncle = is_aunt_or_uncle('John', 'David')
    print(f"\nIs John aunt or uncle of David? {john_david_aunt_uncle}")

    # Q9.2 Write a query: Is X a cousin of Y within N generations?
    sarah_george_cousin_1 = is_cousin_within_n('Sarah', 'George', 1)
    print(f"\nIs Sarah a cousin of George within 1 generation? {sarah_george_cousin_1}")
    sarah_george_cousin_2 = is_cousin_within_n('Sarah', 'George', 2)
    print(f"\nIs Sarah a cousin of George within 2 generations? {sarah_george_cousin_2}")
