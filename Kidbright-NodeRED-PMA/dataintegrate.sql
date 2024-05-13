-- clothesdrying table (light, clotheshumidity, clothestemp)
-- Insert light data into table
INSERT INTO clothesdryingintegrated (ts, lat, lon, sensor, source, value)
SELECT 
    DATE_FORMAT(DATE_ADD(MIN(ts), INTERVAL 3 HOUR), '%Y-%m-%d %H:00:00') AS ts,
    ROUND(AVG(lat), 5) AS lat,
    ROUND(AVG(lon), 5) AS lon,
    'light' AS sensor,
    'clothesdrying' AS source,
    ROUND(AVG(light), 5) AS value
FROM b6510545306.clothesdrying
GROUP BY TIMESTAMPDIFF(HOUR, '2020-01-01 00:00:00', ts) DIV 3;

-- Insert clotheshumidity data into table
INSERT INTO clothesdryingintegrated (ts, lat, lon, sensor, source, value)
SELECT 
    DATE_FORMAT(DATE_ADD(MIN(ts), INTERVAL 3 HOUR), '%Y-%m-%d %H:00:00') AS ts,
    ROUND(AVG(lat), 5) AS lat,
    ROUND(AVG(lon), 5) AS lon,
    'clotheshumidity' AS sensor,
    'clothesdrying' AS source,
    ROUND(AVG(clotheshumidity), 5) AS value
FROM b6510545306.clothesdrying
GROUP BY TIMESTAMPDIFF(HOUR, '2020-01-01 00:00:00', ts) DIV 3;

-- Insert clothestemp data into table
INSERT INTO clothesdryingintegrated (ts, lat, lon, sensor, source, value)
SELECT 
    DATE_FORMAT(DATE_ADD(MIN(ts), INTERVAL 3 HOUR), '%Y-%m-%d %H:00:00') AS ts,
    ROUND(AVG(lat), 5) AS lat,
    ROUND(AVG(lon), 5) AS lon,
    'clothestemp' AS sensor,
    'clothesdrying' AS source,
    ROUND(AVG(clothestemp), 5) AS value
FROM b6510545306.clothesdrying
GROUP BY TIMESTAMPDIFF(HOUR, '2020-01-01 00:00:00', ts) DIV 3;

-- tmd_project table (temp, airhumidity	, rainfall)
-- Insert light data into table
INSERT INTO clothesdryingintegrated (ts, lat, lon, sensor, source, value)
SELECT 
    DATE_FORMAT(DATE_ADD(MIN(ts), INTERVAL 3 HOUR), '%Y-%m-%d %H:00:00') AS ts,
    ROUND(AVG(lat), 5) AS lat,
    ROUND(AVG(lon), 5) AS lon,
    'temp' AS sensor,
    'tmd_project' AS source,
    ROUND(AVG(temp), 5) AS value
FROM b6510545306.tmd_project
GROUP BY TIMESTAMPDIFF(HOUR, '2020-01-01 00:00:00', ts) DIV 3;

-- Insert airhumidity data into table
INSERT INTO clothesdryingintegrated (ts, lat, lon, sensor, source, value)
SELECT 
    DATE_FORMAT(DATE_ADD(MIN(ts), INTERVAL 3 HOUR), '%Y-%m-%d %H:00:00') AS ts,
    ROUND(AVG(lat), 5) AS lat,
    ROUND(AVG(lon), 5) AS lon,
    'airhumidity' AS sensor,
    'tmd_project' AS source,
    ROUND(AVG(airhumidity), 5) AS value
FROM b6510545306.tmd_project
GROUP BY TIMESTAMPDIFF(HOUR, '2020-01-01 00:00:00', ts) DIV 3;

-- Insert rainfall data into table
INSERT INTO clothesdryingintegrated (ts, lat, lon, sensor, source, value)
SELECT 
    DATE_FORMAT(DATE_ADD(MIN(ts), INTERVAL 3 HOUR), '%Y-%m-%d %H:00:00') AS ts,
    ROUND(AVG(lat), 5) AS lat,
    ROUND(AVG(lon), 5) AS lon,
    'rainfall' AS sensor,
    'tmd_project' AS source,
    SUM(rainfall) AS value
FROM b6510545306.tmd_project
GROUP BY TIMESTAMPDIFF(HOUR, '2020-01-01 00:00:00', ts) DIV 3;
