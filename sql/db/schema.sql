CREATE TABLE IF NOT EXISTS "schema_migrations" (version varchar(128) primary key);
CREATE TABLE datums (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  data VARCHAR(255)
);
-- Dbmate schema migrations
INSERT INTO "schema_migrations" (version) VALUES
  ('20231126180137');
