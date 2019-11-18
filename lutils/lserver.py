import paramiko, socket
import sys
from lutils.lutils import printlog
# from lutils import printlog
import requests

class LServer(object):
    """LServer is a class for interacting with Linux server via SSH.
Usage: 
srv = LServer()
srv.connect(ip="192.168.64.76", uname="root", pwd="123456")
srv.getdiskspace()"""
    def __init__(self):
        super(LServer, self).__init__()
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
        self.chan = None
        self.error = 'No error founds while connecting'
        # printlog(self.error)

    def __del__(self):
        self.client.close()

    def connect(self, ip, uname, pw, debug=False):
        """connect to server with ip, username, password"""
        try:
            self.client.connect(ip, username=uname, password=pw)
            self.chan = self.client.invoke_shell()
            if debug == True: printlog("Successfull connected to %s"%ip)
            self.chan.settimeout(5.0)
            self.error = 'No error founds while connecting'
            return True
        except Exception as e:
            self.error = e
            self.chan = None
            printlog(e)
            return False

    def getfeedback(self, regcode = ']#', debug=False):
        """getfeedback from server command line."""
        try:
            if debug: printlog("[getfeedback] Waiting for reply until timeout...")
            buff = ''
            while buff.find(regcode) == -1:
                    resp = self.chan.recv(9999999).decode("utf-8") #CONVERTED to Unicode String
                    buff = "{0}{1}".format(buff, resp)
                    # printlog(buff)
            return buff #return UNICODE String
        except socket.timeout:
            printlog("[getfeedback] Time out while waiting for response from server. Program will exits.")
            sys.exit(1)
        except Exception as e:
            raise(e)
            # printlog(e)
            # sys.exit(1)
    
    def getfeedbackASCII(self, regcode = ']#', debug=False):
        """getfeedback from server command line."""
        try:
            if debug: printlog("[getfeedback] Waiting for reply until timeout...")
            buff = ''
            while buff.find(regcode) == -1:
                    resp = self.chan.recv(9999999)
                    buff = "{0}{1}".format(buff, resp)
                    # printlog(buff)
            return buff #return UNICODE String
        except socket.timeout:
            printlog("[getfeedback] Time out while waiting for response from server. Program will exits.")
            sys.exit(1)
        except Exception as e:
            raise(e)
            # printlog(e)
            # sys.exit(1)
    
    def runcmd(self, cmd, regcode=']#', debug=False):
        try:
            if self.chan is not None:
                self.getfeedback()
                printlog("Begin runcmd: {0}".format(cmd))
                self.chan.send(cmd)
                r1 = self.getfeedback()
                self.chan.send("exit\n")
                # printlog(r1)
                return r1
        except Exception as e:
            raise(e)
    
    def  getdiskspace(self, cmd="df -h\n"):
        if self.chan is not None:
            self.getfeedback()
            printlog("Begin get disk space ...")
            self.chan.send(cmd)
            r1 = self.getfeedback()
            self.chan.send("exit\n")
            # printlog(r1)
            return r1
        else:
            printlog("Unable to accomply because channel is NULL")
            return "Unable to accomply because channel is NULL"
    
    def getDiskSpaceHtml(self, cmd="df -h /\n", isDebug=False): 
        #Remember not add r"" as we need to translate to Enter button pressed"
        if self.chan is not None:
            self.getfeedbackASCII(debug=isDebug)
            printlog("Begin get disk space with command: {0}...".format(cmd))
            self.chan.send(cmd)
            r1 = self.getfeedbackASCII(debug=isDebug)
            self.chan.send("exit\n")
            if isDebug: printlog("r1: {0}".format(r1))
            ss = r1.split(r"\r\n")[1].split()
            if isDebug: printlog("ss: {0}".format(ss))
            xs = r1.split(r"\r\n")[2].split()
            # printlog(xs)
            if len(xs) == 1:
                ys = r1.split(r"\r\n")[3].split()
                percentt = float(ys[3].split("%")[0])
                percentt = '<strong style="color: green;">{0}%</strong>'.format(percentt) if percentt < 50 else '<strong style="color: red;">{0}%</strong>'.format(percentt)
                ret = """<table  border="1" style="width:100%" align="center"><tbody>
<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td><td>{5}</td></tr>
<tr><td>{6}</td><td>{7}</td><td>{8}</td><td>{9}</td><td>{10}</td><td>{11}</td></tr>
</tbody></table>""".format(ss[0], ss[1], ss[2], ss[3], ss[4], ss[5], xs[0], ys[0], ys[1], ys[2], percentt, ys[4])
            else:
                percentt = float(xs[4].split("%")[0])
                percentt = '<strong style="color: green;">{0}</strong>'.format(xs[4]) if percentt < 50 else '<strong style="color: red;">{0}</strong>'.format(xs[4])
                ret = """<table  border="1" style="width:100%" align="center"><tbody>
    <tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td><td>{5}</td></tr>
    <tr><td>{6}</td><td>{7}</td><td>{8}</td><td>{9}</td><td>{10}</td><td>{11}</td></tr>
    </tbody></table>""".format(ss[0], ss[1], ss[2], ss[3], ss[4], ss[5], xs[0], xs[1], xs[2], xs[3], percentt, xs[5])
            return ret
        else:
            printlog("Unable to accomply because channel is NULL")
            return "Unable to accomply because channel is NULL"
    
    def checkProcess(self, cmd="systemctl status sshd | grep Active\n", evid="active (running)", debug=False):
        """Check process running."""
        if self.chan is not None:
            self.getfeedback(debug=debug)
            if debug: printlog("Begin check process with command: {0}".format(cmd))
            self.chan.send(cmd)
            r1 = self.getfeedback(debug=debug)
            self.chan.send("exit\n")
            if debug: printlog(r1)
            if (evid in r1):
                printlog("[checkProcess] The process is ALIVE")
                return True
            else:
                printlog("[checkProcess] The process is DIED")
                return False
        else:
            printlog("[checkProcess] Unable to accomply because channel is NULL")
            return False
            

class LWebservice(object):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)
    
    def check(self, uri, method="get"):
        try:
            if (method=="get"):
                req = requests.get(uri)
                print(req.status_code)
                if (req.status_code in [200,302]):
                    return True
                else:
                    return False
            elif (method == "post"):
                req = requests.post(uri, data = {'epay':'infras'})
                print(req.status_code)
                if (req.status_code in [200,302]):
                    return True
                else:
                    return False
        except Exception as e:
            print(e)
            return False

if __name__ == "__main__":
    # Test LServer
    srv = LServer()
    srv.connect(ip="172.16.10.84", uname="root", pw="db84$$$")
    spaces = srv.getDiskSpaceHtml("df -h / \n", True)
    print(spaces)
    # srv.checkProcess()

    # Test LWS
    # lw = LWebservice()
    # print(lw.check("http://abc.com/services/Interfaces?wsdl"))
    # print(lw.check("http://test.com/Interfaces?wsdl"))
    # print(lw.check("http://abc.com", "post"))
    
    pass



