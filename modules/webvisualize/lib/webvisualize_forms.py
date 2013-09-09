# -*- coding: utf-8 -*-
#
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
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02D111-1307, USA.

"""
Webvisualize forms.
"""
from invenio.webinterface_handler_flask_utils import _
from invenio.wtforms_utils import InvenioBaseForm
from wtforms import validators, TextField, SelectField, RadioField

class AddVisualizationForm(InvenioBaseForm):
    """
    Form for creating a new visualization
    """
    name = TextField(_('Name'), [validators.Required()])
    title = TextField(_('Title'), [validators.Required()])
    description = TextField(_('Description'), [validators.Optional()])
    graph_type = SelectField(_('Graph type'), choices=[('grid', 'Grid'),
                                                       ('graph', 'Graph'), 
                                                       ('map', 'Map'), 
                                                       ('bubbletree', 'Tree')])
    visibility = RadioField(_('Visibility'), choices=[('public','Public'), 
                                                      ('private','Private')])
    url_file = TextField(_('File URL'), [validators.Required(), 
                                        validators.URL(require_tld=False)])
