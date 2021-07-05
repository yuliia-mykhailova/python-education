-- Set order shipping total = 0 for defined city
CREATE OR REPLACE FUNCTION update_shipping_total(find_city varchar)
RETURNS void
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS(SELECT 1 FROM users
          WHERE city = find_city) THEN
      UPDATE orders SET shipping_total = 0
        WHERE carts_cart_id IN (SELECT o.carts_cart_id FROM users u
        JOIN carts c on u.user_id = c.users_user_id
        JOIN orders o on c.cart_id = o.carts_cart_id
        WHERE u.city = find_city);
    ELSE
        RAISE EXCEPTION '% not found', find_city;
    END IF;
END;
$$;


BEGIN;

SELECT update_shipping_total('city 1');
SELECT u.city, o.shipping_total FROM orders o
JOIN carts c ON o.carts_cart_id = c.cart_id
JOIN users u ON u.user_id = c.users_user_id
WHERE u.city = 'city 1';

ROLLBACK;

DROP FUNCTION update_shipping_total(find_city varchar);