create database Havi;
use Havi;

create table Customer (
	cus_code      integer,
	cus_lname     varchar(20),
	cus_fname     varchar(20),
	cus_initial   char(1),
	cus_areacode  integer,
	cus_phone     integer,
	primary key (cus_code)
);

create table Vendor (
	vend_code      integer,
	vend_name      varchar(30),
	vend_contact   varchar(30),
	vend_areacode  integer,
	vend_phone     integer,
	primary key (vend_code)
);

create table Product (
	prod_code   integer,
	prod_desc   varchar(50),
	prod_price  integer,
	prod_quant  integer,
	vend_code   integer,
	primary key (prod_code),
	foreign key (vend_code) references Vendor (vend_code)
);

create table Invoice (
	inv_number  integer,
	cus_code    integer,
	inv_date    date,
	primary key (inv_number),
	foreign key (cus_code) references Customer (cus_code)
);

create table Line (
	inv_number  integer,
	prod_code   integer,
	line_units  integer,
	primary key (inv_number, prod_code),
	foreign key (inv_number) references Invoice (inv_number),
	foreign key (prod_code) references Product (prod_code)
);

insert into Customer values (10010, 'Johnson', 'Albert', 'A', 612, 8442573);
insert into Customer values (10011, 'Edwards', 'Leona', 'K', 763, 8941238);
insert into Customer values (10012, 'Smith', 'Walter', 'W', 612, 8942285);
insert into Customer values (10013, 'Roberts', 'Paul', 'F', 612, 2221672);
insert into Customer values (10014, 'Orlando', 'Myla', NULL, 612, 2971228);

insert into Vendor values (232, 'Bryson', 'Smith', 615, 2233234);
insert into Vendor values (235, 'Walls', 'Anderson', 615, 2158995);
insert into Vendor values (236, 'Jason', 'Schmidt', 651, 2468850);

insert into Product values (12321, 'hammer', 189, 20, 232);
insert into Product values (65781, 'chain', 12, 45, 235);
insert into Product values (34256, 'tape', 35, 60, 236);
insert into Product values (12333, 'drill', 200, 10, 232);

insert into Invoice values (1001, 10011, '2008-08-03');
insert into Invoice values (1002, 10014, '2008-08-04');
insert into Invoice values (1003, 10012, '2008-03-20');
insert into Invoice values (1004, 10014, '2008-09-23');

insert into Line values (1001, 12321, 1);
insert into Line values (1001, 65781, 3);
insert into Line values (1002, 34256, 6);
insert into Line values (1003, 12321, 5);
insert into Line values (1002, 12321, 6);

SELECT cus_code, cus_lname, cus_phone
FROM Customer;

SELECT inv_number, inv_date
FROM Invoice
WHERE cus_code = 10014;

SELECT Product.prod_code, prod_desc, prod_quant
FROM Product, Line
WHERE Product.prod_code = Line.prod_code
AND Line.inv_number = 1001;

SELECT prod_desc, prod_price
FROM Product, Vendor
WHERE Product.vend_code = Vendor.vend_code
AND vend_contact = 'Somebody';

SELECT prod_desc, vend_name, vend_phone
FROM Product, Vendor
WHERE Product.vend_code = Vendor.vend_code
AND prod_quant <= 60;

SELECT DISTINCT prod_desc, cus_fname, cus_lname
FROM Customer, Invoice, Line, Product
WHERE Customer.cus_code = Invoice.cus_code
AND Invoice.inv_number = Line.inv_number
AND Line.prod_code = Product.prod_code;
