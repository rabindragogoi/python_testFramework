import argparse
import importlib
import sys
from project1_testsuite.logger import generate_logger


modules = {'project1': 'project1_testsuite',
               'project2': 'project2_testsuite'
               }

def parse_arguements():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--module', help='Module to be tested', required=True)
    parser.add_argument('-t', '--type', help='Type of the testing Smoke or Regression', required=True)
    return parser.parse_args()


# Prepares the path string where the Test Suite is availlable...
def getClassPath(moduleName):
    return moduleName + '.executeTest.Play_Test'


# Dynamically Loads a class from a string.Returns the class name...
def load_class(full_class_string):
    class_data = full_class_string.split(".")
    module_path = ".".join(class_data[:-1])
    class_str = class_data[-1]

    module = importlib.import_module(module_path)
    return getattr(module, class_str)


if __name__ == '__main__':
    r_args = parse_arguements()
    test_type = r_args.type.lower()
    module_name = r_args.module.lower()
    LOGGER = generate_logger(module_name)
    # Checks if the module name provided as arguement is valid.
    if module_name in modules:
        testStr = getClassPath(modules[module_name])
    else:
        LOGGER.info("Please enter a valid module name OR Check whether the "
                    "module name exist in the property dictionary module...")
        sys.exit(True)
    LOGGER.info(testStr)

    classInstance = load_class(testStr)()
    classInstance.initiate_test(test_type)
