CREATE TABLE examples(
  LastName VARCHAR(50) NOT NULL,
  FirstName VARCHAR(50) NOT NULL
);
PRAGMA table_info('examples');

ALTER TABLE 
  examples
ADD COLUMN
  Country VARCHAR(100) NOT NULL;

ALTER TABLE
  examples
ADD COLUMN
  Age INTEGER NOT NULL;

ALTER TABLE
  examples
ADD COLUMN
  PostCode VARCHAR(100) NOT NULL;

ALTER TABLE
  examples
RENAME COLUMN
  PostCode TO Address;

ALTER TABLE
  examples
DROP COLUMN
  Address;

ALTER TABLE
  examples
RENAME TO
  new_examples;

ALTER TABLE
  new_examples
RENAME To examples;

DROP TABLE examples;

DROP TABLE examples;