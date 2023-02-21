# Bessie + Beau

## Introduction

**Bessie + Beau** is a full-stack e-commerce application for a luxury women fashion and beauty store. The application provides the functionality for a customer to view or search for products, add the product to shopping cart (or to a Wishlist should they need to defer the purchase until a later time), and proceed to a secure checkout to complete purchase by providing their delivery address and making payment with their credit or debit card. At every stage of this process, a confirmation message is displayed on the top right side of the screen to give visual feedback to the user. On completing purchase, Order confirmation email is sent directly to the customer email address for their records. And their Order history and product Wishlist are saved in their profile for them to view and reference. **Happy customers** can leave a testimonial for the store, which they can edit anytime if they want to make some changes.  

### Project Goal

**The goal of this e-Commerce application** is to provide a functional and interactive retail store, with authentication system for users to login to access their relevant data and buy items they want, and to logout. It is a **Business-to-Consumer (B2C)**, designed to sell products to individual customers. It processes orders, accepts payments, and manages shipping and delivery. This application is user centred design; it is intuitive, simple, and easy and enjoyable to use, thus, generating positive user experience. However, it is for illustrative purpose only: no actual payment is made and no real purchase is carried out.

![Bessie + Beau Mockup](/static/docs/img/bessie-beau-mockup.png)

[View Live Project Here](https://bessiebeau.herokuapp.com/)

## Table of Contents

* [Introduction](#introduction)
* [The Strategy Plane](#the-strategy-plane)
  * [Epics](#epics)
  * [EPIC - Setup and Deployment](#epic---setup-and-deployment)
  * [EPIC - User Registration and Accounts](#epic---user-registration-and-accounts)
  * [EPIC - User Profile](#epic---user-profile)
  * [EPIC - Products and Products Management](#epic---products-and-products-management)
  * [EPIC - Product Wishlist](#epic---product-wishlist)
  * [EPIC - Purchase and Checkout](#epic---purchase-and-checkout)
  * [EPIC - Testimonials](#epic---testimonials)
  * [EPIC - SEO and Web Marketing](#epic---seo-and-web-marketing)
  * [EPIC - Error Handling and Message](#epic---error-handling-and-message)
  * [Kanban Board](#kanban-board)
* [The Skeleton Plane](#the-skeleton-plane)
  * [User Experience Design](#user-experience-design)
  * [Wireframes](#wireframes)
  * [Database Schema](#database-schema)
* [The Surface Plane](#the-surface-plane)
  * [Features](#features)
* [SEO and Web Marketing](#seo-and-web-marketing)
* [Technology Stack](#technology-stack)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)
* [Acknowledgements](#acknowledgements)

### The Strategy Plane

### Epics

There are 9 Epics:

1. Setup & Deployment #1
2. User Registration & Accounts #2
3. User Profile #3
4. Products and Products Management #4
5. Product Wishlist #5
6. Purchase and Checkout #6
7. Testimonials #7
8. SEO and Web Marketing #8
9. Error Handling and Message - #30

These nine epics were further developed into **twenty two (22) User Stories**, each with its **Acceptance Criteria** that consist of the requirements that must be met to mark the user story as Done. And for the technical work required to implement the User Stories, I created and assigned **Tasks**.

### EPIC - Setup and Deployment

#### User Story - Setup Project #9

* As a **Developer**, I want to **setup the Django project Environment**, so that **I can initialise the development environment and deploy early**

* Tasks:

  * Task 1 - Create GitHub repository to store project files online and clone to VSCode
  * Task 2 - Create User Project in GitHub to use Kanban feature to handle User Stories
  * Task 3 - Add our user stories in the issues tab
  * Task 4 - Create and activate Virtual Environment on local machine
  * Task 5 - Install Django
  * Task 6 - Create env file to hide sensitive data and include the file in a .gitignore file
  * Task 7 - Install pycodestyle for python style guide checking
  * Task 8 - Install pylint to check code errors and enforce coding standard
  * Task 9 - Install flake8-django to enforce PEP8 compliance specific to Django projects
  * Task 10 - Create a requirements.txt file to let heroku know which packages to install
  * Task 11 - Create the Django project
  * Task 12 - Create home app and add to installed apps in settings.py

#### User Story - Deployment #10

* As a Developer, I want to deploy the project to Heroku early, so that I will be sure the deployed site is working in production environment

* Tasks
  1. install the heroku CLI
  2. Install Django-allauth for account authentication, registration and management
  3. Install Pillow – for images
  4. install Stripe – for our payment solution
  5. Install gunicorn to act as web server
  6. Install django-crispy-forms to style forms
  7. Install Django-countries to provide country choices for forms
  8. Install dj_database_url and psycopg2 to connect to external database.
  9. Install boto3 and django-storages to connect Django to our S3.
  10. Create requirements file
  11. Create a new Heroku App
  12. Create a new database in ElephantSQL
  13. Copy the database URL from the database instance name for this project
  14. Set up a new AWS S3 bucket to securely store static files and images
  15. Add DATABASE_URL from ElephantSQL, Django Secret Key, AWS S3 bucket Access Key and Secret Access Key to Heroku Config Vars
  16. Set to deploy automatically to Heroku when Push to Github
  17. Add hostname of Heroku app to ALLOWED_HOSTS in settings.py
  18. Configure settings.py file to connect to the new ElephantSQL database, to access our AWS S3 bucket, and to point at the correct env.py file in development
  19. In settings.py, replace DEBUG with DEBUG = 'DEVELOPMENT' in os.environment
  20. Add the AWS S3 bucket details to the env.py file
  21. Create a Procfile for Heroku to create a web dyno to run gunicorn and serve our app
  22. Create a superuser for the new database
  
### EPIC - User Registration and Accounts 

#### User Story - Account Registration #11

* As a new User, I want to register by creating a username and password so that I can save my personal details and have access to featured products.

* Acceptance Criteria
  * **Acceptance Criteria 1:**\
   Given that I’m a new user\
   and I’m on the Sign-Up page\
   When I enter mandatory registration information (Email, Username, Password)\
   and I click the Sign-Up button\
   Then I can see a confirmation message that I have to verify my email address and I’m able to confirm my email address.

  * **Acceptance Criteria 2:**\
     Given that I’m a new user\
     and I’m confirmation page for users to confirm their email address\
     When I click the Confirm button to verify my email address\
     Then I can see a confirmation message that an account has been created for me successfully

  * **Acceptance Criteria 3:**\
     Given that I’m a user\
     and I’m on the Sign-Up page\
     When I enter my Email address or Username and Password\
     and I click the Sign-Up button\
     Then I am not registered and I can see an error message that a user is already registered with this e-mail address.

  * **Acceptance Criteria 4:**\
     Given that I’m a new user\
     and I’m on the Sign-Up page\
     When I enter my Email address, preferred Password, and Username that already exist and I click the Sign-Up button\
     Then I am not registered and I can see an error message that a user with that username already exists.

  * **Acceptance Criteria 5**\
     Given that I’m a new user\
     and I’m on the Sign-Up page with a social Login\
     When I click my social media account\
     Then I am logged into my account and I can see a confirmation message that the system signs me in.

* Tasks:
  1. Modify the accounts templates
  2. Create a base template and extend it in home template
  3. Create a link to a Sign-Up page
  4. Implement a method to validate the user registration data and to prevent multiple accounts creation with same username and email address.
  5. Implement a method to send confirmation email to new accounts.
  6. Create a confirmation page for users to confirm their email address
  7. Create a method to redirect the new user to the home page on successful registration.

#### User Story: Account Login #12

* As a registered User, I want to be able to sign in to my account so that I can have access to my personal profile.

* Acceptance Criteria
  * Acceptance Criteria 1:\
    Given that I’m a registered user\
    and I’m on the Sign-In page\
    When I enter my Email address or Username and Password\
    and I click the Sign-In button\
    Then I am logged in to my account so that I can access my personal account information and I can see a successfully signed in message.

  * Acceptance Criteria 2:\
    Given that I’m a registered user\
    and I’m on the Sign-In page\
    When I enter a wrong Email address or Username, or Password\
    and I click the Sign-In button\
    Then I am not logged in and I can see an error message that the e-mail address and/or password I specified are not correct.

  * Acceptance Criteria 3:\
    Given that I’m a registered user\
    and I’m on the Sign-In page\
    When I enter my login details and check “Remember Me” checkbox\
    and I click the Sign-In button\
    Then I am logged in and I can always have automatic access to my account from the same system until I manually sign out

  * Acceptance Criteria 4:
    Given that I’m a registered user
    and I’m on the Sign-In page
    When I click the “Forgot Password?” link
    Then I can reset my password if I’ve forgotten it or I want to update it for security reasons.

* Tasks:
  1. Create a link to a Sign-In page
  2. Create a Sign-In form for registered users to enter their login details
  3. Implement a method to validate the user data matches a user account
  4. Develop a method to highlight an error message in red color below the form field.
  5. Create a method to redirect the new user to the home page on successful sign in.
  6. Implement a method to send confirmation email to new accounts.
  7. Implement a “remember me” functionality on login page.
  8. Implement a method to reset password on login page.

#### User Story: Account Logout #13

* As a User, I want to be able log out of my account, so that I can keep my account secure

* Acceptance Criteria
  * Acceptance Criteria 1:\
    Given that I’m a registered user\
    and I’m logged into my account\
    When I click the logout link\
    Then I can see a visual confirmation page to confirm that I want to sign out.

  * Acceptance Criteria 2:\
    Given that I’m a registered user\
    and I’m on confirmation page to confirm that I want to sign out\
    When I click the sign out button to confirm I want to logout\
    Then I am logged out of my account and I can see a visual confirmation that I have been logged out.

* Tasks:
    Task 1 – Create a link to a Logout functionality
    Task 2 - Create a confirmation page for users to confirm they want to sign out.
    Task 3 - Create a method to redirect the user to the home page on successful sign out.

#### User Story - Social Media Login #14

* As a registered user, I want to sign up and login using my social account ID so that I can have a convenient alternative to login to my account

* Acceptance Criteria
  * Acceptance Criteria 1:\
    Given that I’m a new user\
    and I’m on the Sign-Up page with a social Login (Facebook, Google, Apple)\
    When I click my preferred social media account\
    Then I can sign up using my existing social account IDs so that I can access the application and I \can see a successfully signed in message.

  * Acceptance Criteria 2:\
    Given that I’m a registered user\
    and I’m on the Sign-Up page with a social Login (Facebook, Google, Apple)\
    When I click my preferred social media account\
    Then I am logged in using my existing social account IDs so that I can access my personal account\ information and I can see a successfully signed in message

* Tasks:
  1. Create a social Sign-Up feature for users to register with their social media accounts
  2. Create a method to redirect the new user to the home page on successful registration.
  3. Implement a method to send confirmation email to new accounts.

### EPIC - User Profile

#### User Story - My Account #15

* As a new User, I want to register by creating a username and password so that I can save my personal details and have access to featured products.

* Acceptance Criteria
  * Acceptance Criteria 1:\
    Given that I’m a logged in User\
    When I click my account and I click Account Information link\
    Then I can view my Personal Information.\

  * Acceptance Criteria 2:\
    Given that I’m a logged in User\
    When I click My Account and I click Account Information link\
    Then I can edit my Personal Information.

  * Acceptance Criteria 3:\
    Given that I’m a logged in User\
    and I’m on the Account Information page\
    When I select to Delete Account\
    and click to confirm\
    Then I can delete my Personal Information and close my account.

* Tasks:
    Task 1:Task 1 - Create a user profile page
    Task 2 - Create a method for users to view their Account Information.
    Task 3 - Create a method for users to update their Account Information.
    Task 4 - Create a method for users to delete their Account.
    Task 5 - Account deletion will require a second level confirmation to take effect

#### User Story: My Address #16

* As a User, I want to login to my personalized user profile, so that I can view Default Billing Address and Default Shipping Address.

* Acceptance Criteria
  * Acceptance Criteria 1:\
    Given that I’m a logged in User\
    When I click my account and I click My Address\
    Then I can view Default Billing Address and Default Shipping Address

  * Acceptance Criteria 2:\
    Given that I’m a logged in User\
    and I’m on my My Address page\
    When I click Change Default Billing Address\
    Then I can view and update my Default Delivery Information

  * Acceptance Criteria 3:\
    Given that I’m a logged in User\
    and I’m on my My Address page\
    When I click Default Shipping Address\
    Then I can view and update my Default Shipping Address

* Tasks:
  1. Create a method for users to view a record of their Default Delivery Information and Default Shipping Address.
  2. Implement a method for users to update their Default Billing Information
  3. Implement a method for users to update their Default Delivery Information

#### User Story: My Orders #17

* As a User, I want to login to my account, so that I can view My Orders

* Acceptance Criteria
  * Acceptance Criteria 1:\
   Given that I’m a logged in User\
   When I click my account and I click My Orders\
   Then I can view my order history.

  * Acceptance Criteria 2:\
      Given that I’m a logged in User\
      and I have items in my cart\
      When I click the checkout button\
      Then I have my Default Delivery Information ready to be used

* Tasks:
  1. Create a method for users to view a record of their order history.
  2. Implement a method for Default Billing Information to be prepopulated on checkout
  3. Implement a method for Default Delivery Information to be prepopulated on checkout

### EPIC - Products and Products Management 

#### User Story: View Products #18

* As a User, I want to view a list of products so that I can select the products to purchase.

* Acceptance Criteria
  * Acceptance Criteria 1:\
   Given that I’m a logged in User\
   and I am on the home page\
   When I click the Shop Now button\
   Then I can see a list of all products in the store.

  * Acceptance Criteria 2:\
      Given that I’m a logged in User\
      and I am on the products list page\
      When I click to view individual product details\
      Then I can identify the price, description, detailed reviews, and product image.

  * Acceptance Criteria 3:\
      Given that I’m a logged in User\
      and I am on the products list page\
      When I click a back-to-top button\
      Then I am taken back to the top of the product list without having to scroll through hundreds of products.

* Tasks:
  1. Create a page of a list of all products in the store.
  2. Create a method to view individual product details
  3. Implement a Back-to-top functionality in the products page

#### User Story – Sort and Search Product #19

* As a User, I want to sort and search products, so that I can quickly find the products I want to purchase.

* Acceptance Criteria
  * Acceptance Criteria 1:\
    Given that I’m a logged in User\
    and I am on the products list page\
    When I see a product sort select box\
    Then I can sort products by price, rating, name, or category.

  * Acceptance Criteria 2:\
   Given that I’m a User\
   When I select to view Products by Category\
   Then I will be able to choose any product I may want to buy.

  * Acceptance Criteria 3:\
   Given that I’m a User\
   When I can see the search bar at the top of the page in a visually distinguishable way\
   Then I can easily search for products from any page

  * Acceptance Criteria 4:\
   Given that I’m a User\
   When I can see the search bar at the top of the page in a visually distinguishable way\
   Then I can easily search for products from any page

* Tasks:
  1. Implement product sort selector box option on the products page
  2. Implement a method for user to sort product by name
  3. Implement a method for user to sort product by price
  4. Implement a method for user to sort product by rating
  5. Implement a method for user to sort product by category
  6. Implement search bar functionality that is visible to the user on every page
  7. Implement a method for user to Search for a product by name

#### User Story – Manage Products #20

* As a Superuser, I want to login to my user profile, so that I can manage all products in the store.

* Acceptance Criteria
  * Acceptance Criteria 1:\
   Given that I’m a logged in Superuser\
   When I click My Account\
   and I click Product Management\
   Then I can I can add a product to the store.

  * Acceptance Criteria 2:\
   Given that I’m a logged in Superuser\
   and I’m on Products page\
   When I click the edit link\
   and I click Product Management\
   Then I can edit the product.

  * Acceptance Criteria 3:\
   Given that I’m a logged in Superuser\
   and I’m on Products page\
   When I click the delete link\
   and, I click to confirm the deletion request\
   Then I can delete the product and redirected to all-products page.

* Tasks:
  1. Create a product form for store owner to add products in the store.
  2. Implement a method for store owner to edit products in the store
  3. Implement a method for store owner to delete products in the store
  4. Implement a method to secure the product management links

#### User Story: Product Images #21

* As a User, I want to view the product images from different angles and close-ups, so that I can visualize the product and determine whether it meets my expectation.

* Acceptance Criteria
  * **Acceptance Criteria 1:**\
   Given that I’m a User\
   When I view the list of products page\
   Then I can see a large image of the product.

  * **Acceptance Criteria 2:**\
   Given that I’m a User\
   and I’m on the list of products page\
   When I click on the image of a particular\
   Then I can see a larger image of the individual product that highlights the product.

  * **Acceptance Criteria 3:**\
   Given that I’m a User\
   When I view the list of products page\
   Then I can see a large image of the product.

  * **Acceptance Criteria 4:**\
   Given that I’m a User\
   and I’m on the list of products page\
   When I click on the image of a particular\
   Then I can see a larger image of the individual product that highlights the product.

* Tasks:
  1. Implement a method to add product images
  2. Implement a method to view product images

### EPIC - Product Wishlist

#### User Story - Wishlist #22

* As a User, I want to add products to my Wishlist, so that I can save items I would like to have.

* Acceptance Criteria:
  * Acceptance Criteria 1:\
     Given that I’m a logged in User\
     When I’m on Products page\
     Then I can add products to Wishlist.

  * Acceptance Criteria 2:\
     Given that I’m a logged in User\
     When I add products to my Wishlist\
     Then I can see the number of items on my Wishlist.

  * Acceptance Criteria 3:\
     Given that I’m a logged in User\
     and I have products in my cart\
     When I click the Add to Cart button\
     Then I can move the products from Wishlist to the cart ready for checkout

  * Acceptance Criteria 4:\
    Given that I’m a logged in User\
    When an item is on my Wishlist\
    Then I can delete the item if I’m no longer interested in it.

* Tasks:
  1. Create a Wish List capability
  2. Create a functionality to add products to Wishlist.
  3. Create a functionality to move products from Wishlist to the cart.
  4. Implement a functionality to track products in the Wishlist
  5. Develop a counter for number of Wishlist products added to shopping cart
  6. Create a functionality to delete items from Wishlist.

### EPIC - Purchase and Checkout

#### User Story - Purchase #23

* As a User, I want to be able to add multiple items to a shopping cart, so that I can buy the products I want.

* Acceptance Criteria:\
  * Acceptance Criteria 1:\
    Given that I’m a User\
    When I am on the product detail page\
    Then I have the option to add more than one individual item to the cart.

  * Acceptance Criteria 2:\
    Given that I’m a User\
    When I add a product to the shopping cart\
    Then I will know the total cost of my purchases before checkout.

  * Acceptance Criteria 3:\
    Given that I’m a User\
    When I’m on the shopping cart page\
    Then I can update or remove items on my shopping cart.

  * Acceptance Criteria 4:\
    Given that I’m a User\
    When I add a product to the shopping cart\
    Then I can checkout and buy the products I want.

* Tasks:
  1. Create a shopping cart page
  2. Develop functionality to add products to the shopping cart
  3. Develop functionality to calculate delivery cost
  4. Develop functionality to track products in the shopping cart
  5. Develop a counter for number of products added to shopping cart

#### User Story – Payment #24

* As a User, I want to enter my payment information so that I can pay for my purchases

* Acceptance Criteria:\
  * Acceptance Criteria 1:\
    Given that I am a user\
    When I am on the checkout page\
    Then I can enter my debit/credit card information on the payment form

  * Acceptance Criteria 2:\
    Given that I am a user\
    and I am on the checkout page\
    When I enter in an invalid card number\
    Then the card number turns red below the card field.

  * Acceptance Criteria 3:\
   Given that I am a user\
   When I enter my debit/credit card information click Complete Order button\
   Then my payment is processed.

* Tasks:
  1. Create a function to add stripe prebuilt credit card input to checkout form
  2. Develop functionality to validate a payment card number

#### User Story – Checkout #25

* As a User, I want to select a quantity of a product so that I can proceed to checkout to complete my order.

* Acceptance Criteria:
  * Acceptance Criteria 1:\
   Given that I’m an unregistered User\
   When I’m on the checkout page\
   Then I have the option to enter my payment and delivery details to complete my order.

  * Acceptance Criteria 2:\
    Given that I’m a User\
    When I’m on the checkout page\
    Then I have the option to save delivery information entered to my profile.

  * Acceptance Criteria 3:\
    Given that I’m a registered User\
    and I’m on the checkout page\
    When I enter my payment information\
    Then I can check out using my Delivery Information stored in the system

  * Acceptance Criteria 4:\
    Given that I’m a User\
    When I checkout to finalize purchase\
    Then I will see my Order confirmation page confirming a successful transaction.

  * Acceptance Criteria 5:\
    Given that I’m a User\
    When I checkout after making purchases\
    Then I will receive an Order confirmation email for my records.

* Tasks:
  1. Create a functionality on checkout page to save delivery information entered to profile
  2. Develop a functionality to generate an order number
  3. Create a functionality for Order confirmation page with order summary
  4. Create a functionality to send Order confirmation email
  5. Create a checkout link on shopping cart page
  
### EPIC - Testimonials

#### User Story – Testimonials #26

* As a User, I want to leave a testimonial about the store and its products so that I can provide feedback to store owner and other buyers.

* Acceptance Criteria:
  * Acceptance Criteria 1:\
   Given that I’m a logged in User\
   When I buy a product\
   Then I can write a testimonial about the store and product.

  * Acceptance Criteria 2:\
  Given that I’m a logged in User\
  When I leave a testimonial about the store and product\
  Then I can view my testimonial and testimonials by others.

  * Acceptance Criteria 3:\
  Given that I’m a logged in User\
  When I leave a testimonial about the store and product\
  Then I can edit my testimonial.

  * Acceptance Criteria 4:\
  Given that I’m a logged in User\
  When I leave a testimonial about the store and product\
  Then I can delete my testimonial.

* Tasks:
  1. Create a functionality that allows registered users to add testimonials.
  2. Create a functionality that allows users to view testimonials.
  3. Create a functionality that enable the author of a testimonial to edit it.
  4. Create a functionality that enable the author of a testimonial to delete it.

#### User Story – Ratings #27 (Won't Have)

* As a User, I want to Like or Unlike products so that I will leave my rating of the product quality.

* Acceptance Criteria:
  * Acceptance Criteria 1:\
  Given that I’m a logged in User\
  When I am impressed with the product I bought\
  Then I can click to Like the product to leave positive feedback.

  * Acceptance Criteria 2:\
   Given that I’m a logged in User\
   When I am not impressed with the quality of the product I bought\
   Then I can Dislike the product to leave negative feedback.

* Tasks:
  1. Create a functionality that allows users to rate products purchased.
  2. Create a functionality that enable users to Like products purchased.
  3. Create a functionality that enable users to Unlike products purchased.
  4. Develop functionality to allow users rate products they bought
  5. Develop a counter for number of products Likes and Dislikes

### EPIC - SEO and Web Marketing

#### User Story - Email and Social Media Marketing #28 (Should Have)

* As a Store Owner, I want to send direct marketing messages to customers so that I can to promote my products and increase sales.

* Acceptance Criteria:
  * Acceptance Criteria 1:\
  Given that I’m a store owner\
  When I create newsletter forms to collect customers email address\
  Then I can send direct marketing emails to promote my products

  * Acceptance Criteria 2:\
  Given that I’m a store owner\
  When I set up social media pages\
  Then I send direct marketing messages to followers

  * Acceptance Criteria 3:\
  Given that I’m a store owner\
  When I set up a contact page for customers to contact me\
  Then I can generate more leads through email communication

* Tasks:
  1. Task 1 - Create newsletter signups hosted by Mailchimp.
  2. Task 2 – Create Facebook, Instagram or Twitter pages to promote products
  3. Task 3 - Create contact page for direct contact from customers

#### User Story - Search Engine Optimization #29 (Must Have)

* As a Developer, I want to optimise my e-commerce website for Search Engine so that I can improve its search engine rankings.

* Acceptance Criteria:
  * Acceptance Criteria 1:\
  Given that I’m a Shop Owner\
  When I apply semantic HTML elements and descriptive meta tags in the HTML\
  Then search engines can rank my site highly enough to show up on their first page.

  * Acceptance Criteria 2:\
  Given that I’m a Shop Owner\
  When I create informed and trustworthy your web page content\
  Then Keywords will help users find my site for higher rankings in search engines.

* Tasks:
  1. Apply relevant keywords and descriptive meta tags in templates.
  2. Generate a sitemap.xml file for search engines.
  3. Create a robots.txt file to manage crawl budget
  4. Create a privacy policy statement page
  5. Create a terms of service page
  6. Create delivery and returns page
  7. Create refund policy page
  8. Create user guide page
  9. Create how to shop page

### **EPIC - Error Handling and Message**

#### USER STORY - Handle Errors and Notifications #31 (**Must Have**)

* As a Store Owner, I want to implement logics to handle errors and notifications, so that the site will reduce customer frustration and enhance user experience.

* Acceptance Criteria:
  * Acceptance Criteria 1:\
  Given that I’m a store owner\
  When I create 404 page to handle page not found error\
  Then user will use the link provided if a given page was not found

  * Acceptance Criteria 2:\
   Given that I’m a store owner\
   When I create 500 page to handle internal server error\
   Then user will know it was a system error and need to try again

  * Acceptance Criteria 3:\
  Given that I’m a store owner\
  When I set up bootstrap toast\
  Then I give users real-time notifications on their actions as they browse our store.

* Tasks:
  1. Create 404 page to handle page not found error
  2. Create 500 page to handle internal server error
  3. Implement alert messages to give feedback to the user

#### **Sprints**

These **9 EPICS** and **22 User stories** were then arranged into **Sprints**. I allocated a fixed period of one week per Sprint, within which the planned tasks and User Stories must be completed.

And within each Sprint, I prioritized the User Stories with the **MOSCOW technique**, widely adopted in the Agile community: 

1. **Must Have** - for non-negotiable PBIs that are guaranteed to be delivered.
2. **Should Have** - for important PBIs but not vital.
3. **Could Have** - for desirable items, but less crucial.
4. **Won’t Have** - my Agile team agreed that these PBIs won’t make it to the deployed solution.

The **Tasks** that were not completed had to be rescheduled and prioritized for the next Sprint (timebox):

1. The **My Orders** User Story could not be completed in **Sprint 2** due to the fact that the Checkout functionality in Sprint 3 has to be completed before a user can view their orders in their profile page. Hence my Orders had to be rescheduled for **Sprint 4**.
2. I was unable to implement **View Products, Sort and Search Product, Manage Products, and Product Images User Stories** within **Sprint 2** due to my database. I had to move them to **Sprint 3**.
3. The **Review User Stories** couldn’t not be completed in **Sprint 3** and had to rename as **Testimonial**, adjust the User Stories to fit its current purpose and rescheduled it for **Sprint 4**.

Below is how the sprints were organised:

#### **Sprint 1**:

* EPIC - Setup & Deployment
  * User Story: Setup Project **Must-Have**
  * User Story: Deployment **Must-Have**
* EPIC - User Registration & Accounts
  * Account Registration **Must-Have**
  * User Story: Account Login **Must-Have**
  * User Story: Account Logout **Must-Have**
  * User Story - Social Media Login **Won't-Have**

#### **Sprint 2:**

* User Profile
  * User Story: My Account **Should-Have**
  * User Story: My Address **Should-Have**

#### **Sprint 3:**

* Products and Management
  * User Story – Manage Products **Must-Have**
  * User Story: View Products **Must-Have**
  * User Story – Sort and Search Product **Must-Have**
  * User Story: Product Images **Must-Have**
* EPIC: Purchase and Checkout
  * User Story - Purchase **Must-Have**
  * User Story – Payment **Must-Have**
  * User Story – Checkout **Must-Have**

#### **Sprint 4:**

* EPIC: Testimonials
  * User Story – Testimonials **Should-Have**
  * User Story – Ratings **Won't-Have**
* EPIC: Product Wishlist
  * User Story - Wishlist **Should-Have**
* EPIC: Web Marketing Epic
  * User Story - Search Engine Optimization **Must-Have**
  * User Story - Email and Social Media Marketing **Should-Have**
  * User Story: My Orders **Should-Have**
  
#### **Sprint 5:**

* EPIC: Error Handling and Message
  * USER STORY - Handle Errors and Notifications **Must-Have**

### Kanban Board

![Kanban Board](/media/docs/img/kanban-board.webp)

## The Surface Plane

### Features

#### Homepage

#### Header

The header has two sections arranged horizontally. The top section has the logo, search box, and account-related menus that are arranged horizontally in order of priority of information and features. And the section below it contains mainly products-related menus and a contact page.

* **Logo**
  
  **Bessie + Beau logo** is simple and minimalist in representation with a watermark background. Also, the logo has an implicit link to the homepage, following a long-standing web convention and for fluid user experience.

  ![Bessie + Beau Logo](/media/bessie-beau.webp)

* **Product Search Box**  
  The **Product Search** box provides the functionality that allows Users to quickly search the site for different products by name or category.

* **Navigation Menus**
  * The navigation menus on the top section are Account, Wishlist (visible to logged in users only) and Shopping Cart menus. The account menu, for unanimous users, is a drop-down with a list of “Register” and to “Login” menus. But for logged in users, Account changes to the username of the user with a drop-down list of “My Account” and “Logout” menus. However, there is a third menu called Product Management, which is visible if the user is a superuser, in order words, a store owner or staff.
  
  * Header Navigation
  ![Header Navigation](/media/docs/img/features/navbar.webp)

  * Header Navigation - Logged in User View
  ![Header Navigation - Logged in User View](/media/docs/img/features/navbar-login-user.webp)

  * Header Navigation - SuperUser View
  ![Header Navigation - SuperUser View](/media/docs/img/features/navbar-superuser.webp)

  * The other section below it has Home, All Products category (a drop-down with a list of options to sort products by Price, Rating, Category, and All Products), Clothing (a drop-down with a list of options to sort products by categories: Dresses, Jeans, All Clothing), Shoes and Accessories (a drop-down with a list of options to sort products by categories: Shoes, Bags, Accessories, and All Shoes and Accessories), Beauty category (a drop-down with a list of options to sort products by categories: Makeup and Polish, Eyelashes and Lipsticks, and All Beauty), For Him  (a drop-down with a list of options to sort products by categories: Men Shirts, Mean Jeans, Men Shoes and Accessories, and All menus), Special Offers (a drop-down with a list of options to sort products by categories: Deals, Clearance, and All Specials), and Contact menus.

  * These Menu items let the reader to easily navigate the website without having to rely on the browser’s “forward” and “back” arrows as navigation substitutes. This Full responsive header is fixed and consistent across in all pages (plus the two “hidden” pages) of the website to allow for easy navigation and without the user having to rely on the browser’s “forward” and “back” arrows as navigation substitutes.

#### Hero Image

* The landing includes a hero image of a female model in an elegant dress, with a text overlay that tells boldly that the site is luxury fashion store for women and a Call to Action button that when clicked on the user is taken to the All Products page.
* Handling the hero images on the homepage, I use the picture element - a technique of changing “image displayed to suit different image display sizes.” I created 2 image files of different picture (same model) and sizes for different viewport widths: one serves viewport of 1024px wide or higher and landscape view larger tablets. And the other serves portrait-view mobile devices and small tablets.

Hero Image - Desktop View             |        Hero Image - Mobile View
:-------------------------:|:-------------------------:
![Hero Image Page - Desktop View](/media/docs/img/features/hero-image-desktop.webp)  |  ![Hero Image Page - Mobile View](/media/docs/img/features/hero-image-mobile-view.webp)

* I also use the WebP image formats to maintain both a low file size and high-quality of the hero images, and all other images on the website.

#### **Homepage Main Section**

* The main section introduces the user/customer to the relevant sections of the store, and takes a progressive disclosure approach by revealing to the user the different categories of the store items and encouraging them to go further beyond the homepage to create fluid user experience.
* This main section is structured in such a way that it enables the visitor on the website to immediately ascertain what Bessie Beau is a high-end fashion store, and more importantly, let the user easily access the information that interest them and also encourage the user to want to view more products, and possibly buy them.
* The main section is split into five areas: Women Clothing, Beauty spotlight, Women Accessories, Men fashion, and Testimonials

  ![Homepage Main Section](/media/docs/img/features/homepage-main-section.webp)

#### **The Testimonials page**

* This **Testimonials** app is the first of the three custom models critical to this project.

* Customer testimonials feature is about the success story of Bessie + Beau. The testimonials allow our customers to know more about our products and service and our store as a successful e-commerce business.

* The testimonial is implemented with different levels of permission:
  * **Customer Testimonials - Non-Logged in User View**
  ![Testimonials - Non-Logged in User View](/media/docs/img/features/testimonial-users-view.webp)

  * All non-login users can view the testimonial page. They can also see the add testimonial link. However, the edit and delete testimonial buttons are not visible to them. And while they can see the add testimonial link, they do not have the permission to access the add testimonial form page. So, a non-logged in user must login first to be able to add testimonial. And when this non-login users attempt to access the page by clicking the “Add Testimonial” link, the user will be directed to the account login page to login or signup first.

  * **Customer Testimonials - Login User View**
    ![Testimonials - Logged in User View](/media/docs/img/features/testimonials-loginuser-view.webp)

  * All logged in user can see the **edit** and **delete testimonial** buttons on the testimonial page.
  * The registered users, who has the permission to edit or delete the testimonial, are required to login first to be able to do so.
  * Only the authors can edit their testimonial. But they cannot delete their testimonial.
  * Only the Store owner can delete a testimonial from both the frontend and backend.

**Future Enhancement:**
  
* At the moment, the functional implementation of this testimonial app only provides the customers a way to add testimonials for the store. In the next iteration, this functionality would be extended to include adding reviews and ratings for products, and these reviews would then be used strategically as customer testimonials along with the ratings.

### **Footer**

![Footer](/media/docs/img/features/footer.webp)

* The footer is divided into two major sections that run horizontally on desktop device, but vertically on mobile device:

* The first section holds the Social networks, with links to the store's three relevant social media accounts: Facebook, Instagram, and Twitter. The social networks links communicate with users and encourage them to keep connected with Bessie Beau via social media. The links will open to a new tab to allow easy navigation for the user. It is carefully placed above for visibility, as social media is critical for e-commerce for brand awareness building, product sells, and extension of customer support.

* The second section is divided into four subsections. These four subsections are arranged horizontally on desktop and vertically when viewed on mobile devices.
  * The first sub-section is a newsletter sign-up form that allows and encourages the user to subscribe to receive information related to Bessie Beau’s products and services. To keep it simple and encouraging, the user is required to submit email address only. The newsletter signup functionality was provided by Mailchimp.
  * The second and third sub-sections contain the Customer services information on the policies of the store and how a customer can make purchases on Bessie + Beau. While the fourth sub-section is the copyright information.
* The footer, like the header, is consistent across the pages for easy navigation and intuitive experience.

#### **Contact Page**

![Contact](/media/docs/img/features/contact-us.webp)
This **Contact** is the second of the three custom models critical to this project.

The contact form is kept simple and clear without much information being requested from the user; only the name, email address, subject, and message. This is to encourage the user to get in touch with Bessie + Beau for questions on our products and any other issues. Its functional implementation enables the user to send direct email to the store owner and to also receive an acknowledgment directly in their designated email address.

#### Register Page

Account menu has a drop-down list of Register and Login that is visible to a new and non-logged in user. And the new user can click the register menu to sign up to the site. To register, users are required to enter their email address, username, and password. The email address and password have two-pass verification, which means that the user-registrants are required to confirm each of both entries by entering them a second time. This is to make sure they are entered correctly. All signup form fields are required. Users must fill them and correctly too to be able to complete the registration. The signup form uses an Allauth authentication system to verify these entries. And below these fields are a cancel button in case the new user no longer wants to proceed with the registration and a signup button the user has to click on to proceed with the registration.

![Register](/media/docs/img/features/register.webp)

On submission, a verification email and a link are sent directly to the user’s email address for the user to confirm that they provided the email address and still want to register an account on Bessie + Beau with the email address. When the uses clicks on the provided link, they are directed to a confirmation page.

Clicking the Confirm button finalises the registration process as done. Thereafter, confirmed users can login to their account using their verified email address or username and the password provided on registration.

#### **Login**

![Login Page](/media/docs/img/features/login.webp)

Account menu has a drop-down list of Register and Login that is visible to a new and non-logged in user. The login page allows a registered user to gain access to their Bessie + Beau account.  To be able to login, users must enter their verified email address or username and password provided during registration.

The Login form uses an Allauth authentication system to verify these entries and secure login process. And below these fields are a cancel button in case the registered user no longer wants to login at that time and a login button the user has to click on to submit their information to the authentication server. And if there is a match, the system will authenticate users and grant them access to their accounts.

The login page also has a Forgot Password link that users can click on to reset their password in case they have forgotten it or they simply want a new password for security reason. The login page also has a Remember me checkbox option to reduce how often users log in with two-factor authentication on the same system.

#### Logout

![Logout](/media/docs/img/features/logout.webp)

When the user clicks on the logout page they are directed to a confirmation page, where they can either cancel or continue to log out.

Account menu has a drop-down list of My Account and Logout that is visible to a logged in user. The login user can click the logout menu to sign out of their account.

However, the logout has a second level confirmation system. Clicking on the logout redirects the user to a logout confirmation page. The user has to confirm by clicking the signout completely sign out from the account.  

The Logout form and logout confirmation pages uses an Allauth authentication system.

### Products

* **All Products - User's View**

![All Products](/media/docs/img/features/products-users-view.webp)

The products page displays all the products on sale at Bessie + Beau. It is accessed from the call-to-action Shop Now button on the hero image homepage.

The product page can also be accessed using All Products drop-down menu on the navigation bar. On the navigation bar, Users may also choose to filter products by a specific subcategory from the main categories drop-down. Clothing category, for example, has a dropdown Dresses, Jeans, and All Clothing menus. The products subcategory page has a link to return to the All Products page, a count on number of products in the subcategory on the left hand side and a sort selector box on the right hand side.

![Filter Products by a Subcategory](/media/docs/img/features/product-subcategory-page.webp)

The total number of all the products are displayed at the top right side of the product page. And on the far right hand side is a sort selector box with sorting functionality. To enhance user experience, a user can sort all the products displayed by Price (low to high or high to low), by Rating (low to high or high to low), by Name (A-Z or Z-A), or by Category (A-Z or Z-A).

* **All Products - Superuser's View**
![Products SuperUser View](/media/docs/img/features/products-superuser-views.webp)

Superusers has a different view of the Products from other users. They can see the Edit and Delete buttons and have the permission to edit or delete any products in the store.  

When a user clicks on any of the displayed product, they are taken to the product details page of that specific product to continue with their purchase.

![Products Delete Confirmation](/media/docs/img/features/product-delete-confirmation.webp)

### Product Details

![Product Details](/media/docs/img/features/product-detail.webp)

Product detail page presents the details specific to a given product. The individual Product image is displayed on the left side of the product details area and on the right side are product name, price, labels, rating, product description, a size selector for a product with sizes, quantity selectors to increase and decrease product quantity, Add to Cart, Keep Shopping, and Add to Wishlist buttons. Here a customer can select the quantity of the product to purchase using the displayed quantity selector box, add product to shopping cart by clicking the displayed Add to cart button, or add the product to wishlist to buy later using the Add to wishlist button functionality. There is “keep shopping” button that when click on will return the user to the all product page to continue viewing products.

The superuser also has a different view of the Product details from other users. They can see the Edit and Delete product buttons and have the permission to edit or delete this specific product.  

### Product Wishlist

![Product Wishlist](/media/docs/img/features/products-wishlist.webp)

**Product wishlist** is the third of the three custom models critical to this project.

We can think of a Wishlist as a function of the store, or a function that is part of the user experience. My approach is to put the Wishlist functionality in the Profile app because in Account/Profile we have the dashboard, and the account has to do with user logging in and out and interacting with our application, and this is an important part of user experience. The Wishlist button is on the navbar and visible across the pages for a login user. It is also in the product detail page, and on clicked by non login users, they are directed to login page to either login or first register. A login user can add to Wishlist and remove Wishlist.

A user can view and remove product in wishlist. To view the wishlist, you click the view product button, which takes you to the product detail page. To remove the product from your wishlist, you click the Remove button and the product is removed from your wishlist. A wishlist page without a wishlist item automatically returns “Your wishlist is empty” message.

I’m terms of add product to wish list, we consider the option of delete a product being added if it was already on the wishlist. And the alternative option of allowing the user to add more than one same item to the wishlist. Functionally, I chose and implement the option that allows a user to add same item more than once. The particular goal was to demonstrate the calculation of number of items and total price.

### Add to Cart

![Add to Cart](/media/docs/img/features/add-to-cart.webp)

The Add to Cart is a cart icon on the far right of the navigation bar. When a user adds an item to the cart, the cart icon changes from black to blue colour as an indicator that the item has been added to the shopping cart successfully.

The shopping cart is divided into columns: the product information (image, name, price, quantity, and grant total if there are more than one item), Free delivery offer information that intends to entice the shopper to spend more to avail the free delivery offer if they are below the threshold, a Keep Shopping button incase they are not done shopping yet, and a secure Checkout button that will take them to the Checkout page.

### Shopping Cart

![Shopping Cart](/media/docs/img/features/shopping-cart.webp)

When users add click Go to the Shopping Cart button, they are directed to the Shopping Cart page. Here the user can update the product by increasing or decreasing the product quantity or they may choose to remove products entirely before proceeding to the checkout.

### **Secure Checkout**

![Secure Checkout](/media/docs/img/features/secure-checkout.webp)

When users click on Secure Checkout button on the Shopping Cart page, they are directed to this checkout page. The Checkout page is divided into two columns, sitting side by side.

The left hand side column contains fields for customers personal information such as Full name and Email address, Delivery information such as Phone number and Address, Payment method, and two buttons, one to complete the order and the other button to adjust shopping cart in case the user wants to add more items or remove from the cart. For registered login user the form is pre-filled with their default delivery information for them to fill in other required personal information and their credit or debit card details. For anonymous users, there is a create an account or login to save the information filled into the form.

The form uses Stripe prebuilt credit card input to collect card details: card number, expiry date, and CVC. The stripe payment system is not fully activated and the purchase can only be made with this test card information:

* Card Number - **4242 4242 4242 4242**
* MM/YY - **2424**
* CVC - **424**

The right hand side column holds the summary of the order information. This is necessary so that the Shopper can take another look at the order to ensure they have the right order and correct order information before making purchase. 

### Order Confirmation

![Order Confirmation](/media/docs/img/features/order-confirmation.webp)

When users successfully complete their purchase, an Order Confirmation Email is sent directly to their registered email. The email has a subject: Bessie + Beau Confirmation for Order Number, and a message body of the Order information, which is essentially the Order number, order date, order total, delivery costs, and grand total. This functionality is implemented to be triggered by a webhook from Stripe payment.

### **User Profile**

![User Profile](/media/docs/img/features/profile-page.webp)

The user profile holds information associated with a user such as account information, portrait photograph and order history.

* Functional implementation:
  * Users can only access their profile when they login.
  * Only the creator of a user profile can access and edit profile details.
  * Users can upload their image to their profile.
  * Users can view a record of their product wishlist and order history.
  * The profile provides users a place to save default delivery information 
  * Users can delete their profile.

### Product Management

![Product Management](/media/docs/img/features/product-management.webp)

The **Product Management** page is one of the menus in the drop-down Account menu, and it is visible to the superuser/store owner only. The product management page is where the superuser/store owner can add products to the store as alternative to using the admin page. It contains all the necessary fields including the image field to add a product.

### 404 page

![404 page](/media/docs/img/features/404.webp)

404 error page lets the users know that there is an error with their request. This error might be as a result of typing in an incorrect URL, the page is temporarily unavailable, or no longer exists. The 404 page provides helpful links the user may want to click on that will take them to products and home pages.

Error page can harm SEO because too many broken links will make it difficult for search engines to crawl the site. So this effective custom 404 page is important to SEO because it prevents showing broken links and encourages users to further explore Bessie + Beau website and help them find what they are looking for, thereby enhancing user experience by turning potential negative user experience of encountering an error into a positive one.

### 500 page

![500 page](/static/docs/img/features/500-page.webp)

A 500 error code, like the 404 error, creates poor user experience for shoppers because they are unable to access the page they are looking for. It also has negative effect on SEO, as this might prevent search engine crawlers from access the website.

500 page let the users know that the server encountered an unexpected condition that prevented it from fulfilling their request. It then provides helpful links that the user may want to click on that will take them to products and home pages, thereby improving user experience.
