import sys
import os
import pytest

# Add the project root to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "family-expert-system"))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Define the path to the test file relative to the project root
test_file_path = os.path.join(project_root, "tests", "test_relations.py")

print(f"Running pytest with project_root: {project_root}")
print(f"Test file path: {test_file_path}")
print(f"sys.path: {sys.path}")

# Run pytest
# pytest.main() will run all tests discovered in the current directory and subdirectories
# We can also specify the test file directly: pytest.main([test_file_path])
# For this task, let's run all tests in the 'tests' directory within the project root
pytest.main([os.path.join(project_root, "tests")])
