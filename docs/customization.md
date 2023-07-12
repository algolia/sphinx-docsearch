# Customize

You can configure this extension to match your theme by adding custom templates,
and adding custom CSS.

## Add custom templates

By default, the DocSearch Sphinx extension overrides these templates:

- `searchbox.html` (used by many themes,
   including [Read the Docs](https://sphinx-rtd-theme.readthedocs.io/en/stable/),
   [Alabaster](https://alabaster.readthedocs.io/en/latest/), [Sphinx's built-in themes](https://www.sphinx-doc.org/en/master/usage/theming.html#builtin-themes))
- `sidebar/search.html` (used by the [Furo](https://pradyunsg.me/furo/) theme)

It replaces the entire search form with an empty container {samp}`<div id="{DOCSEARCH_CONTAINER}"></div>`

- Add template with the same name to: `templates_path` as override
- Update `docsearch_container` to match

## Add custom CSS files

- `html_static_path`
- `html_css_files`
