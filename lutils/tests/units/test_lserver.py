import pytest
from lutils.utils import LServer

def test_LServerClass(common_lserver):
    assert isinstance(common_lserver, LServer)
    
def test_connect(common_lserver):
    assert common_lserver.connect(ip="172.16.10.1", uname="user", pw="any", debug=False) == False

def test_connectWithKey(common_lserver):
    assert common_lserver.connectWithKey(ip="172.16.10.1", uname="user", privatekeypath="./nofile") == False

def test_getfeedback(common_lserver):
    assert common_lserver.getfeedback() == False
    
def test_getfeedbackASCII(common_lserver):
    assert common_lserver.getfeedbackASCII() == False
    
def test_runcmd(common_lserver):
    assert common_lserver.runcmd(cmd="ls -al") == False

def test_getdiskspace(common_lserver):
    assert common_lserver.getdiskspace() == "Unable to accomply because channel is NULL"

def test_getDiskSpaceHtml(common_lserver):
    assert common_lserver.getDiskSpaceHtml() == "Unable to accomply because channel is NULL"

def test_checkProcess(common_lserver):
    assert common_lserver.checkProcess() == False