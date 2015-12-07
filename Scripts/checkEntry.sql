DELIMITER //
DROP PROCEDURE IF EXISTS checkEntry // 

CREATE PROCEDURE checkEntry(IN entryId int,IN usernameIn varchar)
BEGIN
   SELECT * 
      FROM entries
      WHERE EntryID = entryId;
      AND User = usernameIn;
      
END//
DELIMITER ;