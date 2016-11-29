import unittest

from cenaming.name_shortener import (
    remove_the, remove_slashed_numbers, remove_state_suffix,
    remove_parenthesis_numbers, remove_with_comma, remove_compound,
    remove_end_descriptors, remove_org_descriptors
)


class TestHelperFunctions(unittest.TestCase):
    def test_remove_the(self):
        self.check_name(remove_the('The Some Company'))

    def test_remove_slashed_numbers(self):
        self.check_name(remove_slashed_numbers('Some Company /1999/'))

    def test_remove_parenthesis_numbers(self):
        self.check_name(remove_parenthesis_numbers('Some Company (1999)'))

    def test_remove_state_suffix(self):
        self.check_name(remove_state_suffix('Some Company (New York)'))

    def test_remove_compound(self):
        self.check_name(remove_compound('Some Company Holdings, Inc.'))

    def test_remove_with_comma(self):
        self.check_name(remove_with_comma('Some Company, Inc.'))
        self.check_name(remove_with_comma('Some Company'))

    def test_remove_end_descriptors(self):
        self.check_name(remove_end_descriptors('Some Company SA LTD'))

    def test_remove_org_descriptors(self):
        company_name = 'The Some Company, Inc. Corp LLC'
        self.check_name(remove_org_descriptors(company_name))

    def check_name(self, result):
        self.assertEquals('Some Company', result)
