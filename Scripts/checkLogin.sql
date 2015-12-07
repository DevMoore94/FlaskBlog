DELIMITER //
DROP PROCEDURE IF EXISTS checkLogin // 

CREATE PROCEDURE checkLogin(IN usernameIn varchar)
BEGIN
   SELECT password 
      FROM users
      WHERE username = usernameIn;
      
      
END//
DELIMITER ;