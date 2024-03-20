--2a

CREATE view friendship_View (userId1, userId2, creationdate) AS (
     SELECT pers1 , pers2, creationdate  
     FROM knows 
  UNION
     SELECT pers2, pers1, creationdate
     FROM knows  	
 )
 
 --SELECT * from friendship_View;
 
 
CREATE VIEW pkp_symmetric AS
Select pers1,
pers2, 
creationdate
from person_knows_person
UNION Select
pers2 AS pers1, 
pers1 AS pers2,
creationdate from person_knows_person;