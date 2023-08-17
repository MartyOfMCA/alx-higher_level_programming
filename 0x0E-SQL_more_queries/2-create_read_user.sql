-- Create the database hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create a new user user_0d_2
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
IDENTIFIED BY 'user_0d_2_pwd';

-- Grant the newly added user the select
-- privilege in the database hbtn_0d_2
GRANT SELECT
ON hbtn_0d_2.*
TO 'user_0d_2'@'localhost';
