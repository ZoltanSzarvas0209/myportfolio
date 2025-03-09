

# TABLE OF CONTENT

1. [ Manual Testing ](#manual)
2. [ Automated Testing ](#auto)
3. [ Bugs and Fixes ](#bugs)

# MANUAL TESTING <a name="manual"></a>

### Testing Responsiveness

<details>

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

</details>

### Testing Functionality of Buttons/Links

<details>

| **Feature** | **Test Method** | **Expectation** | **Outcome** |
|-------------|-----------------|-----------------|-------------|
| Navigation Links | Click each link | Route to relevent page | PASS |

</details>

### Testing Layout/Structure

<details>

| **Feature** | **Test Method** | **Expectation** | **Outcome** |
|-------------|-----------------|-----------------|-------------|

</details>

### Form Validation testing

<details>

| **Feature** | **Test Method** | **Expectation** | **Outcome** |
|-------------|-----------------|-----------------|-------------|

</details>

### Browser Testing

<details>

| **Feature** | **Test Method** | **Expectation** | **Outcome** |
|-------------|-----------------|-----------------|-------------|

</details>

### TESTING USER STORIES

<details>

| **Feature** | **Test Method** | **Expectation** | **Outcome** |
|-------------|-----------------|-----------------|-------------|

</details>




# AUTOMATED TESTING <a name="auto"></a>

### HTML,CSS and JS validation

* HTML VALIDATION:    

W3C validators used for HTML and CSS and JsHint is used to validate JAvaScript.
    


* CSS VALIDATION: 
    

* JavaScript VALIDATION: 
    

## PEP8 , python validation:


## Lighthouse 


## Django Automated Tests

- Django's Testing library was used to test Projects's forms. Corresponding PEP8 validation listed in PEP8 section above. Each form was tested with 3 tests.




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