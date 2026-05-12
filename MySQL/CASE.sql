select * from country;
SELECT Name, LifeExpectancy,
CASE
    WHEN LifeExpectancy <50 THEN "Underdeveloped"
    WHEN LifeExpectancy >=70 THEN "Developed"
    ELSE "Developing"
END  Category
FROM country;

select avg(LifeExpectancy) from country where Region like 'A%';

create table demo
(
amt int
);

insert into demo values(100),(200),(50),(null);
select amt,coalesce(amt,0) from demo;
select avg(amt),avg(coalesce(amt,0)) from demo;

