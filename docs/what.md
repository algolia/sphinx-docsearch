# What is DocSearch?

DocSearch is a program by Algolia for bringing fast and relevant search to every technical content for free.

With DocSearch, Algolia indexes your documentation with a crawler.
The Algolia Crawler comes with a dashboard, where you can configure what is crawled and you can schedule periodic updates.
With your DocSearch credentials, you can access the Algolia dashboard,
where you can see analytics about your Search and change the ranking of your search results.

DocSearch also comes with a UI component that you can add o your website.
This Sphinx extension automatically adds it to your Sphinx project.

:::{seealso}

- [Who can apply?](https://docsearch.algolia.com/docs/who-can-apply/)
- [Crawler GitHub Action](https://github.com/marketplace/actions/algolia-crawler-automatic-crawl)
- [Algolia Crawler docs](https://www.algolia.com/doc/tools/crawler/getting-started/overview/)
:::

## What does this extension do?

- Add DocSearch UI to the HTML element with the ID specified by `docsearch_container` (default: `#docsearch`)
- Override built-in template `searchbox.html` `sidebar/search.html` to fully replace the built-in search form.
  Without that, you would get both the DocSearch results modal and Sphinx's built-in search form.
- Disable Sphinx's built-in search (doesn't index the content)
