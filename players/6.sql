SELECT "first_name", "last_name", "debut"
FROM "players"
WHERE "birth_city" = 'Pittsburgh' AND "birth_state" = 'PA'
ORDER BY "last_name", "first_name", "debut" DESC;
