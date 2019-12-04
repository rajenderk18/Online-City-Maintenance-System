# AVIYAT – A Platform for Grievance Reporting for City Maintenance

> Online City Maintenance System is one of a kind, offering simple, yet powerful maintenance management for common issues related to city. City and municipal maintenance is not a small task for any locality, small or large. When a municipal pipe starts leaking or bursts, it's an emergency that can potentially put people at risk. When a block of streetlights go out, the area they are meant to illuminate feels less safe. These are just a couple examples of the reactive emergency repairs that public works officials must respond to and organize, saying nothing of the planned works that come into play.



<p align="center">
  <img src="https://user-images.githubusercontent.com/35782113/70093396-4d35e980-15ee-11ea-82a9-042872747216.png">
</p>



## Example 

&nbsp;

[![HomePage in use ](https://user-images.githubusercontent.com/35782113/70093397-4d35e980-15ee-11ea-9d63-0e2b2a052f0f.gif)]()
&nbsp;

&nbsp;

------

## Table of Contents 

- [Panther_Youtube_Downloader](#pantheryoutubedownloader)
  * [Example](#example)
  * [Table of Contents](#table-of-contents)
  * [Getting Started](#getting-started)
    + [Prerequisites](#prerequisites)
    + [Clone](#clone)
    + [Running the Panther Youtube Downloader](#running-the-panther-youtube-downloader)
  * [Building the Windows installer](#building-the-windows-installer)
    + [Using pyinstaller](#using-pyinstaller)
    + [Using CX_FREEZE](#using-cxfreeze)
      - [Writing setup.py:](#writing-setuppy)
      - [Creating the Package:](#creating-the-package)
  * [Features](#features)
  * [How it works ? (Instructions)](#how-it-works--instructions)
  * [Usage](#usage)
      - [Downloading the audio and video from a youtube link:](#downloading-the-audio-and-video-from-a-youtube-link)
      - [Playing the audio directly from the "Panther Youtube Downloader":](#playing-the-audio-directly-from-the-panther-youtube-downloader)
        * [Changing the theme of the "Panther Youtube Downloader":](#changing-the-theme-of-the-panther-youtube-downloader)
  * [Executable](#executable)
      - [Version: v0.1](#version-v01)
  * [To-do](#to-do)
  * [Documentation](#documentation)
    + [Making the layout of the Panther Youtube Downloader](#making-the-layout-of-the-panther-youtube-downloader)
    + [Functions used in the Panther Youtube Downloader](#functions-used-in-the-panther-youtube-downloader)
  * [Tests](#tests)
  * [Contributing](#contributing)
  * [FAQ](#faq)
  * [Support](#support)
  * [Donations](#donations)
  * [License](#license)

------

## Getting Started

### Prerequisites

Although, I used the following software (with their corresponding versions) to run this program, AVIYAT should be run with any version of Python 3 +. We need the following packages to run this program:

- Python 3.7.4 (This program should work fine with any installation of Python3+. Although, I used Python 3.7.4)
- Django==2.2.7 (pip install Django==2.2.7)
- googlemaps==3.1.4( pip install googlemaps==3.1.4)
- django-crispy-forms==1.8.0 (pip install django-crispy-forms==1.8.0)
- django-braces==1.13.0 (pip install django-braces==1.13.0)
- django-bootstrap4==1.0.1 ( pip install django-bootstrap4==1.0.1)
- beautifulsoup4==4.8.1( pip install beautifulsoup4==4.8.1)
- misaka==2.1.1( pip install misaka==2.1.1)
- Pillow==6.2.1( pip install Pillow==6.2.1)
- psycopg2==2.8.4 (pip install psycopg2==2.8.4)

For front-end design, I used:

- HTML, CSS, JavaScript, and Bootstrap

For storing database, I used:

- Postgresql

### Clone

- Clone this repo to your local machine using
-  `https://github.com/rajenderk18/Online-City-Maintenance-System.git`

### Running the AVIYAT – (A Platform for Grievance Reporting for City Maintenance)

You can run the program by following the below commands:

```
$ git clone https://github.com/rajenderk18/Online-City-Maintenance-System.git
$ cd Online-City-Maintenance-System
$ python manage.py makemigrations
```

makemigrations, which is responsible for creating new migrations based on the changes you have made to your models.

```
$ python manage.py migrate
```

migrate, which is responsible for applying and un-applying migrations.

If you want to see the SQL statements for migration, You can run below commands:

```
$ python manage.py sqlmigrate
```

To list all the project migrations and their status, run the below command:

```
$ python manage.py showmigrations
```

To run the server, and see your website, you can use below commands:

```
$ python manage.py runserver
```

After running the above command, You can see your website at this address in your browser: 127.0.0.1:8000

If you want to run your website on different port, you just need to provide the port number with 'runserver' command like the example given below:

```
$ python manage.py runserver 8080
```

You can create superuser (or admin) by following commands:

```
$ python manage.py createsuperuser
```

------

## Benefits of AVIYAT (A Grievance Reporting for City Maintenance)

**Easy-to-use web-based applications that help your municipality:**

- Increase asset life
- Prevent asset failures
- Improve labor productivity
- Reduce costly downtimes
- Minimize investment in inventory
- Lower the total cost of maintenance
- Easy-to-use web-based interface



------



## Class Diagram

![1575484594393](C:\Users\rkumar\AppData\Roaming\Typora\typora-user-images\1575484594393.png)





## Usage 

#### Working example of the home page of the website:

![UpdatePage in use](https://user-images.githubusercontent.com/35782113/70093399-4dce8000-15ee-11ea-9fce-163afedea214.gif)



#### Other pages of the website:



![OtherPages in use](https://user-images.githubusercontent.com/35782113/70093398-4dce8000-15ee-11ea-80f6-2c6888df68a2.gif)





## Live Website Link

You can access the website on the following URL: http://citymaintenance.pythonanywhere.com/

## To-do

- [x] Report an Issue feature implemented
- [x] Successfully login, logout.
- [ ] Need to work on Map and draggable marker on map
- [ ] Implementation of list filter for user side
- [ ] Need to implement the email status reporting feature
- [ ] need to work on auto-category select and more details about the specific catogery 

## Documentation 

### Making the layout of the Panther Youtube Downloader

For making the layout of the Panther Youtube Downloader, I used the Tkinter widgets, "Frame" to divide the window area into different sizes. I divide the window into 4 frames:

1. 

## Tests

This program is successfully tested on Window 10, Mac, and Ubuntu 16.04.

------

## Contributing

If interested, you can contribute by following the given step:

1. Fork it using `https://github.com/rajenderk18/Online-City-Maintenance-System.git`
2. Create your feature branch (git checkout -b my-new-feature) 🔨🔨🔨
3. Commit your changes (git commit -am 'Added <xyz> feature')
4. Push to the branch (git push origin my-new-feature)
5. Create new Pull Request 🔃

------

## FAQ

- 

------

## Support

Reach out to me at one of the following places!

- Website at <a href="http://KumarRajender.com" target="_blank">`KumarRajender.com`</a>
- Email me: [rajenderk18@gmail.com](mailto:rajenderk18@gmail.com)

&nbsp;

------

## Credits

- If you think this little youtube downloader is useful to you, then it's a good reason to do a donation.

- 

------

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](https://github.com/rajenderk18/Panther-Calculator/blob/master/LICENSE)**
- Copyright 2019 © <a href="http://KumarRajender.com" target="_blank">Rajender Kumar</a>.
