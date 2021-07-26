from django.test import TestCase

# Create your tests here.
class DemoTests(TestCase):
    def setUp(self):
        self.actual = 1
        self.expected = 1
    def test_actual_expected(self):
        self.assertEqual(self.expected, self.actual)
        self.assertEqual(self.expected, 2)
