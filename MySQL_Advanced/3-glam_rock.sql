-- Select glam rock bands and compute their lifespan.
SELECT
    band_name,
    COALESCE(split, YEAR (CURDATE ())) - formed AS lifespan
FROM
    metal_bands
WHERE
    style LIKE '%Glam rock%'
ORDER BY
    lifespan DESC;