SELECT * FROM (
    SELECT "pl"."first_name", "pl"."last_name"
    FROM "salaries" AS "s"
    JOIN "players" AS "pl" ON "s"."player_id" =  "pl"."id"
    JOIN "performances" AS "p" ON "p"."player_id" =  "pl"."id"
    WHERE "s"."year" = 2001 AND "p"."year" = 2001 AND "p"."H" != 0
    ORDER BY ("s"."salary"/"p"."H"), "pl"."id"
    LIMIT 10
)
INTERSECT
SELECT * FROM (
    SELECT "pl"."first_name", "pl"."last_name"
    FROM "salaries" AS "s"
    JOIN "players" AS "pl" ON "s"."player_id" =  "pl"."id"
    JOIN "performances" AS "p" ON "p"."player_id" =  "pl"."id"
    WHERE "s"."year" = 2001 AND "p"."year" = 2001 AND "p"."RBI" != 0
    ORDER BY ("s"."salary"/"p"."RBI"), "pl"."id"
    LIMIT 10
) ORDER BY "last_name";
