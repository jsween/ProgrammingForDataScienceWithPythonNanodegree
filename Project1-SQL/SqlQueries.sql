/* Question 1
----------
We want to understand more about the movies that families are watching. 
The following categories are considered family movies: Animation, Children, Classics, Comedy, Family and Music.
Create a query that lists each movie, the film category it is classified in, and the number of times it has been rented out. */

/* QUERY 1 - query used to get count of rentals by film in each family friendly category */
WITH T1
AS (SELECT f.title title,
           c.name category
    FROM category c
        JOIN film_category fc
            ON c.category_id = fc.category_id
        JOIN film f
            ON fc.film_id = f.film_id
        JOIN inventory i
            ON f.film_id = i.film_id
        JOIN rental r
            ON i.inventory_id = r.inventory_id
    WHERE c.name IN ( 'Animation', 'Children', 'Classics', 'Comedy', 'Family', 'Music' )
   )
SELECT category,
       COUNT(*) total_rented
FROM t1
GROUP BY 1
ORDER BY 1;               


/* Question 2
----------
Now we need to know how the length of rental duration of these family-friendly movies compares to the duration that all movies are rented for.
Can you provide a table with the movie titles and divide them into 4 levels (first_quarter, second_quarter, third_quarter, and final_quarter) 
based on the quartiles (25%, 50%, 75%) of the average rental duration(in the number of days) for movies across all categories? */

/*Query 2 - query used to get the average length of rental duration for these family-friendly movies */
WITH T2
AS (SELECT *,
           NTILE(4) OVER (ORDER BY t1.rental_duration) as standard_quartile
    FROM
    (
        SELECT f.title,
               c.name,
               f.rental_duration
        FROM category c
            JOIN film_category fc
                ON c.category_id = fc.category_id
            JOIN film f
                ON fc.film_id = f.film_id
    ) T1
   )
SELECT name,
       AVG(rental_duration) rental_duration,
       CASE
           WHEN standard_quartile = '1' THEN
               'first quarter'
           WHEN standard_quartile = '2' THEN
               'second quarter'
           WHEN standard_quartile = '3' THEN
               'third quarter'
           ELSE
               'final quarter'
       END AS level,
       CASE
           WHEN name IN ( 'Animation', 'Children', 'Classics', 'Comedy', 'Family', 'Music' ) THEN
               'family friendly'
           ELSE
               'non-family friendly'
       END AS family_friendly
FROM t2
GROUP BY 1,
         3,
         4
ORDER BY 4,
         1,
         3;


/* Question 3
---------
Finally, provide a table with the family-friendly film category, each of the quartiles, and the corresponding count of movies within 
each combination of film category for each corresponding rental duration category. */

/* Query 3 - query used to get count of movies within each family friendly category */
WITH T1
AS (SELECT c.name,
           f.rental_duration,
           NTILE(4) OVER (ORDER BY f.rental_duration) standard_quartile
    FROM category c
        JOIN film_category fc
            ON c.category_id = fc.category_id
        JOIN film f
            ON fc.film_id = f.film_id
    WHERE c.name IN ( 'Animation', 'Children', 'Classics', 'Comedy', 'Family', 'Music' )
   )
SELECT name,
       standard_quartile,
       COUNT(standard_quartile)
FROM T1
GROUP BY 1,
         2
ORDER BY 1,
         2;

/* Question 4
----------
We want to find out how the two stores compare in their count of rental orders during every month for all the years we have data for. 
Write a query that returns the store ID for the store, the year and month and the number of rental orders each store has fulfilled for 
that month. Your table should include a column for each of the following: year, month, store ID and count of rental orders fulfilled during that month. */

/* Query used to find how the two stores compare in their count of rental order by month/year */

SELECT DATE_PART('month', r.rental_date) Rental_month,
       DATE_PART('year', r.rental_date) Rental_year,
       s.store_id Store_ID,
       COUNT(*) Count_rentals
FROM rental r
    JOIN staff s
        ON r.staff_id = s.staff_id
GROUP BY 1,
         2,
         3
ORDER BY 2,
         1,
         3;