# Manage credentials

Instead of hard-coding your Algolia credentials into your Sphinx configuration,
you should load them via environment variables.

A good practice is to add the environment variables to a `.env` file.
You can use the [`python-dotenv`](https://github.com/theskumar/python-dotenv) package to load them in your Sphinx configuration.

## Create a `.env` file

1. In your Sphinx project directory (which contains the `conf.py` file),
   create a new `.env` file and add your credentials as environment variables:

   ```sh
   # .env file
   DOCSEARCH_APP_ID=<DOCSEARCH_APP_ID>
   DOCSEARCH_API_KEY=<DOCSEARCH_API_KEY>
   DOCSEARCH_INDEX_NAME=<DOCSEARCH_INDEX_NAME>
   ```

   Replace the placeholder values `<...>` with your Algolia credentials.

1. If you're using git, add this file to the `.gitignore` file:

   ```sh
   echo ".env" >> .gitignore
   ```

   :::{note}
   While these credentials are exposed on your website anyway to enable your readers to search on your docs,
   it's still best practice to not commit any credentials to your repository.
   :::

## Load environment variables

To load environment variables from a `.env` file in your Sphinx configuration,
follow these steps:

1. Add the `python-dotenv` package to the list of your dependencies,
   or install it directly:

   ```sh
   pip install python-dotenv
   ```

1. Update your Sphinx configuration:

   ```python
   # conf.py
   import os
   from dotenv import load_dotenv

   load_dotenv()
   # ...
   ```

   This adds the environment variables from your `.env` file to the shell environment,
   which you can inspect with `os.environ` or `os.getenv`.

1. Add the DocSearch credentials, using environment variables:

   ```python
   # conf.py
   # ...
   docsearch_app_id = os.getenv("DOCSEARCH_APP_ID")
   docsearch_api_key = os.getenv("DOCSEARCH_API_KEY")
   docsearch_index_name = os.getenv("DOCSEARCH_INDEX_NAME")
   ```
