from dataclasses import is_dataclass
import unittest
from src.domain.customer.entities import Customer


class TestCustomerUnit(unittest.TestCase):

    def test_if_is_dataclass(self):
        self.assertTrue(is_dataclass(Customer))