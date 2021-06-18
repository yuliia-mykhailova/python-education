CREATE TABLE potential_customers(
    id SERIAL PRIMARY KEY,
    email varchar(100),
    name varchar(100),
    surname varchar(100),
    second_name varchar(100),
    city varchar(50)
);

INSERT INTO potential_customers (email, name, surname, second_name, city) VALUES
    ('ksirrafa201@gmail.com', 'Sufyan', 'Hull', 'second_name1', 'city 1'),
    ('1khaled1094i@gmail.com', 'Linda', 'Smart', 'second_name2', 'city 2'),
    ('usuraj_4ukool@gmail.com', 'Ashleigh', 'Xiong', 'second_name3', 'city 3'),
    ('hadn0has0@gmail.com', 'Abbigail', 'Lyon', 'second_name4', 'city 4'),
    ('rjos@gmail.com', 'Maysa', 'Downs', 'second_name5', 'city 5'),
    ('4mohcenmadrid2@gmail.com', 'Meerab', 'Vazquez', 'second_name6', 'city 17'),
    ('esala@gmail.com', 'Bella', 'Mohamed', 'second_name7', 'city 7'),
    ('qcrispi@gmail.com', 'Nelson', 'Brennan', 'second_name8', 'city 8'),
    ('fjalen.k@gmail.com', 'Sarah', 'Spears', 'second_name9', 'city 9'),
    ('6ckijcyyronny9@gmail.com', 'Marius', 'Curtis', 'second_name10', 'city 10'),
    ('gaziz.boussrirat@gmail.com', 'Katrina', 'Melia', 'second_name11', 'city 17'),
    ('eniraj.sing@gmail.com', 'Natasha', 'Foley', 'second_name12', 'city 11'),
    ('coco.laprincet@gmail.com', 'Pablo', 'Brown', 'second_name13', 'city 12'),
    ('7driss.dissonen@gmail.com', 'Haider', 'Cuevas', 'second_name14', 'city 13'),
    ('isofiko15@gmail.com', 'Olly', 'Pope', 'second_name15', 'city 14'),
    ('ymessi.alsidcheit@gmail.com', 'Dolcie', 'Bradley', 'second_name16', 'city 17'),
    ('7bra@gmail.com', 'Finnlay', 'Lyons', 'second_name17', 'city 15'),
    ('yalaa.1998j@gmail.com', 'Mihai', 'Graves', 'second_name1', 'city 16'),
    ('7sreena@gmail.com', 'Hayden', 'Sinclair', 'second_name2', 'city 17'),
    ('iabdessamad.oualm@gmail.com', 'Penelope', 'Gilliam', 'second_name3', 'city 18'),
    ('dboys-swag@gmail.com', 'Hania', 'Sargent', 'second_name4', 'city 19'),
    ('guhig41s@gmail.com', 'Magdalena', 'Kearney', 'second_name5', 'city 1'),
    ('ghero_ja@gmail.com', 'Miah', 'Mckenna', 'second_name6', 'city 17'),
    ('geo.demonxx666xl@gmail.com', 'Kaira', 'Feeney', 'second_name7', 'city 15'),
    ('kmohamedmesh@gmail.com', 'Naveed', 'Lane', 'second_name4', 'city 17'),
    ('nmomo-fran@gmail.com', 'Alexandra', 'Huber', 'second_name4', 'city 14'),
    ('xchemsoumos@gmail.com', 'Tiana', 'Rivas', 'second_name6', 'city 13'),
    ('fsmartclub.indiai@gmail.com', 'Amiyah', 'Macias', 'second_name4', 'city 12'),
    ('ndimuthu.lakmal2r@gmail.com', 'Everly', 'Griffin', 'second_name13', 'city 11'),
    ('jbru.jhhghj5@gmail.com', 'Denzel', 'Cole', 'second_name11', 'city 17'),
    ('aihab@gmail.com', 'Diogo', 'Holloway', 'second_name10', 'city 18'),
    ('ywissampatrond@gmail.com', 'Millie', 'Tierney', 'second_name9', 'city 10'),
    ('zabd.pp@gmail.com', 'Katy', 'Vickers', 'second_name8', 'city 16'),
    ('snand.kisho@gmail.com', 'Waqas', 'Mullins', 'second_name7', 'city 17'),
    ('roninho@gmail.com', 'Arnie', 'Bray', 'second_name6', 'city 14'),
    ('qjipoboy@gmail.com', 'Chris', 'Ratliff', 'second_name5', 'city 13'),
    ('jsaef.drd@gmail.com', 'Fenton', 'Giles', 'second_name4', 'city 12'),
    ('cfernand@gmail.com', 'Aleisha', 'Couch', 'second_name3', 'city 17');

-- Select users and potential customers from city 17
SELECT name, email FROM potential_customers WHERE city='city 17'
UNION
SELECT first_name, email FROM users WHERE city='city 17';