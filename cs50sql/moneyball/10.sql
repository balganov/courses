SELECT  "pl"."first_name", "pl"."last_name", "s"."salary", "s"."year", "p"."HR"
FROM "salaries" AS "s"
JOIN "players" AS "pl" ON "s"."player_id" =  "pl"."id"
JOIN "performances" AS "p" ON "p"."player_id" =  "pl"."id"
WHERE "s"."year" = "p"."year"
ORDER BY "pl"."id","p"."year" DESC, "P"."HR" DESC, "s"."salary" DESC
