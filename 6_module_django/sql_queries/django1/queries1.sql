SELECT * FROM posts;
SELECT * FROM blog_comment;
SELECT * FROM blog_category;
SELECT * FROM blog_post_categories;


SELECT * FROM auth_user;


SELECT 
	title,
    MAX(created_at) AS last_post_datetime,
	COUNT("posts"."id") AS "cnt"
FROM posts
GROUP BY title

