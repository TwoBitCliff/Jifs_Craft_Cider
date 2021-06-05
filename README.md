# Jif's Craft cider

[View the live website here](https://jifs-craft-cider.herokuapp.com/)

This is the fourth Milestone Project for the Code Institute's Full Stack Developer course.

In this project, I have utitlised skills learnt so far on the course, including HTML, CSS, JavaScript and Python, as well as incorportating Django, Stripe and other packages to create a Eccomerce site, specialising in cider. It allows the user to create a profile, shop for products, save them for later, and request refunds.

As per the standard of Responsive Design, this site is responsive across several devices, making sure to be structured in a cohesive manner and change designs when appropriate. To  achieve this, the site utilises Bootstrap, aiding its design and performance to shape a site that functions across several sized devices.

## UX

### User Stories
* Profile
1. As a user, I want to be able to create an account, and easily log in.
1. As a user, I want to be able to save my delivery information.
1. As a user, I want to be able to request refunds.

* Checkout
1. As a user, I want to add items to a shopping cart.
1. As a user, I want to  easily enter my billing/ delivery information
1. As a user, I want to be kept up to date of the total of the shopping cart


* Products
1. As a user, I want to see a wide variety of products for sale
1. As a user, I want to see price, information and the rating of each product.
1. As a user, I want to browse products by category.

### Design

* Colour Scheme
    * The colour scheme is a simple white with blue accents. 
    * This gives the site a clean look and proffessional look.


* Imagery
    * The background image was sourced from Pixabay.
    * Product images were sourced from google images, and the image url is saved with each product.

## Features

* Responsive across all devices.

* Interactive elements:
    * The purpose of the site is primarily to allow users to purchase products. To that end, large parts of the site are interactive.
    * The user can use the nav bar to browse products by category, price, rating and other filters.         
    * The user is able to create an account, and save delivery information.
    * The user is able to move products in and out of their wishlist and shopping bag.
    * The user is able to apply for refunds.
    * The user is able to submit blog posts and reviews.
    * The user can select a product to see more information about it.
    * Super users aer able to acces the admin, as well as add, edit and delete products.

### Features left to implement

### Languages Used

* [HTML 5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries & Programs Used

1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
1. [jQuery:](https://jquery.com/)
    - jQuery came with Materialize to make the navbar responsive and enable other Materialize functions.
1. [Git:](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the project's code after being pushed from Git.
1. [Microsoft Word:](https://www.microsoft.com/en-gb/microsoft-365/word)
    - Was used to write the content and ensure that the grammatical nature of the content was preserved.
1. [Bootstrap](https://getbootstrap.com/)
    - Was used for styling and ensure that the site's functions correctly.
1. [Jinja](https://en.wikipedia.org/wiki/Jinja_(template_engine))
    - Allows for template functionality, working alongside Python code and performing various functions to ensure the User only sees what they need to. 
1. [AWS](https://aws.amazon.com/)
    - Allows for the storage of static files.

## Deployment

### Heroku

The project was deployed to Heroku using the following steps (which can be found here) [Heroku Deployment](https://blog.heroku.com/six-strategies-deploy-to-heroku)...

1. Log in to Heroku and select 'Create New App'
2. You are then presented with the ability to name your app, which is what creates the URL and must be unique.
3. Select the region that is closest to yourself, once selected, click 'Create App'.
4. On the 'Deployment method' section click on the GitHub 'Connect to GitHub' option.
5. Search for your repository using its name with the Heroku Search function, once found, click 'Connect' to connect the repository from GitHub to Heroku.
6. You then need to select the 'Settings' tab and find the 'Reveal Config Vars' button.
7. Upon clicking the 'Reveal Config Vars' button, input the appropriate IP, PORT, SECRET_KEY, MONGO_URI and MONGO_DBNAME fields,
    with their relevant data from the env.py file.
8. Due to the creation of the Procfile and the requirements.txt file, we can select the 'Enable Automatic Deploys' button to ensure any changes pushed to
    GitHub are also synchronised with Heroku.
9. As there is only one branch, we can select the 'Deploy Branch' button to ensure Heroku receives changes from GitHub.
10. Once this is selected, you should see Heroku building our app and a 'Your app was successfully deployed' message should appear.
11. Simply click 'View' below this to view your live website.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page) just above the "Settings" button on the menu, locate the "Fork" button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Credits

### Content

All content has been written or created by the author.

### Media

1. The background image was sourced from pixabay.

1. The product images were sourced from google images, and the url's are saved to each product.

1. All images belong to their respective ownsers

### Acknowledgements

* Thanks to my girlfriend, parents and other friends for their ideas, support and for reviewing the project at various stages.
* Thanks to my Code Institute Tutor, Mentor and Student Support team for offering me advice and support
during the creation of this project.
* Thanks to the contributors at both Slack and Stack Overflow for help at different stages of the project.
