-- To run the file and interact with the file in terminl: python3 sqlite_shell.py --init file_name.sql


-- discussion_12
CREATE TABLE original AS
    SELECT 1 AS n, "It's" AS word UNION
    SELECT 2 , "The" UNION
    SELECT 3 , "End";

CREATE TABLE code AS
    SELECT "Up" AS x, "Down" AS y UNION
    SELECT "Now" , "Home" UNION
    SELECT "It's" , "What" UNION
    SELECT "See" , "Do" UNION
    SELECT "Can" , "See" UNION
    SELECT "End" , "Now" UNION
    SELECT "What" , "You" UNION
    SELECT "The" , "Happens" UNION
    SELECT "Love" , "Scheme" UNION
    SELECT "Not" , "Mess" UNION
    SELECT "Happens", "Go";

-- decode the message "It's The End" using the code table
CREATE TABLE decode AS
    SELECT y FROM original, code WHERE word = x ORDER BY n;
-- decode the encrypted message "What happens now?" using the same code table
CREATE TABLE double_decode AS
    SELECT b.y FROM original, code AS a, code AS b WHERE word = a.x AND a.y = b.x ORDER BY n;