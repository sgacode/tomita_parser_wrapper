# coding=UTF-8

import os
import subprocess
import logging
from typing import List
import xml.etree.ElementTree as ElementTree

from . import appglobals


logger = logging.getLogger(appglobals.LOGGER_NAME)


class ParserException(Exception):
    pass


class DocumentFact:
    
    def __init__(self, value: str, fact_id: int, fact_pos: int, fact_len: int, lead_id: int=None):
        self.value = value
        self.fact_id = fact_id
        self.fact_pos = fact_pos
        self.fact_len = fact_len
        self.lead_id = lead_id
        
    def __str__(self):
        return str(self.__dict__)
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        return (self.value == other.value and self.fact_id == other.fact_id and self.fact_pos == other.fact_pos
                and self.fact_len == other.fact_len)
        
        
class TomitaParser(object):
    
    def __init__(self, config: str=None, tomita_bin: str=None):
        self.bin = tomita_bin or appglobals.TOMITA_BIN
        if not os.path.exists(self.bin):
            raise ParserException('Tomita executable not found at: {0}'.format(self.bin))
        
        self.config = config
        if not os.path.exists(self.config):
            raise ParserException('Tomita config not found at: {0}'.format(self.config))
        
        logger.debug('Init tomita parser {0} with config {1}'.format(self.bin, self.config))

    def parse(self, text: str) -> List[DocumentFact]:
        logger.debug('Start parse text')
        
        pipe = subprocess.Popen(
            [self.bin, self.config],
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=appglobals.CONFIGS_PATH
        )
        out, err = pipe.communicate(input=text.encode('utf-8'))
        facts = self.parse_facts(out)
        logger.debug('End parse text, found {0} facts'.format(len(facts)))
        
        return facts
    
    def parse_facts(self, response: bytes) -> List[DocumentFact]:
        facts = []
        etree_root = ElementTree.fromstring(response)
        document_element = etree_root.find('document')
        if document_element is None:
            return facts
    
        for fact_element in document_element.find("facts"):
            facts.append(
                DocumentFact(
                    fact_element.find('Name').attrib.get('val'),
                    int(fact_element.attrib.get('FactID')),
                    int(fact_element.attrib.get('pos')),
                    int(fact_element.attrib.get('len')),
                    int(fact_element.attrib.get('LeadID')),
                )
            )
        
        return facts
