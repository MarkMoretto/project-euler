@ECHO off

SETLOCAL

SET folder=chapter1
SET filename=temp-conv-table.c
SET outfilename=temptable

SET gcccmd=gcc -Wall -Wextra %folder%\%filename% -o %outfilename%

%ComSpec% /c "(%gcccmd%)" && %ComSpec% /c "(%outfilename%.exe)"


