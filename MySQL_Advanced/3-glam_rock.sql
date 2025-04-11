-- Select glam rock bands and compute their lifespan.
SELECT
    name AS band_name,
    COALESCE(split, 2020) - formed AS lifespan
FROM
    metal_bands
WHERE
    style = 'Glam rock'
ORDER BY
    lifespan DESC;
