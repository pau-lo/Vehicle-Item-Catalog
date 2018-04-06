# Vehicle-Item-Catalog

A web app that provides a list of vehicle items including their model and a brief description. This app uses third party authorization and authentication and user will have the ability to add, edit or delete items.

# Status

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/BlackrockDigital/startbootstrap-blog-post/master/LICENSE)

### Dependencies

* python2.7

## Download and Installation

Please install [Virtual Box](https://www.virtualbox.org/wiki/Downloads) if you do not already have installed.

As well as, we will need to install [Vagrant](https://www.vagrantup.com/downloads.html) if you do not already have it installed.

To begin using this web app choose one of the following options to get started:

1. Clone or download this repository to your local environment.

2. Look for the * vehicle itme catalog* folder and open it locally.

## Usage

Launch the Vagrant VM from inside the *vagrant* folder with:

`vagrant up`

After the installatin is complete,

Then access the shell with:

`vagrant ssh`

Then move inside the catalog folder:

`cd /vagrant/vehcileItemCatalog`

Then run the application:

We are using python2 which is already specify on my path as just python:

`python app.py`

After the last command you are able to browse the application at this URL:

`http://localhost:5000/`


# Thanks
    
Thanks to the FSND Slack channel for sharing their ideas and advice along the way.


