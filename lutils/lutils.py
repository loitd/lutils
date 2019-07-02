#!/usr/bin/env python
# -------------------------------------------------------
# lutils library
# Author: Tran Duc Loi (loitranduc@gmail.com)
# Git: https://github.com/loitd/lutils
# Documented follow PEP257 
# -------------------------------------------------------
from datetime import date, timedelta, datetime
import time, os
# from deprecated import deprecated


def datetimestr(format="%Y/%m/%d %H:%M:%S"):
    """Return current datetime in specific format."""
    return(datetime.now().strftime(format))

#yesterday
def yesterday():
    """Print yesterday date in datetime value"""
    return (date.today() - timedelta(days=1))

def yesterdaystr(format="%Y/%m/%d"):
    """Print yesterday datetime in string format."""
    return(yesterday().strftime(format))

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

def printlog(content, filepath="./log.txt"):
    """Print to screen output AND write to log file. Added from version 1.0.
    By default log file path is: ./log.txt"""
    try:
        content = u"{0}".format(content) #.encode("utf8")
        print("[{0}]: {1}".format(datetimestr(),content))
        with open(filepath, "a+", encoding="utf-8") as fh:
            fh.write("[{0}]: {1}\r\n".format(datetimestr(), content))
    except Exception as e:
        raise(e)

def printwait(content, timewait, filepath="./log.txt", end="", sym="."):
        """Print incremental symbol while waiting tasks + write to logfile also with incremental symbol"""
        try:
                content = u"{0}".format(content) #.encode("utf8")
                sym = u"{0}".format(sym)
                print("[{0}]: {1} ".format(datetimestr(),content), end=end, flush=True)
                with open(filepath, "a+", encoding="utf-8", newline='') as fh:
                        fh.write("[{0}]: {1} ".format(datetimestr(), content))
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
    
if __name__ == "__main__":
#     print(datetimestr())
#     printx("abc")
        # printlog("Có những chiều thành phố mưa bay!")
        printwait("Xin chờ 1 lát", 10)
        pass