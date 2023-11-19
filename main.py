import copy
import re

import command
import log
import sys
import config
from tkinter import messagebox

if __name__ == '__main__':
    at_log = log.Log()
    at_command = command.Command()
    at_config = config.Config()

    try:
        at_err_flag = False
        at_log.initoutfile()

        at_config.initonlylist(".onlyconfig.ini")
        at_config.initrepeatlist(".repeatconfig.ini")
        at_config.initagreementnamelist(".agreementname.ini")

        at_log_path = sys.argv[1]
        at_file_log = open(at_log_path, 'r', encoding='utf-8')
        at_lines = at_file_log.readlines()
    except UnicodeDecodeError:
        messagebox.showinfo("提示:解析出错", "需要解析的LOG文件编码为UTF-8，配置文件的编码为GBK")
        at_err_flag = True
    except PermissionError:
        messagebox.showinfo("提示:解析出错", "请确认out.csv文件未被占用")
        at_err_flag = True
    finally:
        if at_err_flag:
            sys.exit()

    for at_line in at_lines:
        at_log.reset(at_line.rstrip("\n"))

        if at_log.isagreement() and at_log.isallowagreementsub:
            if not at_log.isagreementmain():
                at_command.add(at_log.str, False)
                at_log.isfinish = True

        if not at_log.isfinish:
            for at_item in at_config.onlylist:
                at_match = re.search(at_item, at_log.str)
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
                                if not at_command.length == 0:
                                    if at_command.cmdlist[0] in at_config.onlylist:
                                        print('other', at_command.cmdlist, at_command.retlist)
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
                    break
                else:
                    if at_log.isagreement() and at_log.isagreementmain():
                        at_log.isallowagreementsub = False


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
                                        print('find', at_command.cmdlist, at_command.retlist)
                                        at_log.outcommandtocsv(at_command, at_config)
                                        at_log.outcommand(at_command)
                            else:
                                if not at_command.length == 0:
                                    if at_command.cmdlist[0] in at_config.repeatlistist:
                                        print('other', at_command.cmdlist, at_command.retlist)
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
                        print('find3', at_log.str)
                        at_log.outstr(at_log.str)
                    break
                else:
                    if at_log.isagreement() and at_log.isagreementmain():
                        at_log.isallowagreementsub = False

    # 结束判断时,则根据条件输出当前协议
    # 协议历史去重开关判断
    if at_log.isopenonlyhistorylist or at_log.isopenrepeathistorylist:
        if not at_command.isequal(at_log.agreementhistorylist[at_command.head]):
            at_log.outcommandtocsv(at_command, at_config)
            at_log.outcommand(at_command)
        else:
            print("end 相同匹配项不输出")
    print("is end")
    messagebox.showinfo("提示", "已完成解析")