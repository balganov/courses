SELECT "d"."name", "e"."per_pupil_expenditure"
FROM "districts" AS "d"
JOIN "expenditures" AS "e" ON "d"."id" = "e"."district_id"
ORDER BY "e"."per_pupil_expenditure" DESC
LIMIT 10;
