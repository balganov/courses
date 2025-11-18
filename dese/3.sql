SELECT COUNT(*) FROM (
SELECT "d"."name", AVG("per_pupil_expenditure") AS 'Average District Per-Pupil Expenditure'
FROM "districts" AS "d"
JOIN "expenditures" AS "e" ON "d"."id" = "e"."district_id"
GROUP BY "d"."name"
);
