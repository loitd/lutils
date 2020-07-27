import setuptools
from setuptools import setup, find_packages

# More on setuptools: https://setuptools.readthedocs.io/en/latest/setuptools.html
# https://github.com/pypa/sampleproject
# https://packaging.python.org/guides/distributing-packages-using-setuptools/#setup-cfg

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='lutils',  
    version='2.11.73',
    
    #this will add to \Scripts folder
    #scripts=['lutils.py'] ,
    
    # Project uses reStructuredText, so ensure that the docutils get installed or upgraded on the target machine
    # comment lines and \ continuations are allowed in requirement strings
    # BazSpam ==1.1, ==1.2, ==1.3, ==1.4, ==1.5, \
    # ==1.6, ==1.7  # and so are line-end comments
    install_requires=[
      'python-telegram-bot>=12.2.0', #for checkpems
      'paramiko', #for LServer
    #   'enum34;python_version<"3.4"',
    #   'pywin32 >= 1.0;platform_system=="Windows"',
    #   'flask',
    ],
    
    # If any package contains *.txt or *.rst files, include them:
    # And include any *.msg files found in the 'hello' package, too:
    # package_data={
    #     '': ['*.txt', '*.rst'],
    #     'hello': ['*.msg'],
    # },
    
    
    # metadata to display on PyPI
    author="Tran Duc Loi",
    author_email="loitranduc@gmail.com",
    description="A Public Loitd Python Utility Library",
    keywords="python python3 library utilities loitd printlog printwait telegram python37",
    platforms='any',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/loitd/lutils",
    project_urls={
        "Website": "https://github.com/loitd/lutils",
        "Documentation": "https://github.com/loitd/lutils",
        "Source Code": "https://github.com/loitd/lutils",
        "Javascript": "https://github.com/loitd/lutilsjs/",
        "Pypi": "https://pypi.org/project/lutils/"
    },
    # include all packages under src
    packages=setuptools.find_packages(),
    # All here: https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Intended Audience :: Developers',
        'Environment :: Console',
        'Topic :: Software Development :: Libraries :: Python Modules',
        "Topic :: Software Development :: Debuggers",
        "Topic :: Software Development :: Libraries",
        "Topic :: System :: Logging",
        "Topic :: System :: Monitoring",
        "Natural Language :: English",
    ],
)