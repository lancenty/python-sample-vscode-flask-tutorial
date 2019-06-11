"""
In this sample, the Flask app object is contained within the show_requirements *module*;
that is, show_requirements contains an __init__.py along with relative imports. Because
of this structure, a file like webapp.py cannot be run directly as the startup
file through Gunicorn; the result is "Attempted relative import in non-package".

The solution is to provide a simple alternate startup file, like this present
startup.py, that just imports the app object. You can then just specify
startup:app in the Gunicorn command.
"""
from hello_app import app
