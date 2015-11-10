DROP TABLE IF EXISTS users;
CREATE TABLE users (
  UserID int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  Username varchar(25) NOT NULL,
  Password  varchar(25) NOT NULL
);
