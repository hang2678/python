#DROP TABLE weather;
CREATE TABLE weather (
	idx integer primary key auto_increment,
    location varchar(15),
    fc_date timestamp,
    description varchar(50),
    temp_min int,
    temp_max int,
    reg_date timestamp default NOW()
) charset=utf8;