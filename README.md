Forked from reyanvaldes/pydf1
https://github.com/reyanvaldes/pydf1.git

and

Forked from metalsartigan/pydf1
https://github.com/metalsartigan/pydf1.git

The names above created this respitory, I use it as a tool.

--------------------------

A very basic Allen Bradley DF1 protocol implementation in Python.

--------------------------

I changed some definitions to make it more user friendly for myself,
but believe that it can help others too. There is still more room for
development with this project.

--------------------------

Examples of the minor changes made are:

Original read binary/bit setup:
"def read_binary(self, file_table=3, start=0, bit=BIT.ALL, total_int=1) -> list():"

Modified read binary/bit setup:
"def read_b(self, file_table=int, start=0, bit=int, total_int=1) -> list():"

if bit == 0:
  bit =BIT.BIT0
if bit == 1:
  bit =BIT.BIT1
if bit == 2:
  bit =BIT.BIT2 ... and so on

if category == 'PRE':
  category = TIMER.PRE
elif category == 'ACC':
  category = TIMER.ACC ... and so on

This was done for all read and write calls. Again, very minor changes done to help myself.

--------------------------

I have used this library with both ML 1000 and SLC  5/04's.
