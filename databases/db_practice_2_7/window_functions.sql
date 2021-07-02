CREATE OR REPLACE FUNCTION compare_product_price_with_avg()
RETURNS TABLE (
                category_title varchar,
                product_title varchar,
                price float,
                avg float
              )
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
        SELECT c.category_title, p.product_title, p.price, AVG(p.price)
            OVER (PARTITION BY p.category_id) AS avg
        FROM products p
        JOIN categories c USING (category_id);
END;
$$;

SELECT * FROM compare_product_price_with_avg();

DROP FUNCTION compare_product_price_with_avg();