[![CI Workflow](https://github.com/ariannasg/optimizing-python/workflows/CI%20Workflow/badge.svg)](https://github.com/ariannasg/optimizing-python/actions?query=workflow%3A%22CI+Workflow%22)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE.md)

# Optimizing Python Code - Course

* [Description](#description)
* [Objectives](#objectives)
* [Local setup](#local-setup)
* [Security](#security)
* [Using IPython](#using-ipython)
* [Using cProfile](#using-cprofile)
* [Using pstats](#using-pstats)
* [License](#license)

## Description
Understanding how to optimise Python by following the course https://www.linkedin.com/learning/faster-python-code/.

## Objectives
- Rules of optimization
- Measuring time
- Using line_profiler
- Picking the right data structure
- Using the bisect module
- Memory allocation in Python
- Caching, cheating, and parallel computing
- NumPy, Numba, and Cython
- Design and code reviews

## Local setup
- Install python 3: https://www.python.org/downloads/.
- Create and activate a virtual environment, then install project dependencies:
    ```
    python3 -m venv ~/.python-envs/<name>
    source  ~/.python-envs/<name>/bin/activate
    (<name>) ➜  make install
    ```
- Configure the IDE Interpreter to use the virtual environment as project interpreter.
- Setup the run configuration in the IDE if needed: https://www.jetbrains.com/help/pycharm/creating-and-editing-run-debug-configurations.html?keymap=secondary_macos.

## Security
Command for running security checks on installed dependencies:
```
make security
```

## Using IPython
This is an example of trying out a timeit calculation using the IPython Notebook. 
To load the code we use the "run" magic method. 
The "-n" tells run not to run the main part of the code, just to load the functions in the file.
```
(optimizing-python) ➜ ipython
Python 3.8.3 (v3.8.3:6f8c8320e9, May 13 2020, 16:29:34) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.15.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: %run -n src/using_timeit.py                                                                                                                                                                  

In [2]: %timeit use_get('a')                                                                                                                                                                         
206 ns ± 9.75 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

In [3]: %timeit use_catch('a')                                                                                                                                                                       
167 ns ± 5.37 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
```

## Using cProfile
- Using the command line:
```
(optimizing-python) ➜ python -m cProfile src/using_cprofile.py
```
- Using the IDE: 
Run the profiler on `src/using_cprofile.py` as specified in https://www.jetbrains.com/help/pycharm/profiler.html

## Using pstats
- Using the command line:
```
(optimizing-python) ➜ python -m pstats src/prof.out 
Welcome to the profile statistics browser.
src/prof.out% stats 3
Thu Jun 11 12:18:52 2020    src/prof.out

         23 function calls in 0.000 seconds

   Random listing order was used
   List reduced from 14 to 3 due to restriction <3>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        1    0.000    0.000    0.000    0.000 /Users/Ari/Documents/Learning/LinkedIn Learning/Optimizing Python Code/optimizing-python/src/using_cprofile_file.py:7(bench_targeted_login_with_file)


src/prof.out% sort ncalls
src/prof.out% stats 3
Thu Jun 11 12:18:52 2020    src/prof.out

         23 function calls in 0.000 seconds

   Ordered by: call count
   List reduced from 14 to 3 due to restriction <3>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        2    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        2    0.000    0.000    0.000    0.000 /Users/Ari/Documents/Learning/LinkedIn Learning/Optimizing Python Code/optimizing-python/src/login.py:30(login)
        2    0.000    0.000    0.000    0.000 /Users/Ari/Documents/Learning/LinkedIn Learning/Optimizing Python Code/optimizing-python/src/login.py:12(user_passwd)


src/prof.out% sort tottime
src/prof.out% stats 3
Thu Jun 11 12:10:40 2020    src/prof.out

         23 function calls in 0.007 seconds

   Ordered by: internal time
   List reduced from 14 to 3 due to restriction <3>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        2    0.007    0.004    0.007    0.004 {method 'execute' of 'sqlite3.Cursor' objects}
        1    0.000    0.000    0.007    0.007 {built-in method builtins.exec}
        2    0.000    0.000    0.007    0.004 /Users/Ari/Documents/Learning/LinkedIn Learning/Optimizing Python Code/optimizing-python/src/login.py:12(user_passwd)

```

## License
This project is licensed under the terms of the MIT License.
Please see [LICENSE](LICENSE.md) for details.