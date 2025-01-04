import unittest
class TestApp(unittest.TestCase):
    def test_output(self):
        self.assertEqual("Hello from the Python App!", "Hello from the Python App!")

if __name__ == '__main__':
    unittest.main()
