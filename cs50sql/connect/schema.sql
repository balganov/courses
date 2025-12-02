CREATE TABLE "users" (
    "id" INTEGER,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "password" TEXT NOT NULL,
    PRIMARY KEY ("id")
);

CREATE TABLE "schools" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "type" TEXT,
    "location" TEXT,
    "year" INTEGER,
    PRIMARY KEY ("id")
);

CREATE TABLE "companies" (
    "id" INTEGER,
    "name" TEXT NOT NULL UNIQUE,
    "industry" TEXT NOT NULL CHECK ("concourse" IN ('A', 'B', 'C', 'D', 'E', 'F', 'T')),
    "location" TEXT NOT NULL,
    PRIMARY KEY ("id")
);

CREATE TABLE "connections" (
    "user_id" INTEGER,
    "connected_to" INTEGER,
    "school_id" INTEGER,
    "school_start_date" NUMERIC,
    "school_graduation_date" NUMERIC,
    "degree" TEXT NOT NULL CHECK ("degree" IN ('BA', 'MA', 'PhD')),
    "company_start_date" NUMERIC,
    "company_end_date" NUMERIC,
    "title" TEXT,
    "destination_code" TEXT,
    "departure_datetime" NUMERIC,
    "arrival_datetime" NUMERIC,
    FOREIGN KEY ("user_id") REFERENCES "users"("id"),
    FOREIGN KEY ("connected_to") REFERENCES "users"("id"),
    FOREIGN KEY ("school_id") REFERENCES "schools"("id")
);
