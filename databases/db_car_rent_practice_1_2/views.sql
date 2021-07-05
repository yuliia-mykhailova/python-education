-- View of 10 the most popular branches with num of cars, rents; max, min and avg prices
CREATE MATERIALIZED VIEW top_branch AS
SELECT b.branch_name,
       CONCAT(c2.city_abbreviation, ' ', a.house,' ', a.street) AS address,
       COUNT(b.id_branch) AS number_of_cars,
       COUNT(r.license_plate) AS number_of_rents,
       MAX(c.price) AS max_car_price,
       MIN(c.price) AS min_car_price,
       AVG(c.price) AS avg_car_price
FROM branch b
INNER JOIN car c USING (id_branch)
INNER JOIN rent r USING (license_plate)
JOIN address a ON a.id_street = b.address
JOIN city c2 USING (id_abbreviation)
GROUP BY b.branch_name, CONCAT(c2.city_abbreviation, ' ', a.house,' ', a.street)
ORDER BY COUNT(r.license_plate) DESC, COUNT(b.id_branch)
LIMIT 10;

SELECT * FROM top_branch;
DROP MATERIALIZED VIEW top_branch;


-- View of potential customers who live in one building with a branch but have never rented a car
CREATE OR REPLACE VIEW potential_customers AS
SELECT c.first_name,
       c.last_name,
       b.branch_name,
       CONCAT(c2.city_abbreviation, ' ', a.house,' ', a.street) AS address
FROM customer c
INNER JOIN branch b USING (address)
LEFT OUTER JOIN rent_customer rc USING (id_customer)
JOIN address a ON a.id_street = b.address
JOIN city c2 USING (id_abbreviation);

SELECT * FROM potential_customers;
DROP VIEW potential_customers;


-- View 10 most profitable branches for last year
CREATE OR REPLACE VIEW top_branch_for_year AS
SELECT b.branch_name,
       CONCAT(c2.city_abbreviation, ' ', a.house,' ', a.street) AS address,
       COUNT(r.license_plate) AS num_of_rents,
       COUNT(c.id_branch) AS num_of_cars,
       SUM(c.price*r.days) AS gain
FROM branch b
INNER JOIN car c USING (id_branch)
JOIN rent r on c.license_plate = r.license_plate
JOIN rent_customer rc USING (id_rent)
JOIN address a on a.id_street = b.address
JOIN city c2 USING (id_abbreviation)
WHERE rc.date BETWEEN '2020-01-01' AND '2020-12-31'
GROUP BY b.branch_name, CONCAT(c2.city_abbreviation, ' ', a.house,' ', a.street)
HAVING COUNT(c.id_branch)>5
ORDER BY SUM(c.price*r.days) DESC
LIMIT 10;


SELECT * FROM top_branch_for_year;
DROP VIEW top_branch_for_year;