-- This script was generated by a beta version of the ERD tool in pgAdmin 4.
-- Please log an issue at httpsredmine.postgresql.orgprojectspgadmin4issuesnew if you find any bugs, including reproduction steps.
BEGIN;


CREATE TABLE public.Orders
(
    id integer NOT NULL,
    product_id integer NOT NULL,
    adres_id integer NOT NULL,
    user_phone_number character varying(20) NOT NULL,
    delivery_date date NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE public.Products
(
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    description text NOT NULL,
    stock_code character varying(13) NOT NULL,
    category_id integer NOT NULL,
    inventory_id integer NOT NULL,
    price double precision NOT NULL,
    discount_id integer NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE public.Users
(
    id integer NOT NULL,
    user_name character varying(15) NOT NULL,
    password character varying(25) NOT NULL,
    first_name character varying(15) NOT NULL,
    last_name character varying(15) NOT NULL,
    phone_number character varying(20) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE public.discount
(
    id integer NOT NULL,
    discount double precision NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE public.inventory
(
    id integer NOT NULL,
    quantity integer NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE public.order_destails
(
    id integer NOT NULL,
    product_id integer NOT NULL,
	quantity integer NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE public.product_category
(
    id integer NOT NULL,
    name character varying(23),
    description character varying(250),
    PRIMARY KEY (id)
);

CREATE TABLE public.user_address
(
    id integer NOT NULL,
    user_id integer NOT NULL,
    adres_line1 character varying(120) NOT NULL,
    adres_line2 character varying(50) NOT NULL,
    zipcode char NOT NULL,
    country name NOT NULL,
    phone integer NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE public.user_payment
(
    id integer NOT NULL,
    user_id integer NOT NULL,
    payment_type character varying(50) NOT NULL,
    provider character varying(25) NOT NULL,
    account_no character varying(25) NOT NULL,
    payment_date date NOT NULL,
    payment_detail character varying(240) NOT NULL,
    PRIMARY KEY (id)
);

ALTER TABLE public.Orders
    ADD FOREIGN KEY (adres_id)
    REFERENCES public.user_address (id)
    NOT VALID;


ALTER TABLE public.Orders
    ADD FOREIGN KEY (product_id)
    REFERENCES public.Products (id)
    NOT VALID;


ALTER TABLE public.Products
    ADD FOREIGN KEY (category_id)
    REFERENCES public.product_category (id)
    NOT VALID;


ALTER TABLE public.Products
    ADD FOREIGN KEY (category_id)
    REFERENCES public.product_category (id)
    NOT VALID;


ALTER TABLE public.Products
    ADD FOREIGN KEY (discount_id)
    REFERENCES public.discount (id)
    NOT VALID;


ALTER TABLE public.Products
    ADD FOREIGN KEY (inventory_id)
    REFERENCES public.inventory (id)
    NOT VALID;


ALTER TABLE public.order_destails
    ADD FOREIGN KEY (product_id)
    REFERENCES public.Products (id)
    NOT VALID;


ALTER TABLE public.user_address
    ADD FOREIGN KEY (user_id)
    REFERENCES public.Users (id)
    NOT VALID;


ALTER TABLE public.user_payment
    ADD FOREIGN KEY (user_id)
    REFERENCES public.Users (id)
    NOT VALID;


ALTER TABLE public.user_payment
    ADD FOREIGN KEY (user_id)
    REFERENCES public.Users (id)
    NOT VALID;
    
insert into discount(id,discount) values(1,10);
insert into discount(id,discount) values(2,10);
insert into discount(id,discount) values(3,10);
insert into discount(id,discount) values(4,10);
insert into discount(id,discount) values(5,10);
insert into discount(id,discount) values(6,10);
insert into discount(id,discount) values(7,10);
insert into discount(id,discount) values(8,10);
insert into discount(id,discount) values(9,10);
insert into discount(id,discount) values(10,10);


insert into inventory(id,quantity) values(1,100);
insert into inventory(id,quantity) values(2,500);
insert into inventory(id,quantity) values(3,110);
insert into inventory(id,quantity) values(4,120);
insert into inventory(id,quantity) values(5,130);
insert into inventory(id,quantity) values(6,140);
insert into inventory(id,quantity) values(7,150);
insert into inventory(id,quantity) values(8,1000);
insert into inventory(id,quantity) values(9,2210);
insert into inventory(id,quantity) values(10,7810);

insert into product_category(id,name,description) values(10,'CASACAS','CASACAS');
insert into product_category(id,name,description) values(20,'PANTALONES','PANTALONES');
insert into product_category(id,name,description) values(30,'CAMISAS','CAMISAS');
insert into product_category(id,name,description) values(40,'ZAPATOS','ZAPATOS');
insert into product_category(id,name,description) values(50,'ZAPATILLAS','ZAPATILLAS');
insert into product_category(id,name,description) values(60,'MEDIAS','MEDIAS');
insert into product_category(id,name,description) values(70,'BUZOS','BUZOS');


Insert into products(id,name,description,stock_code,category_id,inventory_id,price,discount_id)
values(1,'CASACAS DE HOMBRE','CASACAS DE HOMBRE','100',10,1,120.0,1);
Insert into products(id,name,description,stock_code,category_id,inventory_id,price,discount_id)
values(2,'CASACAS DE HOMBRE','CASACAS DE HOMBRE','120',10,1,120.0,1);
Insert into products(id,name,description,stock_code,category_id,inventory_id,price,discount_id)
values(3,'CASACAS DE HOMBRE','CASACAS DE HOMBRE','50',10,1,120.0,1);
Insert into products(id,name,description,stock_code,category_id,inventory_id,price,discount_id)
values(4,'PANTALONES DE HOMBRE','PANTALONES DE HOMBRE','50',10,1,120.0,1);
Insert into products(id,name,description,stock_code,category_id,inventory_id,price,discount_id)
values(5,'PANTALONES DE MUJER','PANTALONES DE MUJER','50',10,1,120.0,1);
Insert into products(id,name,description,stock_code,category_id,inventory_id,price,discount_id)
values(6,'PANTALONES DE NIÑO','PANTALONES DE NIÑO','50',10,1,120.0,1);    
    

END;
