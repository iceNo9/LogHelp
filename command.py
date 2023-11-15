import re
from operator import eq

class Command(object):
    def __init__(self, head) -> None:
        self.head = head
        self.length = 1
        self.srclist = []
        self.cmdlist = []
        self.retlist = []

    def getcmdvalue(rv_str):
        
    def getretvalue(rv_str):
        

    def addsub(self, rv_str):
        self.srclist.append(rv_str)
        self.cmdlist.append(self.getcmdvalue(rv_str))
        self.retlist.append(self.getretvalue(rv_str))

    def isequal(self, rv_command)
        if not self.length == rv_command.length:
            return False
        else:
            at_is_cmdlist_equal_flag = eq(self.cmdlist, rv_command.cmdlist)
            at_is_retlist_equal_flag = eq(self.retlist, rv_command.retlist)
            return at_is_cmdlist_equal_flag & at_is_retlist_equal_flag




