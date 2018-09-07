# from asterisk.agi import *
#
# agi = AGI()
# agi.verbose("python agi started")
# callerId = agi.env['agi_callerid']
# agi.verbose("call from %s" % callerId)
#
# while True:
#     agi.stream_file('vm-extension')
#     result = agi.wait_for_digit(-1)
#     agi.verbose("got digit %s" % result)
#     if result.isdigit():
#         agi.say_number(result)
#     else:
#         agi.verbose("bye!")
#         agi.hangup()
#         sys.exit()

import sys
import os
from asterisk.agi import AGI


def test_call(agi=None, text=""):
    agi.say_alpha(text, "#")
    agi.hangup()


if __name__ == "__main__":
    text = 'abcdefr'
    agi = AGI()
    test_call(agi, text)
