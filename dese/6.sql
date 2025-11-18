SELECT "s"."name"
FROM "schools" as "s"
JOIN "graduation_rates" as "gr" ON "s"."id" = "gr"."school_id"
WHERE "gr"."graduated" = 100;
