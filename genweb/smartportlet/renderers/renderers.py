from five.grok import adapter
from five.grok import implementer
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.interfaces import IContentish
from genweb.smartportlet.renderers.interfaces import IPortletItemRenderer
from genweb.smartportlet.renderers import PortletItemRenderer


@adapter(IContentish)
@implementer(IPortletItemRenderer)
class DefaultPortletItemRenderer(PortletItemRenderer):
    template = ViewPageTemplateFile('templates/default.pt')
    css_class = 'contentish-item'