@ECHO OFF

SET PROMPT=

SETLOCAL
SET MINGW64_HOME=

SET PROMPT={ msys64 env } $P$G
SET "msys64_pth=C:\Users\MMorett1\AppData\Local\Programs\msys64\mingw32"
SET "PATH=%msys64_pth%;%msys64_pth%\bin;%PATH%"



%ComSpec% /k
