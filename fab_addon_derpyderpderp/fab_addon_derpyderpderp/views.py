from pathlib import Path

from flask_appbuilder import BaseView, expose

"""
    Create your Views (but don't register them here, do it on the manager::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)

    
"""


class MyView(BaseView):
    default_view = "derpderp"
    template_folder = Path(__file__).absolute().parent / "templates"

    @expose("/derpderp")
    def derpderp(self):
        self.update_redirect()
        return self.render_template("derp.html")
