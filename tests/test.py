import unittest
from unittest.mock import patch 
from io import StringIO 
from src.add import add, hello_world, subtract

class TestFn(unittest.TestCase):

    def setUp(self):
        pass

    def test_add(self):
        expected = 6
        actual = add(4, 2)
        self.assertEqual(expected, actual)
        
        expected = 4
        actual = add(0, 4)
        self.assertEqual(expected, actual)
        
    def test_hello(self):
        expected = "Hello World"
        actual = hello_world()
        self.assertEqual(expected, actual)
        
    def test_subtract(self):
        expected = 2
        actual = subtract(4, 2)
        self.assertEqual(expected, actual)
        
        expected = 4
        actual = add(0, 4)
        self.assertEqual(expected, actual)
        
    def tearDown(self):
        print("Testing Done")   
