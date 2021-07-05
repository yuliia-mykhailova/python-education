-- All indexes
CREATE INDEX customer_id_customer_idx ON customer(id_customer, address);
DROP INDEX customer_id_customer_idx;

CREATE INDEX rent_customer_id_customer_id_rent_idx ON rent_customer(id_customer, id_rent);
DROP INDEX rent_customer_id_customer_id_rent_idx;

CREATE INDEX car_license_plate_idx ON car USING hash
(
    license_plate
);
DROP INDEX car_license_plate_idx;

CREATE INDEX branch_id_branch_idx ON branch(id_branch);
DROP INDEX branch_id_branch_idx;


-- 1. Select 5 customers who rented the biggest amount of cars and summary spent money
EXPLAIN ANALYSE
SELECT c.*, count(rc.id_customer) AS cars_rented, sum(r.days*c2.price) AS summary_spent FROM customer c
INNER JOIN rent_customer rc USING(id_customer)
JOIN rent r USING(id_rent)
JOIN car c2 USING(license_plate)
GROUP BY c.id_customer
ORDER BY count(rc.id_customer) DESC
LIMIT 5;


-- 2. Select 10 the most expensive unrented cars license plate of which starts with 1a...
EXPLAIN ANALYSE
SELECT c.*, b.branch_name, b.address FROM car c
LEFT OUTER JOIN rent r USING (license_plate)
JOIN branch b on b.id_branch = c.id_branch
WHERE c.license_plate LIKE '1a%'
ORDER BY c.price DESC
LIMIT 10;


-- 3. Select 10 the biggest amount of customers who lives in one building with a branch and the average of prices in each
EXPLAIN ANALYSE
SELECT b.*, COUNT(id_customer) AS customers_in_building, AVG(c2.price) AS avg_of_cars_price FROM branch b
INNER JOIN customer c USING (address)
INNER JOIN car c2 on b.id_branch = c2.id_branch
GROUP BY b.id_branch
ORDER BY COUNT(id_customer) DESC
LIMIT 10;