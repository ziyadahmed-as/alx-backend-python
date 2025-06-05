#!/usr/bin/env python3
"""
test_utils.py

This module contains unit tests for the following utility functions and decorators:

1. access_nested_map: Safely access values in nested dictionaries using a tuple of keys.
2. get_json: Fetch and return the JSON response from a given URL using requests.
3. memoize: A caching decorator that stores the result of a method after the first call.
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json
from utils import memoize

# TestAccessNestedMap class to test the access_nested_map function
class TestAccessNestedMap(unittest.TestCase):
    """Tests for the access_nested_map function."""
    # Test case for parameterized data to check various scenarios
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    
    # Test access_nested_map with various nested maps and paths 
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map returns expected value."""
        self.assertEqual(access_nested_map(nested_map, path), expected)
        
    # Test case for parameterized data to check exceptions
    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b'),
    ])
    # Test access_nested_map raises KeyError for invalid paths
    def test_access_nested_map_exception(self, nested_map, path, expected_key):
        """Test access_nested_map raises KeyError with the correct message."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), f"'{expected_key}'")
      
#thi class to test the get_json and hold payload of the data 
class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        # Create a mock response object
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        # Patch requests.get to return our mock response
        with patch('requests.get') as mock_get:
            mock_get.return_value = mock_response

            # Call the function
            result = get_json(test_url)

            # Assert that requests.get was called exactly once with test_url
            mock_get.assert_called_once_with(test_url)

            # Assert that the output of get_json is equal to test_payload
            self.assertEqual(result, test_payload)
                  
  # TestMemoize class to test the memoize decoratorimport unittest


# TestMemoize class to test the memoize decorator
class TestMemoize(unittest.TestCase):
    def test_memoize(self):
        """Test that the memoize decorator caches the result properly"""
        
        # Define test class with memoized property
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        # Create instance and mock the method
        test_instance = TestClass()
        
        with patch.object(TestClass, 'a_method', return_value=42) as mock_method:
            # First call - should call a_method
            self.assertEqual(test_instance.a_property(), 42)
            
            # Second call - should use cached value
            self.assertEqual(test_instance.a_property(), 42)
            
            # Verify a_method was called only once
            mock_method.assert_called_once()
