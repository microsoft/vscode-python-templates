This project provides a template for starting a new Django application with best practices and common configurations.

For more information on the project, see README.md. 

## Code layout 
Use spaces, not tabs. 4 spaces per indentation level. 

Limit all lines to a maximum of 79 characters.

Surround top-level function and class definitions with two blank lines.

For code layout specifications not mentioned here, adhere to PEP8.  

## Naming Conventions
Use snake_case for variable, function, and file names. 
Use PascalCase class class names. 
Use all uppercase with underscores separating words for constants.
Use whole words in names when possible

Use meaningful variable and function names that reflect their purpose.

## Comments
When there are comments for modules, classes, and functions use docstrings. 

## Tests
Write unit tests for models, views, and forms using Django's built in unittest framework.

## Django instructions 
Avoid business logic in views; delegate complex logic to helper functions or services.

Use descriptive and human-readable URLs.

Follow a consistent folder structure for templates (e.g., app_name/templates/app_name/...).