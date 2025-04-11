-- Select glam rock bands and compute their lifespan
SELECT
    band_name,
    COALESCE(split, 2020) - formed as lifespan
FROM
    metal_bands
WHERE
    style LIKE '%Glam rock%';