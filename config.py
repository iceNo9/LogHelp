import os
class Config(object):
    def __init__(self):
        self.onlylist = []
        self.repeatlist = []
        self.agreementnamelist = [""] * 256

    def initonlylist(self, rv_path):
        at_file_size = os.path.getsize(rv_path)
        if at_file_size:
            at_file_config = open(rv_path, 'r')
            at_lines = at_file_config.readlines()
            for at_line in at_lines:
                self.onlylist.append(at_line.rstrip("\n"))

    def initrepeatlist(self, rv_path):
        at_file_size = os.path.getsize(rv_path)
        if at_file_size:
            at_file_config = open(rv_path, 'r')
            at_lines = at_file_config.readlines()
            for at_line in at_lines:
                self.repeatlist.append(at_line.rstrip("\n"))

    def initagreementnamelist(self, rv_path):
        at_file_size = os.path.getsize(rv_path)
        if at_file_size:
            at_file_config = open(rv_path, 'r')
            at_lines = at_file_config.readlines()
            for at_line in at_lines:
                at_str = at_line.rstrip("\n")
                at_command_head = eval(at_str[0:4])
                at_command_name = at_str[5:len(at_str)]
                self.agreementnamelist[at_command_head] = at_command_name

