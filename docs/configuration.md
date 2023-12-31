# Configure DocSearch

All configuration settings start with `docsearch_`.

## Required configuration

You **must** add at least your credentials to make DocSearch work:

**`docsearch_app_id`**
: Your Algolia application ID.
  You can find it in the [Algolia dashboard](https://dashboard.algolia.com/account/api-keys)

**`docsearch_api_key`**
: Your Search API key.
  You can find it in the [Algolia dashboard](https://dashboard.algolia.com/account/api-keys).

  :::{warning}
  Don't use your Write API key, which is used for crawling your content.
  :::

**`docsearch_index_name`**
: The Algolia index name for your documentation.

## Optional configuration

The Sphinx extension lets you configure these aspects of the DocSearch UI.

**`docsearch_container`** (default `#docsearch`)
: The ID of the HTML element where the search input is added.
  By default, the DocSearch input is added to the HTML element with the ID `docsearch`.
  You can change this setting if you're using a different theme.

**`docsearch_placeholder`** (default: `Search`)
: The placeholder text for the search box.

**`docsearch_initial_query`**
: A query for an initial search if you want to show search results as soon as the user opens the search menu.

**`docsearch_search_parameters`**
:  Any Algolia search parameter you want to add.

**`docsearch_missing_results_url`**
: If specified, DocSearch adds a message to the "No results found" screen with the link to the URL you specified,
  for users to report issues with missing search results.
  You can include the current search query as parameter ${query}. For example:

  ```python
  docsearch_missing_results_url = "https://github.com/example/docs/issues/new?title=${query}"
  ```
