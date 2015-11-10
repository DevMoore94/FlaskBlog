DROP TABLE IF EXISTS entries;
CREATE TABLE entries (
  EntryID int NOT NULL AUTO_INCREMENT,
  Title varchar(50) NOT NULL,
  Content varchar(500) NOT NULL,
  UserID int DEFAULT NULL,
  CONSTRAINT entries_pk PRIMARY KEY (EntryID)
  FOREIGN KEY (UserID) REFERENCES users(UserId)
);

