CREATE TABLE "ingredients" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "price" NUMERIC,
    PRIMARY KEY ("id")
);

CREATE TABLE "donuts" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "gluten_free" BOOLEAN NOT NULL,
    "price" NUMERIC,
    "ingredient_id" INTEGER,
    PRIMARY KEY ("id"),
    FOREIGN KEY ("ingredient_id") REFERENCEs "ingredients"("id")
);

CREATE TABLE "orders" (
    "id" INTEGER,
    "order_number" TEXT NOT NULL UNIQUE,
    "donut_id" INTEGER,
    "customer_id" INTEGER,
    PRIMARY KEY ("id"),
    FOREIGN KEY ("donut_id") REFERENCES "donuts"("id"),
    FOREIGN KEY ("customer_id") REFERENCEs "customers"("id")
);

CREATE TABLE "customers" (
    "id" INTEGER,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT,
    "order_id" INTEGER,
    PRIMARY KEY ("id"),
    FOREIGN KEY ("order_id") REFERENCES "orders"("id")
);
