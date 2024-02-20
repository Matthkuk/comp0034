[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10366523&assignment_repo_type=AssignmentRepo)
# COMP0034 Coursework 2 starter code template

To set up your project:

1. Clone this repository in your IDE (e.g. PyCharm, Visual Studio Code) from GitHub. Follow the help in your IDE
   e.g. [clone a GitHub repo in PyCharm.](https://www.jetbrains.com/help/pycharm/manage-projects-hosted-on-github.html#clone-from-GitHub)
2. Create and then activate a virtual environment (venv). Use the instructions for your IDE
   or [navigate to your project directory and use python.](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
3. Install the requirements from requirements.txt. Use the instructions for your IDE
   or [the pip documentation](https://pip.pypa.io/en/latest/user_guide/#requirements-files).
4. Edit .gitignore to add any config files and folders for your IDE. 

Code:
For my code I have used configs for environments (testing and the normal build), a factory function (create_app), and blueprints (bp and main_bp).
The routes for get requests, single get requests, post requests, delete requests, and patch requests were made.
The routes for the home page and dash app (from previous coursework) are also included.
Model classes are used to model the five different databases. The five databases are referenced using bind keys and each have their own set of routes set up.
The data is read from 5 separate SQLite databases.
Error handling is done in the routes using try and except, custom HTTP error pages (two different designs), and flask flash messages are used to provide further insight into the error.

Tests:
A test for every single flask route using the flask test client is coded.
A test for the failure of each type of route is also added.
I believe that I have covered around half of the errors that will occur in the routes I have coded. I have a failure test as well to check the try and excepts are working as they should. Covering all the bases would be extremely difficult as an individual, but I have covered most of the important functions of the route, such as checking if they function correctly and give the correct outputs and response code.
The image for the successful tests: testing_success.PNG

Use of tools and techniques:
Repository: https://github.com/ucl-comp0035/comp0034-cw2-i-Matthkuk.git
Activate the virtual environments using: .\env\Scripts\activate
Check the requirements are installed: py -m pip install -r requirements.txt
Run the code using: python -m flask --app 'flask_app:create_app()' run --debug
To run tests: python -m pytest -v flask_app\tests\tests_football.py
The code will run the flask app including the dash app.
The data can be found in the data folder. To reset the databases, delete them and then run csv_to_sqlite.py.
The code for the html and css are found in the templates and static folders respectively.