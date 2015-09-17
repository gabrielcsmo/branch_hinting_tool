#!/usr/bin/env python

import os
import sys
import generate_gcov
import constants
import autogen
# import oldVersion_generate_gcov
FLAGS = ""
target = ""


def instrument(target, flags, verbose, build, run):
    global FLAGS
    if flags != "" and flags != None:
        FLAGS = " -d " + flags
    if os.path.isdir(target):
        autogen.start({'path': target}, verbose,build, run)
        # aici trebuie sa adaug generate_gcov
        print "Collect GCOV statistics ..."
        generate_gcov.generate(target, verbose, build, run)

    else:
        command = "gcc -fprofile-arcs -ftest-coverage " \
                  + target + " -o " + target + ".o"
        print command
        os.system(command)
        command = "./" + target + ".o"
        print command
        os.system(command)
        command = "gcov -bcu " + target
        print command
        os.system(command)
