
/* CREATE A PRODUCT */
BEGIN;
INSERT INTO "price" VALUES (1, 10000, 'EUR');
INSERT INTO "products" VALUES (1, 'Box - S', 1);
INSERT INTO "stock" VALUES (1, 1, 100);
COMMIT;

BEGIN;
INSERT INTO "price" VALUES (2, 15000, 'EUR');
INSERT INTO "products" VALUES (2, 'Box - M', 2);
INSERT INTO "stock" VALUES (2, 2, 85);
COMMIT;

BEGIN;
INSERT INTO "price" VALUES (3, 23400, 'EUR');
INSERT INTO "products" VALUES (3, 'Box - L', 3);
INSERT INTO "stock" VALUES (3, 3, 200);
COMMIT;

BEGIN;
INSERT INTO "price" VALUES (4, 30000, 'EUR');
INSERT INTO "products" VALUES (4, 'Box - XL', 4);
INSERT INTO "stock" VALUES (4, 4, 34);
COMMIT;


/* SHOW THE PRODCUTS, PRICE AND STOCK */
SELECT "products".id, "products".name , "stock".quantity, "price".product_price, "price".currency
FROM "products" 
JOIN "stock" ON "stock".product_id = "products".id
JOIN "price" on "products".price_id = "price".id; 


/*DELETE A PRODUCT*/

BEGIN;
DELETE FROM "stock" WHERE product_id = 4;
DELETE FROM "products" WHERE price_id = 4;
DELETE FROM "price" WHERE id = 4;
COMMIT;


/*UPDATE THE STOCK*/

UPDATE "stock"
SET quantity = quantity - 18
WHERE product_id = 3;



/*CREATE A CLIENT*/

BEGIN;
INSERT INTO "clients" VALUES (1, 'Mary Kay', false);
INSERT INTO "contacts" VALUES (1, '+2332313321', 'mk@mail.com', 1);
COMMIT;

BEGIN;
INSERT INTO "clients" VALUES (2, 'John Wick', true);
INSERT INTO "contacts" VALUES (2, '+23334323321', 'jw@mail.com', 2);
COMMIT;

BEGIN;
INSERT INTO "clients" VALUES (3, 'Julien Dupont', false);
INSERT INTO "contacts" VALUES (3, '+2432399999', 'jd@mail.com', 3);
COMMIT;

/* SHOW THE PRODCUTS, PRICE AND STOCK */
SELECT "clients".id, "clients".fullName , "clients".isVip, "contacts".phone, "contacts".email
FROM "clients" 
JOIN "contacts" ON "contacts".client_id = "clients".id

/* CREATE A BAG */

BEGIN;
INSERT INTO "money" VALUES (1, 10000 * 5, 'EUR');
INSERT INTO "bags" VALUES (1, 1, 2);
INSERT INTO "bags_items" VALUES (1, 1, 2, 5);
UPDATE "stock" SET quantity = quantity - 5 WHERE product_id = 1;
COMMIT;

/*SHOW client's bag*/

SELECT "bags".id, "clients".fullName, "products".name, "bags_items".quantity
FROM "bags_items"
JOIN "bags" ON "bags_items".bag_id = "bags".id
JOIN "clients" ON "bags".client_id = "clients".id
JOIN "products" ON "bags_items".product_id = "products".id;

