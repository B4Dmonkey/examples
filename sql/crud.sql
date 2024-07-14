-- create
INSERT INTO datums (data) VALUES (?);

-- read
SELECT * FROM datums;

-- update
UPDATE datums WHERE id=?;

-- delete
DELETE FROM datums WHERE id=?;