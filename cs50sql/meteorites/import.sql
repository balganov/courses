CREATE TABLE "meteorites_temp" (
    "name" TEXT,
    "id" INTEGER,
    "name_type" TEXT,
    "class" TEXT,
    "mass" NUMERIC,
    "discovery" TEXT CHECK ("discovery" in ("Fell", "Found")),
    "year" DATETIME,
    "lat" NUMERIC,
    "long" NUMERIC,
    PRIMARY KEY("id")
);

UPDATE "meteorites_temp"
SET "mass" = NULL
WHERE "mass" = '';

UPDATE "meteorites_temp"
SET "year" = NULL
WHERE "year" = '';

UPDATE "meteorites_temp"
SET "lat" = NULL
WHERE "lat" = '';

UPDATE "meteorites_temp"
SET "long" = NULL
WHERE "long" = '';

CREATE TABLE "meteorites" (
    "id" INTEGER,
    "name" TEXT,
    "class" TEXT,
    "mass" NUMERIC,
    "discovery" TEXT CHECK ("discovery" in ("Fell", "Found")),
    "year" DATETIME,
    "lat" NUMERIC,
    "long" NUMERIC,
    PRIMARY KEY("id")
);

INSERT INTO "meteorites" ("name", "class", "mass", "discovery", "year", "lat", "long")
SELECT "name", "class", ROUND("mass",2), "discovery", "year", ROUND("lat",2), ROUND("long",2)
FROM "meteorites_temp"
WHERE "name_type" != 'Relict'

