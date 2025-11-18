--SELECT COUNT(*) FROM (
SELECT "s"."name", "s"."city"
FROM "schools" AS "s"
JOIN "districts" AS "d" ON "s"."district_id" = "d"."id"
WHERE "s"."state" = 'MA' AND "s"."type" = 'Public School'
AND "d"."type" = 'Public School District';
--);
