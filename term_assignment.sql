use pyqt5

create table project(
	PNO char(20) primary key,
	Pname char(30) not null,
	introduction char(100),
	release_time date not null,
	is_public int not null		--1/0
)

drop table project
insert into project values
('HoKv0.0', '王者荣耀', '我是第一个版本，内测版', '2022-4-15', 0), 
('HoKv1.0', '王者荣耀', '嫦娥和猪八戒新增了情侣特效', '2022-4-16', 0),
('HoKv2.0', '王者荣耀', '峡谷地图修复了小兵所在区域无视野的bug，正式上线', '2022-4-17', 1), 
('HoKv3.0', '王者荣耀', '新特性：孙策大招期间在船上的人可以普攻', '2022-4-17', 1),
('Taobaov0.0', '淘宝', '我是第一个版本，内测版', '2022-4-16', 0),
('Taobaov1.0', '淘宝', '修复ios闪退，正式上线', '2022-4-17', 1),
('Taobaov2.0', '淘宝', '主页组件增添页面自适应功能', '2022-4-18', 1)

create table users(
	UNO char(10) primary key,
	phone_number char(11),
	career char(10)
)
insert into users values
('Jane', '18029906263', '测试人员'), ('May', '17789767232', '测试人员'),
('md', '15276481521', '开发者'), ('kiwi', '13265362084', '开发者')

drop table issues
create table issues(
	INO varchar(50) not null,
	UNO char(10) not null,
	priority int default 1,
	content char(50) not null,
	is_solve int default 0,
	primary key(INO, UNO)
)
insert into issues (INO, UNO, content) values
('2022-04-17 04:30:55', 'May', '部分峡谷地图小兵所在区域无视野'),
('2022-04-16 07:32:55', 'May', 'ios闪退'),
('2022-04-17 02:30:55', 'Jane', '主页按钮被轮播图遮掩'),
('2022-04-18 16:47:21', 'kiwi', 'test'),
('2022-04-18 19:27:14', 'kiwi', 'test')


drop table PR
create table PR(
	PR_time varchar(50) not null,
	UNO char(8) not null,
	is_merge int default 0,
	code char(50),
	primary key(PR_time, UNO)
)

insert into PR (PR_time, UNO, code) values
('2022-04-16 02:30:55', 'md', 'C:\code01.cpp'),
('2022-04-16 21:32:13', 'kiwi', 'C:\code02.cpp'),
('2022-04-13 12:10:51', 'Jane', 'C:\code03.cpp')

select * from users
select * from issues order by priority
select * from PR

select PR_time, PR.UNO, users.career, is_merge, code from PR, users where PR.UNO = users.UNO
select INO, issues.UNO, users.career, is_solve, priority, content from issues, users where issues.UNO = users.UNO

UPDATE PR SET is_merge = 0, code = '测试重新生成' WHERE PR_time = '2022-07-02 23:24:32' and UNO = 'kiwi'
UPDATE issues SET is_solve = 0, content = '测试重新统计' WHERE INO = '2022-04-17 17:30:55' and UNO = 'kiwi'

select PR_time, PR.UNO, users.career, is_merge, code from PR, users where PR.UNO = users.UNO and PR_time = '2022-04-16 21:32:13' and users.UNO = 'kiwi'

select PR_time, PR.UNO, users.career, is_merge, code from PR, users where PR.UNO = users.UNO