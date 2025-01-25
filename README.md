# PythonBatchNovDec2024

A repository with all the classes material for becoming a python developer


## local setup in windows
    Install 
    
        git for windows
    
        vs code
    
        python
            microsoft store -- python3 (version)


    git clone https://github.com/udhayprakash/PythonBatchNovDec2024.git
    
    first time you need to pass the credentials, when running

## Git commands

To clone a repository (not needed in codespace, needed for local development):

    git clone https https://github.com/udhayprakash/PythonBatchNovDec2024.git

To list the local branches:

    git branch

To create a branch:

    git checkout -b class01

To see the latest local changes:

    git status


To check/verify the modified content in existing file,

    git diff 


To stage the changes:

    git add <filename>


To commit the changes:

    git commit -m "commit message"


To push the changes,

    git push origin <sourceBRanch>

        class01 -> main
        ex: git push origin class01


### Daily

To check the branch is clean, 

    git status 

To checkout to the main branch 

    git checkout main 

To get the latest changes 

    git pull origin main 

To create new branch 

    git checkout -b <NEW BRANCH NAME>


## Virtual Environment

    Isolated environment 

    why needed
        - same system, multiple projects
            - different python versions 
            - same python verison, but differenet module versions

    How to create Virtual Environment 
        - Virtualenv
        - venv
        - pipenv
        - poetry 
        - uv

    Using Virtualenv
        
        Install
            pip install virtualenv
        
        create virtual environment
            python -m virtualenv .venv
        
        activate virtual environment
            linux
                source .venv/bin/activate

            windows
                .venv/script/activate

    Using Poetry
        pip install -U pip
        pip install poetry
        python -m poetry init
        python -m poetry shell

        pip install poetry
        poetry add pandas        


## Course Completed

[class00 04th Nov 2024 ](zoomrecordinglink)

    00. Dev Setup
        Installing IDE/Editor
        Installing Python and local setup
        Github access, creating project
        
[class01 06th Nov 2024 ](zoomrecordinglink)

        git commands
        markdown syntax
        daily activity and usage
    
    01.Introduction
        Importance of Python
        Two versions of Python (2.x & 3.x)

[class02 11th Nov 2024 ](zoomrecordinglink)

        PEP 8 Guidelines (https://peps.python.org/pep-0008/)
        Shebang line
        Indendation Issue and best practices
        built-in functions
        print function
        Script mode vs interactive mode
        Jupyter notebook usage
        Ascii and Unicode characters

[class03 13th Nov 2024 ](zoomrecordinglink)

        Comment Operator
        keywords and Identifiers
        Line continuation and statement separator operators

    02.Basics
        Arithmetic operations
            +, -, , /, //, %, *
            divmod() function
            compound opertions

    Assignments:

        1) try to the sum of digits in a integer number, using divmod()
        2) If a clock has revolved for 32 times, and is half way, how many days completed

[class04 15th Nov 2024 ](zoomrecordinglink)

            Practical Problem solving
            working with complex numbers
            abs() function
            Operator precedence in Arithmetic operations

    Assignments:

        1) savings Bank 
        2) Bank loan
            simple interest 
            compund interest
        3) convert from hex to oct , and vice versa
        4) feet to cms conversion

[class05 20th Nov 2024 ](zoomrecordinglink)

    String operations
        Usage of single, double and triple quotes
        len() function
        Indexing and Slicing Strings

[class06 22nd Nov 2024 ](zoomrecordinglink)

        string attributes

[class07 25th Nov 2024 ](zoomrecordinglink)

        string attributes

[class08 27th Nov 2024 ](zoomrecordinglink)

        String formatting: old & new styles, f-strings
        unicode strings

[class09 29th Nov 2024 ](zoomrecordinglink)

        bytearray() and byte() strings
        Usage of help
        Usage of pydoc

    03.Language Components
        Relational Operations
        Logical Operations

[class10 2nd Dec 2024 ](zoomrecordinglink)

        Boolean Operations
        Bitwise Operations
        Identity Operations
            Dual Memory management Strategy
        range() function
        Conditional Operations

[class11 2nd Dec 2024 ](zoomrecordinglink)

        Structural Pattern Matching
        Loops: for & while, break, continue, pass, sys.exit
    # Assignment: Try these break, continue, pass, on a for loop example


[class12 6th Dec 2024 ](zoomrecordinglink)

        Walrus Operator

    04.Exception Handling
        Exceptions Hierarchy
        Different types of errors, error vs exception and exception groups
        Handling single and multiple exceptions
        raising exceptions
        asserts
        traceback
        exception Groups
        warnings

[class13 9th Dec 2024 ](zoomrecordinglink)

    05.Debugging
        Importance of logical errors
        Debugging with pydevd
        Debugging with pdb, ipdb
        breakpoint() function
        PYTHONBREAKPOINT environment variable usage
        post analyses of executed script

[class14 10th Dec 2024 ](zoomrecordinglink)

    06.Collections
        Lists

[class15 11th Dec 2024 ](zoomrecordinglink)

        Copy Problem - shallow copy vs deepcopy
        Tuples & namedtuples
        Immutability & unpacking
        Sets
            attributes, operations

[class16 13th Dec 2024 ](zoomrecordinglink)

        fronzensets
        Dictionaries
            zip() function
            workaround for switch case
        Comprehensions
        Working with Iterables - sum(), max(), min()

[class17 16th Dec 2024 ](zoomrecordinglink)

    07.Functions
        Functions with & without arguments, keyword arguments
        Functions with Different return types and unpacking
        Functions with with Default arguments
        variadic functions : variable arguments and variable keyword arguments
        Functions with keyword only arguments
        Scoping: Global vs Local
            call by reference
            call by value

[class18 17th Dec 2024 ](zoomrecordinglink)

        Partial Functions
        Anonymous(Lambda) Functions
        Higher order functions: map(), filter(), functool.reduce()
        Recursions and recursions limit


[class19 18th Dec 2024 ](zoomrecordinglink)

        inner functions
        closures

    08.Decorator Design Pattern
        Necessity
        function Decorator
        Practical Examples
        syntactic sugar for decorators
        multiple decorators on same function
        decorators with arguments
        functools - wrap, lru_cache
        class decorator


[class20 19th Dec 2024 ](zoomrecordinglink)

    09.Iterables, Iterators, Generators and co-routines
        Iterables
            different ways of extracting values from iterables
        Iterators
            iter() protocol
            itertools module

[class21 20th Dec 2024 ](zoomrecordinglink)

        Generators
            yield vs return
            function vs Generator
            Generator pipelining
            Generator Expression

[class22 23rd Dec 2024 ](zoomrecordinglink)

        Coroutine
            Generator vs Coroutine
            coroutine pipelining


    10.Modules
        Basic Modules
            - math, sys, argparse

[class23 23rd Dec 2024 ](zoomrecordinglink)
            
            os, pathlib, psutil
            

[class24 26th Dec 2024 ](zoomrecordinglink)
           
        shutil, subprocess, getpass
        time related
            - time, datetime, pytz, timeit, calendar
        others
            - random, collections, atexit, contextlib, base64


[class25 27th Dec 2024 ](zoomrecordinglink)

        create user-defined module
        creating user-defined package
        packaging
        creating the wheel files, tar files
        publishing with twine
        egg files

    11.File Operations
        flat files

[class26 30th Dec 2024 ](zoomrecordinglink)

        Non-flat files
            pickle
            shelve
            xml
            csv


[class27 02nd Jan 2024 ](zoomrecordinglink)

            windows local setup
            poetry installation
            Troubleshooting experince
            csv
            dat
            tsv

[class28 06th Jan 2024 ](zoomrecordinglink)

    12.Logging
        Simple logging
        configuring log file
        formatting logs and adding timestamp
        working with file handler and stream hanlder
        configuring multiple handlers
        color logging
        Rotating logger


[class29 08th Jan 2024 ](zoomrecordinglink)

    13. Regular Expressions
        re module
        compiling regex objects
        match & search
        find & finditer
        regex Flags
        Greedy & Non-Greedy patterns
        findall & finditer
        sub and subn
        regex Flags
        groups and groupdicts
        Pearl-style regexes
        Realworld Problem (log analyses, email Validation, etc)


[class30 10th Jan 2024 ](zoomrecordinglink)


    14. OOP
        Importance of OOP
        Instantiation and managing attributes
        constructor and Importance of self
        instance and class variables
        Encapsulation


[class31 13th Jan 2024 ](zoomrecordinglink)

        MRO, Single and multiple inheritance, composition
        Method Overwriting, Operator Overloading
        instance, class and static methods
        property decorator
        Dunder(magic) methods
        reprlib module
        creating context manager class


[class32 15th Jan 2024 ](zoomrecordinglink)


        Dataclasses
        Abstract Classes
        
    14. Code Quality
        pylint
        Autopep8
        typing


[class33 17th Jan 2024 ](zoomrecordinglink)

        profiling
        Objgraph
        doctest

[class34 21st Jan 2024 ](zoomrecordinglink)

        unittest
        pytest

    16. AWS Cloud

        AWS Development setup 
        AWS CLI setup and usage
        AWS IAM 
            creation of Users, Groups, and assiging policies    


[class35 22nd Jan 2024 ](zoomrecordinglink)

    17. Data Science
        statistics
        Numpy
        Pandas
        Matplotlib


[class36 25nd Jan 2024 ](zoomrecordinglink)
        
        Usage of Google Collab
        Numpy

        Usage of Kaggle
        Pandas
        
        Matplotlib


## Next  class

    16. Databases
        db files - sqlite3
        Relational DB - MySQL
        Non-Relational DB - mongoDB

    17. Web Services
        consuming REST API
        scraping web pages
        urllib, requests
