CREATE TABLE IF NOT EXISTS City(
    id_abbreviation serial PRIMARY KEY,
    city_abbreviation varchar(5) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS Address(
    id_street serial PRIMARY KEY ,
    street varchar(30) NOT NULL,
    house varchar(5) NOT NULL,
    phone varchar(10) NOT NULL,
    id_abbreviation INT NOT NULL,
    FOREIGN KEY (id_abbreviation)
        REFERENCES City(id_abbreviation)
);

CREATE TABLE IF NOT EXISTS Customer(
    id_customer serial PRIMARY KEY,
    first_name varchar(20) NOT NULL,
    last_name varchar(30) NOT NULL,
    address INT,
    FOREIGN KEY (address)
        REFERENCES Address(id_street)
);

CREATE TABLE IF NOT EXISTS Branch(
    id_branch serial PRIMARY KEY,
    branch_name varchar(20),
    address INT NOT NULL,
    FOREIGN KEY (address)
        REFERENCES Address(id_street)
);

CREATE TABLE IF NOT EXISTS Car(
    license_plate varchar(15) PRIMARY KEY,
    model varchar(50) NOT NULL,
    price decimal(6, 2) NOT NULL,
    id_branch INT NOT NULL,
    FOREIGN KEY (id_branch)
        REFERENCES Branch(id_branch)
);

CREATE TABLE IF NOT EXISTS Rent(
    id_rent serial PRIMARY KEY,
    days smallint NOT NULL,
    license_plate varchar(15) NOT NULL,
    CONSTRAINT license_plate_fkey
        FOREIGN KEY (license_plate)
            REFERENCES Car(license_plate)
                ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Rent_Customer(
    id_rent INT NOT NULL,
    id_customer INT,
    date timestamp NOT NULL,
    CONSTRAINT id_rent_fkey
        FOREIGN KEY (id_rent)
            REFERENCES Rent(id_rent)
                ON DELETE CASCADE,
    FOREIGN KEY (id_customer)
        REFERENCES Customer(id_customer)
);