-- create tables
create table if not exists mydb.sports
(
    id int auto_increment not null primary key,
    name varchar(50) not null,
    status boolean not null default true,
    recUpdatedAt timestamp not null default current_timestamp on update current_timestamp,
    createdAt timestamp not null default current_timestamp
);

create table if not exists mydb.tours
(
    id int auto_increment not null primary key,
    name varchar(50) not null,
    sportId int not null,
    status boolean not null default true,
    startTime timestamp not null,
    endTime timestamp not null,
    recUpdatedAt timestamp not null default current_timestamp on update current_timestamp,
    createdAt timestamp not null default current_timestamp,
    foreign key (sportId) references sports(id)
);

create table if not exists mydb.matches
(
    id int auto_increment not null primary key,
    name varchar(50) not null,
    tourId int not null,
    status boolean not null default true,
    format varchar(50) not null,
    startTime timestamp not null,
    endTime timestamp not null,
    recUpdatedAt timestamp not null default current_timestamp on update current_timestamp,
    createdAt timestamp not null default current_timestamp,
    foreign key (tourId) references tours(id)
);

create table if not exists mydb.news
(
    id int auto_increment not null primary key,
    title varchar(50) not null,
    description varchar(200) null,
    status boolean not null default true,
    tourId int not null,
    sportId int not null,
    matchId int not null,
    createdAt timestamp not null default current_timestamp,
    foreign key (tourId) references tours(id),
    foreign key (sportId) references sports(id),
    foreign key (matchId) references matches(id)
);
-- seed data
insert ignore into mydb.sports (id, name) values (1, 'Cricket');
insert ignore into mydb.sports (id, name) values (2, 'Football');

insert ignore into mydb.tours (id, name, sportId, startTime, endTime) values (1, 'Indian Premier League, 2023', 1, '2023-04-09 00:00:00', '2023-05-30 00:00:00');
insert ignore into mydb.tours (id, name, sportId, startTime, endTime) values (2, 'India Super League, 2023', 2, '2023-04-21 00:00:00', '2023-06-20 00:00:00');
insert ignore into mydb.tours (id, name, sportId, startTime, endTime) values (3, 'India Tour of West Indies, 2023', 1, '2023-06-10 00:00:00', '2023-06-29 00:00:00');
insert ignore into mydb.tours (id, name, sportId, startTime, endTime) values (4, 'English Premier League, 2022', 2, '2022-04-09 00:00:00', '2022-05-30 00:00:00');

insert ignore into mydb.matches (name, tourId, format, startTime, endTime) values ('GT vs RCB', 1, 'T20', '2023-04-09 18:00:00', '2023-04-09 23:00:00');
insert ignore into mydb.matches (name, tourId, format, startTime, endTime) values ('CSK vs MI', 1, 'T20', '2023-04-10 18:00:00', '2021-04-10 23:00:00');
insert ignore into mydb.matches (name, tourId, format, startTime, endTime) values ('LSG vs KXIP', 1, 'T20', '2023-04-11 18:00:00', '2023-04-11 23:00:00');
insert ignore into mydb.matches (name, tourId, format, startTime, endTime) values ('RR vs SRH', 1, 'T20', '2023-04-12 18:00:00', '2023-04-12 23:00:00');
insert ignore into mydb.matches (name, tourId, format, startTime, endTime) values ('BLR vs BEN', 2, 'soccer', '2023-04-29 18:00:00', '2023-04-29 23:00:00');
insert ignore into mydb.matches (name, tourId, format, startTime, endTime) values ('ATK vs MCFC', 2, 'soccer', '2023-04-21 18:00:00', '2023-04-21 23:00:00');
insert ignore into mydb.matches (name, tourId, format, startTime, endTime) values ('KER vs JFC', 2, 'soccer', '2023-04-22 18:00:00', '2023-04-22 23:00:00');
insert ignore into mydb.matches (name, tourId, format, startTime, endTime) values ('IND vs WI', 3, 'ODI', '2023-06-10 10:00:00', '2023-06-10 23:00:00');
insert ignore into mydb.matches (name, tourId, format, startTime, endTime) values ('IND vs WI', 3, 'ODI', '2023-06-12 10:00:00', '2023-06-12 23:00:00');
insert ignore into mydb.matches (name, tourId, format, startTime, endTime) values ('IND vs WI', 3, 'ODI', '2023-06-14 10:00:00', '2023-06-14 23:00:00');
insert ignore into mydb.matches (name, tourId, format, startTime, endTime) values ('KER vs JFC', 4, 'soccer', '2022-04-09 18:00:00', '2022-04-09 23:00:00');

insert ignore into mydb.news (title, description, sportId, matchId, tourId, createdAt) values ('Titans beat Challengers', 'Gujarat Titans clinched victory by six wickets in their final IPL 2023 league game and also knocked out Royal Challengers Bangalore, at the M Chinnaswamy Stadium in Bengaluru.', 1, 2, 1, '2023-07-16 12:26:23');
insert ignore into mydb.news (title, description, sportId, matchId, tourId, createdAt) values ('Gaikwad-Conway Partnership', 'Top knocks from Ruturaj Gaikwad and Devon Conway guided Chennai Super Kings (CSK) to a six-wicket win over Mumbai Indians (MI) in their Indian Premier League (IPL) match at Chennai on Saturday.', 1, 2, 1, '2023-07-16 12:29:00');
insert ignore into mydb.news (title, description, sportId, matchId, tourId, createdAt) values ('Punjab Kings fall short', 'Marcus Stoinis and Kyle Mayers put on a power-hitting masterclass as Lucknow Super Giants slayed Punjab Kings by 56 runs.', 1, 3, 1, '2023-07-16 12:31:50');
insert ignore into mydb.news (title, description, sportId, matchId, tourId, createdAt) values ('Samad smashes a six after no-ball', 'After Sandeep Sharma overstepped of what was supposed to be the last ball of the innings, Abdul Samad smacked a six down the ground to seal a four-wicket win.', 1, 4, 1, '2023-07-16 12:33:22');
insert ignore into mydb.news (title, description, sportId, matchId, tourId, createdAt) values ('Mumbai City seal playoff spot', 'Mumbai City beat ATK Mohun Bagan 1-0 to become the first side to confirm a playoff spot this season.', 2, 6, 2, '2023-07-16 12:35:09');
insert ignore into mydb.news (title, description, sportId, matchId, tourId, createdAt) values ('East Bengal triumph over Bengaluru','East Bengal FC played against Bengaluru FC in 2 matches this season. Currently, East Bengal FC rank 10th.',2, 5, 2, '2023-07-16 12:37:37');