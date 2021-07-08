-- Returns table with cars and their amount of rents by branch
CREATE OR REPLACE FUNCTION car_rents_by_branch(branch_id int)
RETURNS TABLE(
    license_plate varchar,
    model varchar,
    count_rented int
)
LANGUAGE plpgsql
AS $$
DECLARE
    car_record record;
BEGIN
    FOR car_record IN (SELECT c.license_plate, c.model, COUNT(r.license_plate) AS count_rented
                        FROM car c
                        JOIN rent r USING (license_plate)
                        WHERE c.id_branch=branch_id
                        GROUP BY c.license_plate, c.model
                        ORDER BY count_rented DESC)
        LOOP
            license_plate := car_record.license_plate;
            model := car_record.model;
            count_rented := car_record.count_rented;
            RETURN NEXT;
        END LOOP;
END;
$$;

SELECT * FROM car_rents_by_branch(3);
DROP FUNCTION IF EXISTS car_rents_by_branch(branch_id int);


-- Returns how much money customer spent by customer id
CREATE OR REPLACE FUNCTION customers_spent_money(customer_id int)
RETURNS TABLE(
    first_name varchar,
    last_name varchar,
    address varchar,
    spent_money double precision
)
LANGUAGE plpgsql
AS $$
DECLARE customer_record record;
BEGIN
    FOR customer_record IN (SELECT c.first_name,
                                   c.last_name,
                                   CONCAT(c2.city_abbreviation, ' ', a.house,' ', a.street) AS address,
                                   SUM(r.days*c3.price) AS spent_money
                        FROM customer c
                        JOIN address a ON a.id_street = c.address
                        JOIN city c2 USING (id_abbreviation)
                        JOIN rent_customer rc USING (id_customer)
                        JOIN rent r USING (id_rent)
                        JOIN car c3 USING (license_plate)
                        WHERE c.id_customer=customer_id
                        GROUP BY c.first_name, c.last_name, CONCAT(c2.city_abbreviation, ' ', a.house,' ', a.street)
                        ORDER BY spent_money DESC)
        LOOP
            first_name := customer_record.first_name;
            last_name := customer_record.last_name;
            address := customer_record.address;
            spent_money := customer_record.spent_money;
            RETURN NEXT;
        end loop;
END;
$$;

SELECT * FROM customers_spent_money(4);
DROP FUNCTION IF EXISTS customers_spent_money(branch_id int);