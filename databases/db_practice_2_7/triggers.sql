-- 1
CREATE OR REPLACE FUNCTION product_trigger()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    IF NEW.price=OLD.price OR NEW.price<=0 THEN
        RAISE EXCEPTION 'Wrong price';
    END IF;
    RETURN NEW;
END;
$$;

CREATE TRIGGER new_product_check
BEFORE UPDATE OF price
ON products
FOR EACH ROW
EXECUTE FUNCTION product_trigger();

DROP TRIGGER IF EXISTS new_product_check ON products;

BEGIN;
UPDATE products SET price=60 WHERE product_id=1;
SELECT * FROM products WHERE product_id=1;
ROLLBACK;


-- 2
CREATE OR REPLACE FUNCTION user_trigger()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS(SELECT 1 FROM potential_customers pc
        WHERE pc.email=NEW.email AND
              pc.name=NEW.first_name AND
              pc.surname=NEW.last_name AND
              pc.second_name=NEW.middle_name AND
              pc.city=NEW.city) THEN
        DELETE FROM potential_customers pc
        WHERE NEW.email=pc.email AND
              NEW.first_name=pc.name AND
              NEW.last_name=pc.surname AND
              NEW.middle_name=pc.second_name AND
              NEW.city=pc.city;
    END IF;
    RETURN NEW;
END;
$$;

CREATE TRIGGER new_user_check
AFTER INSERT
ON users
FOR EACH ROW
EXECUTE FUNCTION user_trigger();

DROP TRIGGER IF EXISTS new_user_check ON users;

BEGIN;
INSERT INTO users (user_id, email, password, first_name, last_name, middle_name, is_staff, country, city, address, phone_number)
VALUES (3001, 'ksirrafa201@gmail.com', '1234', 'Sufyan', 'Hull', 'second_name1', 0, 'country 1', 'city 1', 'address', '34343434');
ROLLBACK;
