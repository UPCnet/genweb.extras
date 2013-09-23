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


class GenwebExtrasTesting(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # load ZCML
        import genweb.extras
        xmlconfig.file('configure.zcml', genweb.extras,
                       context=configurationContext)

    def setUpPloneSite(self, portal):
        # install into the Plone site
        applyProfile(portal, 'genweb.extras:default')


GENWEBEXTRAS_FIXTURE = GenwebExtrasTesting()
GENWEBEXTRAS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(GENWEBEXTRAS_FIXTURE, ),
    name='GenwebExtrasLayer:Integration'
)
GENWEBEXTRAS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(GENWEBEXTRAS_FIXTURE, ),
    name='GenwebExtrasLayer:Functional'
)

optionflags = (doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE)
