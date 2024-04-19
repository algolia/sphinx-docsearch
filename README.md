# Algolia DocSearch for Sphinx

This extension for the [Sphinx](https://www.sphinx-doc.org/en/master/) documentation generator
replaces Sphinx's built-in search with Algolia DocSearch.

## Before you begin

[**Apply for DocSearch**](https://docsearch.algolia.com/apply).
You'll get an email with your Algolia credentials.

This extension supports Python versions 3.8 and later and Sphinx versions 5 and later.

## Install

Install the `sphinx-docsearch` package:

```sh
pip install sphinx-docsearch
```

## Configure

1. Add `sphinx-docsearch` to your Sphinx configuration:

   ```python
   # conf.py
   extensions += ["sphinx_docsearch"]
   ```

1. Add your Algolia credentials to your Sphinx configuration:

   ```python
   # conf.py
   docsearch_app_id = "<DOCSEARCH_APP_ID>"
   docsearch_api_key = "<DOCSEARCH_SEARCH_API_KEY>"
   docsearch_index_name = "<DOCSEARCH_INDEX_NAME>"
   ```

   See also: [Configure DocSearch](https://sphinx-docsearch.readthedocs.io/configuration.html).

## Customize

To change what the crawler should extract from your pages, see [Record Extractor](https://docsearch.algolia.com/docs/record-extractor).

You can add [custom templates](https://sphinx-docsearch.readthedocs.io/customization.html#add-custom-templates),
if your Sphinx HTML theme uses templates [not provided](https://sphinx-docsearch.readthedocs.io/themes.html)
by this extension.

You can customize the look of the DocSearch UI by [adding your own CSS](https://sphinx-docsearch.readthedocs.io/customization.html#add-custom-css).
