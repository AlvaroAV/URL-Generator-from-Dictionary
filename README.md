#URL SHORTENER

This is a small Django 1.6 example project. This is a project to generate short URL's based in a words.txt file. 

Software used in this project:

    - Django 1.6
    - South 1.0.1
    - Apache 2.4.7
    - SQLite3

You can execute:

    pip install -U -r requirements.txt

to install both python packages, the file '`requirements.txt`' is in the root folder of the project.

I've used Apache/2.4.7 (Ubuntu), to install it:

    sudo apt-get install apache2

I used the uwsgi mod for apache, you can install it with:

    sudo apt-get install libapache2-mod-wsgi
    sudo service apache2 restart

I run the project in local so I added to my '`/etc/hosts`' the line:

    127.0.0.1       myurlshortener.com


I run the project with Apache, so I've added a folder called "apache" where I included the '`urlshortener.conf`' file.

In this file you should change all repetitions of the path '`/path/to/project/`' for the absolute path where you put the project. If you put the project into '`/var/www/`' you should change '`/path/to/project`' for '`/var/www/`'.

You should put 'urlshortener.conf' inside the folder "/etc/apache2/sites-available/" and create a link from the file in that path to "`/etc/apache2/sites-enabled`", you can do this with:

    cp urlshortener.conf /etc/apache2/sites-available
    cd /etc/apache2/sites-enabled
    ln -s ../sites-available/urlshortener.conf
    sudo apache2 restart


The folder of the project has to be editable by SQLite or the database will give error "unable to read database".



About Django:

- I'v added the views to manage the index and the redirection in the file 'views.py'. I've created also the file 'utils.py' to manage there the code to get the word based on a given URL in the function 'get_word(original_url)'

- I've created a Form `URLForm` to manage the creation of the URL, with a `def clean_original_url` method to ensure the URL doesn't exist already.

- I've added a list of words in the words.txt to the project database using the model "Word". I added the command 'update_words' to update the words. This command by default read the `words.txt` file inside the project but you can specify another txt file using 

    `python manage.py update_words --file /path/to/file`


- I've used signals.py to free a **Word** if the **URL** is deleted
