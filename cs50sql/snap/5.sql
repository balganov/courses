EXPLAIN QUERY PLAN SELECT "friend_id"
FROM "friends" AS "f"
JOIN "users" AS "m" ON "f"."user_id" = "m"."id"
WHERE "m"."username" = "lovelytrust487"
INTERSECT
SELECT "friend_id"
FROM "friends" AS "f"
JOIN "users" AS "m" ON "f"."user_id" = "m"."id"
WHERE "m"."username" = "exceptionalinspiration482";
