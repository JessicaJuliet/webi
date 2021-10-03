# WEBI

![WEBI Mock Up](readme-files/images/webi-mockup.png)

## Purpose

Welcome to WEBI - an e-commerce website where I offer my freelance marketing, design and web development services. I decided to create WEBI to help small businesses and startup companies, who often have a small budget, to avail of affordable website services.

WEBI is a multi-page e-commerce web application which not only offers services to its users, but also informative blog posts and case studies. Its initial vision was to offer website services which comprised of website 'Bundles' and 'Add-ons', but as the project evolved this led to simply an umbrella 'Services' offering. This evolution is mapped out further in the README document. 

**IMPORTANT: Please note, this project is for educational purposes only.**

Visit WEBI at [https://webi-development.herokuapp.com](https://webi-development.herokuapp.com/)

---

## Table of Contents

* [Purpose](#Purpose)
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
    * [Heroku Deployment](#heroku-deployment)
    * [Local Deployment](#local-deployment)
* [Credits](#credits)
    * Code
    * [Acknowledgements](#acknowledgements)

--- 

## User Experience Design

### User Stories

| USER STORY ID                  | AS A       | I WANT TO BE ABLE TO                                        | SO THAT I CAN                                                                 |
|--------------------------------|------------|-------------------------------------------------------------|-------------------------------------------------------------------------------|
| Viewing and Navigation         |            |                                                             |                                                                               |
| 1                              | Prospect   | View a list of services available                 | Select a service to buy                                              |
| 2                              | Prospect   | View specific categories of services                        | Easily find a service suited to my needs                                      |
| 3                              | Prospect   | View individual service details                             | Identify the service price, description and suitability                       |
| 4                              | Prospect   | Easily view the total of my purchases                       | Ensure total cost falls within my budget                                      |
| 5                              | Prospect   | Read blogs                                                  | Expand my knowledge on design and development                                 |
| 6                              | Prospect   | Review case studies                                         | Trust the quality of the freelancing services on offer                        |
| Registration and User Accounts |            |                                                             |                                                                               |
| 7                              | Client     | Easily register for an account                              | Setup my own personal area on the website to see my order history and profile |
| 8                              | Client     | Easily login or logout                                      | Access my personal account information                                        |
| 9                              | Client     | Easily recover my password if I forget it                   | Recover access to my account                                                  |
| 10                             | Client     | Receive an email confirmation after registering             | Verify that my account registration was successful                            |
| 11                             | Client     | Have a personalised user profile                            | View my personal order history and progress                                   |
| Sorting and Searching          |            |                                                             |                                                                               |
| 12                             | Prospect   | Sort the list of all available services                     | Quickly find a service that meets my requirements                             |
| 13                             | Prospect   | Sort services by a specific category                        | Narrow down services to those of interest                                     |
| Purchasing and Checkout        |            |                                                             |                                                                               |
| 14                             | Prospect   | View items in my bag to be purchased                        | See what the total cost of items in my basket are                             |
| 15                             | Prospect   | Adjust the quantity of individual items in my bag           | Make changes to items in my basket before checking out                        |
| 16                             | Prospect   | Easily enter my payment information                         | Purchase my desired services                                                  |
| 17                             | Prospect   | Feel my personal and payment information is safe and secure | Feel comfortable in providing my payment information to make a purchase       |
| 18                             | Prospect   | View my order confirmation after checkout                   | Ensure I have made the correct purchase                                       |
| 19                             | Prospect   | View the progress of my order                               | I know when I can expect it to be ready                                       |
| Admin and Store Owner     |            |                                                             |                                                                               |
| 20                             | Management | Add a service                                      | Add new items to my store                                                     |
| 21                             | Management | Edit/update a service                              | Ammend service/ product decriptions, price and images                         |
| 22                             | Management | Delete a service                                            | Remove any services which are no longer being sold                            |
| 23                             | Management | Edit/ update the status of an order                         | Update clients of their order progress                                        |


### Design Inspiration

Before designing this website, I explored similar sites online to get an idea of the look and feel of websites in the industry. One company which really stood out to me was <a href="https://www.webstudio.ie/" target="_blank">WebStudio</a>. I drew great inpsiration from this website both strucutrally for my database and design-wise. 

<img src="readme-files/images/webstudio.png">

### Colour Scheme

I researched colour schemes on Google and used Adobe's colour picker to choose the blue and pink shades for this website. I selected blue to represent professionalism and pink to show creativity and a nice contrast to the blue. Their Hexadecimal values are listed below:

| Colour | Hex Value |
| ------ | ------ |
| Blue | #093d60 |
| Pink | #feb5c5 |

### Typography
The fonts chosen for this website are Lato for headings and Roboto for the paragraph text. These are both sans serif fonts and I imported them into the CSS file from [Google Fonts](https://fonts.google.com/).

### Logo
I created the logo using Adobe Illustrator. I wanted a modern, clean and sans serif font for the logo and decided on Roboto Regular for this. The colours chosen were a combination of the blue and pink listed in the colour scheme above. The image below demonstrates how the logo should be used against dark and light backgrounds:

<img src="readme-files/images/webi-logo.png">

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

#### Services App

**Category Model**
| Name          | Database Key  | Field Type | Type Validation                       |
|---------------|---------------|------------|---------------------------------------|
| Name          | name          | CharField  | max_length=254                        |
| Friendly Name | friendly_name | CharField  | max_length=254, null=True, blank=True |
| Type          | type          | CharField  | max_length=254, null=True, blank=True |

**Bundle Model**
| Name        | Database Key | Field Type            | Type Validation                                  |
|-------------|--------------|-----------------------|--------------------------------------------------|
| Category    | category     | ForeignKey 'Category' | null=True, blank=True, on_delete=models.SET_NULL |
| Service ID  | service_id   | CharField             | max_length=254, null=True, blank=True            |
| Name        | name         | CharField             | max_length=254                                   |
| Description | description  | TextField             | max_length=350                                   |
| Price       | price        | DecimalField          | max_digits=6, decimal_places=2                   |

**Addon Model**
| Name        | Database Key | Field Type            | Type Validation                                  |
|-------------|--------------|-----------------------|--------------------------------------------------|
| Category    | category     | ForeignKey 'Category' | null=True, blank=True, on_delete=models.SET_NULL |
| Add-on ID   | addon_id     | CharField             | max_length=254, null=True, blank=True            |
| Name        | name         | CharField             | max_length=254                                   |
| Description | description  | TextField             | max_length=350                                   |
| Price       | price        | DecimalField          | max_digits=6, decimal_places=2                   |


**Images Model**
| Name      | Database Key | Field Type | Type Validation                        |
|-----------|--------------|------------|----------------------------------------|
| name      | Name         | CharField  | max_length=254                         |
| Image     | image        | ImageField | null=True, blank=True                  |
| Image URL | image_url    | ImageField | max_length=1024, null=True, blank=True |


#### Checkout App

**Order Model**

| Name           | Database Key   | Field Type               | Type Validation                                                         |
|----------------|----------------|--------------------------|-------------------------------------------------------------------------|
| Order Number   | order_number   | CharField                | max_length=32, null=False, editable=False                               |
| User Profile   | user_profile   | ForeignKey 'UserProfile' | on_delete=models.SET_NULL, null=True, blank=True, related_name='orders' |
| Full Name      | full_name      | CharField                | max_length=50, null=False, blank=False                                  |
| Email          | email          | EmailField               | max_length=254, null=False, blank=False                                 |
| Phone Number   | phone_number   | CharField                | max_length=20, null=False, blank=False                                  |
| Street Address | street_address | CharField                | max_length=80, null=False, blank=False                                  |
| Country        | country        | CharField                | max_length=40, null=False, blank=False                                  |
| County         | county         | CharField                | max_length=80, null=True, blank=True                                    |
| Town or City   | town_or_city   | CharField                | max_length=40, null=False, blank=False                                  |
| Postcode       | postcode       | CharField                | max_length=20, null=True, blank=True                                    |
| Date           | date           | "DateTimeField           | auto_now_add=True                                                       |
| Order Total    | order_total    | DecimalField             | max_digits=10, decimal_places=2, null=False, default=0                  |
| Grand Total    | grand_total    | DecimalField             | max_digits=10, decimal_places=2, null=False, default=0                  |
| Stripe PID     | stripe_pid     | CharField                | max_length=254, null=False, blank=False, default=''                     |


**OrderLineItem Model**

| Name            | Database Key   | Field Type          | Type Validation                                                             |
|-----------------|----------------|---------------------|-----------------------------------------------------------------------------|
| Order           | order          | ForeignKey 'Order'  | null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems' |
| Bundle          | bundle         | ForeignKey 'Bundle' | null=False, blank=False, on_delete=models.CASCADE                           |
| Addon           | addon          | ForeignKey 'Addon'  | null=False, blank=False, on_delete=models.CASCADE                           |
| Quantity        | quantity       | IntegerField        | null=False, blank=False, default=0                                          |
| Line Item Total | lineitem_total | DecimalField        | max_digits=6, decimal_places=2, null=False, blank=False, editable=False     |


#### Case Study App

| Name               | Database Key       | Field Type | Type Validation                                  |
|--------------------|--------------------|------------|--------------------------------------------------|
| Title              | title              | CharField  | max_length=50                                    |
| slug               | slug               | SlugField  | max_length=200, unique=True                      |
| Header Image       | header_image       | ImageField | null=True, blank=True, on_delete=models.SET_NULL |
| Study Subheading 1 | study_subheading_1 | CharField  | max_length=50                                    |
| Study Content 1    | study_content_1    | TextField  | validators=[MinLengthValidator(200)]             |
| Study Subheading 2 | study_subheading_2 | CharField  | max_length=50                                    |
| Study Content 2    | study_content_2    | TextField  | validators=[MinLengthValidator(200)]             |


#### Blog App

| Name               | Database Key       | Field Type | Type Validation                                  |
|--------------------|--------------------|------------|--------------------------------------------------|
| Title              | title              | CharField  | max_length=50                                    |
| slug               | slug               | SlugField  | max_length=200, unique=True                      |
| Header Image       | header_image       | ImageField | null=True, blank=True, on_delete=models.SET_NULL |
| Blog Subheading 1  | blog_subheading_1  | CharField  | max_length=50                                    |
| Blog Content 1     | blog_content_1     | TextField  | validators=[MinLengthValidator(200)]             |
| Blog Subheading 2  | blog_subheading_2  | CharField  | max_length=50                                    |
| Blog Content 2     | blog_content_2     | TextField  | validators=[MinLengthValidator(200)]             |

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
1. Setup Heroku App
    * Go to Heroku.com
    * Click to create new app
    * Name the app and select region
    * Then scroll 'Add-ons' and provision a new 'Heroku Postgress' database
    * Install dj_database_url and psycopg_2 in Gitpod:

    > pip3 install dj_database_url

    > pip3 install psycopg2-binary

    * Freeze requirements to ensure Heroku installs all our app requirements when deployed:
    > pip3 freeze > requirements.txt

2. Setup Database
    * Import dj_database_url in settings.py
    * Replace default database with a call to dj_database_url with the database URL from Heroku
    * Run migrations:
    > pythong3 manage.py migrate
    * Import product data
    > python3 manage.py loaddata categories
    > python3 manage.py loaddata services
    * Remove Heroku database config before committing


### Amazon AWS Setup


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

* Django CKEditor:
    * [Stack Overflow](https://stackoverflow.com/questions/34149541/is-there-any-way-to-change-the-default-text-editor-for-textfield-django-in-admin)
    * [Github Django CKEditor](https://github.com/django-ckeditor/django-ckeditor)

### Acknowledgements

A bit thank you to my mentor, and the Code Institute's tutors, for encouraging and guiding me throughout the development of this project.

[Back to top](#webi)
