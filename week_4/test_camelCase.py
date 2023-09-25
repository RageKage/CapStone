import unittest
from unittest import TestCase

import camelCase

class CamelCaseTest(TestCase):
    
    def test_camel_case_sentence(self):
        self.assertEqual("helloWorld", camelCase.camel_case("Hello World"))
        
    def test_camel_case_sentence_with_spaces(self):
        self.assertEqual("helloWorld", camelCase.camel_case("Hello    World"))
        self.assertEqual("helloWorld", camelCase.camel_case("    Hello World"))
        self.assertEqual("helloWorld", camelCase.camel_case("Hello World    "))
        self.assertEqual("helloWorld", camelCase.camel_case("Hello  World   "))
        
    
    def test_camel_case_sentence_with_blank_or_empty_string(self):
        self.assertEqual("", camelCase.camel_case(""))
        self.assertEqual("", camelCase.camel_case("    "))
        
        
    def test_camel_case_sentence_with_numbers_or_puncation(self):
        self.assertEqual("", camelCase.camel_case("123"))
        self.assertEqual("", camelCase.camel_case("Hello World! asdasd 12312312 #$%^&"))
        self.assertEqual("", camelCase.camel_case("@#$%^&*"))
    

        

if __name__ == "__main__":
    unittest.main()