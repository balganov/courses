CREATE VIEW "most_populated" AS
SELECT "district",
SUM("families") as "families",
SUM("households") as "housholds",
SUM("population") as "population",
SUM("male") as "male",
SUM("female") as "female"
FROM "census"
GROUP BY "district"
ORDER BY "population" DESC;

