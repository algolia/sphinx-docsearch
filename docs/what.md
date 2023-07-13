# What is DocSearch?

DocSearch is a program by Algolia for bringing fast and relevant search to every technical content for free.

With DocSearch, Algolia indexes your documentation with a crawler.
The Algolia Crawler comes with a dashboard, where you can configure what's crawled and you can schedule periodic updates.
With your DocSearch credentials, you can access the Algolia dashboard,
where you can see analytics about your Search and change the ranking of your search results.

DocSearch also comes with a UI component that you can add to your website.
This Sphinx extension automatically adds it to your Sphinx project.

:::{seealso}

- [Who can apply?](https://docsearch.algolia.com/docs/who-can-apply/)
- [Crawler GitHub Action](https://github.com/marketplace/actions/algolia-crawler-automatic-crawl)
- [Algolia Crawler docs](https://www.algolia.com/doc/tools/crawler/getting-started/overview/)
:::

## What does the DocSearch Sphinx extension do?

After applying to DocSearch, Algolia automatically crawls and indexes your docs.
This Sphinx extension adds the DocSearch UI component to your website.
It adds it to an HTML element, which you can select with the [`docsearch_container`](/configuration.md) setting (default: `#docsearch`).

To avoid having two different search interfaces on your website,
this extension replaces the default search box provided by Sphinx.
It overrides the built-in templates `searchbox.html` or `sidebar/search.html`.
This makes the extension work with the [Furo](https://pradyunsg.me/furo/),
[Read The Docs](https://sphinx-rtd-theme.readthedocs.io/en/stable/), and
[Alabaster](https://alabaster.readthedocs.io/en/latest/) themes by default.

For these themes, the extension also adds custom CSS to make the DocSearch search box fit the theme.

If you're using a different theme, see [Customize](/customization.md) for more information.
