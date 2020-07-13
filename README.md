# lutils
## A Loitd's Public Python Utilities Library. 
Website: [https://inneka.com](https://github.com/loitd/lutils/)  
Pip: [https://pypi.org/project/lutils/](https://pypi.org/project/lutils/)  
Git: [https://github.com/loitd/lutils/](https://github.com/loitd/lutils/)  
JS: [https://github.com/loitd/lutilsjs/](https://github.com/loitd/lutilsjs/) - Not equivalent  
## Installation
You can easily install this library with command `pip` or `pipenv`:  
`pip install lutils`  
With specific version (pip will automatically uninstall older version & install specific version):  
`pip install lutils~=2.11.7`  
Update existing installation:
`pipenv update lutils`
Update existing installation (manually):
`pipenv uninstall lutils`  
and then:  
`pipenv install lutils`  
## Note
- Works with Python 3.x. Recommended Python 3.x for performance and full support features
- Support Unicode from version 2.10.2.2. Then please update to newest version.
- Backward compatible with Python 2.7 (recommended for 2.x) from version 2.10.2.1. From 2.10.2.1, lutils works on both 2.x and 3.x
- Any suggestions are welcome with pull request or email at loitranduc[at]gmail.com
- Introduction or guide (docs) if available will be at [https://github.com/loitd/lutils/](https://github.com/loitd/lutils/)  
## Usage
In your python file:  
~~~
# import printlog() to both PRINT to SCREEN & WRITE to LOGFILE
from lutils.lutils import printlog, printwait

# using printlog. If file not exist, printlog will creates a new one
# If the log file exists, printlog will appends to the end of the log file
printlog("abc", "test.log")

# using printwait. Print text to console & write to logfile & wait with dots in specific seconds
printwait("Please wait while doing things", 5, "logfile.log")


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