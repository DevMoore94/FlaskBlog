DROP TABLE IF EXISTS entries;
CREATE TABLE entries (
  EntryID int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  Title varchar(50) NOT NULL,
  Content LONGTEXT NOT NULL,
  User varchar(25) NOT NULL,
  Time timestamp NOT NULL,
  FOREIGN KEY (User) REFERENCES users(Username)
);

