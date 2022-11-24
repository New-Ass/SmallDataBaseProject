"""
create database classDesign;
use classDesign;

# 用户表
create table user (
	id int primary key auto_increment,
	username varchar(16) unique,
	password varchar(16)
);

# 插入用户数据
INSERT INTO USER (username, password)
VALUES
	("admin", "12345"),
	("mcx", "qwe"),
	("lj", "asd"),
	("hn", "zxc");

# 日志
create table log (
	username varchar(16),
	action enum("login", "query", "delete", "add") not null,
	msg varchar(16),
	time timestamp not null default CURRENT_TIMESTAMP
);

# 部门表（和职员表一对多关系）
create table dep (
	id int primary key auto_increment,
	name varchar(16) not null,
	des varchar(32)
);

# 插入数据
INSERT INTO `dep` (`name`, `des`) VALUES ('运营', '好销售，不责任手段');
INSERT INTO `dep` (`name`, `des`) VALUES ('销售', '什么都可以销售');
INSERT INTO `dep` (`name`, `des`) VALUES ('教育', '教书育人');

# 职员详细信息
create table emp_detail (
	id int primary key auto_increment,
	addr varchar(16),
	email varchar(16),
	time timestamp not null default CURRENT_TIMESTAMP
);

# 插入数据（其实 id 和 time 会自动填入不用插入）
INSERT INTO `classdesign`.`emp_detail` (`id`, `addr`, `email`, `time`) VALUES ('1', '东方', '123@qq.com', '2022-07-03 15:41:32');
INSERT INTO `classdesign`.`emp_detail` (`id`, `addr`, `email`, `time`) VALUES ('2', '北方', '456@qq.com', '2022-07-03 15:42:19');
INSERT INTO `classdesign`.`emp_detail` (`id`, `addr`, `email`, `time`) VALUES ('3', '西方', 'qwwer@qq.com', '2022-07-03 15:42:44');
INSERT INTO `classdesign`.`emp_detail` (`id`, `addr`, `email`, `time`) VALUES ('4', '南方', 'asd@qq.com', '2022-07-03 15:43:23');


# 职员表
create table emp (
 id int primary key auto_increment,
 name varchar(16) not null,
 dep_id int not null,
 detail_id int not null,
 foreign key(dep_id) references dep(id),
 foreign key(detail_id) references emp_detail(id)
);

# 插入数据
INSERT INTO `emp` (`name`, `dep_id`, `detail_id`) VALUES ('奥特曼', '1', '2');
INSERT INTO `emp` (`name`, `dep_id`, `detail_id`) VALUES ('迪迦', '1', '3');
INSERT INTO `emp` (`name`, `dep_id`, `detail_id`) VALUES ('戴拿', '2', '4');
INSERT INTO `emp` (`name`, `dep_id`, `detail_id`) VALUES ('盖亚', '3', '1');

# 项目表（和职员表，多对多关系，即一个项目可以有多个职员负责，一个职员可以负责多个项目）
create table project(
	id int primary key auto_increment,
	name varchar(16)
);

# 插入数据
INSERT INTO `project` (`name`) VALUES ('数据库');
INSERT INTO `project` (`name`) VALUES ('网络通信');

# 多对多关系的第三方表
create table emp2pro(
	id int primary key auto_increment,
	emp_id int,
	pro_id int,
	foreign key(emp_id) references emp(id)
    on update cascade
    on delete cascade,
	foreign key(pro_id) references project(id)
    on update cascade
    on delete cascade
);

# 插入数据
INSERT INTO `emp2pro` (`emp_id`, `pro_id`) VALUES ('1', '1');
INSERT INTO `emp2pro` (`emp_id`, `pro_id`) VALUES ('1', '2');
INSERT INTO `emp2pro` (`emp_id`, `pro_id`) VALUES ('3', '2');
"""