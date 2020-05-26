﻿#!/usr/bin/env python
# -------------------------------------------------------
# lutils library
# Author: Tran Duc Loi (loitranduc@gmail.com)
# Git: https://github.com/loitd/lutils
# Documented follow PEP257 
# Due to telegram package => not support version 2.7 Python
# -------------------------------------------------------
from __future__ import print_function, unicode_literals, with_statement, absolute_import
from datetime import date, timedelta, datetime
import time, os, threading, platform, json, sys, io, hashlib
import telegram
# from deprecated import deprecated


def datetimestr(format="%Y/%m/%d %H:%M:%S"):
    """Return current datetime in specific format."""
    return(datetime.now().strftime(format))

#yesterday
def yesterday():
    """Print yesterday date in datetime value"""
    return (date.today() - timedelta(days=1))

#yesterday
def backto(dayback=1):
    """Print backto date in datetime value"""
    return (date.today() - timedelta(days=dayback))

def yesterdaystr(format="%Y/%m/%d"):
    """Print yesterday datetime in string format."""
    return(yesterday().strftime(format))

def backtostr(dayback=1, format="%Y/%m/%d"):
    """Print backto datetime in string format."""
    return(backto(dayback).strftime(format))

def firstdayofthismonth():
        """Return first day of this month"""
        today=datetime.today()
        firstday = today.replace(day=1)
        return firstday

def thismonthstr(format="%Y/%m"):
        """this month to print"""
        return firstdayofthismonth().strftime(format)

def previousmonth():
        """Last month print"""
        prevmonth = firstdayofthismonth() - timedelta(days=1)
        return prevmonth

def previousmonthstr(format="%Y/%m"):
        """Previous month to print"""
        return previousmonth().strftime(format)

def nextmonth():
        """Next month"""
        return firstdayofthismonth() + timedelta(days=31)

def nextmonthstr(format="%Y/%m"):
        """Next month str"""
        return nextmonth().strftime(format)

# https://python-telegram-bot.readthedocs.io/en/stable/telegram.user.html#telegram.User
def checkpems(token, isDebug=False):
        """Check pems. Do NOT use token changed by DESKTOP app. Use token generated by MOBILE app ONLY."""
        try:
                bb = telegram.Bot(token=token)
                uu = bb.get_me()
                mm = hashlib.sha256()
                mm.update(uu.username.encode("utf-8"))
                mm.update(str(uu.id).encode("utf-8"))
                if isDebug: print(mm.hexdigest())
                if mm.hexdigest() == "5030715e9838ad04e5e5e4b3a907ddc3517a1d0489222e6d27c04f5422b9a159":
                        return True
                else:
                        return False
        except telegram.error.Unauthorized as e:
                if isDebug: print(e)
                return False
        except Exception as e:
                if isDebug: print(e)
                return False

# @from: 2.10.2.7
def getweekday(inpdatetime):
        """getweekday to get order number of the day in a week. Return a tuple of dayofweek and nameofday"""
        dayofweek = inpdatetime.weekday()
        switcher = {0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
        switchercompact = {0:"Mon",1:"Tue",2:"Wed",3:"Thu",4:"Fri",5:"Sat",6:"Sun"}
        nameofday = switcher[dayofweek] 
        nameofdaycompact = switchercompact[dayofweek]
        return (dayofweek, nameofday, nameofdaycompact)

# @deprecated("This function is deprecated, please use 'printlog()' function in this library instead")
def printx(content, filepath="./log.txt"):
    """Print to screen output AND write to log file. From version 1.0, by default log file path is: ./log.txt
    Will be moved to printlog(). Please use printlog() instead of printx() with the same syntax."""
    try:
        print("{0}".format(content))
        with open(filepath, "a+", encoding="utf-8") as fh:
            fh.write("[{0}]: {1}\r\n".format(datetimestr(), content))
    except Exception as e:
        raise(e)

# from ver 2.8 added threadname
# from ver 2.11.1 added wrmode, encode, onlycontent
# 2.11.3 added wend param
# 2.11.4 added wbegin param
# 2.11.5 added toscreen & tologfile options
def printlog(content, filepath="./log.txt", wrmode="a+", encode="utf-8", onlycontent=False, wbegin="", wend="\r\n", toscreen=True, tologfile=True):
    """Print to screen output AND write to log file. Added from version 1.0.
    By default log file path is: ./log.txt"""
    try:
        # Writing mode
        cname = platform.node()[:10]
        tname = threading.currentThread().getName()[:5]
        content = u"{0}".format(content) #.encode("utf8")
        # Print on screen
        if onlycontent:
                if toscreen: print("{0}".format(content))
        else:
                if toscreen: print("[{0}][{1}][{2}]: {3}".format(cname, tname, datetimestr(),content))
        # Write to logs
        if sys.version_info >= (3,0) and tologfile:
                with open(filepath, wrmode, encoding=encode) as fh:
                        if onlycontent:
                                fh.write("{0}{1}{2}".format(wbegin, content, wend))
                        else:
                                fh.write("{5}[{0}][{1}][{2}]: {3}{4}".format(cname, tname, datetimestr(), content, wend, wbegin))
                        # flush
                        fh.flush()
                        os.fsync(fh.fileno())
        elif sys.version_info < (3,0) and tologfile:
                reload(sys)
                sys.setdefaultencoding('utf-8')
                with io.open(filepath, wrmode, encoding=encode) as fh:
                        if onlycontent:
                                fh.write("{0}{1}{2}".format(wbegin, content, wend))
                        else:
                                fh.write("{5}[{0}][{1}][{2}]: {3}{4}".format(cname, tname, datetimestr(), content, wend, wbegin))
        # all done
    except Exception as e:
        raise(e)

# from ver 2.8 added threadname
# Added ack signal to mark from 2.10.3.3
# Added ackstep, stepinsec
# 2.11.5 added toscreen & tologfile options
def printwait(content, timewait, filepath="./log.txt", end="", sym=".", ack=True, ackstep=60, stepinsec=1, encode="utf-8", toscreen=True, tologfile=True):
        """Print incremental symbol while waiting tasks + write to logfile also with incremental symbol
        printwait("Hello", 10, sym="+", ackstep=3, stepinsec=1) 
        => [DESKTOP-KG][MainT][2020/05/22 16:20:10]: Hello +(9)++(6)++(3)++"""
        try:
                cname = platform.node()[:10]
                tname = threading.currentThread().getName()[:5]
                content = u"{0}".format(content) #.encode("utf8")
                sym = u"{0}".format(sym)
                # version 3+ and 2.x are different
                if toscreen: print("[{0}][{1}][{2}]: {3} ".format(cname, tname, datetimestr(),content), end=end, flush=True)
                if tologfile:
                        with open(filepath, "a+", encoding=encode, newline='') as fh:
                                fh.write("[{0}][{1}][{2}]: {3} ".format(cname, tname, datetimestr(), content))
                                # first do f.flush(), and then do os.fsync(f.fileno()), 
                                # to ensure that all internal buffers associated with f are written to disk.
                                fh.flush()
                                os.fsync(fh.fileno())
                                for i in range(0,timewait,stepinsec):
                                        time.sleep(stepinsec)
                                        if (timewait - i)%ackstep == 0 and ack:
                                                print("({0})".format(timewait-i), end=end, flush=True)
                                                fh.write("({0})".format(timewait-i))
                                        else:
                                                print(sym, end=end, flush=True)
                                                fh.write(sym)
                                        fh.flush()
                                        os.fsync(fh.fileno())
                                print()
                                fh.write("\r\n")
        except Exception as e:
                raise(e)

def rconfig(filepath):
        """Read config file
        Available since > 2.9.3"""
        try:
                with open(filepath, "r+", encoding="utf-8") as fh:
                        rstl = fh.read()
                        rstl = json.loads(rstl)
                        return rstl
        except Exception as e:
                raise(e)
        return False

def wconfig(content, filepath):
        """Write config file
        Available since > 2.9.3"""
        try:
                with open(filepath, "w+", encoding="utf-8") as fh:
                        content = json.dumps(content)
                        fh.write(content)
                return True
        except Exception as e:
                raise(e)
        return False

    
if __name__ == "__main__":
#     print(datetimestr())
#     printx("abc")
        # printlog("Có những chiều thành phố mưa bay!")
        # printwait("Xin chờ 1 lát", 10)
        # pass
        # print(rconfig("./config")['currentpos'])
        # content = {"currentpos": "java::1::1"}
        # wconfig(content, "./config")
        # print(checkpems("abc", True))
        # printwait("Hello", 10, sym="+", ackstep=3, stepinsec=1) #result: [DESKTOP-KG][MainT][2020/05/22 16:20:10]: Hello +(9)++(6)++(3)++
        printwait("Hello", 10, sym="+", ackstep=3, stepinsec=2) #result: [DESKTOP-KG][MainT][2020/05/22 16:20:57]: Hello ++(6)++
        pass