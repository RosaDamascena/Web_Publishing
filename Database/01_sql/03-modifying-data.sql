DROP TABLE articles;

CREATE TABLE articles(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(100) NOT NULL,
  content VARCHAR(200) NOT NULL,
  createdAt DATE NOT NULL
);
SELECT * FROM articles;

INSERT INTO articles
  (title, content, createdAt)
VALUES
  ('제목', '내용', '2000-01-11');

SELECT rowid, * FROM articles;

INSERT INTO articles
  (title, content, createdAt)
VALUES
  ('제목2', '내용2', '2000-01-12'),
  ('제목3', '내용3', '2000-01-13'),
  ('제목4', '내용4', '2000-01-14');

SELECT rowid, * FROM articles;

INSERT INTO articles
  (title, content, createdAt)
VALUES
  ('제목5', '내용5', '2000-01-15');

SELECT rowid, * FROM articles;

DELETE FROM articles
WHERE rowid=5;

SELECT * FROM articles;

-- 1번 게시글의 제목을 '수정된 제목'
-- UPDATE
UPDATE articles
SET title = '수정된 내용'
WHERE id = 1;

UPDATE articles
SET 
  title = '2번으로',
  content = '수정'
WHERE id = 2;

DELETE FROM articles
WHERE id IN (
  SELECT id
  FROM articles
  ORDER BY createdAt LIMIT 2
);

