SELECT "d"."state", AVG("se"."needs_improvement") "Average need imrpovement"
FROM "districts" as "d"
JOIN "staff_evaluations" as "se" ON "d"."id" = "se"."district_id"
GROUP BY "d"."state"
ORDER BY "Average need imrpovement" DESC
LIMIT 5;
