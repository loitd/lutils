﻿#!/usr/bin/env python
# -------------------------------------------------------
# lutils library
# Author: Tran Duc Loi (loitranduc@gmail.com)
# Git: https://github.com/loitd/lutils
# Documented follow PEP257 
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

def checkpems(token):
        try:
                bb = telegram.Bot(token=token)
                uu = bb.get_me()
                mm = hashlib.sha256()
                mm.update(uu.username.encode("utf-8"))
                if mm.hexdigest() == "6874b180ca9fdedc0b6201053cf5d8c3c2ad75b960bf2dbc7cf8b1ceac7a5f38":
                        return True
                else:
                        return False
        except telegram.error.Unauthorized as e:
                return False
        except Exception as e:
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
def printlog(content, filepath="./log.txt"):
    """Print to screen output AND write to log file. Added from version 1.0.
    By default log file path is: ./log.txt"""
    try:
        cname = platform.node()[:10]
        tname = threading.currentThread().getName()[:5]
        content = u"{0}".format(content) #.encode("utf8")
        print("[{0}][{1}][{2}]: {3}".format(cname, tname, datetimestr(),content))
        if sys.version_info >= (3,0):
                with open(filepath, "a+", encoding="utf-8") as fh:
                        fh.write("[{0}][{1}][{2}]: {3}\r\n".format(cname, tname, datetimestr(), content))
        elif sys.version_info < (3,0):
                reload(sys)
                sys.setdefaultencoding('utf-8')
                with io.open(filepath, "a+", encoding="utf-8") as fh:
                        fh.write("[{0}][{1}][{2}]: {3}\r\n".format(cname, tname, datetimestr(), content))
    except Exception as e:
        raise(e)

# from ver 2.8 added threadname
def printwait(content, timewait, filepath="./log.txt", end="", sym="."):
        """Print incremental symbol while waiting tasks + write to logfile also with incremental symbol"""
        try:
                cname = platform.node()[:10]
                tname = threading.currentThread().getName()[:5]
                content = u"{0}".format(content) #.encode("utf8")
                sym = u"{0}".format(sym)
                # version 3+ and 2.x are different
                print("[{0}][{1}][{2}]: {3} ".format(cname, tname, datetimestr(),content), end=end, flush=True)
                with open(filepath, "a+", encoding="utf-8", newline='') as fh:
                        fh.write("[{0}][{1}][{2}]: {3} ".format(cname, tname, datetimestr(), content))
                        # first do f.flush(), and then do os.fsync(f.fileno()), 
                        # to ensure that all internal buffers associated with f are written to disk.
                        fh.flush()
                        os.fsync(fh.fileno())
                        for i in range(timewait):
                                time.sleep(1)
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
        print("")
        pass