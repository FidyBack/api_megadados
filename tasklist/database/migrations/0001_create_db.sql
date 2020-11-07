DROP TABLE IF EXISTS tasks;
CREATE TABLE tasks (
    uuid BINARY(16) PRIMARY KEY,
    uuiduser BINARY(16),
    description NVARCHAR(1024),
    completed BOOLEAN
);