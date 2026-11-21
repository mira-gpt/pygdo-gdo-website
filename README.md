# pygdo-gdo-website

The GDO project's introductory website, built as a PyGDO module. The public
overview introduces the modular foundation and links to the PyGDO repository
and documentation. Module-license offerings are planned, not yet available.

Place this repository at `gdo/gdo_website` in a PyGDO installation and install
the module using the normal PyGDO administration workflow. The overview is at
`/gdo_website.overview.html`; selecting a site-wide homepage remains a separate
deployment decision. This repository does not enable purchases or payments.

See [LICENSE](LICENSE) for this module's license. Other modules have their own
licenses.

The installation hook seeds `GDO_GDOMod` from modules present under this
PyGDO checkout's `gdo/` directory and a sibling PHPGDO checkout's `GDO/`
directory. It adds missing entries without overwriting existing prices; if the
PHP checkout is absent, PHP entries cannot be discovered on that installation.
Each new entry gets clearly marked placeholder monthly/yearly/lifetime prices
of 1.99 / 19.99 / 99.99. Currency and final commercial pricing are not set.
The separate `pygdo_all_lifetime_price` module setting defaults to 9001; it is
not an individual module price. Catalog rows do not provide purchasing,
payment, license issuance or access control.
