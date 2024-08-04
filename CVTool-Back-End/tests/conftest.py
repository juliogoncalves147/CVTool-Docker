import sys
import os

# Append the root directory of the project to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

print("sys.path:", sys.path)  # Debugging line to ensure path is set correctly
