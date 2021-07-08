-- After adding new car. If the price of new car is less than the avg in branch + 5%
CREATE OR REPLACE FUNCTION car_trigger()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    IF NEW.price<(SELECT AVG(price) FROM car WHERE id_branch=NEW.id_branch) THEN
        UPDATE car SET price=price+price*5/100 WHERE license_plate=NEW.license_plate;
    END IF;
    RETURN NEW;
END;
$$;

CREATE TRIGGER new_car
AFTER INSERT
ON car
FOR EACH ROW
EXECUTE FUNCTION car_trigger();

DROP TRIGGER IF EXISTS new_car ON car;


-- Before deleting a car. Check if there is active rent otherwise - raise exception
CREATE OR REPLACE FUNCTION car_rent_trigger()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS(SELECT 1 FROM car c
        JOIN rent r USING (license_plate)
        JOIN rent_customer rc USING (id_rent)
        WHERE license_plate=OLD.license_plate AND
              rc.date+r.days*interval '1 day'>NOW()) THEN
        RAISE EXCEPTION 'Car still have active rent';
    END IF;
    RETURN OLD;
END;
$$;

CREATE TRIGGER check_car_rent
BEFORE DELETE
ON car
FOR EACH ROW
EXECUTE FUNCTION car_rent_trigger();

DROP TRIGGER IF EXISTS car_rent_trigger ON car;