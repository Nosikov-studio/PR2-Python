BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "verbs" (
	"verb_id"	INTEGER,
	"verb_en"	TEXT,
	"verb_ru"	TEXT,
	PRIMARY KEY("verb_id")
);
INSERT INTO "verbs" VALUES (1,'accept','принимать, соглашаться');
INSERT INTO "verbs" VALUES (2,'achieve','достигать, добиваться');
INSERT INTO "verbs" VALUES (3,'add','добавлять, сложить');
INSERT INTO "verbs" VALUES (4,'admit','признавать, допускать, впускать');
INSERT INTO "verbs" VALUES (5,'advertise','рекламировать');
COMMIT;
