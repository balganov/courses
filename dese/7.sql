SELECT "s"."name"
FROM "schools" AS "s"
JOIN "districts" AS "d" ON "s"."district_id" = "d"."id"
WHERE "d"."name" = 'Cambridge';
