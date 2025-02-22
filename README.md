![Mockup]()


# Introduction

Welcome to MyPortfolio! This is where I showcase my work as a web developer, highlighting the projects I’ve built, the skills I’ve learned, and how I’ve grown throughout my journey with CodeInstitute.

This portfolio brings together some of my key projects, like MyWay (a Django app helping non-verbal children communicate), my fitness app, and Get2Go Holidays (a travel website). Each project tells a story about the challenges I tackled, the technologies I used, and the lessons I learned along the way.

More than just a collection of work, this site reflects my passion for web development, from front-end design to back-end functionality. Whether you're a recruiter, a fellow developer, or just curious about what I do, feel free to explore, check out my projects, and get in touch!

## **[MyPortfolio Live Site]()**


## **[MyPortfolio REPOSITORY]()**


## Table of contents

 1. [ UX ](#ux)
 2. [ Technologies ](#tech)    
 3. [ Target Audience ](#audience)  
 4. [ User Stories ](#user)
 5. [ Planning, Structure and Design ](#design)
     - [ Iterations ](#iterations)
     - [ Layout ](#layout)
     - [ Features ](#features)
     - [ Design Choices ](#designchoice)
     - [ Wireframes ](#wireframes)
     - [ Database ](#database)
     - [ Entity Relationship Diagram ](#erd) 
 6. [ Deployment ](#deployment)
 7. [ Testing/Bugs/Fixes ](#testing)
 8. [ Future Upgrades ](#upgrade)
 9. [ Credits ](#credit)  

## UX <a name="ux"></a>


## Technologies <a name="tech"></a>

<details><summary> Technologies </summary>

* Languages

    * HTML
    * CSS
    * JavaScript
    * Python
    * DTL - Django Template Language

* Version Control

    * Git
    * Github
    * VsCode
    * Heroku

* Frameworks

    * Django
    * Bootstrap

* Database

    * PostgreSQL


* Additional resources

    * Coolors: https://coolors.co/ 
    * Canva: https://www.canva.com/
    * FontAwesome: https://fontawesome.com/search?o=r&m=free&s=solid
    * ChatGPT: https://chat.openai.com/
    * Google Fonts: https://fonts.google.com/
    * W3School: https://www.w3schools.com/

* Testing

    * Google Lighthouse
    * JSHint: https://jshint.com/
    * JSLint: https://www.jslint.com/
    * W3C HTML Validator: https://validator.w3.org/
    * W3C CSS Validator: https://jigsaw.w3.org/css-validator/

</details>

## Target Audience <a name="audience"></a>

* This Full Stack Portfolio Website was created as my Final Project for a Diploma in WebDevelopment with CodeInstitute. It is also targettting potential future employers and recruiters to showcase skills gained duuring my studies.

### User Stories <a name="user"></a>

<details><summary> USER STORIES </summary>

All User Stories Listed in Projects as Issues in Github Repositories and listed by Title in MoSCoW Priotarization section below.

</details>

## Planning, Structure and Design <a name="design"></a>


### Iterations <a name="iterations"></a>

#### MoSCoW Prioritization

<details>

| **User Story** | **Story Points** | **Priority** | **Notes** |
|-------------|-----------------|-----------------|-------------|
| 1. Base Template | 2 | Must Have | Base Template and Navigation |
| 2. Homepage | 2 | Must Have | Home Page with Navigation |
| 3. Django AllAuth | 3 | Must Have | AllAuth Authentication |
| 4. Services | 3 | Must Have | Services page and details with pricing |
| 5. Bag App | 4 | Must Have | Shopping Cart Implementation |
| 6. Cart - CRUD | 2 | Must Have | Shopping cart crud functionality |
| 7. Order Summary | 3 | Must Have | Overview of order |
| 8. Stripe Integration | 4 | Must Have | Stripe payment integration |
| 9. OrderConfirmation | 3 | Must Have | order confirmation e-mail |
| 10. Order History | 3 | Should Have | Logged in user order history |
| 11. Portfolio Homepage | 2 | Must Have | Portfolio homepage with navigation |
| 12. Projects Grid View | 3 | Must Have | Projects Grid View Display |
| 13. Project Details | 3 | Must Have | Project details, links to repositories |
| 14. User Profile | 4 | Must Have | Custome User Profile, with information and order history |
| 15. Profile Update Functionality | 2 | Should Have | Update personnel information |
| 16. Contact Form/App | 3 | Must Have | Contact form |
| 17. Submission confirmation | 2 | Should Have | Enquiry submission confirmation |
| 18. Deployment | 4 | Must Have | Deployment on Heroku |
| 19. Comments App | 3| Could Have | Comment form on projects. |



</details>

#### Iterations Summary

<details>

| **Iteration** | **Features** | **Story Points** | **MoSCoW Focus** |
|-------------|-----------------|-----------------|-------------|
| Iteration 1 | Setup, Authentication, Services | 14 | Must Have and Should Have |
| Iteration 2 | Shopping Bag, Checkout App, Payment | 14 | Must Have and Should Have |
| Iteration 3 | Portfolio and User Profiles | 14 | Must Have and Could Have |
| Iteration 4 | Contact Form,Comments and Deployment | 14 | Must have and Should Have |

</details>

### Layout: <a name="layout"></a>

### Design Choices: <a name="designchoice"></a>

* Colors: Coolors (https://coolors.co/) palette generator was used on the logo designed to pick the below colors for the project. 


* Font family: 


### Features: <a name="features"></a>

1. <details><summary>feature</summary><img src="image of feature"></details>


### Wireframes: <a name="wireframes"></a>

-   <details><summary>Name </summary>
    <img src="image link">
    </details>
-   <details><summary> </summary>
    <img src="">
    </details>

### Database: <a name="database"></a>

### Entity Relationship Diagram: <a name="erd"></a>


- <details><summary> ERD </summary><img src=""></details>


## Deployment <a name="deployment"></a>

- I used Heroku to deploy this project.


- To deploy to Heroku:

1. in Gitpod CLI create your Procfile and make sure it contains the following line of code:   web: gunicorn myway.wsgi
   This tells Heroku how to run the application.
2. Login to Heroku, select 'Create New App', create a unique name for the app and select your nearest region. Click 'Create App'
3. Navigate to the Deploy tab on Heroku dashboard and select Github, search for your project's reposatory and click 'connect'.
4. Navigate to 'settings', click reveal config vars and input the Database and SECRET KEY KEY-VALUE pairs along with all other dependencies relevent to the project.
5. Go to the Deploy tab , scroll to Manual Deploy and clcik on 'Deploy branch'
6. Once build is complete click on 'View' to launch the new app


## Testing/Bugs/Fixes <a name="testing"></a>

- Please see [TESTING.md](TESTING.md) for full manual and automated testing.

## Future Upgrades <a name="upgrade"></a>

## Credits <a name="credit"></a>

* Following resources were used during the project:

- https://www.w3schools.com/  - was used to help with HTML and JavaScript ideas.

- CodeInstitute's Tutor Assistence - Assistence were used in a few occasion:

- ChatGPT: This AI was used consistently, to help troubleshoot errors , refactor code , suggest improvements. - All dependencies are credited in comments.

            
