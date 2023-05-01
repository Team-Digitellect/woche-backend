CREATE DATABASE woche5;

\c woche5;

CREATE TABLE "user" (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    username VARCHAR(80) UNIQUE NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password VARCHAR(500) NOT NULL
);

CREATE TABLE "table" (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(80) NOT NULL,
    user_id UUID NOT NULL REFERENCES "user" (id),
    UNIQUE (name, user_id)
);

CREATE TABLE item (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(80) NOT NULL,
    type VARCHAR(80) NOT NULL,
    table_id UUID NOT NULL REFERENCES "table" (id),
    UNIQUE (name, table_id)
);

CREATE TABLE data (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    value VARCHAR(80) NOT NULL,
    item_id UUID NOT NULL REFERENCES item (id)
);
