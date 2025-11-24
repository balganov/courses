
-- *** The Lost Letter ***
--I searched by the address from the description to get it's id
SELECT * FROM "addresses" WHERE "address" = '900 Somerville Avenue';

--I found packages sent from that address by it's id
SELECT * FROM "packages" WHERE "from_address_id" =
    (SELECT "id"  FROM "addresses" WHERE "address" = '900 Somerville Avenue');

--I found the destination address by specifying that it was a Congratulatory letter
SELECT * FROM "addresses" WHERE "id" =
    (SELECT "to_address_id" FROM "packages" WHERE "from_address_id" =
        (SELECT id  FROM "addresses" WHERE "address" = '900 Somerville Avenue')
    AND "contents" = 'Congratulatory letter');

--I double checked if package was not dropped to another address
SELECT * FROM "scans" WHERE "package_id" = 384;

-- *** The Devious Delivery ***
--I looked for packages without sender address to identify the contents
SELECT * FROM "packages" WHERE "from_address_id" IS NULL;

--I checked the log from scans table by left join and identified the destination
SELECT * FROM "scans"
    LEFT JOIN "addresses" ON "scans"."address_id" = "addresses"."id"
    WHERE "scans"."package_id" = (SELECT "id" FROM "packages" WHERE "from_address_id" IS NULL);


-- *** The Forgotten Gift ***
--I found the package id by specifying the address it was sent from
SELECT * FROM "packages"
JOIN "addresses" ON "packages"."from_address_id" = "addresses"."id"
WHERE "addresses"."address" = '109 Tileston Street'

--I joined 4 tables in order to track locations, drivers' names and addresses. I found out that it was eventually picked up by another driver
SELECT "action", "timestamp", "contents", "name", "address" FROM "scans"
LEFT JOIN "packages" ON "scans"."package_id" = "packages"."id"
LEFT JOIN "drivers" ON "scans"."driver_id" = "drivers"."id"
LEFT JOIN "addresses" ON "scans"."address_id" = "addresses"."id"
WHERE "scans"."package_id" = 9523
ORDER BY "timestamp";
