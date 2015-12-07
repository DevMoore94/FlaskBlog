DELIMITER //
DROP PROCEDURE IF EXISTS checkLogin // 

CREATE PROCEDURE checkLogin(IN usernameIn varchar(25))
BEGIN
   SELECT Password 
      FROM users
      WHERE Username = usernameIn;
      
      
END//
DELIMITER ;
