# Module 5.2 - Working with Data in Files

#### JSON exercise
Using data in file 'data/world_bank_projects.json'

- Find the 10 countries with most projects
- Find the top 10 major project themes (using column 'mjtheme_namecode')
- In 2. above you will notice that some entries have only the code and the name is missing. Create a dataframe with the missing names filled in.

#### Solution Approach
###### Q1. Find the 10 countries with most projects
  - Load JSON file into pandas dataframe
  - Find out column(s) for country names
  - Each dataframe row represents a project
  - Group by countryname and get the number of projects for each country by counting the number of rows
###### Ans1. Top 10 Countries
    People's Republic of China         19
    Republic of Indonesia              19
    Socialist Republic of Vietnam      17
    Republic of India                  16
    Republic of Yemen                  13
    Nepal                              12
    People's Republic of Bangladesh    12
    Kingdom of Morocco                 12
    Africa                             11
    Republic of Mozambique             11

###### Q2. Find the top 10 major project themes
  - Load JSON file into JSON object
  - Each project can belong to one or more project theme as can be seen from the mjtheme_namecode column
  - Flatten mjtheme_namecode column into code and name
  - Some names are empty
  - Deduce empty names from other rows with equal code
  - Group by names and count the number of projects for each name (project theme) by counting the number of rows
  
###### Ans2. Top 10 Project Themes  
    Environment and natural resources management    250
    Rural development                               216
    Human development                               210
    Public sector governance                        199
    Social protection and risk management           168
    Financial and private sector development        146
    Social dev/gender/inclusion                     130
    Trade and integration                           77
    Urban development                               50
    Economic management                             38
###### Q3. Fill up missing names
  - Already done above

