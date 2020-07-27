# Please note that you can NOT place __init__.py at the project root dir or the test will fail to import.
# First pytest will find test file /foo/bar/tests/test_a.py INSIDE root/
# pytest will look UPWARD to find the last folder which still contains an __init__.py file -> foo (in this case)
# To load module -> pytest will insert root/ to the front of sys.path -> loadable module: foo.bar.tests.test_a
# Same logic with conftest.py file
# https://docs.pytest.org/en/latest/pythonpath.html#pythonpath

# Folder Structure

# lutis ------------------------------------------> (project root)
#     - pytest.ini -------------------------------> Pytest configuration file, which by convention resides on the root of your repository or in your tests folder.
#     - .venv ------------------------------------> virtual env
#     - lutils (src) -----------------------------> src folder
#         - __init__.py --------------------------> make it a module to import
#         - algos --------------------------------> member module of src module
#         - tests --------------------------------> all test cases
#             - __init__.py ----------------------> make tests a module to import
#             - units ----------------------------> sub-module of tests with its init
#                 - __init__.py
#                 - test_utils.py ----------------> test file with test detail
#         - utils --------------------------------> utils module of src
#             - __init__.py
#             - lutils.py ------------------------> src file

# https://docs.pytest.org/en/latest/fixture.html#conftest-py-sharing-fixture-functions
# config test file
import pytest
from lutils.utils import LServer

@pytest.fixture(scope="session")
def common_connection():
    """
    SCOPE = [function, class, module, package, session]
    SCOPE default = function
    - function: the fixture is destroyed at the end of the test
    - class: the fixture is destroyed during teardown of the last test in the class
    - module: the fixture is destroyed during teardown of the last test in the module
    - package: the fixture is destroyed during teardown of the last test in the package
    - session: the fixture is destroyed at the end of the session
    Module = You can access this function by listing its name as INPUT of any test or fixture FUNCTION IN or BELOW the directory where conftest.py is LOCATED.
    """
    # print("common_connection fixture is called")
    return "common_connection"

@pytest.fixture(scope="session")
def common_lserver():
    """
    Common LServer object.
    """
    _server = LServer()
    # print("common_connection fixture is called")
    return _server

