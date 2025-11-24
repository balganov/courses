SELECT "d"."name"
FROM "districts" AS "d"
JOIN "expenditures" AS "e" ON "d"."id" = "e"."district_id"
WHERE "e"."pupils" = (SELECT MIN("pupils") FROM "expenditures")
