# BAI501 — Family Relations Expert System (PyDatalog)

This project implements a rule-based expert system for querying complex family relationships using PyDatalog. The entire project is contained within a single Google Colab notebook (`family_expert_system.ipynb`) and is designed to be run online without any external data files.

## How to Run

1.  **Open in Google Colab**: Upload the `family_expert_system.ipynb` notebook to your Google Drive and open it with Google Colab.
2.  **Run All Cells**: From the menu, select **Runtime > Run all**.
3.  **Verify Outputs**: Scroll through the notebook. Each question (Q1, Q2, etc.) has its own dedicated section with a title, the rules, the queries, and a clearly marked `OUTPUT` block that displays the results for that section.

## Project Structure

The notebook is organized sequentially to make it easy to follow and grade:

*   **Header**: Contains student and course information.
*   **Environment Setup**: A code cell that installs `pyDatalog` and initializes all necessary terms.
*   **Safety Guard**: A utility function to prevent common PyDatalog errors.
*   **Question Sections (Q1-Q7)**: Each question is addressed in its own section, which includes:
    *   A Markdown title explaining the goal.
    *   A code cell defining the logical rules.
    *   A code cell that runs the queries for that question.
    *   The formatted output printed directly below the query cell.

## Critical Constraints Met

*   **100% Colab Compatible**: The notebook runs entirely online.
*   **No External Files**: All family facts are defined directly within the notebook code, satisfying the "no CSV" requirement.
*   **Clear, Per-Question Outputs**: Each question's results are printed immediately after its corresponding code, making grading straightforward.
*   **Robustness**: The code includes safeguards against common PyDatalog issues like name shadowing and incorrect variable binding.

## Project Documentation

For a complete, detailed explanation of the project, including a file-by-file overview and a deep dive into the rules and queries for each question, please see the full project report:

- **[View the Full Documentation Report](DOCUMENTATION_REPORT.md)**
