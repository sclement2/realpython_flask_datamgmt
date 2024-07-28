-- SQLite
SELECT 
    book.title
FROM author, book
JOIN book ON book.author_id = author.author_id