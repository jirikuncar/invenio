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
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

"""FileManager Flask Blueprint"""

from flask import request, abort, make_response
from invenio.webinterface_handler_flask_utils import _, InvenioBlueprint
#from werkzeug.utils import secure_filename
from invenio.importutils import autodiscover_modules


blueprint = InvenioBlueprint('filemanager', __name__,
                             url_prefix="/filemanager",
                             #config='invenio.webcomment_config',
                             breadcrumbs=[(_('Visualizations'),
                                           'webvisualize.index')],
                             menubuilder=[('personalize.comment_subscriptions',
                                           _('Your comment subscriptions'),
                                           'webvisualize.index', 20)])

_ACTIONS = dict(map(lambda f: (f.FileAction.name, f.FileAction),
                                autodiscover_modules(['invenio'], 
                                    related_name_re=".+_fileaction\.py")))

@blueprint.route('/', methods=['GET'])
def perform():
    files = request.values.getlist('file')
    action = request.values.get('action')
    if action in _ACTIONS:
        try: 
            content, mimetype = _ACTIONS.get(action)()(files=files, 
                                                params=request.args)
            response = make_response(content)
            response.mimetype = mimetype
            return response
        except:
            return abort(400)        
    return abort(406)