-- If car was never rented and price is <= 500 - delete, else - make discount
CREATE OR REPLACE PROCEDURE check_cars(percent float)
LANGUAGE plpgsql
AS $$
DECLARE
    car_record record;
BEGIN
    FOR car_record IN (SELECT c.license_plate, c.price FROM car c
        LEFT JOIN rent r USING (license_plate)
        WHERE r.license_plate IS NULL)
        LOOP
            IF car_record.price <= 500 THEN
                DELETE FROM car WHERE license_plate=car_record.license_plate;
            ELSE
                UPDATE car
                SET price=price-price*percent/100
                WHERE license_plate=car_record.license_plate;
            END IF;
        END LOOP;
    COMMIT;
END;
$$;

CALL check_cars(10);

SELECT * FROM car c
LEFT JOIN rent r USING (license_plate)
WHERE r.license_plate IS NULL AND price<=500;

DROP PROCEDURE check_cars(percent float);


-- Check if car is in rent
CREATE OR REPLACE PROCEDURE add_rent(rent_id int,
                                    customer_id int,
                                    days_rent int,
                                    license_plate_rent varchar)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS(SELECT * FROM car c
        JOIN rent r USING (license_plate)
        JOIN rent_customer rc USING (id_rent)
        WHERE rc.date+r.days*interval '1 day'>NOW()) THEN
        RAISE EXCEPTION 'Car is still in rent';
    ELSE
        INSERT INTO rent VALUES (rent_id, days_rent, license_plate_rent);
        INSERT INTO rent_customer VALUES (rent_id, customer_id, NOW());
        COMMIT;
    END IF;
END;
$$;

CALL add_rent(60001, 1, 1, 'c1308cc3');
DROP PROCEDURE add_rent(percent float);