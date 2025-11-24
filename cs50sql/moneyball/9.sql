SELECT "t"."name", ROUND(AVG("s"."salary"),2) as "average salary"
FROM "salaries" "s"
JOIN "teams" "t" ON "s"."team_id" =  "t"."id"
WHERE "s"."year" = 2001
GROUP BY "t"."name"
ORDER BY AVG("s"."salary")
LIMIT 5;
