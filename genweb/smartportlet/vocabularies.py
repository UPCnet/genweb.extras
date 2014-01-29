from zope.component import getAdapters
from zope.interface import implements
from zope.schema.interfaces import IVocabularyFactory

from plone.app.portlets.portlets.base import Renderer
from genweb.smartportlet.renderers.interfaces import IPortletContainerRenderer
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


class AvailablePortletContainerRenderers(object):
    """Vocabulary factory for workflow states.
    """
    implements(IVocabularyFactory)

    def __call__(self, context):
        DummyRenderer = Renderer(context, None, None, None, None)
        renderers = [a for a in getAdapters((DummyRenderer,),IPortletContainerRenderer)]
        terms = [SimpleTerm(k, title=v.title) for k, v in renderers]
        return SimpleVocabulary(terms)

AvailablePortletContainerRenderersFactory = AvailablePortletContainerRenderers()
