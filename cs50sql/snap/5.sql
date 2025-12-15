SELECT *
FROM "friends" AS "f"
JOIN "users" AS "m" ON "f"."user_id" = "m"."id"
WHERE "m"."username" = "lovelytrust487"
OR "m"."username" = "exceptionalinspiration482"
ORDER BY "friend_id";
