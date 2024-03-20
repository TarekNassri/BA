CREATE TEMP Table IF NOT EXISTS  place(
 id smallint,
 name text not null,
 url text not null,
 type varchar(10) not null,
 ispartof smallint
);

COPY place FROM 'C:\Temp\social_network\place_0_0.csv' DELIMITER '|' CSV HEADER;
SELECT * FROM place;

INSERT into continent(id, name)
SELECT id, name
FROM place
WHERE type='continent';

SELECT * FROM continent;

INSERT into country(id, name, ispartof)
SELECT id, name, ispartof
FROM place
WHERE type='country';

INSERT into city(id, name, ispartof)
SELECT id, left(name, 50), ispartof
FROM place
WHERE type='city';

SELECT * FROM city;

CREATE TEMP TABLE IF NOT EXISTS organisation (
organisationid smallint,
type varchar(10),
name text,
url text,
organisationplace smallint	
);

COPY organisation FROM 'C:\Temp\social_network\organisation_0_0.csv' DELIMITER '|' CSV HEADER;
SELECT * FROM organisation;

INSERT into university(id, name, islocatedin)
SELECT organisationid, name, organisationplace
FROM organisation
WHERE type='university';

INSERT into company(id, name, islocatedin)
SELECT organisationid, name, organisationplace
FROM organisation
WHERE type='company';

CREATE TEMP TABLE temptagclass (
  id smallint,
  name text,
  url text
);

COPY temptagclass FROM 'C:\Temp\social_network\tagclass_0_0.csv' DELIMITER '|' CSV HEADER;

INSERT into tagclass(id, tagClassName)
SELECT id, name
FROM temptagclass;

COPY isSubclassOf FROM 'C:\Temp\social_network\tagclass_isSubclassOf_tagclass_0_0.csv' DELIMITER '|' CSV HEADER;
SELECT * FROM issubclassof;

CREATE temp TABLE IF NOT EXISTS temptag(
  id serial not null,
  name text not null,
  url text not null	
);


COPY temptag FROM 'C:\Temp\social_network\tag_0_0.csv' DELIMITER '|' CSV HEADER;
SELECT count(*) FROM tag;

insert into tag(id, tagname)
select id,name
from temptag;

COPY hastype FROM 'C:\Temp\social_network\tag_hasType_tagclass_0_0.csv' DELIMITER '|' CSV HEADER;

SELECT * FROM hastype;

COPY person FROM 'C:\Temp\social_network\person_0_0.csv' DELIMITER '|' CSV HEADER;

Select * from person;

COPY forum FROM 'C:\Temp\social_network\forum_0_0.csv' DELIMITER '|' CSV HEADER;

Select * from forum;

COPY post FROM 'C:\Temp\social_network\post_0_0.csv' DELIMITER '|' CSV HEADER; 

select * from post ;

COPY comment FROM 'C:\Temp\social_network\comment_0_0.csv' DELIMITER '|' CSV HEADER;

select * from comment ;

CREATE temp TABLE tempmail (
	PersonID BIGINT,
	email VARCHAR(200)
);

COPY tempmail FROM 'C:\Temp\social_network\person_email_emailaddress_0_0.csv' DELIMITER '|' CSV HEADER;

insert into personEmail(persId, email)
select personID, email
from tempmail;

select * from personEmail ;

CREATE temp TABLE templang (
	PersonID BIGINT,
	language VARCHAR(31)
);

COPY templang FROM 'C:\Temp\social_network\person_speaks_language_0_0.csv' DELIMITER '|' CSV HEADER;

insert into personSpeaks(persId, speaks)
select PersonID, language
from templang;

COPY knows FROM 'C:\Temp\social_network\person_knows_person_0_0.csv' DELIMITER '|' CSV HEADER;

COPY likesComment FROM 'C:\Temp\social_network\person_likes_comment_0_0.csv' DELIMITER '|' CSV HEADER;

COPY  likesPost FROM 'C:\Temp\social_network\person_likes_post_0_0.csv' DELIMITER '|' CSV HEADER;

COPY  hasInterest FROM 'C:\Temp\social_network\person_hasInterest_tag_0_0.csv' DELIMITER '|' CSV HEADER;

COPY studyAt FROM 'C:\Temp\social_network\person_studyAt_organisation_0_0.csv' DELIMITER '|' CSV HEADER;

COPY worksat FROM 'C:\Temp\social_network\person_workAt_organisation_0_0.csv' DELIMITER '|' CSV HEADER;

COPY hasMember FROM 'C:\Temp\social_network\forum_hasMember_person_0_0.csv' DELIMITER '|' CSV HEADER;
COPY forumhasTag FROM 'C:\Temp\social_network\forum_hasTag_tag_0_0.csv' DELIMITER '|' CSV HEADER;

COPY CommenthasTag FROM 'C:\Temp\social_network\comment_hasTag_tag_0_0.csv' DELIMITER '|' CSV HEADER;

COPY posthasTag FROM 'C:\Temp\social_network\post_hasTag_tag_0_0.csv' DELIMITER '|' CSV HEADER;
