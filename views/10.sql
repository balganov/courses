SELECT "english_title" as "Title"
FROM "views"
WHERE "artist" = 'Hokusai'
ORDER BY "entropy" DESC
LIMIT 3;
