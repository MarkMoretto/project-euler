
/*
Project euler problem 698 in SQL
https://projecteuler.net/problem=698
*/

USE CLARITY


DROP TABLE IF EXISTS #_test
CREATE TABLE #_test (
	[idx] NUMERIC(38,0) IDENTITY(1,1) PRIMARY KEY NOT NULL
	,	[string_number] NVARCHAR(500)
)


TRUNCATE TABLE #_test
DECLARE @_row_ct NVARCHAR(200) = '500000000'
DECLARE @_sql NVARCHAR(4000)
SET @_sql = N'INSERT #_test ([string_number])' + CHAR(32)
SET @_sql += N'SELECT TOP ' + @_row_ct + N' NULL' + CHAR(32)
SET @_sql += 'FROM master..sysobjects AS A CROSS JOIN master..sysobjects AS B CROSS JOIN master..sysobjects AS C'
--PRINT @_sql
EXEC(@_sql)
--SELECT COUNT(*) FROM ##_test


UPDATE #_test
SET [string_number] = CONVERT(NVARCHAR(500), [idx])
--SELECT TOP 100 * FROM #_test

DROP TABLE IF EXISTS #_final
;WITH filt1 AS (
	SELECT T.*
	FROM #_test AS T
	WHERE T.[string_number] NOT LIKE '%[^1-3]%'
)
, filt2 AS (

	SELECT F1.[idx] AS [idx]
	,	F1.[string_number] AS [string_number]
	,	LEN(F1.[string_number]) - LEN(REPLACE(F1.[string_number], '1', '')) AS [freq_1]
	,	LEN(F1.[string_number]) - LEN(REPLACE(F1.[string_number], '2', '')) AS [freq_2]
	,	LEN(F1.[string_number]) - LEN(REPLACE(F1.[string_number], '3', '')) AS [freq_3]
	FROM filt1 AS F1
)
SELECT f2.*
INTO #_final
FROM filt2 AS f2
WHERE [freq_1] NOT LIKE '%[^0-3]%'
AND [freq_2] NOT LIKE '%[^0-3]%'
AND [freq_3] NOT LIKE '%[^0-3]%'
--SELECT * FROM #_final


/*
DROP TABLE IF EXISTS #_filter_1
SELECT *
INTO #_filter_1
FROM #_test
WHERE [string_number] NOT LIKE '%[^1-3]%'
--SELECT * FROM #_filter_1

DROP TABLE IF EXISTS #_filter_2
SELECT [idx]
,	string_number
,	LEN(string_number) - LEN(REPLACE([string_number], '1', '')) AS [freq_1]
,	LEN(string_number) - LEN(REPLACE([string_number], '2', '')) AS [freq_2]
,	LEN(string_number) - LEN(REPLACE([string_number], '3', '')) AS [freq_3]
INTO #_filter_2
FROM #_filter_1
--SELECT * FROM #_filter_2

SELECT *
FROM #_filter_2
WHERE [freq_1] NOT LIKE '%[^0-3]%'
AND [freq_2] NOT LIKE '%[^0-3]%'
AND [freq_3] NOT LIKE '%[^0-3]%'
ORDER BY [idx]
*/





