
create table crop_db (
crop_db_id int primary key not null,
crop_name varchar(50),
market_value Float,
yieldd Float,
daysToHarvest int,
stages int [],
crop_water_needs float[],
total_water_required float );

create table crop (
crop_id int primary key not null ,
crop_db_id int not null references crop_db(crop_db_id),
area float,
sowing_day int,
consumption float[]     -- updates every day
);

create table harvest(   -- updates every day
crop_id int primary key not null references crop(crop_id),
growth float , 
biomass float
)

create table water_source(     -- updates every day
tick int not null primary key,     
stock float,						
water_released float
);

create table supply(           -- updates every day
tick int not null primary key,
water_available float,
demand float 
);
create table supply_details(     -- updates every day
tick int not null references supply(tick) ,
crop_id int not null references crop(crop_id),
crop_db_id int not null references crop_db(crop_db_id) ,
demand float,
supply float ,
CONSTRAINT pk_DeSuId PRIMARY KEY (tick,crop_id)
)

create table crop_mix (
crop_id integer primary key not null references crop_db(crop_db_id),
percentage float not null
)
