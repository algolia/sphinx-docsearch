# What is DocSearch?

DocSearch is a program by [Algolia](https://www.algolia.com/) for bringing fast and relevant search to technical content for free.

With DocSearch, Algolia indexes your documentation with the Algolia Crawler.
The crawler has a dashboard,
where you can configure what's crawled and you can schedule periodic updates.
With your DocSearch credentials, you can access the Algolia dashboard,
where you can see analytics for your search and change the ranking of your search results.

- [Crawler dashboard](https://crawler.algolia.com/admin)
- [Algolia dashboard](https://dashboard.algolia.com/)

DocSearch also comes with a UI component that lets your users search your site.

:::{seealso}

- [Who can apply?](https://docsearch.algolia.com/docs/who-can-apply/)
- [Crawler GitHub Action](https://github.com/marketplace/actions/algolia-crawler-automatic-crawl)
- [Algolia Crawler docs](https://www.algolia.com/doc/tools/crawler/getting-started/overview/)

:::

## What does the DocSearch Sphinx extension do?

After applying to DocSearch, Algolia automatically crawls and indexes your docs.

:::{note}

This extension does not configure the crawler.
Because each Sphinx theme controls how the content is rendered,
you may need to adapt the configuration in the [Crawler dashboard](https://crawler.algolia.com/admin).

:::

This Sphinx extension adds the DocSearch UI component to your website.

To avoid having two different search interfaces on your website,
this extension replaces the default search box provided by Sphinx.
The way a search box is added to the website depends on your Sphinx theme.
This extension [supports a few themes](/themes.md) out of the box.
If you're using a different theme, you can add DocSearch through [custom templates and CSS](/customization.md).
