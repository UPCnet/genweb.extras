# -*- coding: utf-8 -*-
import unittest2 as unittest

from Products.CMFCore.utils import getToolByName

from genweb.extras.testing import (
    GENWEBEXTRAS_INTEGRATION_TESTING,
)


class TestExample(unittest.TestCase):

    layer = GENWEBEXTRAS_INTEGRATION_TESTING

    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.qi_tool = getToolByName(self.portal, 'portal_quickinstaller')

    def test_product_is_installed(self):
        """ Validate that genweb.extras has been installed
        """
        pid = 'genweb.extras'
        installed = [p['id'] for p in self.qi_tool.listInstalledProducts()]
        self.assertTrue(pid in installed,
                        'genweb.extras appears not to have been installed')
