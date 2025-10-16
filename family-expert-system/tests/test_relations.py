import pytest
import pandas as pd
from pyDatalog import pyDatalog
from src.facts import load_facts_dataframe, register_pydatalog_facts # This import will trigger pyDatalog.create_terms

# Define the path to the test CSV file
TEST_CSV_FILEPATH = "family-expert-system/data/family_facts.csv"

def test_load_facts_dataframe_row_count():
    """
    Tests that load_facts_dataframe returns a DataFrame with the correct number of rows.
    """
    df = load_facts_dataframe(TEST_CSV_FILEPATH)
    assert len(df) == 35

def test_load_facts_dataframe_john_gender():
    """
    Tests that load_facts_dataframe correctly identifies John's gender.
    """
    df = load_facts_dataframe(TEST_CSV_FILEPATH)
    john_entry = df[df['Name'] == 'John']
    assert not john_entry.empty
    assert john_entry['Gender'].iloc[0] == 'Male'

def test_register_pydatalog_facts_counts():
    """
    Tests that register_pydatalog_facts returns positive counts for males and females.
    Clears pyDatalog state before and after the test.
    """
    pyDatalog.clear() # Clear state before test

    df = load_facts_dataframe(TEST_CSV_FILEPATH)
    summary = register_pydatalog_facts(df)

    assert summary["num_males"] > 0
    assert summary["num_females"] > 0
    assert summary["num_fathers"] > 0
    assert summary["num_mothers"] > 0
    assert summary["num_spouses"] > 0

    pyDatalog.clear() # Clear state after test

# New test for unique spouse count
def test_register_pydatalog_facts_unique_spouses():
    """
    Tests that register_pydatalog_facts returns the correct count of unique unordered spouse pairs.
    """
    pyDatalog.clear() # Clear state before test

    df = load_facts_dataframe(TEST_CSV_FILEPATH)
    summary = register_pydatalog_facts(df)

    # Manually compute unique unordered spouse pairs from the DataFrame
    expected_unique_pairs = set()
    for _, row in df.iterrows():
        person_name = row["Name"]
        spouses_str = row["Spouses"]
        if spouses_str:
            spouses_list = [s for s in spouses_str.split(';') if s and s != person_name]
            for spouse_name in set(spouses_list):
                pair = frozenset({person_name, spouse_name})
                expected_unique_pairs.add(pair)

    assert summary["num_spouses"] == len(expected_unique_pairs)
    pyDatalog.clear() # Clear state after test

# New test for PyDatalog fact presence
def test_pydatalog_fact_presence():
    """
    Tests that PyDatalog facts are correctly registered.
    """
    pyDatalog.clear() # Clear state before test

    df = load_facts_dataframe(TEST_CSV_FILEPATH)
    register_pydatalog_facts(df)

    # Assert presence of a known fact using pyDatalog.ask()
    assert pyDatalog.ask('is_male("John")')

    # Assert absence of a non-existent fact
    assert not pyDatalog.ask('is_male("NonExistentPerson")')

    pyDatalog.clear() # Clear state after test
