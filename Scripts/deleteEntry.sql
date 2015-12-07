DELIMITER //
DROP PROCEDURE IF EXISTS deleteEntry // 

CREATE PROCEDURE deleteEntry(IN entryId int,IN usernameIn varchar)
BEGIN
   DELETE 
      FROM entries
      WHERE EntryID = entryId;
      AND User = usernameIn;
      
END//
DELIMITER ;