CREATE TABLE users(
    id integer primary key
	, name varchar(255) not null
	, email varchar(255) unique not null
	, address varchar(1000)
);

CREATE TABLE posts(
	id integer primary key
	, user_id int not null references users(id)
	, title varchar(255) not null
	, body text
);

ALTER TABLE posts
ADD constraint unique_user_id_title unique(user_id,title);

-- IN PSQL run command conninfo to get host, port etc.

truncate table posts;
truncate table users;

drop table posts;
drop table users;

-- dummy insertions into posts
-- for demonstrating scheduled job

select * from users;
select * from posts;

INSERT INTO posts
VALUES
	(1001, 1, 'python job schedular', 'This is blog demonstrates the use of apschedular (advaced python schedular)')
	, (1002, 1, 'python api', 'This is blog demonstrates the use of apis in python')

-- get total users
SELECT COUNT(id) FROM users;

-- get total posts
SELECT COUNT(id) FROM posts;
