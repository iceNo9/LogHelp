import re
from operator import eq


class Command(object):
    def __init__(self) -> None:
        self.head = 0
        self.length = 0
        self.srclist = []
        self.cmdlist = []
        self.retlist = []

    def reset(self):
        self.head = 0
        self.length = 0
        self.srclist = []
        self.cmdlist = []
        self.retlist = []
    def getcmdvalue(self, rv_str):
        at_match = re.search("\[0x..\]-", rv_str)
        return rv_str[at_match.start() + 1: at_match.end() - 2]

    def getretvalue(self, rv_str):
        at_match = re.search("\[0x..\]-", rv_str)
        return rv_str[at_match.end() + 2: at_match.end() + 6]

    def add(self, rv_str, rv_is_main):
        at_cmd_str = self.getcmdvalue(rv_str)
        self.srclist.append(rv_str)
        self.cmdlist.append(at_cmd_str)
        self.retlist.append(self.getretvalue(rv_str))
        if rv_is_main:
            self.head = eval(at_cmd_str)

    def isequal(self, rv_command):
        if not self.length == rv_command.length:
            return False
        else:
            at_is_cmdlist_equal_flag = eq(self.cmdlist, rv_command.cmdlist)
            at_is_retlist_equal_flag = eq(self.retlist, rv_command.retlist)
            return at_is_cmdlist_equal_flag & at_is_retlist_equal_flag
