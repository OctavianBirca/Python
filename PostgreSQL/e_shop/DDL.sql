CREATE TABLE price (
    id integer PRIMARY KEY,
    product_price integer NOT NULL, 
    currency character varying NOT NULL
);

CREATE TABLE money (
    id integer PRIMARY KEY,
    amount integer NOT NULL, 
    currency character varying NOT NULL
);

CREATE TABLE products (
    id integer PRIMARY KEY,
    product character varying NOT NULL,
    price integer 
);

ALTER TABLE "products"
RENAME product TO name,
RENAME id_p TO id,
RENAME price TO price_id;

DROP TABLE products;

CREATE TABLE products (
    id integer PRIMARY KEY,
    name character varying NOT NULL,
    price_id integer
    );

ALTER TABLE "products"
ADD CONSTRAINT fk_product_price FOREIGN KEY (price_id)
REFERENCES "price" (id) 
; 




CREATE TABLE stock (
    id integer PRIMARY KEY,
    product_id character varying NOT NULL,
    quantity integer 
);

ALTER TABLE "stock"
ALTER COLUMN product_id TYPE integer USING product_id::integer;

ALTER TABLE "stock"
ADD CONSTRAINT fk_product_name FOREIGN KEY (product_id)
REFERENCES "products" (id); 

ALTER TABLE "stock"
RENAME CONSTRAINT fk_product_name TO fk_stock_products;

CREATE TABLE clients (
    id integer PRIMARY KEY,
    fullName character varying NOT NULL,
    isVip boolean DEFAULT false
);

CREATE TABLE contacts (
    id integer PRIMARY KEY,
    phone character varying NOT NULL,
    email character varying NOT NULL,
    client_id integer
);

ALTER TABLE "contacts"
ADD CONSTRAINT fk_client_name FOREIGN KEY (client_id)
REFERENCES "clients" (id); 

ALTER TABLE "contacts"
RENAME CONSTRAINT fk_client_name TO fk_contacts_clients;

CREATE TABLE "bags" (
    id integer PRIMARY KEY,
    cost_id integer NOT NULL,
    client_id integer NOT NULL
);

ALTER TABLE "bags" 
ADD CONSTRAINT fk_bags_money FOREIGN KEY (cost_id)
REFERENCES "money" (id);

ALTER TABLE "bags" 
ADD CONSTRAINT fk_bags_clients FOREIGN KEY (client_id)
REFERENCES "clients" (id);

CREATE TABLE "bags_items" (
    id integer PRIMARY KEY,
    bag_id integer NOT NULL,
    product_id integer NOT NULL,
    quantity integer
);

ALTER TABLE "bags_items" 
ADD CONSTRAINT fk_bags_itmes_bags FOREIGN KEY (bag_id)
REFERENCES "bags" (id),
ADD CONSTRAINT fk_bags_itmes_products FOREIGN KEY (product_id)
REFERENCES "products" (id);




