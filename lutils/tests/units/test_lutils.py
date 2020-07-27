import pytest
from lutils.utils import printlog, printwait, getweekday, datetimestr, yesterday, backto, yesterdaystr, backtostr, firstdayofthismonth
from os.path import isfile
from datetime import datetime

# date_time_str = '2020/09/20 01:55:19'
# date_time_obj = datetime.strptime('2020/09/20 01:55:19', '%Y/%m/%d %H:%M:%S')

def test_datetimestr():
    assert datetimestr(thedate=datetime.strptime('2020/09/20 01:55:19', '%Y/%m/%d %H:%M:%S')) == '2020/09/20 01:55:19'
    
def test_yesterday():
    _yesterday = yesterday(datetime.strptime('2020/09/20 01:55:19', '%Y/%m/%d %H:%M:%S'))
    assert datetimestr(thedate=_yesterday) == '2020/09/19 01:55:19'
    
def test_backto():
    _obj = datetime.strptime('2020/09/20 01:55:19', '%Y/%m/%d %H:%M:%S')
    assert datetimestr(thedate=backto(9, _obj)) == '2020/09/11 01:55:19'

def test_yesterdaystr():
    _obj = datetime.strptime('2020/09/20 01:55:19', '%Y/%m/%d %H:%M:%S')
    _yesterday = yesterday(_obj)
    assert yesterdaystr(thedate=_yesterday) == '2020/09/19'

def test_backtostr():
    _obj = datetime.strptime('2020/09/20 01:55:19', '%Y/%m/%d %H:%M:%S')
    assert backtostr(dayback=10, thedate=_obj) == '2020/09/10'

def test_firstdayofthismonth():
    _obj = datetime.strptime('2020/09/20 01:55:19', '%Y/%m/%d %H:%M:%S')
    _obj1 = datetime.strptime('2020/09/01 01:55:19', '%Y/%m/%d %H:%M:%S')
    assert firstdayofthismonth(thedate=_obj) == _obj1
    
def test_printlog(capsys, tmpdir):
    _msg = "[test_printlog] Yes"
    # _logfile = tmpdir.join("test_printlog.log")
    _logfile = tmpdir.mkdir("test_lutils").join("test_printlog.log")
    printlog(_msg, _logfile)
    out, err = capsys.readouterr()
    assert _msg in out
    # now check the file
    assert isfile(_logfile)
    # check content of _logfile
    assert _msg in _logfile.read()
    
def test_printwait(capsys, tmpdir):
    _msg = "[test_printwait] Yes"
    _logfile = tmpdir.mkdir("test_lutils").join("test_printwait.log")
    printwait(_msg, 2, _logfile)
    out, err = capsys.readouterr()
    assert "{0} ..".format(_msg) in out # a space between _msg and dots
    assert isfile(_logfile)
    
class TestLutils:
    def test_getweekday(self):
        date_time_str = '24/07/2020 01:55:19'
        # This is Friday
        date_time_obj = datetime.strptime(date_time_str, '%d/%m/%Y %H:%M:%S')
        dayofweek, nameofday, nameofdaycompact = getweekday(date_time_obj)
        assert dayofweek == 4
        assert nameofday == "Friday"
        assert nameofdaycompact == "Fri"
    
    # Test of using common fixture function
    @pytest.mark.config
    def test_conftest(self, common_connection):
        assert common_connection == "common_connection"
    
if __name__ == "__main__":
    # test_printlog(capsys)
    # test_printwait(capsys)
    pass