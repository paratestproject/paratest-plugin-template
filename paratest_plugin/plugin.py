import os
import sys

def find(path, test_pattern, file_pattern, output_path):
    # Your code goes here. You must return a dict or generator with (test name, test execution line).
    # Remember to use paths relative to the given path.
    # example:
    for root, _, files in os.walk(path):
        for filename in files:
            # as example, filtering to use just test_* files
            if not filename.startswith('test_'):
                continue

            relative = os.path.join(root, filename).replace(path, '')
            name = filename.replace('_', ' ')
            command = "run --whatever {path}".format(path=path)
            yield name, command


if __name__ == '__main__':
    for test, cmd in find(sys.argv[1], None, None, "output"):
        print("Test %s -> %s" % (test, cmd))
