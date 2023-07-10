# Sphinx Algolia DocSearch extension

This extension for the [Sphinx](https://www.sphinx-doc.org/en/master/) replaces Sphinx' built-in search with Algolia DocSearch.

**WORK IN PROGRESS**

## What is DocSearch?

DocSearch is a program by Algolia for bringing fast and relevant search to every technical documentation for free.

- DocSearch is not just for open source projects
- DocSearch indexes your content using the Algolia Crawler to get the data in
- You add the DocSearch UI package to your site to help the users get the data, search-as-you-type

## Before you begin

- Create your DocSearch account / apply for DocSearch

## Install

1. Install the `sphinx-docsearch` extension from PyPI
1. Add `sphinx-docsearch` to the extensions in your Sphinx configuration file

## Configure

- `docsearch_app_id` (required)
- `docsearch_api_key` (required)
- `docsearch_index_name` (required)
- `docsearch_container` (default `#docsearch`)
- `docsearch_initial_query`
- `docsearch_placeholder`
- `docsearch_search_parameters`
- `docsearch_missing_results_url`

## Style

- Add custom styles in `{html_static_path}/{custom.css}` (relative to Sphinx project directory)
- Add configuration:
  
  - `html_static_path`: `{html_static_path}`
  - `html_css_files`: `[{custom.css}]`
