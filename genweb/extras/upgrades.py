# -*- coding: utf-8 -*-
import logging

from Products.CMFCore.utils import getToolByName


PROFILE_ID = 'profile-genweb.extras:default'
LOGGER = 'genweb.extras'


def update_rolemap_tool(context, logger=None):
    if logger is None:
        logger = logging.getLogger(LOGGER)
    setup = getToolByName(context, 'portal_setup')
    setup.runImportStepFromProfile(PROFILE_ID, 'rolemap')
