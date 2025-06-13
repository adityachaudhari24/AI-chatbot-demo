# AI-chatbot-demo
AI-chatbot-demo


Steps to configure project

1. install virtual environment using `python -m venv venv` / `python3 -m venv venv` based on which python is installed. and then activate it using `source venv/bin/activate`

2. create .env file to put the OPENAI token key and also install `pip install python-dotenv`

3. do install open ai using `pip install openai`

4. freez the dependencies using `pip freeze > requirements.txt`


## Notes

Q. what is Virtual Environment ?
A virtual environment is a self-contained directory that contains a Python installation for a particular version of Python, along with additional packages. It allows you to manage dependencies for different projects separately without conflicts.
command to create venv : `python3 -m venv venv`

Q. What is activating the Virtual Environment?
Isolation: Activating the virtual environment ensures that any packages you install or scripts you run use the Python interpreter and libraries specific to that environment, rather than the global Python installation.

Dependency Management: Different projects may require different versions of libraries. By using a virtual environment, you can maintain these dependencies separately.

command to create activate virtual environment : 
MAC and Linux - `source venv/bin/activate`
WINDOWS - `.\venv\Scripts\activate`


Q. what is pip freez and why we need it?
The command `pip freeze > requirements.txt` is used to create a file named requirements.txt that contains a list of all the installed Python packages in the current environment along with their versions. This file is useful for:

Reproducibility: Allowing others to replicate the environment by installing the same packages.
Deployment: Simplifying the process of setting up environments in different systems or servers.
To install the packages listed in requirements.txt, you can use the command `pip install -r requirements.txt`.



OR try just executing pythonsetup.sh 