CREATE DATABASE chemical_db;

USE chemical_db;

CREATE TABLE chemicals (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cas_number VARCHAR(20) NOT NULL,
    ec_number VARCHAR(20) NOT NULL,
    name TEXT NOT NULL
);

CREATE INDEX idx_cas_number ON chemicals (cas_number);
CREATE INDEX idx_ec_number ON chemicals (ec_number);

select * from chemicals;

DROP TABLE chemicals;

DELETE FROM chemicals;