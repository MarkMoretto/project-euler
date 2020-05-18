@ECHO off


SET PYSPARK_DRIVER_PYTHON=jupyter
SET PYSPARK_DRIVER_PYTHON_OPTS='notebook'
SET "BROWSER=C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

pyspark
