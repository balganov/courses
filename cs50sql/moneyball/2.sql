SELECT "s"."year", "s"."salary"
FROM "salaries" AS "s"
JOIN "players" AS "p" ON "s"."player_id" =  "p"."id"
WHERE "p"."first_name" = 'Cal' AND "p"."last_name" = "Ripken"
ORDER BY "year" DESC;
