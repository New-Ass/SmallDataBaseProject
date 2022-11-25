# SmallDataBaseProject
基于学校课程创建的数据库小项目,上传至 Github 以作纪念。
Create a small database project based on the school curriculum and upload it to Github as a souvenir

## 项目简单介绍
如果是中文用户，可以直接查看该项目下的 **数据库课设.md** 文件内容，了解代码详情以及代码演示。或者选择查看[我的博客](https://new-ass.github.io/2022/11/24/mysql-shu-ju-ku-xue-xi-9-shu-ju-ku-ke-she-qi-ye-ren-shi-xi-tong/)

## 项目运行
请确保所有的 **.py** 文件在同一个文件夹下，运行时只需要运行 **main.py** 文件
在运行文件前请确保代码中 **connect_database(self) 函数** 各项参数都已经根据您本地电脑配置修改完成， 该项目中大约有 7~8 个 **connect_database(self) 函数** 

## (The following is a machine translation)
## Brief introduction
This project is based on the school database course curriculum design requirements to write a single enterprise personnel system.
The project uses the PyQt5 module to build the UI interface, and the data is stored in the MySQL database.

## The functionality that the project can achieve
1. User registration
2. User Login
    -- The functions available to admin and ordinary users are different
    -- Make sure that admin has an id of 1 in the database table you are using
    -- The functions enjoyed by admin include: querying information, adding information, deleting information, and querying logs
    -- Ordinary users enjoy functions including: querying information, adding information, and deleting information
3. Information query
4. Information added
5. Log queries
    -- Record the user of the operation and add the deletion query. If the operator is None, then None is the first user with a name above it.
6. The original MySQL data insertion is in the **数据库相关代码.py**

## Project code running
Make sure that all .py files are in the same folder, and only main.py files need to be run when running

Before running the file, please make sure that the parameters of the **connect_database(self) function** in the code have been modified according to the configuration of your local computer, there are about 7~8 **connect_database(self) functions** in the project
