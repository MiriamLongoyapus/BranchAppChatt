STEO ONE

1. Install Python: Django is a Python web framework, so you need to have Python installed on your system.
   You can download the latest version of Python from the official Python website at python.org .

2. Install pip: Pip is a package manager for Python. It is used to install Django and other Python packages.
   python3 get-pip.py
   python -m pip --version

3. Set up a virtual environment: Run the following command to create a virtual environment:
   python3 -m venv myenv
   Replace myenv with the name you want to give to your virtual environment.
4. Activate the virtual environment by running:
   source myenv/bin/activate
5. Install Django: Run the following command in the command prompt or terminal:
   pip install Django
6. Verify the installation: Run the following command:
   python -m django --version
   This will display the version of Django installed on your system.




STEP TWO

1. Create the app:
   python3 manage.py startapp app_name
   Replace app_name with the desired name for your app.

2. Method 2: Run the following command:
   python3 manage.py startapp app_name
   Replace app_name with the desired name for your app.

3. Configure the app: Open the settings.py file located in your project's directory. In the INSTALLED_APPS list,
   add the name of your app as a string. For example:
   INSTALLED_APPS = [
    ...
    'app_name',
    ...
]

4. Migrate the database: Run the following command
   python3 manage.py migrate
   python3 manage.py migrate
5. Runnserver:
   python3 manage.oy runserver
7. Start coding: Now that your app is set up, you can start writing code for your app. 
The main files you will work with are models.py, views.py, and urls.py.

