SELECT "pl"."first_name", "pl"."last_name", "s"."salary"
FROM "salaries" AS "s"
JOIN "players" AS "pl" ON "s"."player_id" =  "pl"."id"
WHERE "s"."year" = 2001
ORDER BY "s"."salary", "pl"."first_name", "pl"."last_name", "pl"."id"
LIMIT 50;
