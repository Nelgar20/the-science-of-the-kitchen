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
The low score on the blog page is due to unsecure resources loaded from cloudinary over HTTP instead HTTPS.
![image](static/images/lighthouse-bad-score.png)
Article detail page
![image](static/images/article-detail-lighthouse-validation.png)
About us page
![image](static/images/lighthouse-validation-about-us.png)
# Manual testing