SELECT "p"."year", "p"."HR"
FROM "performances" AS "p"
JOIN "players" AS "pl" ON "p"."player_id" =  "pl"."id"
WHERE "pl"."first_name" = 'Ken' AND "pl"."last_name" = "Griffey" AND "pl"."birth_year" = 1969
ORDER BY "p"."year" DESC;
