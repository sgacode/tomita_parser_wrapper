# coding=UTF-8

import unittest
from typing import List

from unittest_data_provider import data_provider

from tomita import appglobals
from tomita.parser import TomitaParser, DocumentFact
from .data_providers import *


class TestParsePersons(unittest.TestCase):
    
    @data_provider(persons_data_provider)
    def test_parse_persons(self, text: str, facts: List[DocumentFact]):
        parser = TomitaParser(appglobals.CONFIG_PERSONS)
        parsed_facts = parser.parse(text)
        self.assertEqual(parsed_facts, facts)