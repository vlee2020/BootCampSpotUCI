DROP TABLE ratings;
DROP TABLE books;

CREATE TABLE "books" (
    "isbn" VARCHAR   NOT NULL,
    "title" VARCHAR   NOT NULL,
    "author" VARCHAR   NOT NULL,
    "publisher" VARCHAR   NOT NULL,
    "publication_date" DATE   NOT NULL,
    CONSTRAINT "pk_books" PRIMARY KEY (
        "isbn"
     )
);

CREATE TABLE "ratings" (
    "isbn" VARCHAR   NOT NULL,
    "google_rtg" INT,
    "goodreads_rtg" INT   NOT NULL,
    "nyt_ind" BOOLEAN   NOT NULL,
    "weeks" INT   
);

ALTER TABLE "ratings" ADD CONSTRAINT "fk_ratings_isbn" FOREIGN KEY("isbn")
REFERENCES "books" ("isbn");

SELECT * FROM ratings;