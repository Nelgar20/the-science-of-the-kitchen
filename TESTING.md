# Manual testing

| Feature/Test | Expected Outcome | Result |
| --- | --- | --- |
| Name of the blog in Navbar | Redirects to homepage | Pass |
| Navbar links | Redirect to relevant pages (Blog, About Us, Categories,(Sign in-Log in-Log out), and Search ) | Pass |
| Footer Contact Us link | Redirect to About us page | Pass |
| Footer social Links | Open relevant sites in new tabs | Pass |
| Blog page | Display 6 articles with images, title, category and author | Pass |
| Click on Article | Redirects to article detail | Pass |
| Click on Category | Redirects to article list with the selected category's articles | Pass |
| Search with keyword | Redirects to article list and display articles that contains the relevant keyword | Pass |
| Pagination | Next/Previous buttons load correct pages and hold a search keyword if prompted | Pass |
| Sign Up Link | Redirects to registration page | Pass |
| Sign Up Form; empty field | Prompt to complete form | Pass |
| Sign Up Form; username already used, short password, common password | won't continue and would return red alerts | Pass |
| Sign Up Form; valid new user | Redirects to homepage with a success notification | Pass
| Login Link | Redirects to login page | Pass |
| Log in with empty fields | Prompt messages to compile the fields | Pass. |
| Login with incorrect values | display error messages | Pass |
| Login with correct values | redirects to homepage with success message | Pass |
| Navbar when Logged out | display register and log in | Pass |
| Navbar When Logged in | display log out | Pass |
| Empty collaboration form | prompt to complete form | Pass |
| Completed collaboration form | displays success message and sends the request | Pass. |
| Leaving a comment | if user logged, can leave the comment, and get a success message. If not, can't and need to log in to be able  | Pass. |
| If user logged | comment form and submit button are displayed displayed   | Pass. |
| Edit, delete and update button| Are displayed only to the user that left the comment | Pass. |
| Updating a comment | display a success message and update the comment | Pass. |
| Deleting a comment | appear a modal to ask confirmation for deletion | Pass. |
| Confirming deletion | display a success message and delete the comment | Pass. |
| Logout Button. | Redirects to logout confirmation page. | Pass. |
| Logout Confirmation. | Displays confirmation before logging out. | Pass. |
| Responsive Design | the site is responsive on multiple devices | Pass. |


# Validation 

## HTML validation using W3C HTML validator
### Home | home.html validation
Errors founded
![image](static/images/Home-validation-error.png)
Errors fixed
![image](static/images/home-validation-pass.png)

### Blog | article_list.html
Passed
![image](static/images/blog-validation-pass.png)

### Blog | article_detail.html
Errors founded
![image](static/images/article-detail-validation-errors.png)
Errors fixed
![image](static/images/article-detail-validation-pass.png)

### About | about.html
Errors founded
![image](static/images/about-validation-errors.png)
Errors fixed
![image](static/images/about-validation-pass.png)

### Signup | signup.html
Errors founded
![image](static/images/signup-validation-errors.png)
Errors fixed
![image](static/images/signup-validation-pass.png)

### Login | login.html
Errors founded
![image](static/images/login-validation-error.png)
Errors fixed
![image](static/images/login-validation-pass.png)

### Logout | logout.html
Pass
![image](static/images/logout-validation-pass.png)

## CSS validation W3C CSS validator
Passed with 4 warnings
![image](static/images/css-validation-pass-1.png)
![image](static/images/css-validation-warnings-4.png)
Eliminated the redundant css style, the other two warnings refer to the root class.
![image](static/images/css-validation-pass-2.png)
![image](static/images/css-validation-warnings-2.png)


## JavaScript validation using JSHint
![image](static/images/jshint-validation.png)

## Python validation using PEP8CI link
About | views.py
![image](static/images/about-view-py.png)
About | models.py 
![image](static/images/about-models-py.png)
Blog | views.py
![image](static/images/blog-view-py.png)
Blog | models.py
![image](static/images/blog-models-py.png)
## Lighthouse validation
Homepage
![image](static/images/lighthouse-validation-home.png)
Blog page
![image](static/images/lighthouse-blog-validation.png)
The low score on the blog page is due to unsecure resources loaded from cloudinary over HTTP instead HTTPS. As future improvement will be to review and update existing image URLs in the database.
![image](static/images/lighthouse-bad-score.png)
Article detail page
![image](static/images/article-detail-lighthouse-validation.png)
About us page
![image](static/images/lighthouse-validation-about-us.png)