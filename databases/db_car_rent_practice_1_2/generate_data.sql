INSERT INTO city (id_abbreviation, city_abbreviation)
SELECT
       i::int,
       'C' || i::text
FROM generate_series(1, 195) s(i);
SELECT * FROM city;


INSERT INTO address (id_street, street, house, phone, id_abbreviation)
SELECT
       i::int,
       'street ' || i::text,
       floor(random()*30)::text,
       floor(random()*(9999999999-1000000000)+1000000000)::text,
       floor(random()*(195-1)+1)::int
FROM generate_series(1, 10000) s(i);


INSERT INTO customer (id_customer, first_name, last_name, address)
SELECT
       i::int,
       'name ' || i::text,
       'surname ' || i::text,
       floor(random()*(10000-1)+1)::int
FROM generate_series(1, 50000) s(i);
SELECT * FROM customer;


INSERT INTO branch (id_branch, branch_name, address)
SELECT
       i::int,
       'br_name ' || i::text,
       floor(random()*(10000-1)+1)::int
FROM generate_series(1, 30000) s(i);


INSERT INTO car (license_plate, model, price, id_branch)
SELECT
       left(md5(i::text), 8)::text,
       'model ' || i::text,
       floor(random()*(10000-500)+500)::decimal,
       floor(random()*(30000-1)+1)::int
FROM generate_series(1, 60000) s(i);


INSERT INTO rent (id_rent, days, license_plate)
SELECT
       i::int,
       floor(random()*(100-1)+1)::int,
       left(md5(floor(random()*(60000-1)+1)::text), 8)::text
FROM generate_series(1, 60000) s(i);


INSERT INTO rent_customer (id_rent, id_customer, date)
SELECT
       i::int,
       floor(random()*(50000-1)+1)::int,
       random() * (timestamp '2021-12-31' - timestamp '2018-01-01')+timestamp '2018-01-01'::timestamp
FROM generate_series(1, 60000) s(i);