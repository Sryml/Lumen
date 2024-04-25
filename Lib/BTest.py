# Author: Sryml
# Email: sryml@hotmail.com
# Python Version: 1.5.2
# License: MIT

import traceback
import sys
import types
import string

from Lumenx import printx


class Run:
    def __init__(self):
        # Initialize the tests list and longest_test_name
        self.tests = []
        self.longest_test_name = 0
        self.prefix = "test_"
        self.prefix_len = len(self.prefix)
        try:
            1 / 0  # Raise a ZeroDivisionError intentionally to catch and process later
        except ZeroDivisionError:
            # Get the namespace of the test case
            glob = sys.exc_info()[2].tb_frame.f_back.f_globals
            for k, v in glob.items():
                # Check if the variable is a test function by matching the prefix and type
                if (
                    k[: self.prefix_len] == self.prefix
                    and type(v) == types.FunctionType
                ):
                    # If the test function name is longer, update the longest_test_name
                    if len(k) > self.longest_test_name:
                        self.longest_test_name = len(k)
                    # Append the test function to the tests list
                    self.tests.append(v)

        self.run_tests()

    def run_tests(self):
        passed = 0
        failed = 0
        # Iterate through the test functions
        for test_func in self.tests:
            try:
                test_func()  # Execute the test function
                # Prepare the success message
                s = "Test | %%-%ds | passed" % (
                    self.longest_test_name - self.prefix_len
                )
                printx(s % test_func.__name__[self.prefix_len :])

                passed = passed + 1
            except:
                s = "Test | %%-%ds | failed at:" % (
                    self.longest_test_name - self.prefix_len
                )
                printx(s % test_func.__name__[self.prefix_len :])
                # Get the exception information
                exc_type, exc_value, exc_traceback = sys.exc_info()
                exception_str = traceback.format_exception(
                    exc_type, exc_value, exc_traceback
                )
                # Only print the first traceback
                exception_str = string.join(
                    exception_str[:1] + exception_str[-2:],
                    "",
                )
                # Print each line of the exception
                exception_str = string.split(exception_str, "\n")
                for s in exception_str:
                    printx(s)

                failed = failed + 1
        printx(
            "Total tests: %d, Passed: %d, Failed: %d"
            % (len(self.tests), passed, failed)
        )


"""
import BTest

# Execute at the bottom of the file:
BTest.Run()
"""
