## Source Data

The source_data directory is meant to be an archive for all food safety and 
foodborne illness data that we collect. NO DATA SHOULD BE ALTERED IN THIS
DIRECTORY, EVER. Data files can and should be added to this directory, but
naming conventions for files must be maintained at all times so that each
filename is unique.

When you want to work with one of these data sets, you must make a new
directory under the working_data directory and copy files from source_data
into that new directory. Treat these source_data files in this directory as 
"forensic evidence" that should never be tampered with.

See the README file in the working_data directory to learn more about how
to work with files and create datasets in that part of the repository.

===

### About Naming Conventions

Unique and highly descriptive file names are are crucial to success in a
project like this. For this reason, we are writing a very specific naming
convention standard here that must be followed with all source data files.
Each file name will consist of multiple elements, separated by underscores,
and the procedure for building a file name will be further described below.

First, we will take a cue from Ruby on Rails migrations. When a migration is 
made, the file name takes the form "YYYYMMDDHHMMSS_create_products.rb", as 
one example. So we will use a timestamp coding element to begin the name of 
each file.

Next, the source data file should have the directory structure it belongs in
as part of its name. This means that a file that originated from New York
state should start with something like:

`20140704230703_state_ny_`

This is so that if, for whatever reason, a file gets "misplaced", we will be
able to see right away that it's in the wrong directory just by looking at 
this directory element. Note that underscores are being used between the 
timestamp and directory elements and between subdirectories in the directory
element.

For the next step, you should choose a descriptive name or phrase to 
indicate what the file contains, and it should be easy to see and understand 
at a glance. For example:

`20140704230703_state_ny_2011_DOH_restaurant_violations`

In general, if a date or time range is relevant to the contents of the file,
start the descriptive name element of the file name with an appropriate date
indication.

If you have retrieved the file directly from a governmental or 
organizational server, we would like to preserve the original name of the 
file you have retrieved as part of the new file's unique name. This could
be used in lieu of a descriptive name element. Replace any dashes (-) or 
other symbols in original names with underscores, and start their names
with date indications whenever necessary. As an example:

`20140704230703_state_ny_2011_dohviol_63401.9`

Lastly, be sure to end the name with a filename extension that indicates what 
the file is.

`20140704230703_state_ny_2011_dohviol_63401.9.csv`

__NOTE: Please try to standardize all file contents into UTF-8 wherever 
possible. This may mean having to open the file in several editors and 
saving it a few different ways.__

===

We know that naming conventions like this may seem like a bit of "overkill"
but trust us... doing things the right way from the beginning will save a
lot of headaches down the road. Data projects like this need to have strict
naming convention standards in order to make working with large collections
of diverse files easier. And when we want to manipulate many files at once
with scripts, it will be a lot easier to do so when they all have a standard 
name.

Thank you for taking an interest in the work ahead - together we can make
a difference, preventing sickness and saving lives!
  
sincerely,

The FIDDLE Team
