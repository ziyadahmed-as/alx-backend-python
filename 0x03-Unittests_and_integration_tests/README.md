## Unit Tests for Utility Functions

This repository contains a comprehensive set of unit tests for utility functions defined in the utils.py module. The test suite verifies the behavior of three key components:

access_nested_map

get_json

memoize (decorator)

These tests are written using Python’s built-in unittest framework and enhanced with parameterized for multiple test scenarios.

# 📂 Project Structure
The Structure of the Unit test assignment 
.
├── utils.py              # Contains utility functions and decorators (not included here)
├── test_utils.py         # This file – unit tests for functions in utils.py
└── README.md             # Project documentation
# ✅ Tested Components
1. access_nested_map
Tests the retrieval of values from nested dictionaries using a tuple path.
Includes:

Valid path access with expected return values

Invalid path access raising KeyError

2. get_json
Mocks HTTP GET requests to verify the get_json function returns the correct JSON payload.
Tests:

Requests to two different URLs with predefined responses

Ensures requests.get() is called once

3. memoize Decorator
Tests the custom @memoize decorator to ensure:

The decorated method is only executed once

The result is cached for subsequent calls

Correct result is returned