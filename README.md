# DevOps-Blog

This is a very basic blog post site setup to demonstrate Django framework & CRUD functionality.
Agile methology have being used during deployment setup.
This is a blogpost site dedicated for people who are interested in all things DevOps.
This site contains articles of interest in all aspects and areas of DevOPs.
The site could also contains tutorials that would be of interest in for Developers,IT admins,Geeks & hobbiest.


## Features

The site main feature is CRUD
The user can register to add posts themselves
The site was setup with seperate apps for Templates,About & Contacts
The site feature blog post infomation about devops related topics
The site features contact page 


### Features Left to Implement

- Contacts page
- Tutorials
- About

- Social media login
- Search feature


## User stories 

- As a site user I can login to a registered account so that access the comment and like functionality
- As a Site Admin I can create, read, update  posts so that I can manage the blog content
- As a Site Admin I can create draft posts so that I can finish writing the content later
- As a Site Admin I can approve or disapprove comments s
- 
- As a Site User & Admin I can view comments on an individual 
- As a Site User & Admin I can view the number of likes on each post 

- As a Site User I can register an account 
- As a site user I can logout of my registered account
- As a Site User I can view a list of posts so that I can select one to read
- As a Site User I can view a paginated list of posts so that easily select a post to view
- As a Site User I can click on a post so that I can read the full text
- As a Site User I can leave comments on a post so that I can engage with other users
- As a Site User I can like or unlike a post so that I can interact with the content
- As a Site User I can login to my profile so that I can view all my previously created posts
- As a site user I can filter the reviews 
- As a site user I can edit my comments to add additional content


## Testing
- I have tested page on Chrome,Firefox,Safari,Edge
- I have tested page with Google lighthouse
- I have tested with W3C HTML Validator
- I have tested with W3C CSS Validator
- I have tested with JSHint

## Bugs

- Issue with added images to posts -- fixed by adding  urllib3==1.26.15
- Issues with delete of post -- pending

## Lighthouse

## Mobile
![image](https://github.com/niallos11/devops-blog/assets/5288061/28112275-5efc-4317-a646-526f61274bf3)

## Desktop

![image](https://github.com/niallos11/devops-blog/assets/5288061/0f572e8e-343c-4fbc-8cf3-0372371e2796)

### Validator Testing

### HTML
- No errors were returned when passing through the official - https://validator.w3.org/nu/?doc=https%3A%2F%2Fdevopsblog-9ee0000374f1.herokuapp.com%2F


### CSS
- Error were found - https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fdevopsblog-9ee0000374f1.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en
- 21	.thin	Value Error : font-weight 4000 is not valid, only values lower than or equal to 1000.0 are allowed. : 4000
- 50	.image-flash	Value Error : background-color #20vff02 is not a background-color value : #20vff02
Fixed errors.

### Color Contrast Accessibility Validator
![image](https://github.com/niallos11/devops-blog-dev/assets/5288061/6374a305-d7e7-4d21-99b1-99573de778fd)


### Javascript
- The javascript code was run through jshint to check for any errors.

### Python
- The python code was run through Pep8 to check for errors. 


### Unfixed Bugs

- Tutorials & Contact custom models are not completed.
- Delete blog post fails with error - MultipleObjectsReturned at /delete_comment.
- Debug is still set to true as I get a error when enabling. Need to fix errors first.
- Collectect static is still set to 1 as deploy to heroku fails without it.


### WireFrames
This site was designed and planned out with wireframes before deployment. 

![image](https://github.com/niallos11/devops-blog-dev/assets/5288061/8a37c175-6863-490e-9b6f-567dbe4b5a3f)



### Deployment:
- The site was build using CodeAnywhere
- The site was deployed to GitHub.
- The site was deployed to Heroku.


The live link can be found here - https://devopsblog-9ee0000374f1.herokuapp.com/


## Credits
- Code Institute
- Special thanks to student care
- Hello Django walkthrough project
- I Think Therefore I Blog walkthrough project


### Content
- The main code base was taken from I Think Therefore I Blog.
- Content for DevOps posts & blogs were taken from various sources and google searches online.
- The fonts were taken from google fonts - [https://fonts.google.com/specimen/Short+Stack
](https://fonts.google.com/specimen/Press+Start+2P) & https://fonts.google.com/specimen/VT323

### Media

- The images used for the background page were taken from a Open Source site.
- The fav icon was taken from - https://www.favicon.cc
- The images were resized with Bulk Resize Photos - https://bulkresizephotos.com/en
