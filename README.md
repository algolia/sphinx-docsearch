# Algolia DocSearch Sphinx extension

This extension for the [Sphinx](https://www.sphinx-doc.org/en/master/) documentation generator
replaces Sphinx's built-in search with Algolia DocSearch.

## Before you begin

[**Apply for DocSearch**](https://docsearch.algolia.com/apply). You'll get an email with your Algolia credentials.

This extension supports Python versions 3.8, 3.9, 3.10, and 3.11 and Sphinx versions 5 and later.

## Install

Install the `sphinx-docsearch` extension from PyPI:

```sh
pip install sphinx-docsearch
```

## Configure

1. Add `sphinx-docsearch` to your Sphinx configuration file `conf.py`:

   ```python
   extensions += ["sphinx_docsearch"]
   ```

1. Add your Algolia credentials to your Sphinx configuration:

   ```python
   docsearch_app_id = "<DOCSEARCH_APP_ID>"
   docsearch_api_key = "<DOCSEARCH_SEARCH_API_KEY>"
   docsearch_index_name = "<DOCSEARCH_INDEX_NAME>"
   ```

1. Optional: change configuration settings

## Customize

- Customize crawling (link to DocSearch or Crawler doc)
- Add custom templates
- Add custom CSS
