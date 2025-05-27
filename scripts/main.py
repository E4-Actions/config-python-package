import sys
import e4_utilities

if __name__ == '__main__':
    directory = sys.argv[1]
    package_name = sys.argv[2]

    python_package = e4_utilities.PythonPackage(directory)
    python_package.init(package_name)
    python_package.save_config()