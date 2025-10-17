import sys
import os
import pytest
from pyDatalog import pyDatalog

# Add the project root to sys.path for direct execution
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.facts import load_facts_dataframe, register_pydatalog_facts, load_facts_into_pydatalog, X, Y, P, father, mother, parent, child, son, daughter, is_male, is_female, sibling, grandparent, grandchild, uncle, aunt, cousin
from src.rules import define_family_rules, sample_queries

# CSV path (relative to repo root)
CSV_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "family_facts.csv")

def setup_module(module):
    pyDatalog.clear()
    # Define all PyDatalog terms for use in tests
    pyDatalog.create_terms('X, Y, P, P1, P2, father, mother, parent, child, son, daughter, is_male, is_female, sibling, grandparent, grandchild, uncle, aunt, cousin')

def teardown_module(module):
    pyDatalog.clear()

def test_load_facts_dataframe_has_john_and_counts():
    df = load_facts_dataframe(CSV_PATH)
    assert len(df) == 35
    john_row = df[df['Name'] == 'John']
    assert not john_row.empty
    assert john_row.iloc[0]['Gender'] == 'Male'

def test_register_and_unique_spouse_count_and_gender():
    pyDatalog.clear()
    df = load_facts_dataframe(CSV_PATH)
    summary = register_pydatalog_facts(df)
    assert summary['num_males'] > 0
    assert summary['num_females'] > 0
    assert summary['num_spouses'] >= 0
    
    
    
def test_define_rules_and_children_of_john():
    pyDatalog.clear()
    # load and register facts into pydatalog
    load_facts_into_pydatalog(CSV_PATH)

    # define rules (must be done after facts are loaded)
    define_family_rules()

    # Use pyDatalog.ask with a string query to avoid module-variable injection issues
    q = pyDatalog.ask('child(X, "John")')
    children = set()
    if q and q.answers:
        # each answer is a tuple of values corresponding to variables in the query
        for ans in q.answers:
            # ans[0] is the value of X in this answer
            children.add(str(ans[0]))

    expected = {'David', 'Emma', 'Diana'}
    assert children == expected

    pyDatalog.clear()

def test_sample_queries_return_types():
    pyDatalog.clear()
    load_facts_into_pydatalog(CSV_PATH)
    define_family_rules()
    q = sample_queries()
    assert isinstance(q, dict)
    assert 'children_of_john' in q and isinstance(q['children_of_john'], list)
    assert 'all_sons' in q and isinstance(q['all_sons'], list)
    assert 'all_daughters' in q and isinstance(q['all_daughters'], list)
    pyDatalog.clear()

# New test for grandparent rule
def test_grandparent_rule():
    pyDatalog.clear()
    load_facts_into_pydatalog(CSV_PATH)
    define_family_rules()
    assert grandparent('John', 'Nora') # John is grandparent of Nora
    assert not grandparent('John', 'David') # John is not grandparent of David
    pyDatalog.clear()

# New test for uncle/aunt rules
def test_uncle_aunt_rules():
    pyDatalog.clear()
    load_facts_into_pydatalog(CSV_PATH)
    define_family_rules()
    assert uncle('Paul', 'Kevin') # Paul is uncle of Kevin
    assert aunt('Olivia', 'Kevin') # Olivia is aunt of Kevin (Olivia is sibling of Michael, Michael is parent of Kevin)
    assert not uncle('Diana', 'Kevin') # Diana is not uncle of Kevin (she's female)
    pyDatalog.clear()

# New test for cousin rule
def test_cousin_rule():
    pyDatalog.clear()
    load_facts_into_pydatalog(CSV_PATH)
    define_family_rules()
    assert cousin('Alice', 'Grace') # Alice (child of Kevin) and Grace (child of Linda) are cousins because Kevin and Linda are siblings
    assert not cousin('John', 'Nora') # John is not cousin of Nora
    pyDatalog.clear()

def test_grandchildren_of_john():
    pyDatalog.clear()
    load_facts_into_pydatalog(CSV_PATH)
    define_family_rules()
    # use string-based query for robustness
    q = pyDatalog.ask('grandparent("John", X)')
    grandchildren = set()
    if q and q.answers:
        for ans in q.answers:
            grandchildren.add(str(ans[0]))
    expected = {"Emily","James","Liam","Mark","Michael","Nora","Olivia","Paul","Tom"}
    assert grandchildren == expected
    pyDatalog.clear()

def test_uncles_and_aunts_of_kevin():
    pyDatalog.clear()
    load_facts_into_pydatalog(CSV_PATH)
    define_family_rules()
    # uncles of Kevin (male siblings of parents)
    q = pyDatalog.ask('uncle(X, "Kevin")')
    uncles = set(str(ans[0]) for ans in q.answers) if q and q.answers else set()
    expected_uncles = {"Michael","Paul","Tom"}
    assert uncles == expected_uncles

    # aunts of Kevin
    q2 = pyDatalog.ask('aunt(X, "Kevin")')
    aunts = set(str(ans[0]) for ans in q2.answers) if q2 and q2.answers else set()
    expected_aunts = {"Olivia"}
    assert aunts == expected_aunts
    pyDatalog.clear()

def test_cousins_of_sarah():
    pyDatalog.clear()
    load_facts_into_pydatalog(CSV_PATH)
    define_family_rules()
    q = pyDatalog.ask('cousin(X, "Sarah")')
    cousins = set(str(ans[0]) for ans in q.answers) if q and q.answers else set()
    expected = {"Adam","Ella","George"}
    assert cousins == expected
    pyDatalog.clear()
