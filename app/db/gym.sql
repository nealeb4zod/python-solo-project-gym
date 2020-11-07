DROP TABLE activities;
DROP TABLE members;
DROP TABLE membership_types;
DROP TABLE instructors;


CREATE TABLE instructors (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    date_of_birth DATE NOT NULL,
    address TEXT,
    phone_number VARCHAR(255) NOT NULL
);

CREATE TABLE membership_types (
    id SERIAL PRIMARY KEY,
    typed VARCHAR(255) NOT NULL
);

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    date_of_birth DATE NOT NULL,
    address TEXT,
    phone_number VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    membership_type INT REFERENCES membership_types(id),
    start_date DATE NOT NULL,
    active_membership BOOLEAN NOT NULL
);

CREATE TABLE activities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    instructor INT REFERENCES instructors(id),
    date_time TIMESTAMP NOT NULL,
    duration INT NOT NULL,
    capacity INT NOT NULL,
    membership_type INT REFERENCES membership_types(id)
);
