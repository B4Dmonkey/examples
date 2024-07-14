-- migrate:up
CREATE TABLE datums (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  data VARCHAR(255)
);

-- migrate:down
DROP TABLE datums;
