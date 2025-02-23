

# TABLE OF CONTENT

1. [ Manual Testing ](#manual)
2. [ Automated Testing ](#auto)
3. [ Bugs and Fixes ](#bugs)

# MANUAL TESTING <a name="manual"></a>

### Testing Responsiveness

<details>

| **Feature** | **Test Method** | **Expectation** | **Outcome** |
|-------------|-----------------|-----------------|-------------|

</details>

### Testing Functionality of Buttons/Links

<details>


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

Bugs found during development:

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

 