SELECT "d"."city", AVG("se"."needs_improvement") "Average needs imrpovement"
FROM "districts" as "d"
JOIN "staff_evaluations" as "se" ON "d"."id" = "se"."district_id"
GROUP BY "d"."city"
ORDER BY "Average needs imrpovement" DESC
LIMIT 5;
