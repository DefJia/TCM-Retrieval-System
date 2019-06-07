-- drop tables
drop table if exists symptom;
drop table if exists illness;
drop table if exists anagraph;
drop table if exists medicine;
drop table if exists illness_anagraph;
drop table if exists symptom_illness;
drop table if exists anagraph_medicine;

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
  name varchar(10) not null unique,
  property varchar(5) check(property in ('先煎', '后下'))
);

-- Relations
create table symptom_illness(
  illness_id integer,
  symptom_id integer,
  foreign key (illness_id) references illness(id),
  foreign key (symptom_id) references symptom(id)
);
create table illness_anagraph(
  illness_id integer,
  anagraph_id integer,
  foreign key (illness_id) references illness(id),
  foreign key (anagraph_id) references anagraph(id)
);
create table anagraph_medicine(
  anagraph_id integer,
  medicine_id integer,
  grams integer,
  foreign key (anagraph_id) references anagraph(id),
  foreign key (medicine_id) references medicine(id)
);

-- init data
insert into symptom('name') values ('头疼');
insert into symptom('name') values ('头痛');
insert into symptom('name') values ('发热');
insert into symptom('name') values ('脚痛');
insert into symptom('name') values ('口苦');
insert into symptom('name') values ('咽干');

insert into illness('name') values ('少阳症');

insert into anagraph('name') values ('小柴胡汤');

insert into medicine('name') values ('枸杞');
insert into medicine('name') values ('当归');

insert into symptom_illness (symptom_id, illness_id) values (1, 1);
insert into symptom_illness (symptom_id, illness_id) VALUES (2, 1);
insert into illness_anagraph (illness_id, anagraph_id) VALUES (1, 1);
insert into anagraph_medicine (anagraph_id, medicine_id, grams) VALUES (1, 2, 5);
insert into anagraph_medicine (anagraph_id, medicine_id, grams) VALUES (1, 1, 10);
