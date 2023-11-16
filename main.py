import copy
import re

import command
import log
import sys
import config

if __name__ == '__main__':
    at_log = log.Log()
    at_command = command.Command()
    at_config = config.Config()

    at_log.initoutfile()

    at_config.initonlylist(".onlyconfig.ini")
    at_config.initrepeatlist(".repeatconfig.ini")
    at_config.initagreementnamelist(".agreementname.ini")

    at_log_path = sys.argv[1]
    at_file_log = open(at_log_path, 'r')
    at_lines = at_file_log.readlines()

    for at_line in at_lines:
        at_log.reset(at_line.rstrip("\n"))
        print(at_log.str)

        if at_log.isagreement() and at_log.isallowagreementsub:
            if not at_log.isagreementmain():
                at_command.add(at_log.str, False)
                at_log.isfinish = True

        if not at_log.isfinish:
            for at_item in at_config.onlylist:
                at_match = re.search(at_item, at_log.str)
                print(at_match,at_item,at_log.str)
                if at_match:
                    at_log.isfinish = True
                    if at_log.isagreement():
                        if at_log.isagreementmain():
                            # 协议历史去重开关判断
                            if at_log.isopenonlyhistorylist:
                                # 先处理旧的指令
                                if not at_command.length == 0:
                                    if not at_command.isequal(at_log.agreementhistorylist[at_command.head]):
                                        at_log.outcommandtocsv(at_command, at_config)
                                        at_log.outcommand(at_command)
                                    else:
                                        print("单匹相同匹配项不输出")
                            else:
                                at_log.outcommandtocsv(at_command, at_config)
                                at_log.outcommand(at_command)

                            # 拷贝新实例加入历史记录
                            at_tmp_command = copy.deepcopy(at_command)
                            at_log.agreementhistorylist[at_tmp_command.head] = at_tmp_command
                            at_command.reset()
                            at_command.add(at_log.str, True)

                            # 允许子协议
                            at_log.isallowagreementsub = True
                    else:
                        at_log.outstr(at_log.str)

        if not at_log.isfinish:
            for at_item in at_config.repeatlist:
                at_match = re.search(at_item, at_log.str)
                if at_match:
                    at_log.isfinish = True
                    if at_log.isagreement():
                        if at_log.isagreementmain():
                            # 协议历史去重开关判断
                            if at_log.isopenrepeathistorylist:
                                # 先处理旧的指令
                                if not at_command.length == 0:
                                    if not at_command.isequal(at_log.agreementhistorylist[at_command.head]):
                                        at_log.outcommandtocsv(at_command, at_config)
                                        at_log.outcommand(at_command)
                                    else:
                                        print("单匹相同匹配项不输出")
                            else:
                                at_log.outcommandtocsv(at_command, at_config)
                                at_log.outcommand(at_command)

                            # 拷贝新实例加入历史记录
                            at_tmp_command = copy.deepcopy(at_command)
                            at_log.agreementhistorylist[at_tmp_command.head] = at_tmp_command
                            at_command.reset()
                            at_command.add(at_log.str, True)

                            # 允许子协议
                            at_log.isallowagreementsub = True
                    else:
                        at_log.outstr(at_log.str)

    # 结束判断时，如果允许子协议，则输出当前协议
    if at_log.isallowagreementsub:
        at_log.outcommandtocsv(at_command, at_config)
        at_log.outcommand(at_command)

    print("is end")
