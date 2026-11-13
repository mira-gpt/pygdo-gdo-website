import unittest
from unittest.mock import patch

from gdo.gdo_website.method.overview import overview


class OverviewTest(unittest.TestCase):
    def test_intro_and_future_licensing(self):
        with patch('gdo.base.Application.Application.get_mode', return_value=None):
            html = overview().gdo_execute().render_html()
        self.assertIn('Build things', html)
        self.assertIn('github.com/gizmore/pygdo', html)
        self.assertIn('licenses for various modules in the future', html)
        self.assertNotIn('<form', html)
