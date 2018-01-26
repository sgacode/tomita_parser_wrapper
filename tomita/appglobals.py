# coding=UTF-8

import os.path

CONFIGS_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '..',
    'configs'
)

TOMITA_BIN = '/usr/local/bin/tomita'

CONFIG_PERSONS = os.path.join(CONFIGS_PATH, 'config_person.proto')

LOGGER_NAME = 'tomita_parser'