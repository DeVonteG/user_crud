CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(45),
    last_name VARCHAR(45),
    hobbies TEXT,
    active BOOLEAN DEFAULT 1
);

--INSERT Test Records:

INSERT INTO user(
    first_name,
    last_name,
    hobbies
) Values (
    "DeVonte",
    "Gray",
    "Playing Video Games"
);    

INSERT INTO user(
    first_name,
    last_name,
    hobbies
) Values (
    "Jane",
    "Doe",
    "Playing Tennis"
); 

INSERT INTO user(
    first_name,
    last_name,
    hobbies
) Values (
    "John",
    "Doe",
    "Playing Golf"
); 