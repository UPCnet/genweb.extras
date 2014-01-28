# -*- coding: utf-8 -*-
import doctest
from plone.app.testing import (
    applyProfile,
    PLONE_FIXTURE,
    PloneSandboxLayer,
)
from plone.app.testing.layers import (
    FunctionalTesting,
    IntegrationTesting,
)
from Products.CMFCore.utils import getToolByName
from zope.configuration import xmlconfig


class GenwebSmartPortletTesting(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # load ZCML
        import genweb.smartportlet
        xmlconfig.file('configure.zcml', genweb.smartportlet,
                       context=configurationContext)

    def setUpPloneSite(self, portal):
        # install into the Plone site
        applyProfile(portal, 'genweb.smartportlet:default')


GENWEBEXTRAS_FIXTURE = GenwebSmartPortletTesting()
GENWEBEXTRAS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(GENWEBEXTRAS_FIXTURE, ),
    name='GenwebSmartPortletLayer:Integration'
)
GENWEBEXTRAS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(GENWEBEXTRAS_FIXTURE, ),
    name='GenwebSmartPortletLayer:Functional'
)

optionflags = (doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE)
