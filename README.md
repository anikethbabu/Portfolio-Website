# Portfolio-Website  

### After running the commands below you can connect to the MySql docker container using port 3307.  

docker run -p 3307:3306 --name my-mysql -e MYSQL_ROOT_PASSWORD=root -d mysql/mysql-server:5.7   
exec -it my-mysql /bin/bash  
mysql -uroot -p -A  
update mysql.user set host='%' where user='root';  
flush privileges;  

### In my Sql scripts run ddl.sql then category.sql to create database and add data


