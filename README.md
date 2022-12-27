# Portfolio-Website  

## Setup

### Run MySQL in a docker container
```
docker run -p 3307:3306 --name my-mysql -e MYSQL_ROOT_PASSWORD=root -d mysql/mysql-server:5.7   
```

### Resolve connection issue
After running the commands below you can connect to the MySql docker container using port 3307

```
exec -it my-mysql /bin/bash  
mysql -uroot -p -A  
update mysql.user set host='%' where user='root';  
flush privileges;  
```

### Create database and insert static data
Open MySQL Workbench and connect to newly created mysql server.  Run ddl.sql to create the database and then the tables.  Then category.sql to add data

### Before running the python code
Before running the python code create a virtual environment and install the requirements.txt using pip install -r requirements.txt.

