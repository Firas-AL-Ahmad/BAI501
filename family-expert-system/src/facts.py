"""
This module provides functions to load family facts from a CSV file into a pandas DataFrame,
normalize names, and register these facts into a PyDatalog knowledge base.

Example usage:
    df = load_facts_into_pydatalog("family-expert-system/data/family_facts.csv")
    print(df.head())
"""
import pandas as pd
from typing import Dict
import re

try:
    from pyDatalog import pyDatalog
except ImportError:
    raise ImportError(
        "pyDatalog is not installed. Please install it using: pip install pyDatalog"
    )

# Define PyDatalog terms globally
pyDatalog.create_terms('father, mother, parent, child, son, daughter, is_male, is_female, spouse, X, Y')

def _normalize_name(name: str) -> str:
    """Strips leading/trailing whitespace and collapses multiple internal spaces."""
    if not isinstance(name, str):
        return ""
    return re.sub(r'\s+', ' ', name).strip()

def load_facts_dataframe(filepath: str) -> pd.DataFrame:
    """
    Loads family data from a CSV file, normalizes names, and ensures the correct header.

    Args:
        filepath: The path to the CSV file.

    Returns:
        A cleaned pandas DataFrame with family facts.
    """
    df = pd.read_csv(filepath)

    # Ensure header matches exactly
    expected_header = ["Name", "Gender", "Father", "Mother", "Spouses", "Notes"]
    if list(df.columns) != expected_header:
        raise ValueError(f"CSV header does not match expected: {expected_header}")

    # Normalize relevant columns
    for col in ["Name", "Father", "Mother", "Spouses"]:
        df[col] = df[col].apply(_normalize_name)

    return df

def register_pydatalog_facts(df: pd.DataFrame) -> Dict[str, int]:
    """
    Registers family facts from a DataFrame into PyDatalog.

    Args:
        df: A pandas DataFrame containing family facts.

    Returns:
        A dictionary summarizing the number of registered facts.
    """
    # Clear existing facts to ensure a clean state for registration
    pyDatalog.clear()

    # Initialize counters
    summary = {
        "num_fathers": 0,
        "num_mothers": 0,
        "num_spouses": 0, # This will be updated after processing all spouses
        "num_males": 0,
        "num_females": 0,
    }

    # Track unique spouse pairs for accurate counting across all individuals
    unique_spouse_pairs = set()

    # Add facts from DataFrame
    for _, row in df.iterrows():
        person_name = row["Name"]
        gender = row["Gender"]
        father_name = row["Father"]
        mother_name = row["Mother"]
        spouses_str = row["Spouses"]

        # Add gender facts
        if gender == "Male":
            + is_male(person_name)
            summary["num_males"] += 1
        elif gender == "Female":
            + is_female(person_name)
            summary["num_females"] += 1

        # Add father facts
        if father_name:
            + father(person_name, father_name)
            summary["num_fathers"] += 1

        # Add mother facts
        if mother_name:
            + mother(person_name, mother_name)
            summary["num_mothers"] += 1

        # Add spouse facts (symmetric)
        if spouses_str:
            spouses_list = [s for s in spouses_str.split(';') if s and s != person_name]
            for spouse_name in set(spouses_list): # Use set to handle duplicates
                if spouse_name:
                    # Add symmetric facts to PyDatalog
                    + spouse(person_name, spouse_name)
                    + spouse(spouse_name, person_name)

                    # Add to unique_spouse_pairs set (unordered)
                    pair = frozenset({person_name, spouse_name})
                    unique_spouse_pairs.add(pair)

    # Update num_spouses in summary after processing all individuals
    summary["num_spouses"] = len(unique_spouse_pairs)

    return summary

def load_facts_into_pydatalog(filepath: str) -> pd.DataFrame:
    """
    Convenience function to load facts from CSV, register them in PyDatalog,
    print a summary, and return the cleaned DataFrame.

    Args:
        filepath: The path to the CSV file.

    Returns:
        A cleaned pandas DataFrame with family facts.
    """
    df = load_facts_dataframe(filepath)
    summary = register_pydatalog_facts(df)

    print("\n--- PyDatalog Facts Registration Summary ---")
    print(f"Number of males registered: {summary['num_males']}")
    print(f"Number of females registered: {summary['num_females']}")
    print(f"Number of father facts registered: {summary['num_fathers']}")
    print(f"Number of mother facts registered: {summary['num_mothers']}")
    print(f"Number of spouse facts registered (symmetric): {summary['num_spouses']}")
    print("------------------------------------------")

    return df

if __name__ == "__main__":
    CSV_FILEPATH = "family-expert-system/data/family_facts.csv"
    print(f"Loading facts from: {CSV_FILEPATH}")
    df_facts = load_facts_into_pydatalog(CSV_FILEPATH)
    print("\nFirst 5 rows of loaded DataFrame:")
    print(df_facts.head().to_markdown(index=False))
