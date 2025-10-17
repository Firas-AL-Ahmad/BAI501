# Assumptions Made During CSV Construction

*   **Missing Parents:** Represented by an empty string `""`.
*   **Multiple Spouses:** Encoded using a semicolon `;` as a separator within the 'Spouses' column.
*   **Ambiguous/Inconsistent Entries:**
    *   Mark's father being Mark was kept as-is, as per the source data.
*   **Name Normalization:** Names are trimmed of leading/trailing whitespace and multiple internal spaces are collapsed to a single space. Casing is preserved.
*   **Unrelated Individuals:** Defined as individuals who have no family relationships (no parent, child, or spouse facts) within the dataset. These are individuals who form a connected component of size 1 in the family graph.
*   **Observed Counts:**
    *   Total number of people: 35
    *   Number of males: 17
    *   Number of females: 18

### Data Additions (for Q6–Q8)
- Added **Amir** (married to Sarah) → shows *mother-in-law (Emily → Amir)*.
- Added **Fatima** (married to George) → shows *siblings-in-law* relations.
- Added **Rania** (second spouse of Paul) and **Oliver** (her child with Hassan) → show *step-parent* and *step-sibling* cases.
- Added **Hassan** as Rania’s previous husband → enables *multiple marriages* and *step-family* examples.
