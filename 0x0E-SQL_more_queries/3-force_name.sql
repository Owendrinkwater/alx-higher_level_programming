-- Create force_name table with a NOT NULL constraint on name

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
