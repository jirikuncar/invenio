# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2013, 2014 CERN.
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

"""
    invenio.modules.filemanager.views
    ---------------------------------

    File Manager interface.
"""

from flask import request, abort, make_response, Blueprint

from .registry import fileactions_lookup

blueprint = Blueprint('filemanager', __name__, url_prefix="/filemanager")


@blueprint.route('/<action>', methods=['GET'])
def perform(action):
    """Perform file action."""
    files = request.values.getlist('file')
    if action in fileactions_lookup:
        try:
            content, mimetype = fileactions_lookup[action](
                files=files, params=request.values)
            response = make_response(content)
            response.mimetype = mimetype
            return response
        except:
            return abort(400)
    return abort(406)
