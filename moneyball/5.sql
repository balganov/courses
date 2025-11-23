SELECT DISTINCT "t"."name"
FROM "performances" AS "p"
JOIN "players" AS "pl" ON "p"."player_id" =  "pl"."id"
JOIN "teams" AS "t" ON "p"."team_id" = "t"."id"
WHERE "pl"."first_name" = 'Satchel' AND "pl"."last_name" = "Paige"
;
