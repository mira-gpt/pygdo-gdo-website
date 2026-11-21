from pathlib import Path

from gdo.base.Application import Application
from gdo.gdo_website.GDO_GDOMod import GDO_GDOMod


class InstallGDOMods:
    """Seed missing local modules without changing any existing prices."""

    PLACEHOLDER_PRICES = {
        'gdomod_monthly_price': '1.99',
        'gdomod_yearly_price': '19.99',
        'gdomod_lifetime_price': '99.99',
    }

    @staticmethod
    def discover(pygdo_root, phpgdo_root):
        found = set()
        roots = (('pygdo', Path(pygdo_root) / 'gdo', 'module_', '.py'),
                 ('phpgdo', Path(phpgdo_root) / 'GDO', 'Module_', '.php'))
        for framework, root, prefix, suffix in roots:
            if not root.is_dir():
                continue
            for directory in root.iterdir():
                if not directory.is_dir():
                    continue
                name = directory.name
                if not name.isascii() or len(name) > 96:
                    continue
                # PHP also has provider repositories such as phpgdo-mysql
                # containing Module_DBMS.php; keep their directory identity.
                entry = directory / (prefix + name + suffix)
                if entry.is_file() or (framework == 'phpgdo' and
                                       any(p.is_file() for p in directory.glob('Module_*.php'))):
                    found.add((framework, name))
        return sorted(found)

    @classmethod
    def now(cls):
        root = Path(Application.file_path()).resolve()
        # A missing sibling PHP checkout is valid; no absent catalog entries are invented.
        return cls.seed(cls.discover(root, root.parent / 'phpgdo'))

    @classmethod
    def seed(cls, modules):
        table = GDO_GDOMod.table()
        added = 0
        for framework, name in modules:
            key = {'gdomod_framework': framework, 'gdomod_name': name}
            if not table.get_by_vals(key):
                GDO_GDOMod.blank({**key, **cls.PLACEHOLDER_PRICES}).insert()
                added += 1
        return added
