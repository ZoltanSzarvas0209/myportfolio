![Mockup](static/images/amiresponsivemp4.jpg)


# Introduction

Welcome to MyPortfolio! This is where I showcase my work as a web developer, highlighting the projects I’ve built, the skills I’ve learned, and how I’ve grown throughout my journey to become a Web Developer.

This portfolio brings together some of my key projects, like MyWay (a Django app helping non-verbal children communicate), my fitness app, and Get2Go Holidays (a travel website). Each project tells a story about the challenges I tackled, the technologies I used, and the lessons I learned along the way.

More than just a collection of work, this site reflects my passion for web development, from front-end design to back-end functionality. Whether you're a recruiter, a fellow developer, or just curious about what I do, feel free to explore, check out my projects, and get in touch!

## **[MyPortfolio Live Site](https://myportfoliomp4-6577cc735470.herokuapp.com/)**


## **[MyPortfolio REPOSITORY](https://github.com/ZoltanSzarvas0209/myportfolio.git)**


## Table of contents

 1. [ UX ](#ux)
 2. [ Technologies ](#tech)    
 3. [ Target Audience ](#audience)  
 4. [ User Stories ](#user)
 5. [ Planning, Structure and Design ](#design)
     - [ Iterations ](#iterations)
     - [ Layout ](#layout)
     - [ Apps ](#apps)
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
    * SQLite


* Additional resources

    * Canva: https://www.canva.com/
    * FontAwesome: https://fontawesome.com/search?o=r&m=free&s=solid
    * ChatGPT: https://chat.openai.com/
    * W3School: https://www.w3schools.com/
    * Squoosh: https://squoosh.app/ 

* Testing

    * Google Lighthouse
    * JSHint: https://jshint.com/
    * W3C HTML Validator: https://validator.w3.org/
    * W3C CSS Validator: https://jigsaw.w3.org/css-validator/

</details>

## Target Audience <a name="audience"></a>

This Full Stack Portfolio Website was built as my final project for the Diploma in Web Development with Code Institute. While it meets the course requirements, it’s also designed to showcase my skills to potential employers and recruiters, giving them a clear view of what I’ve learned and what I can do.

To meet the final project criteria for the Level 5 Diploma in Web Development, I added a major feature: IT/Web Development Services with Stripe payment integration (test mode). Right now, this is mainly for demonstration purposes, but in the future, I plan to expand it and use the platform to offer freelance services. This way, visitors looking for web development or IT solutions could connect with me directly through the site.

### User Stories <a name="user"></a>

<details><summary> USER STORIES </summary>

1. Base Template: 
As a visitor , I want to see a consistent website that I can navigate easily, so I can quickly find relevant sections.

Acceptance criteria 1
Navigation Accessibility

Given that I am a visitor on the website, when I access the homepage, I should see a clear and well-structured navigation menu that includes links to all key sections (e.g., Home, Services, Contact).

Acceptance criteria 2
Responsive and Intuitive Navigation

Given that I am browsing the website on different devices (desktop, tablet, mobile), when I interact with the navigation menu, it should be fully responsive, easy to use, and provide a smooth transition between sections.

NOTES: slightly revised to better reflect it's purpose.

2. HomePage:
As a visitor, I want to explore the Homepage, so I can understand what the site is about

Acceptance criteria 1
Clear and Engaging Homepage Content

Given that I am a visitor on the website, when I land on the homepage, I should see a clear heading, a brief description of the site's purpose, and visually engaging elements (e.g., images, icons, or banners) that communicate the main offerings.

Acceptance criteria 2
Easy Access to Key Information

Given that I am on the homepage, when I scroll or interact with the content, I should find intuitive sections such as an introduction, key features, a call-to-action (e.g., “Learn More” or “Get Started”), and navigation options leading to other relevant pages.

3. AllAuth Authentication
As a visitor , I want to register/login, so I can access premium features

Acceptance criteria 1
Successful Registration and Login

Given that I am a new visitor, when I fill out the registration form with valid details (e.g., username, email, password) and submit it, I should receive a confirmation email and be able to log in successfully.
Given that I am a returning visitor, when I enter my correct login credentials, I should be granted access to my account and redirected to the appropriate dashboard or homepage.

Acceptance criteria 2
Restricted Access to Premium Features

Given that I am not logged in, when I try to access premium features, I should see a prompt directing me to register or log in before proceeding.
Given that I am logged in as a premium user, when I navigate to premium features, I should have full access without restrictions.

4. Service Page
As a visitor, I want to see available service and prices so I can decide what to purchase.

Acceptance criteria 1
Clear Display of Services and Prices

Given that I am a visitor on the website, when I navigate to the services page, I should see a well-organized list of available services along with their descriptions and corresponding prices.

5. Shopping Cart:
As a user, I want to add services to the cart so I can review them before purchase.

Acceptance criteria 1
Adding Services to the Cart

Given that I am a user browsing the services page, when I click on the "Add to Cart" button for a service, the selected service should be added to my cart, and I should receive a confirmation message or visual indicator (e.g., cart icon update).

Acceptance criteria 2
Viewing and Managing Cart Items

Given that I have added services to my cart, when I navigate to the cart page, I should see a list of selected services with their names, prices, and total cost. I should also have the option to remove services or update quantities before proceeding to checkout.

6. Shopping Bag functions
As a user, I want to remove items from my cart so I can adjust my order.

Acceptance criteria 1
Removing an Item from the Cart

Given that I have items in my cart, when I click the "Remove" button next to a service, the selected service should be removed from my cart immediately, and the total price should be updated accordingly.

Acceptance criteria 2
Confirmation of Removal

Given that I have removed an item from my cart, when I check my cart again, the removed item should no longer be visible, and I should receive a confirmation message indicating that the item has been successfully removed.

7. Order Summary:
As a user I want to see an overview of my order before completing the payment

Acceptance criteria 1
Order Summary Display

Given that I am on the checkout page, when I review my order, I should see a clear overview of all selected services, including their names, quantities, individual prices, and the total cost before proceeding to payment.

Acceptance criteria 2
Option to Modify Order

Given that I am reviewing my order, when I decide to make changes, I should have the option to go back to the cart to add, remove, or update services before finalizing the payment.

8. Stripe Integration:
As a user I want a seamless payment experience so I can complete my purchase easily

Acceptance criteria 1
Successful Payment Processing and Confirmation

Given that I have entered valid payment details, when I complete the transaction, the payment should be processed securely, and I should receive a confirmation message.

9. Order/Email confirmation:
As a user I want to receive an order confirmation e-mail so I know the payment was successful.

Acceptance criteria 1
Automatic Order Confirmation Email

Given that I have successfully completed my payment, when the transaction is processed, I should receive an order confirmation email containing my order details, including purchased services, total amount paid, and a unique order reference number.

10. Order History:
As a user I want to view my past orders so I can track my purchases.

Acceptance criteria 1
Order History Access

Given that I am logged into my account, when I navigate to the "Order History" or "My Purchases" section, I should see a list of all my past orders, including order numbers, dates, purchased services, and total amounts paid.

11. HomePage:
As a visitor I want to be able to view different sections of the portfolio so I can assess the developer

Acceptance criteria 1
Clear Navigation to Portfolio Sections

Given that I am a visitor on the portfolio website, when I access the homepage or navigation menu, I should see clearly labeled sections (e.g., Projects, Skills, About, Contact) that allow me to explore different aspects of the developer's work.

Acceptance criteria 2
Detailed Project Showcase

Given that I am browsing the portfolio, when I select a project, I should see a detailed project page that includes a project description, technologies used, key features, and links to live demos or GitHub repositories, helping me assess the developer's skills and experience.

12. Project Grid View:
As a visitor, I want browse past projects so I can evaluate the developers work

Acceptance criteria 1
Project Gallery Display

Given that I am a visitor on the portfolio website, when I navigate to the "Projects" or "Portfolio" section, I should see a visually organized gallery or list of past projects, each with a title, thumbnail image, and brief description.

Acceptance criteria 2
Detailed Project Information

Given that I am interested in a specific project, when I click on it, I should be directed to a dedicated project page that includes a detailed description, technologies used, key features, challenges overcome, and links to a live demo or GitHub repository.

13. Project Details:
As a visitor, I want to be able to view all projects in depth so I can evaluate their quality.

Acceptance criteria 1
Comprehensive Project Details

Given that I am viewing a project, when I click on its title or thumbnail, I should be taken to a dedicated project page that provides an in-depth description, including the project’s purpose, key features, technologies used, development process, and challenges overcome.

Acceptance criteria 2
Interactive and Visual Elements

Given that I am exploring a project in detail, when I view the project page, I should see relevant visual elements such as screenshots, demo videos, or links to live versions and GitHub repositories, allowing me to assess the quality and functionality of the work.

14. User Profile:
As a user, I want a profile page so I can view my order history.

Acceptance criteria 1
Profile Page Access and Order History Display

Given that I am a logged-in user, when I navigate to my profile page, I should see my personal information along with a dedicated section for my order history, listing past purchases with order numbers, dates, and total amounts.

15. Profile Update Functionality:
As a user, I want to update my details so I can manage my information.

Acceptance criteria 1
Profile Update Functionality

Given that I am a logged-in user, when I navigate to my profile settings, I should be able to update my personal information, including name, email, phone number, and password, with a clear “Save Changes” button.

Acceptance criteria 2
Successful Update Confirmation

Given that I have updated my details, when I submit the changes, my information should be saved successfully, and I should receive a confirmation message or email verifying that my details have been updated.

16. Contact Form:
As a user/visitor , I want to send an enquiry so I can contact the developer directly.

Acceptance criteria 1
Enquiry Form Availability and Submission

Given that I am a user or visitor on the website, when I navigate to the “Contact” section, I should see a clearly labeled enquiry form with fields for my name, email, subject, and message, along with a “Submit” button.

Acceptance criteria 2
Successful Enquiry Submission and Confirmation

Given that I have filled out the enquiry form with valid details, when I submit it, I should receive an on-screen confirmation message stating that my enquiry has been sent successfully, and if applicable, an email confirmation with expected response time.

17. Submission confirmation:
As a visitor, I want to receive a confirmation so I know my enquiry was sent.

Acceptance criteria 1
On-Screen Confirmation Message

Given that I have submitted an enquiry form with valid details, when I click the “Submit” button, I should see an on-screen confirmation message stating that my enquiry has been successfully sent.

18. DeploymentL
As the owner, I want the website to be live so can be contacted by potential employers or buyers for my services.

Acceptance criteria 1
Deploy site on Heroku

19. Comments App:
As a user I want to be able to leave a comment so I can provide a feedback.

Acceptance criteria 1

Comment Submission Functionality

Given that I am a logged-in user, when I navigate to a feedback or comments section, I should see a comment input field where I can type my feedback and submit it using a “Post Comment” button.




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

<details><summary>SUMMARY</summary>

| **Iteration** | **Features** | **Story Points** | **MoSCoW Focus** |
|-------------|-----------------|-----------------|-------------|
| Iteration 1 | Setup, Authentication, Services | 14 | Must Have and Should Have |
| Iteration 2 | Shopping Bag, Checkout App, Payment | 14 | Must Have and Should Have |
| Iteration 3 | Portfolio and User Profiles | 14 | Must Have and Could Have |
| Iteration 4 | Contact Form,Comments and Deployment | 14 | Must have and Should Have |

</details>

<details><summary>UPDATES Following Iteration 1</summary>

Features Implemented (User Stories Fulfilled)
The following features have been completed as part of Iteration 1 to establish the main structure of the project:

1. Authentication (Django AllAuth) – Implemented user authentication and login/logout functionality.
2. Base Template & Navigation – Established the main layout and navigation system.
3. Homepage – Created a home page with navigation and an introduction to the platform.
4. Services Page – Built a services page displaying details and pricing.
5. Shopping Bag App – Developed a shopping cart system.
6. Portfolio Homepage – Designed the portfolio homepage to showcase projects.
7. Projects Grid View – Implemented a grid layout for displaying projects.
8. Project Details Page – Project details been replaced with links to the actual Repositories of the Projects.
9. Contact Form – Reused from a previous project, allowing users to send inquiries.

Key Changes from the Original Plan

1. Brought Forward Several Features – Homepage, Base Template, Services, Contact Form, Portfolio Homepage, Projects Grid & Details, and Shopping Bag App were all completed in Iteration 1 instead of later iterations. This change helped establish the core structure early.
2. Checkout & Stripe Integration Prioritized – Initially planned for Iteration 3, this has been moved to Iteration 2 as a top priority.
3. User Profiles Elevated in Priority – Custom user profiles were made part of Iteration 2, as they are necessary for order history.
4. Order History & Confirmation Email Delayed – These features are still important but have been shifted to Iteration 3 to focus on payment functionality first.
5. Deployment Moved to the Final Iteration – Originally in Iteration 3, deployment will now be handled in Iteration 4 after ensuring all core features (especially Stripe) are functional.
6. Comments App Remains Optional – It has been kept as a "Could Have" feature for Iteration 4, depending on available time.
</details>

### Layout: <a name="layout"></a>

### Design Choices: <a name="designchoice"></a>

####
<details> <summary>Color Palette</summary>
<img src="static/images/readme_images/colorpalette.jpeg">
</details>

- White (Translucent) – rgba(255, 255, 255, 0.2)
- Dark Gray (Translucent) – rgba(50, 49, 49, 0.8)
- Blue – #5b7cfa
- Purple – #945bd6
- Black (Translucent) – rgba(0, 0, 0, 0.6)
- White (More Translucent) – rgba(255, 255, 255, 0.3)
- Light Blue – #6e8efb

### Apps: <a name="apps"></a>

- Home App: landing page / navigation for site including Services, Portfolio and contact section 

- Portfolio App: Entry point for my personnal portfolio, app includes a section for my projects , about section ,where work history can be found and a tech section indicating languages I commonly use and my progress.

- Services App: Included in project to demonstrate ability to integrate "e-commerce" features with payment integration(Stripe).

- Contact App:
 Re-used code I wrote for MyWay Project with a simple custom form and model. There is 1 simple template featuering the form so users can submit messages for the owner( superuser to see)

- Bag App:
The codebase for this app is largly reused from CodeInstitute's BoutiqueAdo's tutorial with customised to suit myportfolio's needs. Changes were also made to The associated javascripts to make all features work as expected in this project.

There is no model associated with this app.

Context.py was created to make bag_contents avaialble throughout the site.

- Checkout App:
Similarly to Bag App the mayority of the code is reused and then customised to work in this project. 

- Comments App: A feature added to provide users with crud functionality and to grant the ability for potential future employers and/or fellow coders to leave feedback.

- Profiles App: to integrate user profiles , it serves to customise user experience and gives the ability to maintain purchase history.

### Features: <a name="features"></a>

1. <details><summary>Header</summary><img src="static/images/readme_images/features/header.jpg"></details>

- Profile Picture
- Navigation bar
- Shoppping bag
- Accounts Icon

2. <details><summary>Footer</summary><img src="static/images/readme_images/features/footer.jpg"></details>

- Contact Info
- Social Icons
- Download CV Section

3. <details><summary>HOME</summary><img src="static/images/readme_images/features/home.jpg"></details>

- Navigation Page

4. <details><summary>PORTFOLIO</summary><img src="static/images/readme_images/features/portfolio.jpg"></details>

- Portfolio navigation page with links to projects, about and tech sections.

5. <details><summary>SERVICES</summary><img src="static/images/readme_images/features/services.jpg"></details>

- Currently serves the purpose of showcasing ability to create e-commerce functionality with a natural flow of shopper experience.
- services.html is to display a list of services available for visitors to purchase. 
- Each "card", Service listed has a title , a description and a price and the image itself is a link to the next step in the shoppers journey.

6. <details><summary>SERVICE_DETAILS</summary><img src="static/images/readme_images/features/service_details.jpg"></details>

- following up from services.html, this page provides further details about the selected service.
- service_detail page also features increment and decrement buttons for easy adjustment in order.
- back and add to bag buttons are provided for next steps.

7. <details><summary>BAG</summary><img src="static/images/readme_images/features/bag.jpg"></details>

- a shopping cart collecting all items added.
- features a summary of the order with ability for adjustments
- keep shopping and checkout buttons are provided as options for the user for next steps.

8. 
<details><summary>CHECKOUT</summary><img src="static/images/readme_images/features/checkout1.jpg"></details>
<details><summary>CHECKOUT</summary><img src="static/images/readme_images/features/checkout2.jpg"></details>


- Final order summary for user to see items to be purchased
- A form to fillout for details to complete the purchase
- Card details form integrated with stripe
- Adjust bag and complete order buttons
- links to login and/o create an account.

9. <details><summary>ORDER CONFIRMATION</summary><img src="static/images/readme_images/features/confirmation.jpg"></details>

- Confirmation page with order numbers, billing details and order summary.

10. <details><summary>PROFILE</summary><img src="static/images/readme_images/features/profile.jpg"></details>

- Page is only available for registered users.
- Form to update billing address - also pre-fills information at checkout.
- Order History section with details about previous orders and links to order confirmations.

11. <details><summary>CONTACT</summary><img src="static/images/readme_images/features/contact.jpg"></details>

- contact form that submits a message for the superuser/ owner of the site - accessible in admin

12. <details><summary>ABOUT</summary><img src="static/images/readme_images/features/about.jpg"></details>

- Work history/ CV section

13. <details><summary>TECH</summary><img src="static/images/readme_images/features/tech.jpg"></details>

- List of technologies currently used, previously studied and progress.

14. Other Features:

- Hover effect over icons and main navigation pages
- Transition: Buttons, Navbar, Profile image
- Toasts - user feedback for improved UX


### Wireframes: <a name="wireframes"></a>

I used miro.com to sketch basic wireframes for the project. There are several minor differences from the final product but overall the project stayed true to its original design.

-   <details><summary> home.html </summary>
    <img src="static/images/readme_images/wireframes/wireframe_home.jpg">
    </details>

-   <details><summary> Portfolio.html </summary>
    <img src="static/images/readme_images/wireframes/wireframe_protfolio.jpg">
    </details>

-   <details><summary> About.html </summary>
    <img src="static/images/readme_images/wireframes/wireframe_about.jpg">
    </details>

-   <details><summary> contact.html </summary>
    <img src="static/images/readme_images/wireframes/wireframe_contact.jpg">
    </details>

-   <details><summary> services.html </summary>
    <img src="static/images/readme_images/wireframes/wireframe_services.jpg">
    </details>

-   <details><summary> bag.html </summary>
    <img src="static/images/readme_images/wireframes/wireframe_bag.jpg">
    </details>

-   <details><summary> checkout.html </summary>
    <img src="static/images/readme_images/wireframes/wireframe_checkout.jpg">
    </details>

-   <details><summary> Checkout_success.html </summary>
    <img src="static/images/readme_images/wireframes/wireframe_checkout_success.jpg">
    </details>

-   <details><summary> service_details.html </summary>
    <img src="static/images/readme_images/wireframes/wireframe_service_details.jpg">
    </details>

-   <details><summary> profile.html </summary>
    <img src="static/images/readme_images/wireframes/wireframe_profile.jpg">
    </details>

-   <details><summary> tech.html </summary>
    <img src="static/images/readme_images/wireframes/wireframe_tech.jpg">
    </details>



### Database: <a name="database"></a>

### Entity Relationship Diagram: <a name="erd"></a>

Entity Relationship Diagram

1. User: AllAuth , Django's built in authentication system.
2. UserProfile: Created so order history can be maintained to registered users. It has a one to one relationship to User and One to Many to the Order model.
3. Order: each order is linked to at least one OrderLineItem making it a One to Many relationship.
4. OrderLineItem: maintains a Many to One relationship to the Services model.
5. Service: represent all the services that are on offer and has a One to Many link to OrderLineItem
6. Project: each object is a completed project uploaded to the site. The user(in this case myself) can have many projects therefore its a One to Many link.
7. Comments: created so visitors can leave comments/feedback on the projects. Each Project can have many comments and each user can make many comment so User to Comments is One to Many and Projects to Comments is also One to Many relationship.
8. Contact: ITs a general contact form , where anyone can leave a message/submit an enquiry.One to Many link.

- <details><summary> ERD </summary><img src="static/images/readme_images/erd.jpeg"></details>


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

The Comment App was implemented as an optional extra feature for this project - while it is functional there are several improvements that can be done but had no scope for it during this project.

- Toast messages are not working correctly and need looking into in more depth.
- when user clicks the edit comment button, the site reloads with the relevant comment but is not automatically scrolled to the right section.
- when comments are opened on any of the projects all project divs are expanding and it is not visually appealing.
- Further validation can be implemented on the checkout form to make it more user friendly.

The above issue were noted but not yet addressed.

## Credits <a name="credit"></a>

* Following resources were used during the project:

- BoutiqueAdo walkthrough from CodeInstitute's tutorials have been used on several occasion in this project:
    1. Bag App was reused from the tutorial and modified to suit this project.
        - models, views, and templates all used as base code but modified.
    2. Checkout App was reused from the tutorials and modified to suit this project.
        - models, views, and templates all used as base code but modified.
    3. Some html templates were also used as a base but subject to restructuring to maintain consistency in this project.

- https://www.w3schools.com/  - was used to help with HTML and JavaScript ideas.

- CodeInstitute's Tutor Assistence - Assistence were used in a few occasion:

- ChatGPT: This AI was used consistently, to help troubleshoot errors , refactor code , suggest improvements. - All dependencies are credited in comments.
    1. Mayor dependency: the entire webhooks.py file in checkout app was created with the help of ChatGPT.
    2. Django testing: tool used both to troubleshoot failing tests and write additional ones for a more extensive check.

            
