# HIVE COMMANDS

load data local inpath 'h1b_data.csv' into table big_data.h1b_data_new;

#Query 1:Which worksite has popular job title?
select worksite, job_title, count(job_title) from h1b_data_new
group by worksite, job_title
Order by job_title desc;
limit 50;

#Query 2: Is number of petitions with Data Engineer job title increasing over time?
select year, count(year) from big_data.h1b_data_new
where job_title like '%DATA ENGINEER%'
Group by year;

#Query 3: Which part of US has most data engineer jobs?
select worksite, count(worksite) from h1b_data_new
where job_title like '%DATA ENGINEER%
Group by worksite
Order by worksite
limit 20;

#Query 4: Which industry has greatest number of Data scientist position?
select soc_name, Count(soc_name) from h1b_data_new
where job_title like '%DATA SCIENTIST%'
Group by soc_name
Order by soc_name
limit 20;


#query 5: Which employer files the most petitions each year?
select employer_name, year, count(year) from h1b_data_new
group by year employer_name
order by year
limit 20;

#Query 6: What is the general trend of the employer’s H1b status in the period 2011-16?
select year, count(year) from h1b_data_new
where case_status = 'CERTIFIED'
group by year
Order by year desc;

#Query 7: What is general trend of the employer name with respect to the year?
select year, employer_name, count(employer_name) from h1b_data_new
group by employer_name, year
order by employer_name
limit 20;
