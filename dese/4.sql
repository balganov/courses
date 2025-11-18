--SELECT COUNT(*) FROM (
SELECT "d"."city", COUNT("s"."name") AS 'Number of Schools'
FROM "schools" AS "s"
JOIN "districts" AS "d" ON "s"."district_id" = "d"."id"
GROUP BY "d"."name"
ORDER BY 'Number of Schools'
LIMIT 10
--);
