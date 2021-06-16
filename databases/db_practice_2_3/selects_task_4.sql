-- 4.1 Select products that were never added to cart
SELECT * FROM products LEFT JOIN cart_product cp on products.product_id = cp.products_product_id WHERE products_product_id IS NULL;

-- 4.2 Select products that were never added to order (but could had been added to cart)
SELECT * FROM products WHERE product_id IN (
    SELECT products_product_id FROM cart_product LEFT JOIN orders o USING(carts_cart_id) WHERE o.carts_cart_id IS NULL
    );

-- 4.3 Select top 10 products that were added to cart most often
SELECT product_title, COUNT(product_id) FROM products INNER JOIN cart_product cp on products.product_id = cp.products_product_id
GROUP BY product_title
ORDER BY COUNT DESC
LIMIT 10;

-- 4.4 Select top 10 products that were added to order most often
SELECT product_title, COUNT(carts_cart_id) FROM products INNER JOIN cart_product cp on products.product_id = cp.products_product_id
JOIN orders o USING (carts_cart_id)
GROUP BY product_title
ORDER BY COUNT(carts_cart_id) DESC
LIMIT 10;

-- 4.5 Select top 5 users that spent more money in total
SELECT users.*, MAX(o.total) FROM users INNER JOIN carts c on users.user_id = c.users_user_id INNER JOIN orders o on c.cart_id = o.carts_cart_id
WHERE o.order_status_order_status_id=4
GROUP BY users.user_id
ORDER BY MAX DESC
LIMIT 5;

-- 4.6 Select top 5 users that made the biggest amount or orders
SELECT users.*, COUNT(users_user_id) FROM users INNER JOIN carts c on users.user_id = c.users_user_id INNER JOIN orders o on c.cart_id = o.carts_cart_id
GROUP BY users.user_id
ORDER BY COUNT DESC
LIMIT 5;

-- 4.7 Select top 5 users that created carts but didn't make an order
SELECT users.*, COUNT(c.users_user_id) FROM users INNER JOIN carts c on users.user_id = c.users_user_id LEFT JOIN orders o on c.cart_id = o.carts_cart_id
WHERE o.carts_cart_id IS NULL
GROUP BY users.user_id
ORDER BY COUNT DESC
LIMIT 5;
