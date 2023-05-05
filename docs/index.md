# DocSearch for Sphinx

This extension for the Sphinx documentation generator adds Algolia DocSearch to your Sphinx documentation.

## Before you begin

First, apply to the DocSearch program and get your Algolia credentials.

## Get started

1. Install the DocSearch extension:

   ```sh
   pip install sphinxawesome-docsearch
   ```

1. Add the DocSearch extension to your Sphinx configuration:

   ```python
   # conf.py
   extensions += ["sphinxawesome.docsearch"]
   ```

1. Add the DocSearch configuration:

   ```python
   # conf.py
   docsearch_app_id = "{YourApplicationID}"
   docsearch_api_key = "{YourSearchAPIKey}"
   docsearch_index_name = "{YourIndexName}"  
   ```

   For more configuration options, see {doc}`configuration`.

1. Tweak the styles.

```{toctree}
:hidden: true
what-is-docsearch
configuration
```
