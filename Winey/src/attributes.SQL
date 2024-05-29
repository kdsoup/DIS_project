CREATE TABLE Wine (
    id SERIAL PRIMARY KEY,
    country VARCHAR(100) NOT NULL,
    description VARCHAR(200) default NULL,
    name VARCHAR(100) default NULL,
    points FLOAT default NULL,
    price FLOAT default NULL,
    province VARCHAR(100) default NULL,
    region_1 VARCHAR(100) default NULL,
    region_2 VARCHAR(100) default NULL,
    variety VARCHAR(100) default NULL,
    winery VARCHAR(100) default NULL
);
