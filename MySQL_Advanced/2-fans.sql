-- List countries ranked by total number of fans.
SELECT
    origin,
    SUM(fans) as nb_fans
FROM
    metal_bands
GROUP BY
    origin
ORDER BY
    nb_fans DESC;