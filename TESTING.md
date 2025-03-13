![Mockup](static/images/amiresponsivemp4.jpg)

# TABLE OF CONTENT

1. [ Manual Testing ](#manual)
2. [ Automated Testing ](#auto)
3. [ Bugs and Fixes ](#bugs)

# MANUAL TESTING <a name="manual"></a>

### Testing Responsiveness

<details>

| **Feature** | **Test Method** | **Expectation** | **Outcome** |
|-------------|-----------------|-----------------|-------------|
| Header Responsivness | Developer Tools: 320px/375px/425px/768px/1024px/1440px | Fully Responsive Layout | PASS |
| Footer Responsiveness | Developer Tools: 320px/375px/425px/768px/1024px/1440px | Fully Responsive Layout| PASS |
| Home Page | Developer Tools: 320px/375px/425px/768px/1024px/1440px | Fully Responsive Layout| PASS |
| Portfolio Page | Developer Tools: 320px/375px/425px/768px/1024px/1440px | Fully Responsive Layout| PASS |
| Service Page | Developer Tools: 320px/375px/425px/768px/1024px/1440px | Fully Responsive Layout| PASS |
| Contact Page | Developer Tools: 320px/375px/425px/768px/1024px/1440px | Fully Responsive Layout| PASS |
| Service_details Page | Developer Tools: 320px/375px/425px/768px/1024px/1440px | Fully Responsive Layout| PASS |
| Bag Page | Developer Tools: 320px/375px/425px/768px/1024px/1440px | Fully Responsive Layout| PASS | 
| Checkout Page | Developer Tools: 320px/375px/425px/768px/1024px/1440px | Fully Responsive Layout| PASS | 
| Checkout_success | Developer Tools: 320px/375px/425px/768px/1024px/1440px | Fully Responsive Layout| PASS | 
| Profile Page | Developer Tools: 320px/375px/425px/768px/1024px/1440px | Fully Responsive Layout| PASS | 
| Project Page | Developer Tools: 320px/375px/425px/768px/1024px/1440px | Fully Responsive Layout| PASS | 
| About Page | Developer Tools: 320px/375px/425px/768px/1024px/1440px | Fully Responsive Layout| PASS |
| Tech Page | Developer Tools: 320px/375px/425px/768px/1024px/1440px | Fully Responsive Layout| PASS | 

</details>

### Testing Functionality of Buttons/Links

<details>

| **Feature** | **Test Method** | **Expectation** | **Outcome** |
|-------------|-----------------|-----------------|-------------|
| Navigation Links - Home | Click on link | Route to relevent page | PASS |
| Navigation Links - Portfolio | Click on link | Route to relevent page | PASS |
| Navigation Links - Services | Click on link | Route to relevent page | PASS |
| Navigation Links - Contact | Click on link | Route to relevent page | PASS |
| Navigation Links - Accounts | Click on link/icon | Route to relevent page | PASS |
| Navigation Links - Shopping Bag | Click on link/icon | Route to relevent page | PASS |
| Accounts Link/Icon suboption - MyProfile | Click on link | Route to relevent page | PASS |
| Accounts Link/Icon suboption - Login | Click on link | Route to relevent page | PASS |
| Accounts Link/Icon suboption - Logout | Click on link | Route to relevent page | PASS |
| Accounts Link/Icon suboption - Register | Click each link | Route to relevent page | PASS |
| Home - Services | Click on link | Route to relevent page | PASS |
| Home - Portfolio | Click on link | Route to relevent page | PASS |
| Home - Contact | Click on link | Route to relevent page | PASS |
| Portfolio - Project | Click on link | Route to relevent page | PASS |
| Portfolio - About | Click on link | Route to relevent page | PASS |
| Portfolio - Tech | Click on link | Route to relevent page | PASS |
| Service - Each uploaded image | Click on each uploaded Service | Take to service_details | PASS |
| Service_details - Image | Click on Service image | open image in new tab | PASS |
| Service - back | Click on button | Take back to services | PASS |
| Service - add to bag | Click on button | add item to shopping cart | PASS |
| Projects - view repo | Click on button | take to relevent github repo | PASS |
| Projects - view project | Click on button | take to live project website | PASS |
| Projects - comments | Click on button | expand div to display comments | PASS |
| Projects - edit | Click on button | edit an existing comment | PASS |*
| Projects - delete | Click on button | delete comment | PASS |
| Projects - post comment | Click on button | content written in form is posted as comment | PASS |
| About - email link | Click on link | open up blank email addressed to my e-mail | PASS |
| About - linkedin link | Click on link | open up LinkedIn | PASS |
| Bag - keep shopping | Click on button | back to services | PASS |
| Bag - secure checkout | Click on button | proceed to checkout | PASS |
| Bag - decrease quantity button | Click on button | decrease amount displayed | PASS |
| Bag - increase quantity | Click on button | increase amount displayed | PASS |
| Bag - update | Click on button | update quantity, total | PASS |
| Bag - remove | Click on button | remove item from shopping cart | PASS |
| Checkout - adjust bag | Click on button | take back to shopping cart | PASS |
| Checkout - complete order | Click on button | process payment provided form validation passed | PASS |
| Footer - email | clcik on e-mail address | open email , ready to be sent to addresee | PASS |
| Footer - icons | click on each icon | open it in new tab | PASS |
| Footer - CV | click on download icon | download CV | PASS |


-*: edit button dosen't automatically takes the user back to the comment, however feature is functonal - listed for future upgrade
</details>


### Form Validation testing

<details>

| **Feature** | **Test Method** | **Expectation** | **Outcome** |
|-------------|-----------------|-----------------|-------------|
| Contact Form | Enter invalid input: No Title | No submission allowed - "Please fill in this field response" | PASS |
| Contact Form | Enter invalid input: No Content | No submission allowed - "Please fill in this field response" | PASS |
| Contact Form | Enter valid input | Submission allowed - "confirmation feedback" | PASS |
| Service_details - quantity input | click decrease/increase to reach 0/100 | no change in input | PASS |
| Service_details - quantity manual input | Enter invalid input | quantity autoatically adjusted to an accepted value | PASS |
| bag.html - quantity input | click decrease/increase to reach 0/100 | no change in input | PASS |
| bag.html - quantity manual input | Enter invalid input | quantity autoatically adjusted to an accepted value | PASS |
| Checkout.html Form | No input in fields/test them all individually | No submission allowed - "Please fill in this field response" | PASS |
| Checkout.html Card | no input | No submission allowed - "Your card number is incomplete" | PASS |
| Checkout.html Card | no date input | No submission allowed - "Your expiry date is incomplete" | PASS |
| Checkout.html Card | no security code input | No submission allowed - "Your security code is incomplete" | PASS |
| Checkout.html Card | no post code input | No submission allowed - "Your postal code is incomplete" | PASS |

</details>

### Browser Testing

<details>

| **Feature** | **Test Method** | **Expectation** | **Outcome** |
|-------------|-----------------|-----------------|-------------|
| Google Chrome | non scripted test of features on desktop | full functionality and compatibility with browser | PASS |
| Google Chrome | non scripted test of features on mobile | full functionality and compatibility with browser | PASS |
| Microsoft Edge | non scripted test of features on desktop | full functionality and compatibility with browser | PASS |
| Microsoft Edge | non scripted test of features on mobile | full functionality and compatibility with browser | PASS |
| Samsung Internet | non scripted test of features on mobile | full functionality and compatibility with browser | PASS |

</details>

# AUTOMATED TESTING <a name="auto"></a>

### HTML,CSS and JS validation

W3C validators used for HTML and CSS and JsHint is used to validate JAvaScript.

#### HTML VALIDATION:    
    
-   <details> <summary> index.html </summary>
    <img src="static/images/readme_images/html_validation/home_html.jpg">
    </details>

-   <details> <summary> portfolio.html </summary>
    <img src="static/images/readme_images/html_validation/portfolio_html.jpg">
    </details>

-   <details> <summary> tech.html </summary>
    
    Section element was replaced with div to clear warning.

    <details> <summary> Warning </summary>
    <img src="static/images/readme_images/html_validation/tech_warning_html.jpg">
    </details>

    <details> <summary> Fixed </summary>
    <img src="static/images/readme_images/html_validation/tech_fixed_html.jpg">
    </details>

    </details>

-   <details> <summary> about.html </summary>
    <img src="static/images/readme_images/html_validation/about_html.jpg">
    </details>

-   <details> <summary> project.html </summary>
    <img src="static/images/readme_images/html_validation/project_html.jpg">
    </details>

-   <details> <summary> contact.html </summary>
    <img src="static/images/readme_images/html_validation/contact_html.jpg">
    </details>

-   <details> <summary> service.html </summary>
    <img src="static/images/readme_images/html_validation/services_html.jpg">
    </details>

-   <details> <summary> service_details.html </summary>
    
    Service-btn id removed and replaced with class on relevent elements.

    <details> <summary> Error </summary>
    <img src="static/images/readme_images/html_validation/service_details_error_html.jpg">
    </details>

    <details> <summary> Fixed </summary>
    <img src="static/images/readme_images/html_validation/service_details_fixed_html.jpg">
    </details>

    </details>

-   <details> <summary> bag.html </summary>
    <img src="static/images/readme_images/html_validation/bag_html.jpg">
    </details>

-   <details> <summary> checkout.html </summary>
    <img src="static/images/readme_images/html_validation/checkout_html.jpg">
    </details>

-   <details> <summary> checkout_success.html </summary>
    <img src="static/images/readme_images/html_validation/checkout_success_html.jpg">
    </details>

-   <details> <summary> profile.html </summary>
    
    Error was due to the need of authentication prevent the validator from fetching the data. Used direct input to go around this problem.

    <details> <summary> Error </summary>
    <img src="static/images/readme_images/html_validation/profile_error_html.jpg">
    </details>

    <details> <summary> Fixed </summary>
    <img src="static/images/readme_images/html_validation/profile_directinput_html.jpg">
    </details>

    </details>


#### CSS VALIDATION: 
    
-   <details> <summary> base.css </summary>
    <img src="static/images/readme_images/validation/basecss.jpg">
    </details>

-   <details> <summary> checkout.css </summary>
    <img src="static/images/readme_images/validation/checkoutcss.jpg">
    </details>

#### JavaScript VALIDATION: 

-   <details> <summary> base.html </summary>
    <img src="static/images/readme_images/validation/base.html_jshint.jpg">
    </details>

    1. JSHint does not inherently know about Bootstrap, so it assumes bootstrap is an undeclared variable.

-   <details> <summary> base.js </summary>
    <img src="static/images/readme_images/validation/base.js_jshint.jpg">
    </details>

-   <details> <summary> quantity_input_script.html </summary>
    <img src="static/images/readme_images/validation/quantity_input_jshint.jpg">
    </details>

-   <details> <summary> quantity_input_script.html / additional js added to handle manual inputs </summary>
    <img src="static/images/readme_images/validation/quantity_additional_jshint.jpg">
    </details>

-   <details> <summary> project.html </summary>
    <img src="static/images/readme_images/validation/project.html_jshint.jpg">
    </details>

-   <details> <summary> stripe_elements.js </summary>
    <img src="static/images/readme_images/validation/stripe_elements.js_jshint.jpg">
    </details>

    1. Stripe JS Library link is included in base.html

-   <details> <summary> bag.html </summary>
    <img src="static/images/readme_images/validation/bag.html_jshint.jpg">
    </details>
    

#### PEP8 , python validation:

Common issues were rectified in each file before validation:
    1. line too long  -  no line should exceed 79 characters, adhering to PEP8.
        - there are a few exception , where issue was kept to maintain readability of the code and to avoid introducing errors.
    2. no new line at the end of the file
    2. trailing whitespace

Unexpected errors:
    1. had to redo line 38 at checkout, models.py as splitting the row to comply with pep8 caused the tests to fail.
    - no further investigation took place at this time as pep8 error had no immediate effect on the overall project.

-   <details> <summary> SERVICES APP </summary>
    
    <details> <summary> Model </summary>
    <img src="static/images/readme_images/pep8/service_model.jpg">
    </details>

    <details> <summary> View </summary>
    <img src="static/images/readme_images/pep8/service_view.jpg">
    </details>

    <details> <summary> Urls </summary>
    <img src="static/images/readme_images/pep8/service_urls.jpg">
    </details>

    <details> <summary> Tests </summary>
    <img src="static/images/readme_images/pep8/service_tests.jpg">
    </details>

    </details>

-   <details> <summary> PROFILES APP </summary>
    
    <details> <summary> Model </summary>
    <img src="static/images/readme_images/pep8/profiles_model.jpg">
    </details>

    <details> <summary> View </summary>
    <img src="static/images/readme_images/pep8/profiles_view.jpg">
    </details>

    <details> <summary> Urls </summary>
    <img src="static/images/readme_images/pep8/profiles_urls.jpg">
    </details>

    <details> <summary> Tests </summary>
    <img src="static/images/readme_images/pep8/profiles_test.jpg">
    </details>

    <details> <summary> TestForms </summary>
    <img src="static/images/readme_images/pep8/profiles_test_forms.jpg">
    </details>

    <details> <summary> Forms </summary>
    <img src="static/images/readme_images/pep8/profiles_form.jpg">
    </details>

    </details>

-   <details> <summary> PORTFOLIO APP </summary>
    
    <details> <summary> Model </summary>
    <img src="static/images/readme_images/pep8/portfolio_model.jpg">
    </details>

    <details> <summary> View </summary>
    <img src="static/images/readme_images/pep8/portfolio_views.jpg">
    </details>

    <details> <summary> Urls </summary>
    <img src="static/images/readme_images/pep8/portfolio_urls.jpg">
    </details>

    <details> <summary> Tests </summary>
    <img src="static/images/readme_images/pep8/portfolio_tests.jpg">
    </details>

    </details>

-   <details> <summary> HOME APP </summary>

    <details> <summary> View </summary>
    <img src="static/images/readme_images/pep8/home_views.jpg">
    </details>

    <details> <summary> Urls </summary>
    <img src="static/images/readme_images/pep8/home_urls.jpg">
    </details>

    <details> <summary> Tests </summary>
    <img src="static/images/readme_images/pep8/home_tests.jpg">
    </details>

    </details>

-   <details> <summary> CONTACT APP </summary>
    
    <details> <summary> Model </summary>
    <img src="static/images/readme_images/pep8/contact_model.jpg">
    </details>

    <details> <summary> View </summary>
    <img src="static/images/readme_images/pep8/contact_views.jpg">
    </details>

    <details> <summary> Urls </summary>
    <img src="static/images/readme_images/pep8/contact_urls.jpg">
    </details>

    <details> <summary> Tests </summary>
    <img src="static/images/readme_images/pep8/contact_tests.jpg">
    </details>

    <details> <summary> TestForms </summary>
    <img src="static/images/readme_images/pep8/contact_test_form.jpg">
    </details>

    <details> <summary> Form </summary>
    <img src="static/images/readme_images/pep8/contact_form.jpg">
    </details>

    </details>

-   <details> <summary> COMMENTS APP </summary>
    
    <details> <summary> Model </summary>
    <img src="static/images/readme_images/pep8/comment_model.jpg">
    </details>

    <details> <summary> Urls </summary>
    <img src="static/images/readme_images/pep8/comment_urls.jpg">
    </details>

    <details> <summary> Tests </summary>
    <img src="static/images/readme_images/pep8/comment_tests.jpg">
    </details>

    <details> <summary> TestForms </summary>
    <img src="static/images/readme_images/pep8/comment_test_forms.jpg">
    </details>

    <details> <summary> Form </summary>
    <img src="static/images/readme_images/pep8/comment_form.jpg">
    </details>

    </details>

-   <details> <summary> CHECKOUT APP </summary>
    
    <details> <summary> Model </summary>
    <img src="static/images/readme_images/pep8/checkout_models.jpg">
    </details>

    <details> <summary> View </summary>
    <img src="static/images/readme_images/pep8/checkout_views.jpg">
    </details>

    <details> <summary> Urls </summary>
    <img src="static/images/readme_images/pep8/checkout_urls.jpg">
    </details>

    <details> <summary> Tests </summary>
    <img src="static/images/readme_images/pep8/checkout_tests.jpg">
    </details>

    <details> <summary> TestForms </summary>
    <img src="static/images/readme_images/pep8/checkout_test_forms.jpg">
    </details>

    <details> <summary> Form </summary>
    <img src="static/images/readme_images/pep8/checkout_forms.jpg">
    </details>

    <details> <summary> Signals </summary>
    <img src="static/images/readme_images/pep8/checkout_signals.jpg">
    </details>

    <details> <summary> Webhooks </summary>
    <img src="static/images/readme_images/pep8/checkout_webhooks.jpg">
    </details>

    </details>

-   <details> <summary> BAG APP </summary>
    
    <details> <summary> View </summary>
    <img src="static/images/readme_images/pep8/bag_views.jpg">
    </details>

    <details> <summary> Urls </summary>
    <img src="static/images/readme_images/pep8/bag_urls.jpg">
    </details>

    <details> <summary> Tests </summary>
    <img src="static/images/readme_images/pep8/bag_tests.jpg">
    </details>

    <details> <summary> Context </summary>
    <img src="static/images/readme_images/pep8/bag_context.jpg">
    </details>

    </details>


## Lighthouse 

    Initial test result were a lot lower than expected. There is a general mid-range, 78% score on best practises accross the site ,mainly due to third party (Stripe) cookies.
    I decided not to address this for the time being as Stripe functionality is key and priority in this project.

    Accessibility scores 100% in most, above 90% for the rest but 1 page. bag.html flags no alt attributes and no accessible names, however upon changing these the warnings did persist and therefore this will need to be investigated further.

    Performance is generally good accross the site with some pages falling in the needs improvement range( 50% - 89% ). I have coverted most images to increase performance from jpeg to webp. Also, included rel=preload and fetchpriority=high links at the <head> for css files and profile image. This had some improvement ,however a few of the site's pages still flaging the issue and needs looking into it more in depth.

-   <details> <summary> All lighthouse testing  </summary>
    
    <details> <summary> home </summary>
    <img src="static/images/readme_images/lighthouse/home_lighthouse.jpg">
    </details>

    <details> <summary> portfolio </summary>
    <img src="static/images/readme_images/lighthouse/portfolio_lighthouse.jpg">
    </details>

    <details> <summary> project </summary>
    <img src="static/images/readme_images/lighthouse/project_lighthouse.jpg">
    </details>

    <details> <summary> about </summary>
    <img src="static/images/readme_images/lighthouse/about_lighthouse.jpg">
    </details>

    <details> <summary> tech </summary>
    <img src="static/images/readme_images/lighthouse/tech_lighthouse.jpg">
    </details>

    <details> <summary> contact </summary>
    <img src="static/images/readme_images/lighthouse/contact_lighthouse.jpg">
    </details>

    <details> <summary> service </summary>
    <img src="static/images/readme_images/lighthouse/service_lighthouse.jpg">
    </details>

    <details> <summary> service_details </summary>
    <img src="static/images/readme_images/lighthouse/service_details_lighthouse.jpg">
    </details>

    <details> <summary> bag </summary>
    <img src="static/images/readme_images/lighthouse/bag_lighthouse.jpg">
    </details>

    <details> <summary> checkout </summary>
    <img src="static/images/readme_images/lighthouse/checkout_lighthouse.jpg">
    </details>

    <details> <summary> checkout_success </summary>
    <img src="static/images/readme_images/lighthouse/checkout_lighthousecheckout_success_lighthouse.jpg">
    </details>

    <details> <summary> profile </summary>
    <img src="static/images/readme_images/lighthouse/profile_lighthouse.jpg">
    </details>

    </details>


## Django Automated Tests

- Django's Testing library was used to test Projects's forms,models,views and urls. Corresponding PEP8 validation listed in PEP8 section above.

1. <details> <summary> Services APP </summary>
    
    <details> <summary> Services </summary>
    <img src="static/images/readme_images/tests/service_app_tests.jpg">
    </details>

    <details> <summary> Test Error </summary>
    <img src="static/images/readme_images/tests/service_negative_price.jpg">
    </details>

    <details> <summary> Solution </summary>
    code added to Service model to make sure no negative value is allowed on service price.
        def clean(self):
        if self.price < 0:
            raise ValidationError({"price": "Price cannot be negative."})
    </details>
    </details>

2. <details> <summary> Profiles APP </summary>
    <img src="static/images/readme_images/tests/profiles_app_tests.jpg">
    </details>

3. <details> <summary> Portfolio APP </summary>
    <img src="static/images/readme_images/tests/portfolio_app_tests.jpg">
    </details>

4. <details> <summary> Home APP </summary>
    <img src="static/images/readme_images/tests/home_app_test.jpg">
    </details>

5. <details> <summary> Contact APP </summary>
    <img src="static/images/readme_images/tests/contact_app_tests.jpg">
    </details>

6. <details> <summary> Comments APP </summary>
    <img src="static/images/readme_images/tests/comments_app_tests.jpg">
    </details>

7. <details> <summary> Checkout APP </summary>
    <img src="static/images/readme_images/tests/checkout_app_tests.jpg">
    </details>

8. <details> <summary> Bag APP </summary>
    <img src="static/images/readme_images/tests/bag_app_tests.jpg">
    </details>

# Bugs and Fixes <a name="bugs"></a>

Bugs found/Minor fixes during development:

1. footer dosn't stay at the bottom of the view and displaced when content isn't filling in the entire view.

-   <details> <summary> Image of issue </summary>
    <img src="static/images/readme_images/bugs/issue1.jpg">
    </details>

- solution: set <footer> elements position to relative and then used javascript to posititon footer absolute to the bottom when content isn't filling in the view.


2. Displaced footer element when dropdown opens on smaller devices (tech.html).

-   <details> <summary> Image of issue </summary>
    <img src="static/images/readme_images/bugs/issue2.jpg">
    </details>

- solution: vh-100 bootstrap class removed has solved the issue.

3. Webhook handler did not work during development with local listener set up:

-   <details> <summary> Image of issue </summary>
    <img src="static/images/readme_images/bugs/python_404.jpg">
    </details>

-   <details> <summary> Image of issue </summary>
    <img src="static/images/readme_images/bugs/stripe_cli.jpg">
    </details>

-   <details> <summary> Image of issue </summary>
    <img src="static/images/readme_images/bugs/stripe_events_succeed.jpg">
    </details>

-   <details> <summary> Image of issue </summary>
    <img src="static/images/readme_images/bugs/stripe_webhook_listener.jpg">
    </details>

-   <details> <summary> Image of issue </summary>
    <img src="static/images/readme_images/bugs/trigger_succeed.jpg">
    </details>

- solution: after a throughout investigation where I checked my checkout views, urls and webhooks.py for errors followed by making sure the local listener is connected and listening on stripe and checking the events( where payments appeared succesfully) I eventually found that the stripe listener in the cli was triggered with an incorrect path.
The correct trigger is stripe listen --forward-to localhost:8000/checkout/stripe/webhook/ while during development the 
 stripe listen --forward-to localhost:8000/stripe/webhook/ path was used resulting in the 404 error.

4. Order confirmation page does not show the total cost of the order:

investigating this I found that a variable was called incorrectly.

-   <details> <summary> Image of issue </summary>
    <img src="static/images/readme_images/bugs/issue3.jpg">
    </details>

-   <details> <summary> Image of issue </summary>
    <img src="static/images/readme_images/bugs/issue3_solution.jpg">
    </details>

- solution: order.total was changed to order.order_total to reference the variable correctly.

5. Home Page and Portfolio main sections are out of alignment and text overflowing on smaller devices:

-   <details> <summary> Image of issue </summary>
    <img src="static/images/readme_images/bugs/issue5.jpg">
    </details>

- solution: easy fix, bootstrap class applying padding was replaced by custom class and adjusted with media queries to suit all sizes.

6. Services page out of alignment not fully center.

- solution: overlapping bootstrap and css styles removed as well as unused div elements.

7. Service_details page increase and decrease button visually unapplealing:

-   <details> <summary> Image of issue </summary>
    <img src="static/images/readme_images/bugs/issue7.jpg">
    </details>

- solution: custom class written in base.css to improve the look.

8. Bag.html-s table is out of alignment on screens less than 768px.

- solution: added media quieries to fex responsiveness.
