 #BlockNews
 
[Link to Live Site Here]()
 
---
![AmIResponsive]()
---
 
# User Experience (UX)
 
* ## Vision      
 
* ## Aims
 
* ## Target Audience
 
* ## User Stories
 
* ## Development Method
 
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
 
