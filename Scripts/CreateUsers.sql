DROP TABLE IF EXISTS entries;
CREATE TABLE users (
  UserID int NOT NULL AUTO_INCREMENT,
  Username varchar(50) NOT NULL,
  Password  varchar(500) NOT NULL,
  UserID int DEFAULT NULL,
  CONSTRAINT entries_pk PRIMARY KEY (EntryID)
);
