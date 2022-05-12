from django.test import TestCase

from books.store.logic import operations


class LogicTestCase(TestCase):
    def test_plus(self):
        result = operations(6, 5, '+')
        self.assertEqual(11, result)

    def test_minus(self):
        result = operations(6, 7, '-')
        self.assertEqual(-1, result)


