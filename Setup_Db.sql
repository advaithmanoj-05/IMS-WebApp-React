
-- Run 1st :- CREATE DATABASE --
CREATE DATABASE `stockmanagementsystem`;
USE `stockmanagementsystem`;
-- ---------------------------------


-- Run 2nd :- CREATE TABLE --
CREATE TABLE stocks (
    id INT NOT NULL AUTO_INCREMENT,
    item_id MEDIUMTEXT NOT NULL,
    name MEDIUMTEXT NOT NULL,
    price MEDIUMTEXT NOT NULL,
    quantity MEDIUMTEXT NOT NULL,
    category MEDIUMTEXT NOT NULL,
    date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(id)
);
-- ---------------------------------