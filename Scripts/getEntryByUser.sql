DELIMITER //
DROP PROCEDURE IF EXISTS getEntryByUser // 

CREATE PROCEDURE getEntryByUser(IN usernameIn varchar(25))
BEGIN
   SELECT * 
      FROM entries
      WHERE User = usernameIn;
END//
DELIMITER ;
