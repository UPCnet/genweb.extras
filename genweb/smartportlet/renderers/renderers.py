from five.grok import adapter
from five.grok import implementer
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.interfaces import IContentish
from plone.app.portlets.portlets.base import IPortletRenderer
from genweb.smartportlet.renderers.interfaces import IPortletItemRenderer
from genweb.smartportlet.renderers.interfaces import IPortletContainerRenderer
from genweb.smartportlet.renderers import PortletItemRenderer
from genweb.smartportlet.renderers import PortletContainerRenderer


@adapter(IContentish)
@implementer(IPortletItemRenderer)
class DefaultPortletItemRenderer(PortletItemRenderer):
    template = ViewPageTemplateFile('templates/item_default.pt')
    css_class = 'contentish-item'


@adapter(IPortletRenderer, name='li_container_renderer')
@implementer(IPortletContainerRenderer)
class ListPortletContainerRenderer(PortletContainerRenderer):
    title = "View with items wrapped in ul > li"
    template = ViewPageTemplateFile('templates/container_li.pt')
    css_class = 'portlet-container-list'    


@adapter(IPortletRenderer, name='div_container_renderer')
@implementer(IPortletContainerRenderer)
class DivPortletContainerRenderer(PortletContainerRenderer):
    title = "View with items wrapped in div > div"
    template = ViewPageTemplateFile('templates/container_div.pt')
    css_class = 'portlet-container-div'        