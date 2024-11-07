# test_app.py
import unittest
from app import add, subtract

class TestApp(unittest.TestCase):
    # Positive scenario
    def test_add(self):
        self.assertEqual(add(5, 5), 10)
    
    # Negative scenario
    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)

    # Edge case
    def test_add_edge_case(self):
        self.assertEqual(add(0, 0), 0)

if __name__ == "__main__":
    unittest.main()
