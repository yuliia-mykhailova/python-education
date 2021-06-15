CREATE TABLE Users(
    user_id SERIAL,
    email varchar(255),
    password varchar(255),
    first_name varchar(255),
    last_name varchar(255),
    middle_name varchar(255),
    is_staff smallint,
    country varchar(255),
    city varchar(255),
    address text,
    PRIMARY KEY (user_id)
);

CREATE TABLE Order_status(
    order_status_id SERIAL,
    status_name varchar(255),
    PRIMARY KEY (order_status_id)
);

CREATE TABLE Categories(
    category_id SERIAL,
    category_title varchar(255),
    category_description text,
    PRIMARY KEY (category_id)
);

CREATE TABLE Products(
    product_id SERIAL,
    product_title varchar(255),
    product_description text,
    in_stock INT,
    price FLOAT,
    slug varchar(45),
    category_id INT,
    PRIMARY KEY (product_id),
    FOREIGN KEY (category_id)
        REFERENCES Categories(category_id)
);

CREATE TABLE Carts(
    cart_id SERIAL,
    Users_user_id INT,
    subtotal DECIMAL,
    total DECIMAL,
    timestamp TIMESTAMP(2),
    PRIMARY KEY (cart_id),
    FOREIGN KEY (Users_user_id)
        REFERENCES Users(user_id)
);

CREATE TABLE Cart_product(
    carts_cart_id SERIAL,
    products_product_id INT,
    FOREIGN KEY (carts_cart_id)
        REFERENCES Carts(cart_id),
    FOREIGN KEY (products_product_id)
        REFERENCES Products(product_id)
);

CREATE TABLE Orders(
    order_id SERIAL,
    Carts_cart_id INT,
    Order_status_order_status_id INT,
    shipping_total DECIMAL,
    total DECIMAL,
    created_at TIMESTAMP(2),
    updated_at TIMESTAMP(2),
    PRIMARY KEY (order_id),
    FOREIGN KEY (Carts_cart_id)
        REFERENCES Carts(cart_id),
    FOREIGN KEY (Order_status_order_status_id)
        REFERENCES Order_status(order_status_id)
);