-- Select category title and total amount of products in each in descending order
SELECT category_title, COUNT(*) FROM categories JOIN products USING (category_id)
GROUP BY category_title
ORDER BY COUNT DESC;