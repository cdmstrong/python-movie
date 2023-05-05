DROP TABLE IF EXISTS Movie;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Staff;

CREATE TABLE Staff
(
	Login			VARCHAR(20)		PRIMARY KEY,
	Password		VARCHAR(40)		NOT NULL,
	FirstName		VARCHAR(20)		NOT NULL,
	LastName		VARCHAR(20)		NOT NULL,
	Mobile			VARCHAR(20)		NOT NULL,
	Email			VARCHAR(50),
	Address			VARCHAR(60),
	Compensation	DECIMAL(10,2)	NOT NULL CHECK (Compensation > 0)
);

INSERT INTO Staff VALUES ('ktaylor', 	'8888', 'Ken', 		'Taylor', 	'0477934342', 'nbrown@mrc.com.au', 		'6 North Terrace Queensland QLD', 	87800.90);
INSERT INTO Staff VALUES ('mmiller', 	'9999', 'Maggie', 	'Miller', 	'0411248453', 'mmiller@mrc.com.au', 	'55/28 Castlehigh St Newtown NSW', 	99000.50);
INSERT INTO Staff VALUES ('jdavis', 	'0123', 'Jamie', 	'Davis', 	'0422349845', 'jdavis@mrc.com.au', 		'8 Grenfell Way Petersham NSW', 	110915.20);
INSERT INTO Staff VALUES ('njohnson', 	'4567', 'Neil', 	'Johnson', 	'0455989822', 'njohnson@mrc.com.au', 	'49 North Terrace Queensland QLD', 	89900.00);
INSERT INTO Staff VALUES ('ganderson', 	'8901', 'Glen', 	'Anderson',	'0413834588', 'ganderson@mrc.com.au', 	'1/15 Castlehigh St Newtown NSW', 	75900.90);
INSERT INTO Staff VALUES ('cbowtel', 	'2222', 'Carie', 	'Bowtel', 	'0481773921', 'cbowtel59@gmail.com', 	'12 Glenfield St Eastgarden NSW', 	99200.70);
INSERT INTO Staff VALUES ('jswift', 	'3333', 'James', 	'Swift', 	'0422834091', 'jamesswift@hotmail.com',	'7 Tesolin Road Eastgate QLD', 		79230.25);
INSERT INTO Staff VALUES ('mchan', 		'5555', 'Maggie', 	'Chan', 	'0449123875', 'maggie_chan@msn.com', 	'22 Greenway St Townsville QLD', 	109355.30);
INSERT INTO Staff VALUES ('opalster', 	'6666', 'Oliver', 	'Palster', 	'0433981245', 'oliver.p@hotmail.com', 	'10 South Terrace Perth City WA', 	94812.80);
INSERT INTO Staff VALUES ('jkeller', 	'7777', 'Jack', 	'Keller',	'0451389100', 'jkeller72@msn.com', 		'36/78 Pitt St Sydney NSW', 		69995.00);

CREATE TABLE Genre
(
	GenreID			SERIAL 			PRIMARY KEY,
	GenreName		VARCHAR(20)		NOT NULL UNIQUE
);

INSERT INTO Genre VALUES (1,  'Action');
INSERT INTO Genre VALUES (2,  'Adventure');
INSERT INTO Genre VALUES (3,  'Comedy');
INSERT INTO Genre VALUES (4,  'Romance');
INSERT INTO Genre VALUES (5,  'Science fiction');
INSERT INTO Genre VALUES (6,  'Crime film');
INSERT INTO Genre VALUES (7,  'Drama');
INSERT INTO Genre VALUES (8,  'Thriller');
INSERT INTO Genre VALUES (9,  'Superhero');
INSERT INTO Genre VALUES (10, 'Horror');
INSERT INTO Genre VALUES (11, 'Fiction');
INSERT INTO Genre VALUES (12, 'Fantasy');
INSERT INTO Genre VALUES (13, 'History');
INSERT INTO Genre VALUES (14, 'Biographical');
INSERT INTO Genre VALUES (15, 'Documentary');
INSERT INTO Genre VALUES (16, 'Musical');
INSERT INTO Genre VALUES (17, 'Narrative');
INSERT INTO Genre VALUES (18, 'Mystery');
INSERT INTO Genre VALUES (19, 'Science');
INSERT INTO Genre VALUES (20, 'War');

CREATE TABLE Movie
(
	ID				SERIAL			PRIMARY KEY,
	Title			VARCHAR(100)	NOT NULL,
	ReleaseDate		DATE			NOT NULL,
	PrimaryGenre	INTEGER			NOT NULL,
	SecondaryGenre	INTEGER,
	AvgRating		DECIMAL(2,1)	CHECK (AvgRating >= 0 AND AvgRating <= 5),
	ManagedBy		VARCHAR(20),
	Description		VARCHAR(500),
	FOREIGN KEY (ManagedBy) REFERENCES Staff,
	FOREIGN KEY (PrimaryGenre) REFERENCES Genre,
	FOREIGN KEY (SecondaryGenre) REFERENCES Genre
);

INSERT INTO Movie (Title, ReleaseDate, PrimaryGenre, SecondaryGenre, AvgRating, ManagedBy, Description) VALUES ('Captain America: Civil War',	'28/04/2016',  1,	  20, 	4.6, 'jdavis',	'Friction arises between the Avengers when one group supports the government''s decision to implement a law to control their powers while the other opposes it.');
INSERT INTO Movie (Title, ReleaseDate, PrimaryGenre, SecondaryGenre, AvgRating, ManagedBy, Description) VALUES ('Avengers: Endgame', 			'24/04/2019',  1,	NULL, 	5.0, 'mchan',	'After Thanos, an intergalactic warlord, disintegrates half of the universe, the Avengers must reunite and assemble again to reinvigorate their trounced allies and restore balance.');
INSERT INTO Movie (Title, ReleaseDate, PrimaryGenre, SecondaryGenre, AvgRating, ManagedBy, Description) VALUES ('Spider-Man: Homecoming', 		'28/06/2017',  1,	NULL, 	  0, 'jkeller', 'Peter Parker balances his life as an ordinary high school student in Queens with his superhero alter-ego Spider-Man, and finds himself on the trail of a new menace prowling the skies of New York City.');
INSERT INTO Movie (Title, ReleaseDate, PrimaryGenre, SecondaryGenre, AvgRating, ManagedBy, Description) VALUES ('Iron Man 3', 					'24/04/2013',  1,	NULL, 	  0, 'jdavis', 	'Tony Stark encounters a formidable foe called the Mandarin. After failing to defeat his enemy, Tony embarks on a journey of self-discovery as he fights against the powerful Mandarin.');
INSERT INTO Movie (Title, ReleaseDate, PrimaryGenre, SecondaryGenre, AvgRating, ManagedBy, Description) VALUES ('The Lost City', 				'25/03/2022',  1,	   2,	4.2, 'jswift', 	'Reclusive author Loretta Sage writes about exotic places in her popular adventure novels that feature a handsome cover model named Alan. While on tour promoting her new book with Alan, Loretta gets kidnapped by an eccentric billionaire who hopes she can lead him to an ancient city''s lost treasure from her latest story. Determined to prove he can be a hero in real life and not just on the pages of her books, Alan sets off to rescue her.');
INSERT INTO Movie (Title, ReleaseDate, PrimaryGenre, SecondaryGenre, AvgRating, ManagedBy, Description) VALUES ('Star Wars: The Last Jedi',		'14/12/2017',  1, 	   5,	4.8, 'mchan', 	NULL);
INSERT INTO Movie (Title, ReleaseDate, PrimaryGenre, SecondaryGenre, AvgRating, ManagedBy, Description) VALUES ('The Godfather', 				'02/11/1972',  6, 	   7,	5.0, 'ktaylor', 'Don Vito Corleone, head of a mafia family, decides to hand over his empire to his youngest son Michael. However, his decision unintentionally puts the lives of his loved ones in grave danger.');
INSERT INTO Movie (Title, ReleaseDate, PrimaryGenre, SecondaryGenre, AvgRating, ManagedBy, Description) VALUES ('The Dark Knight', 				'28/04/2016',  1,	   8,	4.9, 'jdavis', 	'After Gordon, Dent and Batman begin an assault on Gotham''s organised crime, the mobs hire the Joker, a psychopathic criminal mastermind who offers to kill Batman and bring the city to its knees.');
INSERT INTO Movie (Title, ReleaseDate, PrimaryGenre, SecondaryGenre, AvgRating, ManagedBy, Description) VALUES ('Avengers: Infinity War', 		'27/04/2018',  1,	   9,	4.7, 'ktaylor', NULL);
INSERT INTO Movie (Title, ReleaseDate, PrimaryGenre, SecondaryGenre, AvgRating, ManagedBy, Description) VALUES ('Terminator 2 Judgement Day',	'05/09/1991', 12,     18,	3.9, 'jkeller', 'A terminator is sent on a mission to kill Sarah''s son, John Connor. However, another cyborg, who was once after Sarah''s life, has now been assigned to protect him.');

COMMIT;