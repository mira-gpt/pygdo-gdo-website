import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from gdo.gdo_website.GDO_GDOMod import GDO_GDOMod
from gdo.gdo_website.InstallGDOMods import InstallGDOMods
from gdo.gdo_website.module_gdo_website import module_gdo_website


class GDOModTest(unittest.TestCase):
    def test_discovers_both_frameworks_and_skips_non_modules(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            py = root / 'pygdo' / 'gdo' / 'quote'
            php = root / 'phpgdo' / 'GDO' / 'Quote'
            py.mkdir(parents=True)
            php.mkdir(parents=True)
            (py / 'module_quote.py').touch()
            (php / 'Module_Quote.php').touch()
            provider = root / 'phpgdo' / 'GDO' / 'phpgdo-mysql'
            provider.mkdir()
            (provider / 'Module_DBMS.php').touch()
            (root / 'pygdo' / 'gdo' / 'not_a_module').mkdir()
            self.assertEqual([('phpgdo', 'Quote'), ('phpgdo', 'phpgdo-mysql'), ('pygdo', 'quote')],
                             InstallGDOMods.discover(root / 'pygdo', root / 'phpgdo'))
            self.assertEqual([('pygdo', 'quote')],
                             InstallGDOMods.discover(root / 'pygdo', root / 'absent'))

    def test_seed_only_inserts_missing_rows(self):
        table = Mock()
        table.get_by_vals.side_effect = [object(), None]
        blank = Mock()
        with patch.object(GDO_GDOMod, 'table', return_value=table), \
             patch.object(GDO_GDOMod, 'blank', return_value=blank) as make:
            self.assertEqual(1, InstallGDOMods.seed([('pygdo', 'existing'), ('phpgdo', 'New')]))
        make.assert_called_once_with({'gdomod_framework': 'phpgdo', 'gdomod_name': 'New',
                                     **InstallGDOMods.PLACEHOLDER_PRICES})
        blank.insert.assert_called_once()

    def test_bundle_price_default_and_model_registration(self):
        module = module_gdo_website()
        self.assertIn(GDO_GDOMod, module.gdo_classes())
        config = {item.get_name(): item for item in module.gdo_module_config()}
        self.assertEqual('9001', config['pygdo_all_lifetime_price']._initial)
