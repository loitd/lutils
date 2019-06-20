import paramiko, socket
import sys
from lutils import printlog

class LServer(object):
    """docstring for LServer"""
    def __init__(self):
        super(LServer, self).__init__()
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
        self.chan = None
        self.error = 'No error founds while connecting'
        # printlog(self.error)

    def connect(self, ip, uname, pw):
        try:
            self.client.connect(ip, username=uname, password=pw)
            self.chan = self.client.invoke_shell()
            printlog("Successfull connected to %s"%ip)
            self.chan.settimeout(5.0)
            self.error = 'No error founds while connecting'
            return True
        except Exception as e:
            self.error = e
            self.chan = None
            printlog(e)
            return False

    def getfeedback(self, regcode = ']#'):
        try:
            printlog("Waiting for reply until timeout...")
            buff = ''
            while buff.find(regcode) == -1:
                    resp = self.chan.recv(9999999)
                    buff = "{0}{1}".format(buff, resp)
                    printlog(buff)
            return buff
        except socket.timeout:
            printlog("Time out while waiting for response from server. Program will exits.")
            sys.exit(1)
        except Exception as e:
            raise(e)
            # printlog(e)
            # sys.exit(1)
    
    def  getdiskspace(self):
        if self.chan is not None:
            self.getfeedback()
            printlog("Begin get disk space ...")
            self.chan.send("df -h\n")
            r1 = self.getfeedback()
            self.chan.send("exit\n")
            printlog(r1)
            return r1
        else:
            printlog("Unable to accomply because channel is NULL")
            return "Unable to accomply because channel is NULL"

    def __del__(self):
        self.client.close()

if __name__ == "__main__":
#     print(datetimestr())
#     printx("abc")
#     printlog("abc")
    srv = LServer()
    srv.connect("192.168.64.76", "root", "123456")
    srv.getdiskspace()