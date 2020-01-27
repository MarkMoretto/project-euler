@ECHO OFF

IF NOT `%PROMPT%==` {
	SET PROMPT=
}


SETLOCAL
SET PROMPT={ rust } $P$G

%ComSpec% /k
