import re
from operator import eq

class Command(object):
    def __init__(self, head) -> None:
        self.head = head
        self.length = 1
        self.cmdlist = []
        self.retlist = []

    def addsub(self, rv_cmd, rv_ret):
        self.cmdlist.append(rv_cmd)
        self.retlist.append(rv_ret)

    def isequal(self, rv_command)
        if not self.length == rv_command.length:
            return False
        else:
            at_is_cmdlist_equal_flag = eq(self.cmdlist, rv_command.cmdlist)
            at_is_retlist_equal_flag = eq(self.retlist, rv_command.retlist)
            return at_is_cmdlist_equal_flag & at_is_retlist_equal_flag




