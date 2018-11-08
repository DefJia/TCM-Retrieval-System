-- drop tables
drop table symptom;
drop table illness;
drop table anagraph;
drop table medicine;
drop table illness_anagraph;
drop table illness_symptom;
drop table anagraph_medicine;

-- create basic tables
create table symptom(
  id integer primary key AUTOINCREMENT,
  name varchar(10) not null unique
);
create table illness(
  id integer primary key AUTOINCREMENT,
  name varchar(10) not null unique
);
create table anagraph(
  id integer primary key AUTOINCREMENT,
  name varchar(10) not null unique
);
create table medicine(
  id integer primary key AUTOINCREMENT,
  name varchar(10) not null unique
);

-- Relations
create table illness_symptom(
  illness varchar,
  symptom varchar,
  foreign key (illness) references illness(id),
  foreign key (symptom) references symptom(id)
);
create table illness_anagraph(
  illness varchar,
  anagraph varchar,
  foreign key (illness) references illness(id),
  foreign key (anagraph) references anagraph(id)
);
create table anagraph_medicine(
  anagraph varchar,
  medicine varchar,
  foreign key (anagraph) references anagraph(id),
  foreign key (medicine) references medicine(id)
);

-- init data
insert into symptom('name') values ('头疼');
insert into symptom('name') values ('脚痛');

insert into illness('name') values ('少阳症');

insert into anagraph('name') values ('小柴胡汤');

insert into medicine('name') values ('枸杞');
insert into medicine('name') values ('当归');

insert into illness_symptom (illness, symptom) values (1, 1);
insert into illness_symptom (illness, symptom) VALUES (1, 2);
insert into illness_anagraph (illness, anagraph) VALUES (1, 1);
insert into anagraph_medicine (anagraph, medicine) VALUES (1, 2);
insert into anagraph_medicine (anagraph, medicine) VALUES (1, 1);
