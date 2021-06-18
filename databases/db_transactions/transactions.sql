-- Set price lower for 10% than rollback
BEGIN;
UPDATE products SET price=price-price*0.1;
SELECT price FROM products;
ROLLBACK;


-- Set price lower for 40% for products where in stock(10-20) and price(380-400)
BEGIN;
SAVEPOINT before_updating_price;

UPDATE products SET price=price-price*0.4
WHERE in_stock BETWEEN 10 AND 20
AND price BETWEEN 380 AND 400;

ROLLBACK TO before_updating_price;
COMMIT;


-- Add new status for order, change status of orders for 01.05.2020-30.06.2020 new status
BEGIN;
SAVEPOINT before_insert_new_status;

INSERT INTO order_status
VALUES (6, 'Renewed');

SELECT * FROM order_status;

SAVEPOINT before_changing_orders;
UPDATE orders
SET order_status_order_status_id=6
WHERE order_status_order_status_id=5
AND created_at BETWEEN '2020-05-01' AND '2020-06-30'
AND total BETWEEN 500 AND 1100;

SELECT * FROM orders
WHERE order_status_order_status_id=6;

ROLLBACK TO before_changing_orders;
ROLLBACK TO before_insert_new_status;
COMMIT;


-- Add new potential customer, change name, delete user by old name
BEGIN;
INSERT INTO potential_customers(email, name, surname, second_name, city)
VALUES ('someemail@gmail.com', 'Linda', 'Smith', 'second_name14', 'city 17');

SELECT * FROM potential_customers;

UPDATE potential_customers
SET name = 'Fill'
WHERE name = 'Linda';
SAVEPOINT update_point;

DELETE FROM potential_customers
WHERE name = 'Linda';

ROLLBACK TO SAVEPOINT update_point;
COMMIT;