-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS fruits;
DROP SEQUENCE IF EXISTS fruits_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS fruits_id_seq;
CREATE TABLE fruits (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    calory INTEGER
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO fruits (name, calory) VALUES ('Apple', 15);
INSERT INTO fruits (name, calory) VALUES ('Pear', 1);
INSERT INTO fruits (name, calory) VALUES ('Orange', 3);
INSERT INTO fruits (name, calory) VALUES ('Mango', 8);
INSERT INTO fruits (name, calory) VALUES ('Kiwi', 25);
