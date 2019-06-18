# lutils
## A Loitd's Public Utilities Project
Website: [https://inneka.com](https://inneka.com)  
Pip: [https://pypi.org/project/lutils/](https://pypi.org/project/lutils/)
## Installation
You can easily install this library with command `pip`  
`pip install lutils`
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

Easy upload with keering:  
`python -m keyring set https://upload.pypi.org/legacy/ loitd`