# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2013 CERN.
##
## Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

"""Visualization Config administration interface"""


#from flask.ext.admin import expose
from invenio.adminutils import InvenioModelView
from invenio.sqlalchemyutils import db
from invenio.webvisualize_model import VslConfig
from wtforms.fields import SelectField


class VslConfigAdmin(InvenioModelView):
    _can_create = True  
    _can_edit = True
    _can_delete = True

    #inline_models = [PidLog]
    form_overrides = dict(graph_type=SelectField)
    form_args = dict(
        # Pass the choices to the `SelectField`
        graph_type=dict(
            choices=[('grid', 'Grid'), ('graph', 'Graph'), ('map', 'Map')]
        ))

    column_list = ('name','title', 'creator', 'graph_type','description', 'config')
    page_size = 100

    def __init__(self, model, session, **kwargs):
        super(VslConfigAdmin, self).__init__(model, session, **kwargs)

def register_admin(app, admin):
    """
    Called on app initialization to register administration interface.
    """
    admin.add_view(VslConfigAdmin(VslConfig, db.session, name='VslConfig', category="Web Visualizer"))
