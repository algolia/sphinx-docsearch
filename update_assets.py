"""
Update DocSearch assets from jsDelivr.

This extension bundles the JavaScript and CSS for DocSearch.
This module downloads the latest version of these assets from
the jsDelivr CDN.
"""
import httpx
from pathlib import Path
import re

def update_docsearch_assets() -> None:
    """Update the DocSearch assets."""
    for package in ["@docsearch/js", "@docsearch/css"]:
        _download_asset(package)

def _download_asset(package: str) -> None:
    """Download an asset from jsDelivr."""
    cdn_uri = f"https://cdn.jsdelivr.net/npm/{package}@latest/{_jsdelivr_file_name(package)}"
    response = httpx.get(cdn_uri)
    output = package.replace("@", "").replace("/", ".")
    output_path = Path("src/sphinx_docsearch/static/").resolve()
    with open(Path(output_path / output).absolute(), "w") as f:
        f.write(re.sub(r"//#.*\n$", "", response.text))


def _jsdelivr_file_name(package: str) -> str:
    """Get the filename for an asset on jsDelivr from NPM."""
    npm_uri = f"https://registry.npmjs.org/{package}/latest"
    return httpx.get(npm_uri).json()["jsdelivr"]

if __name__ == "__main__":
    update_docsearch_assets()
