CREATE TABLE hello (
    id SERIAL PRIMARY KEY,
    message TEXT NOT NULL
);

INSERT INTO hello (message)
VALUES ('Hello from PostgreSQL!');
