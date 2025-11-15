# -*- coding: utf-8 -*-

from enum import Enum


class FileType(Enum):
    """ from official doc page  7-17"""
    #  80-83 reserved
    STATUS = 0x84
    BIT = 0x85
    TIMER = 0x86
    COUNTER = 0x87
    CONTROL = 0x88
    INTEGER = 0x89
    FLOAT = 0x8A
    OUT_LOGIC = 0x8B
    IN_LOGIC = 0x8C
    STRING = 0x8D
    ASCII = 0x8E
    BCD = 0x8F
