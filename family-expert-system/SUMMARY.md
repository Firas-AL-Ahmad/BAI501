# Assumptions Made During CSV Construction

*   **Missing Parents:** Represented by an empty string `""`.
*   **Multiple Spouses:** Encoded using a semicolon `;` as a separator within the 'Spouses' column.
*   **Ambiguous/Inconsistent Entries:**
    *   Mark's father being Mark was kept as-is, as per the source data.
*   **Name Normalization:** Names are trimmed of leading/trailing whitespace and multiple internal spaces are collapsed to a single space. Casing is preserved.
*   **Observed Counts:**
    *   Total number of people: 35
    *   Number of males: 17
    *   Number of females: 18
