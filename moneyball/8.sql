SELECT "s"."salary"
FROM "salaries" AS "s"
JOIN "players" AS "pl" ON "s"."player_id" =  "pl"."id"
JOIN "performances" AS "p" ON "p"."player_id" =  "pl"."id"
WHERE "p"."year" = 2001 AND "s"."year" = 2001
ORDER BY "p"."HR" DESC
LIMIT 1;
