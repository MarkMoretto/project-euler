@ECHO OFF

SETLOCAL
SET PYTHONPATH=
SET pyexe=%LocalAppData%\Programs\Spyder\venv
SET "PATH=%pyexe%;%pyexe%\Scripts;%pyexe%\Lib;%PATH%"

REM python setup.py build_ext --inplace
REM pause

python setup.py develop
PAUSE