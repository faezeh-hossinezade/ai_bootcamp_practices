
-- Section1

SELECT
    p.platform_name AS platform_name,
    AVG(rs.num_sales) AS Average
FROM platform p
JOIN game_platform gp ON gp.platform_id = p.id
JOIN region_sales rs ON rs.game_platform_id = gp.id
GROUP BY p.id
ORDER BY Average DESC;

-- Section2

SELECT
    g.game_name AS game_name,
    p.platform_name AS platform_name,
    gpl.release_year AS release_year,
    pu.publisher_name AS publisher_name,
    SUM(rs.num_sales) AS global_sales
FROM game g
JOIN game_publisher gpu ON g.id = gpu.game_id
JOIN publisher pu ON pu.id = gpu.publisher_id
JOIN game_platform gpl ON gpu.id = gpl.game_publisher_id
JOIN platform p ON gpl.platform_id = p.id
JOIN region_sales rs ON rs.game_platform_id = gpl.id
GROUP BY g.id, gpl.id, p.id, pu.id
ORDER BY global_sales DESC
LIMIT 20;

-- Section3

SELECT
    game_name,
    COUNT(DISTINCT platform_id) AS platform_count
FROM (
SELECT
    g.game_name AS game_name,
    gpl.platform_id AS platform_id
FROM game g
JOIN game_publisher gpu ON gpu.game_id = g.id
JOIN game_platform gpl ON gpl.game_publisher_id = gpu.id
) AS game_platofrm_count
GROUP BY game_name
HAVING platform_count > 5
ORDER BY platform_count DESC, game_name;

-- Section4

SELECT
    p.platform_name AS platform,
    ge.genre_name AS genre,
    DENSE_RANK() OVER (PARTITION BY p.platform_name ORDER BY SUM(rs.num_sales) DESC) AS genre_in_platform_rank,
    SUM(rs.num_sales) AS genre_sale,
    DENSE_RANK() OVER (ORDER BY SUM(rs.num_sales) DESC) AS total_rank
FROM genre ge
JOIN game ga ON ge.id = ga.genre_id
JOIN game_publisher gpu ON ga.id = gpu.game_id
JOIN game_platform gpl ON gpu.id = gpl.game_publisher_id
JOIN platform p ON gpl.platform_id = p.id
JOIN region_sales rs ON rs.game_platform_id = gpl.id
GROUP BY ge.id, p.id
ORDER BY genre_sale DESC, p.platform_name, ge.genre_name;

-- Section5

SELECT
    game_name,
    region_name,
    total_sales,
    rank_in_region
FROM (
    SELECT
        g.game_name AS game_name,
        r.region_name AS region_name,
        SUM(rs.num_sales) AS total_sales,
        DENSE_RANK() OVER (PARTITION BY r.region_name ORDER BY SUM(rs.num_sales) DESC) AS rank_in_region
    FROM game g
    JOIN game_publisher gpu ON gpu.game_id = g.id
    JOIN game_platform gpl ON gpl.game_publisher_id = gpu.id
    JOIN region_sales rs ON rs.game_platform_id = gpl.id
    JOIN region r ON r.id = rs.region_id
    GROUP BY g.id, r.id
) AS game_region_sales
WHERE rank_in_region < 11
ORDER BY region_name, total_sales DESC, game_name;

-- Section6

SELECT
    g.game_name AS game_name,
    group_concat(p.publisher_name ORDER BY publisher_name) AS publishers
FROM game g
JOIN game_publisher gp ON gp.game_id = g.id
JOIN publisher p ON p.id = gp.publisher_id
GROUP BY g.id
HAVING COUNT(gp.publisher_id) > 1
ORDER BY g.game_name;


