-- 1
CREATE OR REPLACE PROCEDURE decrease_unpopular_products_price(percent float)
LANGUAGE plpgsql
AS $$
BEGIN
    IF percent > 0 THEN
        UPDATE products SET price=price-price*percent/100
        WHERE product_id IN (SELECT product_id FROM products p
            LEFT OUTER JOIN cart_product cp ON p.product_id = cp.products_product_id);
        COMMIT;
    ELSE
        RAISE EXCEPTION 'Unacceptable percent number';
    END IF;
END;
$$;


CALL decrease_unpopular_products_price(10.0);
CALL decrease_unpopular_products_price(-10.0);

SELECT price FROM products p
LEFT OUTER JOIN cart_product cp ON p.product_id = cp.products_product_id;

DROP PROCEDURE decrease_unpopular_products_price(percent float);


-- 2
CREATE OR REPLACE PROCEDURE staff_order_discount(percent float)
LANGUAGE plpgsql
AS $$
DECLARE
    order_row record;
BEGIN
    FOR order_row IN SELECT o.order_id, o.carts_cart_id FROM orders o
    JOIN carts c on c.cart_id = o.carts_cart_id
    JOIN users u on u.user_id = c.users_user_id
    WHERE is_staff=1 AND order_status_order_status_id IN (1, 2)
        LOOP
            IF EXISTS(SELECT COUNT(cp.products_product_id) FROM cart_product cp
                WHERE carts_cart_id=order_row.carts_cart_id
                HAVING COUNT(cp.products_product_id) > 5) THEN
                UPDATE orders SET total=total-total* percent /100, shipping_total=0
                WHERE order_id=order_row.order_id;
            END IF;
        END LOOP;
    COMMIT;
END;
$$;


CALL staff_order_discount(10.0);

SELECT * FROM orders WHERE order_id=16;

DROP PROCEDURE staff_order_discount(percent float);
