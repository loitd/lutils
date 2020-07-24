import pytest
from lutils.utils import printlog, printwait, getweekday
from os.path import isfile
from datetime import datetime

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
        date_time_obj = datetime. strptime(date_time_str, '%d/%m/%Y %H:%M:%S')
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