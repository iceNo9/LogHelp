import re

class Log(object):
    def __init__(self, rv_str:=""):
        self.str = rv_str

    def reset(self, rv_str):
        self.str = rv_str

    def isagreement(self):
        at_match = re.search("\[0x..]-", self.str)
        if at_match:
            return True
        else:
            return False

        
        