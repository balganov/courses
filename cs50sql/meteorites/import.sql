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
