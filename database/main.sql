CREATE DATABASE IF NOT EXISTS address;
USE address;

CREATE TABLE IF NOT EXISTS ADDRESS.address (
    Id BIGINT UNSIGNED auto_increment NOT NULL,
    Name varchar(100) NOT NULL,
    Total BIGINT UNSIGNED NOT NULL,
    CONSTRAINT address_pk PRIMARY KEY (Id),
    CONSTRAINT address_unique UNIQUE KEY (Name)
);

CREATE TABLE IF NOT EXISTS ADDRESS.people (
    Id BIGINT UNSIGNED auto_increment NOT NULL,
    Name varchar(100) NOT NULL,
    Surname varchar(100) NOT NULL,
    `Number` LONGTEXT NOT NULL,
    Country LONGTEXT NOT NULL,
    Is_blocked BOOL NOT NULL,
    address_book BIGINT UNSIGNED NOT NULL,
    CONSTRAINT people_pk PRIMARY KEY (Id),
    CONSTRAINT people_unique UNIQUE KEY (Name, Surname, address_book)
);

CREATE TABLE IF NOT EXISTS ADDRESS.`delete` (
    Id BIGINT UNSIGNED auto_increment NOT NULL,
    Info LONGTEXT NOT NULL,
    `Date` DATETIME NOT NULL,
    address_book BIGINT UNSIGNED NOT NULL,
    CONSTRAINT delete_pk PRIMARY KEY (Id)
);

CREATE TABLE IF NOT EXISTS ADDRESS.edit (
    Id BIGINT UNSIGNED auto_increment NOT NULL,
    Info LONGTEXT NOT NULL,
    address_book BIGINT UNSIGNED NOT NULL,
    CONSTRAINT edit_pk PRIMARY KEY (Id)
);

CREATE TABLE IF NOT EXISTS ADDRESS.`search` (
    Id BIGINT UNSIGNED auto_increment NOT NULL,
    Info LONGTEXT NOT NULL,
    address_book BIGINT UNSIGNED NOT NULL,
    CONSTRAINT search_pk PRIMARY KEY (Id)
);