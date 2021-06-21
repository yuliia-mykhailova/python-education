-- 1
EXPLAIN ANALYZE
SELECT potential_customers.*
FROM potential_customers
WHERE city
LIKE '%1%';

CREATE INDEX potential_customers_city_idx ON potential_customers(city);
DROP INDEX potential_customers_city_idx;

-- 2
EXPLAIN ANALYSE
SELECT users.*
FROM users
INNER JOIN carts c on users.user_id = c.users_user_id
INNER JOIN orders o on c.cart_id = o.carts_cart_id
WHERE is_staff=1 AND o.total>1000;

CREATE INDEX users_user_id_idx ON users(user_id);
CREATE INDEX carts_user_id_idx ON carts(users_user_id);
CREATE INDEX order_cart_id_idx ON orders(carts_cart_id, total);
DROP INDEX users_user_id_idx;
DROP INDEX carts_user_id_idx;
DROP INDEX order_cart_id_idx;


-- 3
EXPLAIN ANALYSE
SELECT p.*, COUNT(cp.products_product_id) AS to_be_in_cart_times
FROM products p
JOIN cart_product cp ON p.product_id = cp.products_product_id
GROUP BY p.product_id
ORDER BY to_be_in_cart_times;

CREATE INDEX products_product_id_idx ON products(product_id);
CREATE INDEX cart_product_products_product_id_idx ON cart_product(products_product_id);
DROP INDEX products_product_id_idx;
DROP INDEX cart_product_products_product_id_idx;


-- 4
EXPLAIN ANALYZE
SELECT products.*
FROM products
INNER JOIN categories
USING(category_id)
WHERE category_id<10 OR category_id IN (13, 17)
ORDER BY category_id;

CREATE INDEX categories_category_id_idx ON categories (category_id);
CREATE INDEX products_category_id_idx ON products (category_id);
DROP INDEX categories_category_id_idx;
DROP INDEX products_category_id_idx;
