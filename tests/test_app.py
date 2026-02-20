import unittest

from app import greeting, normalize_name


class TestApp(unittest.TestCase):
    def test_normalize_name_strips_and_collapse_spaces(self) -> None:
        self.assertEqual(normalize_name("  Ada   Lovelace "), "Ada Lovelace")

    def test_greeting(self) -> None:
        self.assertEqual(greeting("Ada"), "Hola, Ada!")
