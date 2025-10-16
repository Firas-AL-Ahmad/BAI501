import pandas as pd

# Structured family data
family_data = [
    {"Name": "John", "Gender": "Male", "Father": "", "Mother": "", "Spouses": "Mary", "Notes": "1st marriage"},
    {"Name": "Mary", "Gender": "Female", "Father": "", "Mother": "", "Spouses": "John;Peter", "Notes": "Multiple marriages → Peter is stepfather to John’s children"},
    {"Name": "Peter", "Gender": "Male", "Father": "", "Mother": "", "Spouses": "Mary", "Notes": "Stepfather to David, Emma, Diana"},
    {"Name": "David", "Gender": "Male", "Father": "John", "Mother": "Mary", "Spouses": "Sophia;Clara", "Notes": "Multiple marriages"},
    {"Name": "Emma", "Gender": "Female", "Father": "John", "Mother": "Mary", "Spouses": "Paul;Alex", "Notes": "Multiple marriages"},
    {"Name": "Diana", "Gender": "Female", "Father": "John", "Mother": "Mary", "Spouses": "", "Notes": "Sibling to David & Emma"},
    {"Name": "Sophia", "Gender": "Female", "Father": "", "Mother": "", "Spouses": "David", "Notes": "Mother of Paul, Olivia, Michael, Tom"},
    {"Name": "Clara", "Gender": "Female", "Father": "", "Mother": "", "Spouses": "David", "Notes": "Stepmother to David’s children with Sophia"},
    {"Name": "Paul", "Gender": "Male", "Father": "David", "Mother": "Sophia", "Spouses": "Emma", "Notes": "Husband of Emma, father of Nora, Liam, Emily, James"},
    {"Name": "Olivia", "Gender": "Female", "Father": "David", "Mother": "Sophia", "Spouses": "Michael;Tom", "Notes": "Mother of Kevin, Linda, Lucas, Tom’s wife later"},
    {"Name": "Michael", "Gender": "Male", "Father": "David", "Mother": "Sophia", "Spouses": "Olivia", "Notes": "Father of Kevin, Linda, Lucas"},
    {"Name": "Tom", "Gender": "Male", "Father": "David", "Mother": "Sophia", "Spouses": "Olivia", "Notes": "Half-step tie: later married Olivia, father of Ivy & Daniel"},
    {"Name": "Kevin", "Gender": "Male", "Father": "Michael", "Mother": "Olivia", "Spouses": "Linda", "Notes": "Father of Isla, Noah, Alice"},
    {"Name": "Linda", "Gender": "Female", "Father": "Michael", "Mother": "Olivia", "Spouses": "Kevin;Lucas", "Notes": "Multiple marriages"},
    {"Name": "Lucas", "Gender": "Male", "Father": "Michael", "Mother": "Olivia", "Spouses": "Linda", "Notes": "Father of Zoe, Grace, Henry, Layla, Ryan"},
    {"Name": "Nora", "Gender": "Female", "Father": "Paul", "Mother": "Emma", "Spouses": "Liam", "Notes": "Mother of George, Ella"},
    {"Name": "Liam", "Gender": "Male", "Father": "Paul", "Mother": "Emma", "Spouses": "Nora", "Notes": "Father of George, Ella"},
    {"Name": "Emily", "Gender": "Female", "Father": "Paul", "Mother": "Emma", "Spouses": "James", "Notes": "Mother of Sarah, Adam"},
    {"Name": "James", "Gender": "Male", "Father": "Paul", "Mother": "Emma", "Spouses": "Emily", "Notes": "Father of Sarah, Adam"},
    {"Name": "Isla", "Gender": "Female", "Father": "Kevin", "Mother": "Linda", "Spouses": "", "Notes": "Adopted by Anna"},
    {"Name": "Noah", "Gender": "Male", "Father": "Kevin", "Mother": "Linda", "Spouses": "", "Notes": "–"},
    {"Name": "Alice", "Gender": "Female", "Father": "Kevin", "Mother": "Linda", "Spouses": "", "Notes": "–"},
    {"Name": "Zoe", "Gender": "Female", "Father": "Lucas", "Mother": "Linda", "Spouses": "", "Notes": "Adopted by Daniel"},
    {"Name": "Grace", "Gender": "Female", "Father": "Lucas", "Mother": "Linda", "Spouses": "", "Notes": "–"},
    {"Name": "Henry", "Gender": "Male", "Father": "Lucas", "Mother": "Linda", "Spouses": "", "Notes": "–"},
    {"Name": "Layla", "Gender": "Female", "Father": "Lucas", "Mother": "Linda", "Spouses": "", "Notes": "–"},
    {"Name": "Ryan", "Gender": "Male", "Father": "Lucas", "Mother": "Linda", "Spouses": "", "Notes": "–"},
    {"Name": "George", "Gender": "Male", "Father": "Liam", "Mother": "Nora", "Spouses": "", "Notes": "–"},
    {"Name": "Ella", "Gender": "Female", "Father": "Liam", "Mother": "Nora", "Spouses": "", "Notes": "–"},
    {"Name": "Sarah", "Gender": "Female", "Father": "James", "Mother": "Emily", "Spouses": "", "Notes": "–"},
    {"Name": "Adam", "Gender": "Male", "Father": "James", "Mother": "Emily", "Spouses": "", "Notes": "–"},
    {"Name": "Ivy", "Gender": "Female", "Father": "Tom", "Mother": "Olivia", "Spouses": "", "Notes": "–"},
    {"Name": "Daniel", "Gender": "Male", "Father": "Tom", "Mother": "Olivia", "Spouses": "", "Notes": "Adoptive father of Zoe"},
    {"Name": "Anna", "Gender": "Female", "Father": "Mark", "Mother": "Ella", "Spouses": "", "Notes": "Adoptive mother of Isla"},
    {"Name": "Mark", "Gender": "Male", "Father": "Mark", "Mother": "Diana", "Spouses": "", "Notes": "Descendant of Diana"}
]

# Create DataFrame
df = pd.DataFrame(family_data)

# Save to CSV
csv_path = "family-expert-system/data/family_facts.csv"
df.to_csv(csv_path, index=False)

# Print summary
print(f"Total number of people: {len(df)}")
print(f"Number of males: {df[df['Gender'] == 'Male'].shape[0]}")
print(f"Number of females: {df[df['Gender'] == 'Female'].shape[0]}")
print("\nFirst 5 rows preview:")
print(df.head().to_markdown(index=False))
