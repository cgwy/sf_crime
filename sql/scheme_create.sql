use sf;
drop table if exists `train`;
create table `train` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`Dates` varchar(25),
	`Category` varchar(100),
	`Descript` varchar(100),
	`DayOfWeek` varchar(15),
	`PdDistrict` varchar(30),
	`Resolution` varchar(100),
	`Address` varchar(100),
	`X` varchar(20),
	`Y` varchar(20),
	PRIMARY KEY (`id`)
);
 alter table train add Neighborhood varchar(20);
