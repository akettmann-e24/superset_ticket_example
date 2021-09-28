import logging

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from flask_appbuilder import AppBuilder
from flask_appbuilder.basemanager import BaseManager
from flask_babel import lazy_gettext as _
from fab_addon_derpyderpderp.views import MyView


log = logging.getLogger(__name__)

"""
   Create your plugin manager, extend from BaseManager.
   This will let you create your models and register your views
   
"""


class MyAddOnManager(BaseManager):
    def __init__(self, appbuilder):
        """
        Use the constructor to setup any config keys specific for your app.
        """
        super(MyAddOnManager, self).__init__(appbuilder)

    def register_views(self):
        """
        This method is called by AppBuilder when initializing, use it to add you views
        """
        self.appbuilder: "AppBuilder"
        self.appbuilder.add_view(
            MyView,
            "MyView",
            category="MyAddonCategory",
            category_label="MyAddonCategory",
            category_icon="air-freshener",
        )

    def pre_process(self):
        pass

    def post_process(self):
        pass
