SELECT "d"."city", COUNT("s"."name") AS "Number of Schools"
FROM "schools" AS "s"
JOIN "districts" AS "d" ON "s"."district_id" = "d"."id"
WHERE "s"."type" = 'Public School'
GROUP BY "d"."city"
HAVING "Number of Schools" <= 3
ORDER BY "Number of Schools" DESC, "d"."city"
LIMIT 10
