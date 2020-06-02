@ECHO off

SETLOCAL

SET folder=chapter1
SET filename=powerfunc.c
SET outfilename=powers

SET gcccmd=gcc -Wall -Wextra %folder%\%filename% -o %outfilename%

%ComSpec% /c "(%gcccmd%)" && %ComSpec% /c "(%outfilename%.exe)"


