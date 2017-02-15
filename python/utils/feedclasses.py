#!/bin/usr/python

import unittest
import subprocess

from functools import wraps

# These two functions are responsible to provide a metaprogramming
# which will allow us to pass a list of args to a generic test case
# this way it will execute as separated test cases in 'paralalel'.
# Allowing us to see which test fail in a separated way.


# Put the commands to be tested here in CMD_LIST
CMD_LIST = ['ls','du -Z .']


def args(*args):
    """
        Adds to the method in TestCase class a list of args to
        be handle in meta_to_class
    """
    def wrapper(func):
            setattr(func, '%n_args', args)
            return func
    return wrapper


def meta_to_class(cls):
    """
        In the TestCase class executes for first.
        @for does a search if the methods has n_args, or the list
        of args we put there using @args decorator.
        If so, the next step is get each element on the list
        and create testcase_name function/method with it.
        After all puts these new methods in decorated class and
        returns it.
    """
    def put_into_class(func, *args, **kwargs):
        @wraps(func)
        def wrapper(self):
            return func(self, *args, **kwargs)
        return wrapper

    for n, func in list(cls.__dict__.items()):
        if hasattr(func, '%n_args'):
            arg_list = getattr(func, '%n_args')[0]
            for arg in arg_list:
                testcase_name = getattr(arg, "__name__",
                                        "{0}_{1}".format(n, arg.split(' ')[0]))
                setattr(cls, testcase_name, put_into_class(func, arg))
            delattr(cls, n)
    return cls


@meta_to_class
class major_Case(unittest.TestCase):

    @args(CMD_LIST)
    def test_cmd_execute(self, cmd):
        process = subprocess.Popen(cmd.split(' '), stdout=subprocess.PIPE)
        output, err = process.communicate()
        print "cmd output:\n", output
        # if return code equal 1 it failed, otherwise it success.
        self.assertEqual(process.returncode, 0)


if __name__ == '__main__':
        unittest.main()
