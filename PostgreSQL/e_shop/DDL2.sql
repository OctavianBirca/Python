CREATE TABLE price (
    id SERIAL PRIMARY KEY,
    product_price integer NOT NULL, 
    currency character varying NOT NULL
);

CREATE TABLE money (
    id SERIAL PRIMARY KEY,
    amount integer NOT NULL, 
    currency character varying NOT NULL
);


CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name character varying NOT NULL,
    price_id integer
    );

ALTER TABLE "products"
ADD CONSTRAINT fk_product_price FOREIGN KEY (price_id)
REFERENCES "price" (id) 
; 




CREATE TABLE stock (
    id SERIAL PRIMARY KEY, 
    product_id integer NOT NULL,
    quantity integer 
);



ALTER TABLE "stock"
ADD CONSTRAINT fk_stock_products FOREIGN KEY (product_id)
REFERENCES "products" (id); 


CREATE TABLE clients (
    id SERIAL PRIMARY KEY,
    fullName character varying NOT NULL,
    isVip boolean DEFAULT false
);

CREATE TABLE contacts (
    id SERIAL PRIMARY KEY,
    phone character varying NOT NULL,
    email character varying NOT NULL,
    client_id integer
);

ALTER TABLE "contacts"
ADD CONSTRAINT fk_contacts_clients FOREIGN KEY (client_id)
REFERENCES "clients" (id); 


CREATE TABLE "bags" (
    id SERIAL PRIMARY KEY,
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
    id SERIAL PRIMARY KEY,
    bag_id integer NOT NULL,
    product_id integer NOT NULL,
    quantity integer
);

ALTER TABLE "bags_items" 
ADD CONSTRAINT fk_bags_itmes_bags FOREIGN KEY (bag_id)
REFERENCES "bags" (id),
ADD CONSTRAINT fk_bags_itmes_products FOREIGN KEY (product_id)
REFERENCES "products" (id);
