# WEBI

<img href="">

## Purpose
### Introduction

Small companies and startups often have a small budget for website development services. I decided to create **WEBI** to offer my design and development freelancing skills to small companies who wish to build a professional face for their brand online but are restricted by budget. In addition, my freelancing services span beyond just design and development, and include marketing and hosting services also.

## Table of Contents

* [Purpose](#Purpose)
    * [Introduction](#Introduction)
* [User Experience Design](#user-experience-design)
    * [User Stories](#user-stories)
    * [Design Inspiration](#design-inspiration)
    * [Colour Scheme](#colour-scheme)
    * [Typography](#typography)
    * [Logo](#logo)
* [Website Structure](#website-structure)
    * [Wireframes](#wireframes)
    * [Data Schema](#data-schema)
* Features
    * Existing Features
    * Features to be Implemented
* [Technologies Used](#technologies-used)
    * [Languages](#languages)
    * [Libraries and Frameworks](#libraries-and-frameworks)
    * [Tools](#tools)
* Testing
* [Deployment](#deployment)
    * [Project Creation](#project-creation)
    * Heroku Deployment
    * [Local Deployment](#local-deployment)
* [Credits](#credits)
    * Code
    * [Acknowledgements](#acknowledgements)

--- 

## User Experience Design

### User Stories

| USER STORY ID                  | AS A        | I WANT TO BE ABLE TO                                                | SO THAT I CAN                                                                                     |
|--------------------------------|-------------|---------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| Viewing and Navigation         |             |                                                                     |                                                                                                   |
| 1                              | Prospect     | View a list of services available                                   | Select a service to buy                                                                           |
| 2                              | Prospect     | View specific categories of services                                | Easily find a service suited to my needs                                                          |
| 3                              | Prospect     | View individual service details                                     | Identify the service price and description                                                        |
| 4                              | Prospect     | Easily view the total of my purchases                               | Measure cost against business budget & see if I can afford to include additional service add-ons  |
| Registration and User Accounts |             |                                                                     |                                                                                                   |
| 5                              | Client   | Easily register for an account                                      | Setup my own personal area on the website to see my order history and profile                     |
| 6                              | Client   | Easily login or logout                                              | Access my personal account information                                                            |
| 7                              | Client   | Easily recover my password if I forget it                           | Recover access to my account                                                                      |
| 8                              | Client   | Receive an email confirmation after registering                     | Verify that my account registration was successful                                                |
| 9                              | Client   | Have a personalised user profile                                    | View my personal order history, order confirmations and save my payment details                   |
| Sorting and Searching          |             |                                                                     |                                                                                                   |
| 10                             | Prospect     | Sort the list of all available services                             | Quickly find a service that meets my requirements                                                 |
| 11                             | Prospect     | Sort services by a specific category                                | Narrow down services to those of interest                                                         |
| 14                             | Prospect     | Search for a product by name or description                         |                                                                                                   |
| 15                             | Prospect     | Easily see what I've searched for and the number of results         |                                                                                                   |
| Purchasing and Checkout        |             |                                                                     |                                                                                                   |
| 12                             | Prospect     | Easily select the size and quantity of a product when purchasing it |                                                                                                   |
| 13                             | Prospect     | View items in my bag to be purchased                                | See what the total cost of items in my basket are                                                 |
| 14                             | Prospect     | Adjust the quantity of individual items in my bag                   | Make changes to items in my basket before checking out                                            |
| 15                             | Prospect     | Easily enter my payment information                                 | Purchase my desired serviceds                                                                     |
| 16                             | Prospect     | Feel my personal and payment information is safe and secure         | Provide my payment information to make a purchase                                                 |
| 17                             | Prospect     | View and order confirmation after checkout                          | Ensure I have made the correct purchase                                                           |
| 18                             | Prospect     | Receive an email confirmation after checking out                    | Record details of my purchase history                                                             |
| Admin and Store Management     |             |                                                                     |                                                                                                   |
| 19                             | Manager | Add a service/product                                               | Add new items to my store                                                                         |
| 20                             | Manager | Edit/update a service/product                                       | Ammend service decriptions, price and images                                                      |
| 21                             | Manager | Delete a product                                                    | Remove any items which are no longer being sold                                                   |

### Design Inspiration

Before designing this website, I explored similar sites online to get an idea of the look and feel of websites in the industry. One company which really stood out to me was <a href="https://www.webstudio.ie/" target="_blank">WebStudio</a>. I drew great inpsiration from this website both strucutrally for my database and design-wise. 

<img src="readme-files/readme-images/webstudio.png">

### Colour Scheme

I researched colour schemes on Google and used Adobe's colour picker to choose the blue and pink shades for this website. I selected blue to represent professionalism and pink to show creativity and a nice contrast to the blue. Their Hexadecimal values are listed below:

| Colour | Hex Value |
| ------ | ------ |
| Blue | #093d60 |
| Pink | #feb5c5 |

### Typography
The fonts chosen for this website are Lato for headings and Roboto for the paragraph text. These are both sans serif fonts and I imported them into the CSS file from Google Fonts.

### Logo
I created the logo using Adobe Illustrator. I wanted a modern, clean and sans serif font for the logo and decided on Roboto Regular for this. The colours chosen were a combination of the blue and pink listed in the colour scheme above. The image below demonstrates how the logo should be used against dark and light backgrounds:

<img src="readme-files/readme-images/webi-logo.png">

[Back to top](#webi)

---

## Website Structure

### Wireframes

I created wireframes for this web application using balsamiq:

| Desktop Wireframes | Mobile Wireframes | Tablet Wireframes |
|--------------------|-------------------|-------------------|
| [Homepage](readme-files/wireframes/homepage-desktop.png) | [Homepage](readme-files/wireframes/homepage-mobile.png) | [Homepage](readme-files/wireframes/homepage-tablet.png) |
| [Bundles](readme-files/wireframes/bundles-desktop.png) | [Bundles](readme-files/wireframes/bundles-mobile.png)| [Bundles](readme-files/wireframes/bundles-tablet.png) |
| [Add-ons](readme-files/wireframes/addons-desktop.png) | [Add-ons](readme-files/wireframes/addons-mobile.png) | [Add-ons](readme-files/wireframes/addons-tablet.png) |
| [About](readme-files/wireframes/about-desktop.png) | [About](readme-files/wireframes/about-mobile.png) | [About](readme-files/wireframes/about-tablet.png) |
| [Blog](readme-files/wireframes/blog-desktop.png) | [Blog](readme-files/wireframes/blog-mobile.png) | [Blog](readme-files/wireframes/blog-tablet.png)  |

### Data Schema

#### Product App

**Category Model**
| Name           | Database Key  | Field Type |
|----------------|---------------|------------|
| Name           | name          | CharField  |
| Friendly Name  | friendly_name | CharField  |

**Bundle Model**
| Name          | Database Key | Field Type   |
|---------------|--------------|--------------|
| Service ID    | service_id   | IntegerField |
| Name          | name         | CharField    |
| Description   | description  | TextField    |
| Price         | price        | DecimalField |

**Images Model**
| Name         | Database Key | Field Type |
|--------------|--------------|------------|
| Image        | image        | URLField   |
| Image URL    | image_url    | ImageField |

**Design Model**
| Name         | Database Key | Field Type   |
|--------------|--------------|--------------|
| Design ID    | design_id    | IntegerField |
| Name         | name         | CharField    |
| Description  | description  | TextField    |
| Price        | price        | DecimalField |
| Quantity     | quantity     | IntegerField |

**Addons Model**
| Name           | Database Key | Field Type   |
|----------------|--------------|--------------|
| Add-on ID      | addon_id     | IntegerField |
| Name           | name         | CharField    |
| Description    | description  | TextField    |
| Price          | price        | DecimalField |
| Quantity       | quantity     | IntegerField |


#### Checkout App

**Order Model**

| Name           | Database Key   | Field Type               |
|----------------|----------------|--------------------------|
| Order Number   | order_number   | CharField                |
| User Profile   | user_profile   | ForeignKey 'UserProfile' |
| Full Name      | full_name      | CharField                |
| Email          | email          | EmailField               |
| Phone Number   | phone_number   | CharField                |
| Street Address | street_address | CharField                |
| Country        | country        | CharField                |
| Town or City   | town_or_city   | CharField                |
| Postcode       | postcode       | CharField                |
| Date           | date           | "DateTimeField"          |
| Order Total    | order_total    | DecimalField             |
| Grand Total    | grand_total    | DecimalField             |
| Stripe PID     | stripe_pid     | CharField                |

**OrderLineItem Model**

| Name            | Database Key   | Field Type           |
|-----------------|----------------|----------------------|
| Order           | order          | ForeignKey 'Order'   |
| Product         | product        | ForeignKey 'Product' |
| Quantity        | quantity       | IntegerField         |
| Line Item Total | lineitem_total | DecimalField         |


#### Blog App

[Back to top](#webi)

--- 
## Technologies Used

### Languages
* [HTML](https://en.wikipedia.org/wiki/HTML) was the main language used to create this website
* [CSS](https://en.wikipedia.org/wiki/CSS) was used to add bespoke design
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript) was used to create interactive elements on the website
* [Python](https://www.python.org/) was used for the backend of the website

### Libraries and Frameworks
* [Django](https://www.djangoproject.com/) was used as the Python-based web framework
* [Bootstrap](https://getbootstrap.com/) was used as the front-end framework
* [Google Fonts](https://fonts.google.com/) was used to find, sample and import fonts for the logo and website
* [Font Awesome](https://fontawesome.com/) was used for icons across the website

### Tools
* [Git](https://git-scm.com/) was used as the version control software to add, commit and push code to the GitHub repository
* [Gitpod](https://gitpod.io/) was used as the development environment to write my code
* [GitHub](https://github.com/) is the hosting site used to store the source code for the Website
* [Heroku](https://dashboard.heroku.com/) was used to run the application in the cloud
* [W3C Markup validator](https://validator.w3.org/) was used regularly to check for any errors in the HTML on the site
* [W3C CSS validator](https://jigsaw.w3.org/css-validator/) was used regularly to check for any errors in the CSS on the site
* [Adobe Illustrator](https://www.adobe.com/ie/products/illustrator.html) was used to create the logo and high fidelity mock ups
* [TinyPNG](https://tinypng.com/) was used to reduce the size of all the images on the website
* [balsamiq](https://balsamiq.com/wireframes/) was used to create low-fidelity wireframes of the website
* [JSHint](https://jshint.com/) was used to test the JavaScript code for errors
* [PEP8 Online](http://pep8online.com/) was used to check for PEP8 compliance
* [TableConvert](https://tableconvert.com/) was used to convert csv data to markdown tables

[Back to top](#webi)

--- 

## Deployment

### Project Creation
This project was created on GitHub using the following steps:

1. On Github, a new repository named ‘webi’ was created by navigating to ‘New’ on the Repositories page, selecting the CI full template, providing a ‘Repository name’, ‘Description’ and then clicking ‘Create repository’
2. Once the repository was created, I clicked the ‘Gitpod’ button to create the workspace in Gitpod
3. Version control was used throughout the project using the following commands: git commit -m "descriptive updates" - This command was used to commit changes to the local repository
4. git push - This command was used to push all committed changes to the GitHub repository

A new Django project was created as follows:

1. In the terminal, type ‘pip3 install django’ to install Django from the Python package index (version 3) and install in Gitpod
2. To create the project in the current directory, type ‘django-admin startproject webi .’ in the terminal
3. A .gitignore was created by typing ‘touch .gitignore’ in the terminal (included in CI template) which excluded our development database file (*.sqlite3) and compiled Python code (*.pyc and __pycache__) we don’t need in version control
4. Test Django is installed correctly by typing ‘python3 manage.py runserver’ in the terminal
5. Run the initial migrations by typing ‘python3 manage.py migrate’ in the terminal

A super user was created as follows:
1. Type ‘python3 manage.py createsuperuser’ in the terminal
2. Set a username, email address and password

In Django a SECRET_KEY is automatically included in the settings.py file. This was removed after the initial commit as follows:
1. Find a Django Secret Key generator online and copy SECRET_KEY
2. Set the secret key in the environment variable
3. Check the server still runs
4. Push to GitHub

### Heroku Deployment


### Local Deployment

The following steps are required to run this locally:

1. Go to the GitHub repository
2. Click the 'Code' dropdown menu
3. Copy Git URL from HTTPS box (https://github.com/JessicaJuliet/webi.git), or select to download the ZIP file
4. If usings the Git URL, open a new terminal in your IDE and type the 'git clone' command in the CLI and paste the copied URL
5. A clone of this project will be created locally on your machine
6. Alternatively, if you download the ZIP, unpackage locally and open in your IDE

[Back to top](#webi)

--- 

## Credits

### Code

### Acknowledgements

A bit thank you to my mentor, and the Code Institute's tutors, for encouraging and guiding me throughout the development of this project.

[Back to top](#webi)
