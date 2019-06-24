# lutils
## A Loitd's Public Utilities Project
Website: [https://inneka.com](https://inneka.com)  
Pip: [https://pypi.org/project/lutils/](https://pypi.org/project/lutils/)
Git: [https://github.com/loitd/lutils/](https://github.com/loitd/lutils/)
## Installation
You can easily install this library with command `pip`  
`pip install lutils`  
with specific version:  
`pip install lutils~=1.4`
Update existing installation:
`pipenv uninstall lutils`  
and  
`pipenv install lutils`  
Note: support Unicode from version 1.4. Then please update to newest version.
## Usage
In your python file:  
~~~
# import printlog()
from lutils.lutils import printlog

# using printx. If file not exist
printlog("abc", "test.log")
~~~
To connect SSH to Linux servers and get disk space status
~~~
# import LServer
from lutils.lutils import LServer

# init instance
srv = LServer()

# connect to server
srv.connect(ip="192.168.1.2", uname="root", pwd="123456")

# get disk space
srv.getdiskspace()
~~~
## For developers
To build this package:  
* `pip install --upgrade pip setuptools wheel`
* `pip install tqdm`
* `pip install --user --upgrade twine keyring`  

Compiling this package:  
* `python setup.py sdist bdist_wheel`  

Upload to PyPI:  
* `python -m twine upload --skip-existing dist/*`  
or
* `python -m twine upload --skip-existing -u loitd --repository-url https://upload.pypi.org/legacy/ dist/*`  

Easy upload with keyring:  
`python -m keyring set https://upload.pypi.org/legacy/ loitd`