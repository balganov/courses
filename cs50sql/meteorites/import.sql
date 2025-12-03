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
)
