graduation_rates

SELECT "s"."name", "e"."per_pupil_expenditure"
FROM "schools" AS "s"
JOIN "expenditures" AS "e" ON "d"."id" = "e"."district_id"
ORDER BY "e"."per_pupil_expenditure" DESC
LIMIT 10;

