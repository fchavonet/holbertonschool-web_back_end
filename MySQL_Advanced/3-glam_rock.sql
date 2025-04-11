-- Select glam rock bands and compute their lifespan.
SELECT band_name, COALESCE((IFNULL (split, 2024)) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%';
