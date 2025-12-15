EXPLAIN QUERY PLAN WITH "temp" AS (
    SELECT "to_user_id" AS "user_id", COUNT(*)
    FROM "messages" AS "m"
    JOIN "users" AS "u" ON "m"."from_user_id" = "u"."id"
    WHERE "u"."username" = "creativewisdom377"
    GROUP BY "to_user_id"
    ORDER BY COUNT(*) DESC
)
SELECT "user_id" FROM "temp" LIMIT 3;
