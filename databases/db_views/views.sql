-- View for Products table
CREATE MATERIALIZED VIEW most_expensive_not_added_to_cart AS
SELECT products.* FROM products
WHERE  product_id NOT IN (
SELECT products_product_id FROM cart_product
)
ORDER BY price DESC
LIMIT 5;

SELECT most_expensive_not_added_to_cart.* FROM most_expensive_not_added_to_cart;

DROP MATERIALIZED VIEW most_expensive_not_added_to_cart;


-- View for Orders and Order_status
CREATE OR REPLACE VIEW max_orders_by_status AS
SELECT os.status_name, o.shipping_total, MAX(total) AS max_total  FROM orders o
JOIN order_status os ON os.order_status_id = o.order_status_order_status_id
GROUP BY os.status_name, o.shipping_total;

SELECT max_orders_by_status.* FROM max_orders_by_status;

DROP VIEW max_orders_by_status;


-- View for Products and Categories
CREATE OR REPLACE VIEW categories_avg_and_count_products AS
SELECT c.*, COUNT(product_id) AS products_in_category, AVG(p.price) AS avg_price FROM categories c
JOIN products p USING (category_id)
GROUP BY c.category_id
ORDER BY c.category_id;

SELECT categories_avg_and_count_products.* FROM categories_avg_and_count_products;

DROP VIEW categories_avg_and_count_products;