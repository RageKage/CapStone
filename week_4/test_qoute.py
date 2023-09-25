import unittest 
from unittest import TestCase

import quote

class QouteTest(TestCase):
    def test_get_quote_for_small_lawn_same_day(self):
        self.assertEqual(15, quote.lawn_quote("small", True))
        
        
    def test_get_quote_for_small_lawn_not_same_day(self):
        actual_qoute = quote.lawn_quote("small", False)
        expected_qoute = 10
        self.assertEqual(expected_qoute, actual_qoute)
    
    def  test_get_quote_for_medium_lawn_same_day(self):
        actual_qoute = quote.lawn_quote("medium", True)
        expected_qoute = 20
        self.assertEqual(expected_qoute, actual_qoute)
        
    def  test_get_quote_for_medium_lawn_same_day(self):
        actual_qoute = quote.lawn_quote("medium", False)
        expected_qoute = 15
        self.assertEqual(expected_qoute, actual_qoute)
        
    def  test_get_quote_for_large_lawn_same_day(self):
        actual_qoute = quote.lawn_quote("large", True)
        expected_qoute = 25
        self.assertEqual(expected_qoute, actual_qoute)
        
    def  test_get_quote_for_large_lawn_not_same_day(self):
        actual_qoute = quote.lawn_quote("large", False)
        expected_qoute = 20
        self.assertEqual(expected_qoute, actual_qoute)
        
    def  test_quote_for_unknown_size(self):
        actual_qoute = quote.lawn_quote("AAAA", False)

        self.assertIsNone( actual_qoute)
        
        
        
        
if __name__ == "__main__":
    unittest.main()