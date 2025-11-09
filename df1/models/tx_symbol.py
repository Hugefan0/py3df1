# -*- coding: utf-8 -*-

from enum import Enum


class TxSymbol(Enum):
    """ Official doc page 2-6 """
    SOH = 0x01 # 0000 0010 - Half-Duplex
    STX = 0x02
    ETX = 0x03
    EOT = 0x04 # 0000 0100 - Half-Duplex
    ENQ = 0x05
    ACK = 0x06
    DLE = 0x10
    NAK = 0x0f
