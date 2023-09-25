
import unittest
from unittest import TestCase

import area

class AreaTest(TestCase):
    
    def test_triangle_area(self):
        self.assertEqual(10, area.tri_area(5, 4))
        
    def test_triangle_area_floating_point(self):
        self.assertAlmostEqual(17.79875, area.tri_area(7.25, 4.91))
        
    def test_negative_base_height_raises_value_error(self):
        with self.assertRaises(ValueError):
            area.tri_area(-5, 4)
        
        with self.assertRaises(ValueError):
            area.tri_area(2, -4)
            
        with self.assertRaises(ValueError):
            area.tri_area(-2, -4)        
        
    def test_area_height_or_base_zero_raises_ValueError(self):
        self.assertEqual(0, area.tri_area(0, 4))
        self.assertEqual(0, area.tri_area(0, 0))
        self.assertEqual(0, area.tri_area(1,0))
        
    


if __name__ == "__main__":
    unittest.main()