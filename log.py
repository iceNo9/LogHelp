import re
import command
import csv
from tkinter import messagebox


class Log(object):
    def __init__(self, rv_str=""):
        self.str = rv_str
        self.isfinish = False
        self.isallowagreementsub = False
        self.agreementhistorylist = [command.Command()] * 256
        self.isopenonlyhistorylist = False
        self.isopenrepeathistorylist = True

    def reset(self, rv_str):
        self.str = rv_str
        self.isfinish = False

    def isagreement(self):
        at_match = re.search("\[0x..\]-", self.str)
        if at_match:
            return True
        else:
            return False

    def isagreementmain(self):
        at_match = re.search("CMD", self.str)
        if at_match:
            return True
        else:
            return False

    def modifyhistoryagreement(self, rv_agreement):
        self.agreementhistorylist[rv_agreement.head] = rv_agreement

    def initoutfile(self):
        with open('out.log', 'w') as at_file:
            at_file.truncate()
        with open('out.csv', 'w') as at_file:
            at_file.truncate()

    def outcommandtocsv(self, rv_command, rv_config):
        with open('out.csv', 'w', newline='') as at_file:
            at_writer = csv.writer(at_file)
            at_col_1 = rv_config.agreementnamelist[rv_command.head]
            at_col_2 = ''
            at_col_3 = ''
            at_col_4 = ''

            at_head_flag = True
            for at_item in rv_command.cmdlist:
                if at_head_flag:
                    at_col_2 = at_item
                    at_head_flag = False

                at_col_2 += ',' + at_item

            at_head_flag = True
            for at_item in rv_command.retlist:
                if at_head_flag:
                    at_col_3 = at_item
                    at_head_flag = False

                at_col_3 += ',' + at_item

            at_head_flag = True
            for at_item in rv_command.srclist:
                if at_head_flag:
                    at_col_4 = at_item
                    at_head_flag = False

                at_col_4 += '\n' + at_item

            at_writer.writerow([at_col_1, at_col_2, at_col_3, at_col_4])

    def outcommand(self, rv_command):
        with open('out.log', 'a') as at_file:
            at_head_flag = True
            at_str = ''
            for at_item in rv_command.srclist:
                if at_head_flag:
                    at_str = at_item
                    at_head_flag = False

                at_str += '\n' + at_item

            at_file.write(at_str + "\n")


    def outstr(self, rv_str):
        with open('out.log', 'a') as at_file:
            at_file.write(rv_str + "\n")
