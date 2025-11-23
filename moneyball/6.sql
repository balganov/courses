SELECT "t"."name", SUM("p"."H") as "total hits"
FROM "performances" AS "p"
JOIN "teams" AS "t" ON "p"."team_id" = "t"."id"
GROUP BY "t"."name", "p"."year"
HAVING "p"."year" = 2001
ORDER BY "total hits" DESC
LIMIT 5;
