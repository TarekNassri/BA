CREATE TABLE IF NOT EXISTS continent(
	id BIGINT PRIMARY KEY,
	name VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS country(
	id BIGINT PRIMARY KEY,
	name VARCHAR(50),
	isPartOF BIGINT REFERENCES continent(id) ON DELETE NO ACTION ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS city(
	id BIGINT PRIMARY KEY,
	name VARCHAR(50),
	isPartOF BIGINT REFERENCES country(id) ON DELETE NO ACTION ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS person(
	id BIGINT PRIMARY KEY,	
	firstName VARCHAR(50) NOT NULL,
	lastName VARCHAR(50)  NOT NULL,
	gender VARCHAR(20),
	birthday DATE CHECK (birthday <= CURRENT_DATE),
	creationDate TIMESTAMPTZ NOT NULL,
	locationIP VARCHAR(20),
	browserUsed VARCHAR(50),
	isLocatedIn BIGINT REFERENCES city(id) ON DELETE NO ACTION ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS personEmail(
	id SERIAL PRIMARY KEY,
	persId BIGINT NOT NULL REFERENCES person(id) ON DELETE CASCADE ON UPDATE CASCADE,
	email VARCHAR(50) NOT NULL CHECK  (email LIKE '%@%.%'),
	UNIQUE(persId, email)
);

CREATE TABLE IF NOT EXISTS personSpeaks(
	id SERIAL PRIMARY KEY,
	persId BIGINT NOT NULL REFERENCES person(id) ON DELETE CASCADE ON UPDATE CASCADE,
	speaks VARCHAR(50) NOT NULL,
    UNIQUE(persId, speaks)
);

CREATE TABLE IF NOT EXISTS knows(
	pers1 BIGINT NOT NULL REFERENCES person(id) ON DELETE CASCADE ON UPDATE CASCADE,
	pers2 BIGINT NOT NULL REFERENCES person(id) ON DELETE CASCADE ON UPDATE CASCADE,
	creationdate TIMESTAMPTZ,
	PRIMARY KEY (pers1, pers2)
);

CREATE TABLE IF NOT EXISTS tag(
	id BIGINT PRIMARY KEY,
	tagName VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS tagClass(
	id BIGINT PRIMARY KEY,
	tagClassName VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS hasType(
	tagId BIGINT NOT NULL REFERENCES tag(id) ON DELETE CASCADE ON UPDATE CASCADE,
	tagClassId BIGINT NOT NULL REFERENCES tagclass(id) ON DELETE NO ACTION ON UPDATE CASCADE,
	PRIMARY KEY (tagId, tagClassId)
);

CREATE TABLE IF NOT EXISTS isSubclassOf(
	tagClassId BIGINT REFERENCES tagClass(id) ON DELETE CASCADE ON UPDATE CASCADE,
	subClassId BIGINT REFERENCES tagClass(id) ON DELETE CASCADE ON UPDATE CASCADE,
	--check that something isn't it's own subclass
	CONSTRAINT chk_reflexiv_class CHECK (tagclassId <> subclassId),
	PRIMARY KEY (tagClassId, subClassId)
	
);

CREATE TABLE IF NOT EXISTS forum(
	id BIGINT PRIMARY KEY,
	title VARCHAR(255),
	creationdate TIMESTAMPTZ NOT NULL,
	moderator BIGINT REFERENCES person(id) ON DELETE NO ACTION ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS forumHasTag(
	forumId BIGINT NOT NULL REFERENCES forum(id) ON DELETE CASCADE ON UPDATE CASCADE,
	tagId BIGINT NOT NULL REFERENCES tag(id) ON DELETE CASCADE ON UPDATE NO ACTION,
	PRIMARY KEY (forumId, tagId)
);

CREATE TABLE IF NOT EXISTS hasMember(
	forumId BIGINT NOT NULL REFERENCES forum(id) ON DELETE CASCADE ON UPDATE CASCADE,
	persId BIGINT NOT NULL REFERENCES person(id) ON DELETE CASCADE ON UPDATE CASCADE,
	joindate DATE NOT NULL,
	PRIMARY KEY(persId, forumId)
);

CREATE TABLE IF NOT EXISTS post(
	id BIGINT PRIMARY KEY,
	imageFile VARCHAR(200),
	creationDate timestamp with time zone,
	locationIP VARCHAR(31),
	browserUsed VARCHAR(127),
	lang VARCHAR(50) DEFAULT NULL,
	content VARCHAR(250),
	length BIGINT,
	creator BIGINT references person(id),
	forumId BIGINT REFERENCES forum(id) ON DELETE CASCADE ON UPDATE CASCADE,
	islocatedIn BIGINT references country(id)
);

CREATE TABLE comment (
	id BIGINT PRIMARY KEY,
	creationDate timestamp with time zone,
	locationIP VARCHAR(31),
	browserUsed VARCHAR(31),
	content VARCHAR(250),
	length BIGINT,
	creator BIGINT references person(id),
	islocatedIn BIGINT references country(id),
	replyOfPost BIGINT references post(id) ON DELETE CASCADE ON UPDATE CASCADE,
	replyOfComment BIGINT references comment(id) ON DELETE CASCADE ON UPDATE CASCADE
CONSTRAINT reply CHECK(
    (replyOfComment IS NOT NULL AND replyOfPost IS NULL) OR
    (replyOfComment IS NULL AND replyOfPost IS NOT NULL)) -- Kommentar kann sich nur auf einen Kommentar ODER einen Post beziehen
);

CREATE TABLE IF NOT EXISTS university(
	id BIGINT PRIMARY KEY,
	name VARCHAR(255) NOT NULL,
	islocatedin BIGINT REFERENCES city(id) ON DELETE NO ACTION ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS company(
	id BIGINT PRIMARY KEY,
	name VARCHAR(255) NOT NULL,
	islocatedin BIGINT REFERENCES country(id) ON DELETE NO ACTION ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS studyAt(
	persId BIGINT NOT NULL REFERENCES person(id) ON DELETE CASCADE ON UPDATE CASCADE,
	uniId BIGINT NOT NULL REFERENCES university(id) ON DELETE CASCADE ON UPDATE CASCADE,
	classyear INTEGER NOT NULL,
	PRIMARY KEY (persId, uniId)
);

CREATE TABLE IF NOT EXISTS worksAt(
	persId BIGINT NOT NULL REFERENCES person(id) ON DELETE CASCADE ON UPDATE CASCADE,
	compId BIGINT NOT NULL REFERENCES company(id) ON DELETE CASCADE ON UPDATE CASCADE,
	workfrom INTEGER NOT NULL,
	PRIMARY KEY (persId, compId)
);

CREATE TABLE IF NOT EXISTS likesPost (
  personId BIGINT REFERENCES person (id)
  ON DELETE CASCADE --loesche alle Likes einer Person, wenn diese geloescht wird
  ON UPDATE CASCADE,
  postId BIGINT REFERENCES post(id)
  ON DELETE CASCADE -- loesche alle Likes eines Posts, wenn dieser geloescht wird
  ON UPDATE CASCADE,
  lp_creationDate TIMESTAMP WITH TIME ZONE NOT NULL,
  PRIMARY KEY (personId, postId)
);

CREATE TABLE IF NOT EXISTS likesComment (
  personId BIGINT REFERENCES person(id)
  ON DELETE CASCADE --loesche alle Likes einer Person, wenn diese geloescht wird
  ON UPDATE CASCADE,
  commentId BIGINT REFERENCES comment(id)
  ON DELETE CASCADE -- loesche alle Likes eines Kommentars, wenn dieser geloescht wird
  ON UPDATE CASCADE,
  lc_creationDate TIMESTAMP WITH TIME ZONE NOT NULL,
  PRIMARY KEY (personId, commentId)
);

CREATE TABLE IF NOT EXISTS hasInterest(
	persId BIGINT NOT NULL REFERENCES person(id) ON DELETE CASCADE ON UPDATE CASCADE,
	tagId BIGINT NOT NULL REFERENCES tag(id) ON DELETE CASCADE ON UPDATE CASCADE,
	PRIMARY KEY(persId, tagId)
);  

CREATE TABLE IF NOT EXISTS CommenthasTag (
	CommentID BIGINT,
	tagID BIGINT
);

CREATE TABLE IF NOT EXISTS posthasTag (
	PostID BIGINT,
	TagID BIGINT
);
 