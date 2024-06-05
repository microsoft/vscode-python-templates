# FastAPI Template

This sample repo contains the recommended structure for a Python FastAPI project. In this sample, we use `fastapi` to build a web application and the `pytest` to run tests.

For a more in-depth tutorial, see our [Fast API tutorial](https://code.visualstudio.com/docs/python/tutorial-fastapi).

## Running the Sample

This sample makes use of Dev Containers, in order to leverage this setup, make sure you have [Docker installed](https://www.docker.com/products/docker-desktop).

To successfully run this example, we recommend the following VS Code extensions:

- [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Python Debugger](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)
- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) 

In addition to these extension there a few settings that are also useful to enable. You can enable to following settings by opening the Settings editor (`Ctrl+,`) and searching for the following settings:

- Python > Analysis > **Type Checking Mode** : `basic`
- Python > Analysis > Inlay Hints: **Function Return Types** : `enable`
- Python > Analysis > Inlay Hints: **Variable Types** : `enable`

- Open template repo 
- Open the Command Palette in VS Code (**View > Command Palette...**) and run the **Dev Container: Reopen in Container** command.
- Run the app using the Run and Debug view or by pressing `F5`
- Test the API functionality by navigating to `/docs` URL to view the Swagger UI
- To run tests using `pytest`, navigate to the Test Panel to configure your Python test or by triggering the **Python: Configure Tests** command from the Command Palette.
