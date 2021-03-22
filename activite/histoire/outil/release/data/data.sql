CREATE TABLE facts(
  "subject" TEXT,
  "link" TEXT,
  "goal" TEXT
);
CREATE TABLE rules(
"id" INTEGER NOT NULL PRIMARY KEY,
"premises" TEXT,
"conclusion" TEXT
);
