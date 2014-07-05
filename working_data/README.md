## Working Data

The working_data directory is the home for "projects" that involve the
massaging, cleanup, or improvement of source datasets.

__NO SOURCE FILES SHOULD EVER BE ADDED HERE. ADD THEM FIRST TO THE 
source_data DIRECTORY, ALWAYS.__

We will need proper procedures in place to account for multiple people
collaborating on cleaning up or constructing data in any particular working 
dataset. This is why there is always a separation between original source 
data and working data, just in case something goes terribly wrong and we 
need to start over. Additionally, it may be useful to be able to create 
scripts or run other types of comparison between the source data file and 
the working data file.

Directories and files in the working_data directory should always be
considered "temporary". __*Don't assume that your work is going to be safe
if you ever try to merge your branch with another one!!*__

===

### How To Create A Working Data Project

The first thing you should do is come up with a descriptive directory name 
for your working data project. Any name will do as long as it doesn't exist 
already in the working_data directory.

Next create a README file in your new directory and include a brief 
description of what you're trying to accomplish in your working data project 
so that others will know what they can do to help you out.

Copy all the source_data files you need into your working_data working data
project directory, and you can then modify them however you see fit, including 
choosing appropriate final names for the files for when they become clean 
data files.

Then have at it!

__NOTE: Please try to standardize all file contents into UTF-8 wherever 
possible. This may mean having to open the file in several editors and 
saving it a few different ways.__

===

### PostgreSQL Cheat Sheet

After you start PostgreSQL from the command line, usually with the "psql" 
command, you'll need to enter "slash commands" at the postgres prompt.
Here is a quick list of commands you'll use all the time.

__List databases__
postgres=# \l

__Create database__
postgres=# CREATE DATABASE demodb1 WITH OWNER demorole1 ENCODING 'UTF8';

__Grant privileges to new user__
postgres=# GRANT ALL PRIVILEGES ON DATABASE demodb1 TO demorole1;

__Load data into database__
postgres=# pg_dump <databasename> > <outfile> 

__Connect to database__
postgres=# \c <databasename>

__List tables in connected database__
postgres=# \dt

__List columns on table__
postgres=# \d <tablename>

__Backup database__
postgres=# pg_dump <databasename> > <outfile> 

__Drop database__
postgres=# DROP DATABASE demodb1;

===

### Standardizing Data Into Its Final Form

> __*"This isn't even my final form!" --Frieza, Dragonball Z*__

===

We know that procedures like this may seem like a bit of "overkill" but trust 
us... doing things the right way from the beginning will save a lot of 
headaches down the road. Data projects like this need to have strict 
standards in order to make working with large collections of diverse files 
easier. And when we want to manipulate many files at once with scripts, it 
will be a lot easier to do so when all working data projects follow a standard 
procedure.

Thank you for taking an interest in the work ahead - together we can make
a difference, preventing sickness and saving lives!
  
sincerely,

The FIDDLE Team
