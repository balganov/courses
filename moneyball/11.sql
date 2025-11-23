SELECT  "pl"."first_name", "pl"."last_name", ("s"."salary"/"p"."H") as "dollars per hit"
FROM "salaries" AS "s"
JOIN "players" AS "pl" ON "s"."player_id" =  "pl"."id"
JOIN "performances" AS "p" ON "p"."player_id" =  "pl"."id"
WHERE "s"."year" = 2001 AND "p"."year" = 2001 AND "p"."H" != 0
ORDER BY "dollars per hit", "pl"."first_name", "pl"."last_name"
LIMIT 10;
