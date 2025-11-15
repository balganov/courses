SELECT "first_name", "last_name", "height" AS "above average height"
FROM "players"
--WHERE "height" > (SELECT AVG("height") FROM "players")
ORDER BY "height" DESC;
