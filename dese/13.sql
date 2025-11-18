SELECT "d"."state", "se"."needs_improvement"
FROM "districts" as "d"
JOIN "staff_evaluations" as "se" ON "d"."id" = "se"."district_id"
ORDER BY "se"."needs_improvement" DESC
LIMIT 5;
