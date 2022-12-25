# Portfolio-Website

docker run -p 3307:3306 --name my-mysql -e MYSQL_ROOT_PASSWORD=root -d mysql/mysql-server:5.7
exec -it my-mysql /bin/bash
mysql -uroot -p -A
update mysql.user set host='%' where user='root';
flush privileges;

create table IF NOT EXISTS FOOD_CATEGORY(
CATEGORY_ID int not null auto_increment, 
CATEGORY_NAME char(40) NOT NULL, 
IMAGE_FILE_NAME char(45) NOT NULL,
primary key (CATEGORY_ID)
);
SHOW DATABASES;
CREATE DATABASE RESTAURANT;
USE RESTAURANT;
SELECT * from FOOD_CATEGORY;
INSERT INTO FOOD_CATEGORY (CATEGORY_NAME,IMAGE_FILE_NAME)
VALUES ('Specialty Pizza','speciality.png');
INSERT INTO FOOD_CATEGORY (CATEGORY_NAME,IMAGE_FILE_NAME)
VALUES ('Breads & Oven-Baked Dips','breadandovenbakeddips.png');
INSERT INTO FOOD_CATEGORY (CATEGORY_NAME,IMAGE_FILE_NAME)
VALUES ('Chikcen','Speciality.png');
INSERT INTO FOOD_CATEGORY (CATEGORY_NAME,IMAGE_FILE_NAME)
VALUES ('Desserts','desserts.png');
INSERT INTO FOOD_CATEGORY (CATEGORY_NAME,IMAGE_FILE_NAME)
VALUES ('Pasta','pasta.png');
INSERT INTO FOOD_CATEGORY (CATEGORY_NAME,IMAGE_FILE_NAME)
VALUES ('Oven Baked Sandwiches','sandwiches.png');
INSERT INTO FOOD_CATEGORY (CATEGORY_NAME,IMAGE_FILE_NAME)
VALUES ('Salads','salads.png');
INSERT INTO FOOD_CATEGORY (CATEGORY_NAME,IMAGE_FILE_NAME)
VALUES ('Drinks','drinks.png');
INSERT INTO FOOD_CATEGORY (CATEGORY_NAME,IMAGE_FILE_NAME)
VALUES ('Extras','extras.png');
COMMIT;
