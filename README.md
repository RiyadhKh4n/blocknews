# Cryptics
 
[Cryptics Deployed Site]()

The purpose of Cryptics is to allow users to track their cryptocurrency holdings by utilising the CoinMarketCap API. Users are able to create multiple portfolios where they can add their assets and track the profitability and performance of their holdings.  

Cryptics is a Full Stack Application built with the Django Framework which includes full CRUD funcitionality allowing users to Sign Up / Log In to their account and add, edit or delete portfolios and track their crypto holdings all in one application.

The project is inspired by the [CoinMarketCap Portfolio Tracker](https://coinmarketcap.com/portfolio-tracker/) which is a useful tool I myself use to track my crypto assets. Cryptics aims to provide similar functionality and ease of use as the market leader. 
 
---

![AmIResponsive]()

---

# User Experience (UX)
 
* ## Vision      
    My vision for Cryptics is to be an application crypto enthusiasts go to if they want to manage their portfolios and track the performance of them. The website is meant to be simple yet effective and provide a real use case to people interested in cryptocurrency. The website will be easy to navigate and I will take a mobile first approach when developing the user interface for the application. I want Cryptics to be responsive and to provide all the necessary features expected in a portfolio tracking application.

* ## Aims
    To provide users an easy to use application they can go to when they want to track and manage their cryptocurrency holdings.  
 
* ## Target Audience
    Cryptocurrency is for everyone! However, the program does require users to have a basic understanding about crypto and portfolio management. Additionally, in the UK you must be at least 18 to own crypto assets as a result, my target audience is for cryptocurrency enthusiasts 18+.
 
* ## User Stories

1. As a **Site User** I can **create an account** so that **I can interact with the site**
2. As a **Site User** I can **view a paginated list of coins** so that **view all tokens in portfolio**
3. As a **Site User** I can **create an Portfolio** so that **I can track my crypto holdings**
4. As a **Site User** I can **view my Portfolio** so that **I can view the tokens within**
5. As a **Site User** I can **chose a token to add** so that **I can expand my portfolio**
6. As a **Site User** I can **add a token to my portfolio** so that **I can add to my holdings**
7. As a **Site User** I can **read about the website** so that **I can understand the application**

* ## Development Method
    When developing Cryptics I will take an Agile Approach. Meaning I will take an iterative approach to project management and software development helping me to deliver value faster and speed up development time. I will focus on working software over comprehensive documentation and responding to change over following a plan when creating the project.  
 
* ## Scope
 
* ## Structure
 
## Design
 
 
# Features
 
Here describes the main features of the website and what the user can expect when viewing ~
 
## Existing Features:
 
 
## Future Features:
 
 
# Technologies
## Languages Used
 
- [Python](https://www.python.org/) - Python is an interpreted high-level general-purpose programming language
 
- I used GitHub [Project Board]() to keep track of all the tasks necessary in order to build this application
 
## Frameworks, Libraries & Programs Used:
 
1. [GitPod](https://www.gitpod.io/):
    * GitPod was the IDE used to create the site
 
2. [Git](https://git-scm.com/):
    * Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
 
3. [GitHub](https://github.com/):
    * GitHub is used to store the projects code after being pushed from Git.
 
4. [Google Developer Tools](https://developer.chrome.com/docs/devtools/):
    * Used to test the program throughout development
 
5. [Os Library](https://docs.python.org/3/library/os.html)
    * Used to clear the console.
 
6. [Heroku](https://dashboard.heroku.com/login)
    * Used to Deploy the Project
 
8. [AMiResponsive](http://ami.responsivedesign.is/)
    * To generate the image at the beginning of the README
 
 
10. [TinyPNG](https://tinypng.com/)
    * This was used to compress all images used in the README.md
 
11. [PEP8](http://pep8online.com/)
    * Used to validate my Python code
 
12. [favicon.cc](https://www.favicon.cc/)
    * Used to generate the favicon address from the hosted site
 
15. [Requests](https://pypi.org/project/requests/)
    * Allowed me to sent HTTP requests without having to manually add query to strings to the URLs
 
# Testing
 
Due to the size of the testing section for CoinFrog I have created [TESTING.md](TESTING.md). It ashows any errors/bugs I encountered, and how I fixed them when creating this project. This is also contains my testing for user stories and any bugs.
 
[Link To Testing.md](TESTING.md)
   
# Deployment
 
Deploying the project using Heroku:
* Visit the [Heroku](https://dashboard.heroku.com/login) site and create an account
* Click the "New" Button
* Click the "Create new app" button
* Provide a name for the app in the App name input field
* Select your region from the choose region dropdown menu
* Click the "Create App" button
* Once redirected, proceed to the settings tab
* Click on the "config vars" button
* Supply a KEY of `PORT` and it's value of `8000`. The click the "add" button
* Next step is to add Buildpacks, click the "Add Buildpack" button
* The `python` buildpack needs to be added first then the `nodejs` buildpack
* Once the buildpacks have completed, go to the deploy screen, once in the deploy screen, select GitHub as the deployment method and connect your GitHub profile
* Search for the repository that you wish to deploy to Heroku and click "connect"
* Once your repository is connected to Heroku you can choose to either manually or automatically deploy your app.
* By selecting automatic deploys, Heroku will build a new version of the app each time a change has been pushed to the repository
* Manual deploys allow you to build a new version of your app whenever you click manual deploy
* If your build is successful you will then be able to visit the live site by clicking the link that is provided to you by Heroku
 
Command to add packages to requirements.txt, `pip3 freeze --local > requirements.txt`
 
## Making a Local Clone
 
1. Log in to GitHub and locate the [GitHub Repository](https://github.com/RiyadhKh4n/blocknews)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.
 
    $ `git clone LINK`
 
7. Press Enter. Your local clone will be created.
 
```shell
$ git clone INSERT LINK
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```
 
Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.
 
[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/RiyadhKh4n/CoinFrog)
 
You will need to also install all required packages in order to run this application on Heroku, refer to [requirements.txt](requirements.txt)
* Command to install this apps requirements is `pip3 install -r requirements.txt`
 
# Credits
 
 
## Code
 
 
### Acknowledgements
* Tim - My Mentor
* Tutor Support
* Fellow students from Slack
 
