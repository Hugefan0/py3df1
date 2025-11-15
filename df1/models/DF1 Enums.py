from enum import Enum

PLC_SUPPORTED = {'MicroLogix 1100', 'MicroLogix 1000', 'SLC 500', 'SLC 5/03', 'SLC 5/04', 'PLC-5'}
SEND_SEQ_SLEEP_TIME = 0.0001  # magic with this sleep time to get faster processing in the Send Command sequence
WAIT_RECONNECT = 1  # Wait few seconds for open after close
EXPECT_MSG_SLEEP_TIME = 0.02 # Sleep time when receiving messages

BUFFER_SIZE = 4096
RECEIVE_TIMEOUT = 1
CONNECT_TIMEOUT = 5
THREAD_START_TIMEOUT = 2
SEND_QUEUE_SIZE = 100

class TxSymbol(Enum):
    """ Official doc page 2-6 """
    SOH = 0x01 # 0000 0010 - Half-Duplex
    STX = 0x02 # 0000 0001
    ETX = 0x03 # 0000 0011
    EOT = 0x04 # 0000 0100 - Half-Duplex
    ENQ = 0x05 # 0000 0101
    ACK = 0x06 # 0000 0110
    DLE = 0x10 # 0001 0000
    NAK = 0x0F # 0000 1111
    
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
    
class TIMER(Enum):
    """ Timer attributes"""
    EN = 0x01  # only the Enable bit
    TI = 0x02  # TT bit only
    DN = 0x03  # the Done Bit
    PRE = 0x04  # PRE category
    ACC = 0x05  # ACCumulator

    STATUS = 0x07  # return all status bits (EN, TI, DN)
"""timer
    0 EN
    1 TT
    2 DN
    3 PRE
    4 ACC"""
    
class COUNTER(Enum):
    """ Counter attributes"""
    CU = 0x01
    CD = 0x02
    DN = 0x03
    OV = 0x04
    UN = 0x05
    UA = 0x06
    PRE = 0x07
    ACC = 0x08
    STATUS = 0x09  # return all status bits (CU,CD,DN,OV,UN,UA)
    
"""counter 
0 CU
1 CD
2 DN
3 OV
4 UN
5 PRE
6 ACC"""


class BIT(Enum):
    """ BIT attributes"""
    BIT0 = 0x00
    BIT1 = 0x01
    BIT2 = 0x02
    BIT3 = 0x03
    BIT4 = 0x04
    BIT5 = 0x05
    BIT6 = 0x06
    BIT7 = 0x07
    BIT8 = 0x08
    BIT9 = 0x09
    BIT10 = 0x0A
    BIT11 = 0x0B
    BIT12 = 0x0C
    BIT13 = 0x0D
    BIT14 = 0x0E
    BIT15 = 0x0F
    ALL = 0xA0
    
class StsCodes(Enum):
    """Official doc page8-2 """

    """Local STS Error Codes"""
    SUCCESS = 0x0
    DST_OUT_OF_BUFFER = 0x01
    DELIVERY_NOT_GUARANTEED_NO_ACK = 0x02
    DUPLICATE_TOKEN_HOLDER = 0x03
    LOCAL_PORT_DISCONNECTED = 0x04
    APP_LAYER_TIMEOUT_WAITING_FOR_RESPONSE = 0x05
    DUPLICATE_NODE_DETECTED = 0x06
    STATION_OFFLINE = 0x07
    HARDWARE_FAULT = 0x08

    """Remote STS Error Codes"""
    ILLEGAL_COMMAND_OR_FORMAT = 0x10
    HOST_PROBLEM_WONT_COMMUNICATE = 0x20
    REMOTE_HOST_MISSING = 0x30
    REMOTE_HARDWARE_FAULT = 0x40
    ADDRESS_PROBLEM_OR_MEMORY_PROTECT_RUNGS = 0x50
    COMMAND_PROTECTION_SELECTION = 0x60
    PROCESSOR_IN_PROGRAM_MODE = 0x70
    COMPATIBILITY_FILE_MISSING_OR_COMM_ZONE_PROBLEM = 0x80
    CANNOT_BUFFER_COMMAND = 0x90
    WAIT_ACK_BUFFER_FULL = 0xA0
    PROBLEM_DUE_TO_DOWNLOAD = 0xB0
    WAIT_ACK_BUFFER_FULL_2 = 0xC0
    UNUSED_1 = 0xD0
    UNUSED_2 = 0xE0
    ERROR_CODE_IN_EXT_STS_BYTE = 0xF0
    
INITIAL_MODBUS = 0xFFFF
INITIAL_DF1 = 0x0000

table = (
    0x0000, 0xC0C1, 0xC181, 0x0140, 0xC301, 0x03C0, 0x0280, 0xC241,
    0xC601, 0x06C0, 0x0780, 0xC741, 0x0500, 0xC5C1, 0xC481, 0x0440,
    0xCC01, 0x0CC0, 0x0D80, 0xCD41, 0x0F00, 0xCFC1, 0xCE81, 0x0E40,
    0x0A00, 0xCAC1, 0xCB81, 0x0B40, 0xC901, 0x09C0, 0x0880, 0xC841,
    0xD801, 0x18C0, 0x1980, 0xD941, 0x1B00, 0xDBC1, 0xDA81, 0x1A40,
    0x1E00, 0xDEC1, 0xDF81, 0x1F40, 0xDD01, 0x1DC0, 0x1C80, 0xDC41,
    0x1400, 0xD4C1, 0xD581, 0x1540, 0xD701, 0x17C0, 0x1680, 0xD641,
    0xD201, 0x12C0, 0x1380, 0xD341, 0x1100, 0xD1C1, 0xD081, 0x1040,
    0xF001, 0x30C0, 0x3180, 0xF141, 0x3300, 0xF3C1, 0xF281, 0x3240,
    0x3600, 0xF6C1, 0xF781, 0x3740, 0xF501, 0x35C0, 0x3480, 0xF441,
    0x3C00, 0xFCC1, 0xFD81, 0x3D40, 0xFF01, 0x3FC0, 0x3E80, 0xFE41,
    0xFA01, 0x3AC0, 0x3B80, 0xFB41, 0x3900, 0xF9C1, 0xF881, 0x3840,
    0x2800, 0xE8C1, 0xE981, 0x2940, 0xEB01, 0x2BC0, 0x2A80, 0xEA41,
    0xEE01, 0x2EC0, 0x2F80, 0xEF41, 0x2D00, 0xEDC1, 0xEC81, 0x2C40,
    0xE401, 0x24C0, 0x2580, 0xE541, 0x2700, 0xE7C1, 0xE681, 0x2640,
    0x2200, 0xE2C1, 0xE381, 0x2340, 0xE101, 0x21C0, 0x2080, 0xE041,
    0xA001, 0x60C0, 0x6180, 0xA141, 0x6300, 0xA3C1, 0xA281, 0x6240,
    0x6600, 0xA6C1, 0xA781, 0x6740, 0xA501, 0x65C0, 0x6480, 0xA441,
    0x6C00, 0xACC1, 0xAD81, 0x6D40, 0xAF01, 0x6FC0, 0x6E80, 0xAE41,
    0xAA01, 0x6AC0, 0x6B80, 0xAB41, 0x6900, 0xA9C1, 0xA881, 0x6840,
    0x7800, 0xB8C1, 0xB981, 0x7940, 0xBB01, 0x7BC0, 0x7A80, 0xBA41,
    0xBE01, 0x7EC0, 0x7F80, 0xBF41, 0x7D00, 0xBDC1, 0xBC81, 0x7C40,
    0xB401, 0x74C0, 0x7580, 0xB541, 0x7700, 0xB7C1, 0xB681, 0x7640,
    0x7200, 0xB2C1, 0xB381, 0x7340, 0xB101, 0x71C0, 0x7080, 0xB041,
    0x5000, 0x90C1, 0x9181, 0x5140, 0x9301, 0x53C0, 0x5280, 0x9241,
    0x9601, 0x56C0, 0x5780, 0x9741, 0x5500, 0x95C1, 0x9481, 0x5440,
    0x9C01, 0x5CC0, 0x5D80, 0x9D41, 0x5F00, 0x9FC1, 0x9E81, 0x5E40,
    0x5A00, 0x9AC1, 0x9B81, 0x5B40, 0x9901, 0x59C0, 0x5880, 0x9841,
    0x8801, 0x48C0, 0x4980, 0x8941, 0x4B00, 0x8BC1, 0x8A81, 0x4A40,
    0x4E00, 0x8EC1, 0x8F81, 0x4F40, 0x8D01, 0x4DC0, 0x4C80, 0x8C41,
    0x4400, 0x84C1, 0x8581, 0x4540, 0x8701, 0x47C0, 0x4680, 0x8641,
    0x8201, 0x42C0, 0x4380, 0x8341, 0x4100, 0x81C1, 0x8081, 0x4040)

'''''''''
def compute_crc(data):
    """ Data is what's BETWEEN the initial DLE STX and the final DLE ETX. """
    data = list(data)
    data.append(0x03)  # Because Allen Bradley...
    crc = INITIAL_DF1
    for a in data:
        idx = table[(crc ^ a) & 0xff]
        crc = ((crc >> 8) & 0xff) ^ idx
    swapped = ((crc << 8) & 0xff00) | ((crc >> 8) & 0x00ff)
    return swapped
'''

'''''''''
No Parity
start bit
data bit 0
data bit 1
data bit 2
data bit 3
data bit 4
data bit 5
data bit 6
data bit 7
one stop bit

With Parity
start bit
data bit 0
data bit 1
data bit 2
data bit 3
data bit 4
data bit 5
data bit 6
data bit 7
even parity bit
one stop bit
'''

'''''''''
How the Transmitter Operates
The following program describes the actions of the transmitter:

TRANSMITTER is defined as
loop
Message=GET-MESSAGE-TO-SEND
Status=TRANSFER(Message)
SIGNAL-RESULTS(Status)
end loop
loop
WAIT for response on path 2 or timeout.
if received DLE ACK then return SUCCESS
else if received DLE NAK then
if nak-limit is exceeded then return FAILURE
else
begin
count NAK re-tries;
SEND-MESSAGE(message);
start timeout
end
else if timeout
if enq-limit is exceeded then return FAILURE
else
begin
count ENQ re-tries;
send DLE ENQ on path 1;
start timeout
end
end loop
SEND (message) is defined as
begin
BCC = 0
send DLE STX on path 1
for every byte in the message do
begin
add the byte to the BCC;
send the corresponding data symbol
on
path 1
end
send DLE ETX BCC on path 1
end
GET-MESSAGE-TO-SEND
This is an operating-system-dependent interface
routine that waits and allows the rest of the
system to run until the message source has supplied
 a message to be sent.
SIGNAL-RESULTS
This is an implementation-dependent routine that
tells the message source of the results of the
attempted message transfer.
WAIT
This is an operating-system-dependent routine
that waits for any of several events to occur
while allowing other parts of the system to run.
TRANSFER (Message) is defined as
initialize nak-limit and enq-limit
SEND(Message)
start timeout
'''

'''''''''
The following program describes the actions of the receiver in detail.

RECEIVER is defined as
variables
LAST-HEADER is 4 bytes copied out of the last good message
RESPONSE is the value of the last ACK or NAK sent
BCC is an 8-bit block check accumulator
LAST-HEADER = invalid
LAST RESPONSE = NAK
loop
reset parity error flag
GET-SYMBOL
if DLE STX then
begin
BCC = 0
GET-SYMBOL
while it is a data symbol
begin
if buffer is not overflowed put
data in buffer
GET-SYMBOL
end
if the control symbol is not a DLE ETX then send DLE
NAK
else if error flag is set then send DLE NAK
else if BCC is not zero then send DLE NAK
else if message is too small then send DLE NAK
else if message is too large then send DLE NAK
else if header is same as last message send a DLE ACK
else if message sink is full send DLE NAK
else
begin
send message to message sink
send a DLE ACK
save a last header
end
end
else if DLE ENQ then send LAST-RESPONSE
else LAST-RESPONSE = NAK
end loop
GET-SYMBOL is defined as
loop
GET-CHAR
if char is not DLE
begin
add char to BCC
return the char and data flag
end
else
begin
GET-CHAR
if char is a DLE
begin
add char to BCC
return DLE and data flag
end
else if char is an ACK or NAK send it to the transmitter
else if char is an ETX
begin
GET-CHAR
add char to BCC
return ETX with a control flag
end
else return char with a control flag
end
end loop
'''
'''''''''
apply port configuration 0F 8F    7-4
bit write 0F 02 ➄  7-4
change mode
0F 3A   7-5
change mode 0F 80   7-5
close file 0F 82     7-5
diagnostic status 06 03         ➄ 7-6
disable forces 0F 41     ➄ ➄ 7-6
disable outputs 07 00  7-6
download all request 0F 50  ➄  7-7
download completed 0F 52      ➄  7-7
download request 0F 05  7-8
echo 06 00         ➄ 7-8
enable outputs 07 01  7-9
enable PLC scanning 07 03  7-9
enter download mode 07 04  7-9
enter upload mode 07 06  7-10
exit download/upload mode 07 05  7-10
file read 0F 04   7-10
file write 0F 03   7-11
get edit resource 0F 11     ➄  7-11
initialize memory 0F 57     ➄ ➄ 7-12
modify PLC-2 compatibility
file 0F 5E  7-12
open file 0F 81     7-13
physical read
04    7-13
physical read 0F 09  7-13
physical write 0F 08  7-14
protected bit write 02       7-15
protected typed file read 0F A7    7-16

'''
