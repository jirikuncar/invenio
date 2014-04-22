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
    invenio.modules.visualizations.views
    ------------------------------------

    Visualization interface.
"""

from flask import Blueprint, render_template
from flask.ext.breadcrumbs import default_breadcrumb_root, register_breadcrumb
# from flask.ext.menu import register_menu

from invenio.base.i18n import _

from . import api
from .errors import VisualizationError

blueprint = Blueprint("visualizations", __name__, url_prefix="/visualization",
                      template_folder="templates", static_folder="static")

default_breadcrumb_root(blueprint, ".visualizations")


@blueprint.errorhandler(VisualizationError)
def errorhandler(error):
    return render_template('404.html'), 404


@blueprint.route("/view/<uuid>", methods=["GET"])
@register_breadcrumb(blueprint, '.', _('Visualizations'))
def view(uuid):
    visualization = api.Visualization.get_visualization(uuid)
    return render_template(
        ['visualizations/{0}.html'.format(
            visualization.model_info['names'][0]),
         'visualizations/view.html'], visualization=visualization)
