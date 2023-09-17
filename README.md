## What Is FIDDLE?

__F__ oodborne
__I__ llness
__D__ ata
__D__ umps, 
__L__ iberators, and 
__E__ xtractors

This is a public domain repository of data and code related to foodborne
illnesses in the United States. Our goal is to gather, clean, and 
disseminate the information that could lead to eliminating illness and
saving lives.

### Getting Started

See the Prezi presentation: https://prezi.com/7s1edw-6xqgo/the-problem-with-food-safety-data/

Check out the Github wiki link in the right sidebar of the repository's home 
page, it contains much background and several pages worth of content and 
research done so far on the problem, we highly recommend reading through it 
first.

Each folder in the repository should contain a README file that explains more 
about naming conventions, standards, and other best practices for collecting, 
managing, and working with datasets.

### How To Set Up Your System To Work With This Repository

#### 0. Create Accounts and SSH keys

The first thing you should do is to create accounts at [Github](http://github.com/) 
and [Heroku](http://heroku.com/) and enable SSH keys. You can follow all the 
instructions to generate SSH keys at the link below, then add them in the same 
way to your Github and Heroku accounts:

[https://help.github.com/articles/generating-ssh-keys](https://help.github.com/articles/generating-ssh-keys)

#### 1. Set Up Homebrew

Our team is primarily using Python and PostgreSQL for data cleansing and
data warehousing. On Mac OS, we recommend you use the Homebrew package
manager to maintain a common development environment and only use a Python
and PostgreSQL installed via Homebrew. Learn more about Homebrew here:

[http://brew.sh/](http://brew.sh/)

Follow all the instructions there to get Homebrew running, and get used to
running the following commands before you begin each work session:

~~~~
$ brew update
$ brew upgrade
$ brew doctor
~~~~

The following Homebrew packages are commonly installed for working with
the data and code from this repository, and we recommend you install them
before you begin work:

~~~~
ack                     harfbuzz      pango        sqlite
atk                     icu4c         pcre         subversion
autoconf                imagemagick   pillow       suite-sparse
automake                isl           pixman       swig
brew-pip                jasper        pkg-config   tbb
cairo                   jpeg          portmidi     webp
cloog                   libffi        postgresql   wget
cmake                   libmpc        py2cairo     wxmac
fontconfig              libpng        pypy         wxpython
freetype                libtiff       pyqt         xz
gdbm                    libtool       python       zeromq
gdk-pixbuf              libyaml       qt		
gettext                 little-cms    rbenv		
gfortran                makedepend    readline	
git                     matplotlib    scons		
glib                    mercurial     sdl		
gmp                     mpfr          sdl_image	
go                      neon          sdl_mixer	
gobject-introspection   numpy         sdl_ttf	
graphicsmagick          openblas      serf	
graphviz                openssl       sip	
gtk+                    ossp-uuid     smpeg
~~~~

If you're not using Homebrew, we recommend you use the latest versions of 
each of these packages in whatever package manager you are using. It's 
reasonably likely that you won't run into too many problems if you're a 
little more bleeding edge than Homebrew is.

####2. Heroku

In addition to this repository, we will maintain a Heroku instance with a 
web server / web site that will have live visualizations and informational 
content. This repository will act as a gateway to deploy to that instance. 
Stay tuned for more details about this as we progress.

[http://heroku.com/](http://heroku.com/)

Install the Heroku toolbelt following these instructions:

[https://toolbelt.heroku.com/](https://toolbelt.heroku.com/)

####3. ScraperWiki

We also plan to make use of the ScraperWiki tool, at least for gathering data
at first, but possibly to also mirror data or to act as a center for working
data prior to adding to this repository. ScraperWiki can run code written in 
several lanugages, but we'll continue to recommend Python for the time being.

[https://scraperwiki.com/](https://scraperwiki.com/)

####4. Clone, Research, Code, and Send Us Pull Requests

Once you have satisfied all of these requirements, you can clone this repo in
the usual way:

`git clone git@github.com:mik3cap/food-fiddle.git`

Read through all of the directory structures to get a feel for the data and 
our process. There are README files in each directory explaining further how 
to get set up to work with datasets. If you find data sources that we do not 
have that you believe are useful, please add them, but PLEASE follow the 
naming conventions we are using for files. It's vital that we maintain 
consistency even though we are using git and Github for source and data 
control. We need to avoid namespace collisions so that people don't lose their 
work or have to perform painful merges or rebases when they pull from the repo.

Again, first check out the wiki link below "pull requests" at the top right 
sidebar of the repository home page. Read through it to understand more about 
what the project is about, and use it to discuss our goals, ask questions, and 
help us find and provide solutions to the problem of foodborne illness.

Thank you for taking an interest in the work ahead - together we can make
a difference, preventing sickness and saving lives!
  
  
sincerely,

The FIDDLE Team
