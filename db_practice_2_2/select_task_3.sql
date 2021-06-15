-- Select products that > 80.00 and <= 150.00
SELECT * FROM products WHERE price BETWEEN 80.00 AND 150.00;

SELECT * FROM products WHERE price > 80.00 AND price <= 150.00;

-- Select orders that were created after 01.10.2020
SELECT * FROM orders WHERE created_at > '2020-10-01';

-- Select orders that were added during first 6 months
SELECT * FROM orders WHERE created_at BETWEEN '2020-01-01' AND '2020-06-30';

SELECT * FROM orders WHERE created_at >= '2020-01-01' AND created_at <= '2020-06-30';

-- Select products from categories 7, 11 and 18
SELECT * FROM products WHERE category_id IN (7, 11, 18);

SELECT  * FROM products WHERE category_id=7 OR category_id=11 OR category_id=18;

-- Select unfinished orders by 31.12.2020
SELECT * FROM orders WHERE order_status_order_status_id NOT IN (4, 5) AND created_at<='2020-12-31';

-- Select carts that were created but order was never added
SELECT * FROM carts c LEFT JOIN orders o on c.cart_id = o.carts_cart_id WHERE o.carts_cart_id IS NULL;
SELECT cart_id FROM carts EXCEPT SELECT carts_cart_id FROM orders;