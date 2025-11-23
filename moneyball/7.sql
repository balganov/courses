SELECT "pl"."first_name", "pl"."last_name"
FROM "salaries" AS "s"
JOIN "players" AS "pl" ON "s"."player_id" =  "pl"."id"
ORDER BY "s"."salary" DESC
LIMIT 1;
