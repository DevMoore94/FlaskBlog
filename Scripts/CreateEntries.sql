DROP TABLE IF EXISTS entries;
CREATE TABLE entries (
  EntryID int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  Title varchar(50) NOT NULL,
  Content varchar(500) NOT NULL,
  User varchar(25) NOT NULL,
  FOREIGN KEY (User) REFERENCES users(Username)
);

