WITH "cte" AS (
    SELECT "username", "to_user_id", COUNT(*)
    FROM "messages" AS "m"
    JOIN "users" AS "u" ON "m"."to_user_id" = "u"."id"
    GROUP BY "to_user_id"
    ORDER BY COUNT(*) DESC
)
SELECT "username" FROM "cte" LIMIT 1;
