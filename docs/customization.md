# Customize

You can configure this extension to match your theme by adding custom templates,
and adding custom CSS.

## Add custom templates

By default, the DocSearch Sphinx extension overrides these templates:

- `searchbox.html` (used by many themes,
   including [Read the Docs](https://sphinx-rtd-theme.readthedocs.io/en/stable/),
   [Alabaster](https://alabaster.readthedocs.io/en/latest/), [Sphinx's built-in themes](https://www.sphinx-doc.org/en/master/usage/theming.html#builtin-themes))
- `sidebar/search.html` (used by the [Furo](https://pradyunsg.me/furo/) theme)

If you're using any of the [listed themes](/themes.md), DocSearch works without additional configuration.

If you're using any other theme, you can add custom templates in your Sphinx configuration.
The extension works best, if the theme uses a separate template for the search box.

To add a custom template, follow these steps:

1. Create a new directory in your Sphinx project, such as `_templates/`.
1. Create a custom template file with the same name as the template you want to override from your theme, such as `_templates/searchbox.html`:

   ```html+jinja
   {# _templates/searchbox.html #}
   <div id="searchbox"></div>
   ```

   This replaces the theme's `searchbox.html` template with an empty `div` element.

1. Update your Sphinx configuration:

   ```python
   # conf.py
   template_path = ["_templates"] 
   docsearch_container = "#searchbox"
   ```

## Add custom CSS

To modify the style of the DocSearch search box and modal dialog, you can add custom CSS files to your project:

1. Create a new directory in your Sphinx project, such as `_static/`.
1. Create a new CSS file with styles you want to change:

   ```css
   /* _static/custom.css */
   :root {
     --docsearch-primary-color: #d83fe0;
   }
   .DocSearch-Button {
     border-radius: 0; 
   }
   ```

   You can change many styles of the DocSearch UI with [CSS custom properties](https://github.com/algolia/docsearch/blob/main/packages/docsearch-css/src/_variables.css).

1. Update your Sphinx configuration:

   ```python
   # conf.py
   html_static_path = ["_static"]
   html_css_files = ["custom.css"]
   ```
