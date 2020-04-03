@ECHO OFF

SETLOCAL

REM python setup.py build_ext --inplace
REM pause

::python setup_708.py develop
python setup_708.py build_ext --inplace
PAUSE