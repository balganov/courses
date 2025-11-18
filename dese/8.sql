SELECT "d"."name", "e"."pupils"
FROM "districts" AS "d"
JOIN "expenditures" AS "e" ON "d"."id" = "e"."district_id";

