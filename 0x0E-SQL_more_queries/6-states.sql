-- Create the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Connect to the newly created database
CONNECT hbtn_0d_usa;

-- Create the table named states in the 
-- current database
CREATE TABLE IF NOT EXISTS states
(
	id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
	name VARCHAR(256) NOT NULL
);
