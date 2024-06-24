# Django Template

This sample repo contains the recommended structure for a Python Django project. In this sample, we use `django` to build a web application and the `unittest` to run tests.

For a more in-depth tutorial, see our [Django tutorial](https://code.visualstudio.com/docs/datascience/data-science-tutorial).

The code in this repo aims to follow Python style guidelines as outlined in [PEP 8](https://peps.python.org/pep-0008/).

## Running the Sample

To successfully run this example, we recommend the following VS Code extensions:
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Python Debugger](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)
- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) 

- Open the template folder in VS Code (**File** > **Open Folder...**)
- Create a Python virtual environment using the **Python: Create Environment** command found in the Command Palette (**View > Command Palette**). Ensure you install dependencies found in the `pyproject.toml` file
- Ensure your newly created environment is selected using the **Python: Select Interpreter** command found in the Command Palette
- Create and initialize the database by running `python manage.py migrate` in an activated terminal. 
- Run the app using the Run and Debug view or by pressing `F5`
- Run tests by running `python manage.py test` in an activated terminal
