-- Create a new database
Create database CienciaDatos

-- Select the database to work with
use CienciaDatos

-- Create a table to store product data
create table producto(id int, nombre varchar(20), clase varchar (20))

-- Create a table to store users data
create table usuario(id int, nombre varchar(20), direccion varchar (50))

-- Create a table to store sales data
create table venta(id int, costo int)

-- Add sample products to the product table
INSERT INTO producto (id, nombre, clase) VALUES
(1, 'Laptop', 'Electronics'),
(2, 'Mouse', 'Accessories'),
(3, 'Keyboard', 'Accessories'),
(4, 'Monitor', 'Electronics'),
(5, 'Notebook', 'Stationery');

-- Add sample users to the user table
INSERT INTO usuario (id, nombre, direccion) VALUES
(1, 'Alice', 'San Jose'),
(2, 'Bob', 'Alajuela'),
(3, 'Carlos', 'Cartago'),
(4, 'Diana', 'Heredia'),
(5, 'Eva', 'Puntarenas');

-- Add sample sales records to the sales table
INSERT INTO venta (id, costo) VALUES
(1, 500),
(2, 25),
(3, 45),
(4, 300),
(5, 15);