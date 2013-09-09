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

"""WebVisualize Flask Blueprint"""


from flask import render_template, flash, redirect, url_for, abort, jsonify

from invenio.webinterface_handler_flask_utils import _, InvenioBlueprint
from invenio.webuser_flask import current_user

from invenio.sqlalchemyutils import db
from invenio.webvisualize_model import VslConfig
from invenio.webvisualize_forms import AddVisualizationForm
from invenio.websession_model import User

# Just for visualize/navigation
from invenio.websearch_model import Collection


blueprint = InvenioBlueprint('webvisualize', __name__,
                             url_prefix="/visualize",
                             #config='invenio.webcomment_config',
                             breadcrumbs=[(_('Visualizations'),
                                           'webvisualize.index')],
                             menubuilder=[('personalize.comment_subscriptions',
                                           _('Your comment subscriptions'),
                                           'webvisualize.index', 20)])

from invenio.importutils import autodiscover_modules
_VISUALIZERS = dict(map(lambda v: (v.Visualizer.graph_type, v.Visualizer),
                        autodiscover_modules(['invenio'], 
                        related_name_re=".+_webvisualizer\.py")))

@blueprint.invenio_set_breadcrumb(_("View"))
@blueprint.route('/view/<cid>', methods=['GET'])
#@blueprint.invenio_authenticated
def view(cid): 
    vc = VslConfig.query.get(cid)
    if vc and vc.graph_type in _VISUALIZERS and (current_user.get_id() == vc.id_creator 
                                                 or vc.is_public):
        visualizer = _VISUALIZERS[vc.graph_type]()
        return render_template(visualizer.template, visualize_config=vc, 
                               visualizer=visualizer)
    #No visualizer or not creator of the visualization        
    return redirect(url_for('webvisualize.index'))

@blueprint.route('/dataset/<name>.json', methods=['GET'])
def dataset(name):
    vc = VslConfig.query.filter_by(name=name).first()
    return jsonify(vc.json_config) if vc else abort(404)

@blueprint.route('/', methods=['GET'])
@blueprint.invenio_authenticated
def index():
    user = User.query.get(current_user.get_id())
    public_vsl_configs = VslConfig.query.filter_by(visibility='public')

    # Merge user's visualizations and public ones without duplicates
    all_vsl_configs = user.visualization_configs + list(set(public_vsl_configs) 
                                                - set(user.visualization_configs))
    return render_template('webvisualize_index.html', vsl_configs=all_vsl_configs)

@blueprint.route('/new', methods=['GET', 'POST'])
@blueprint.invenio_authenticated
def new():
    form = AddVisualizationForm()
    if form.validate_on_submit():
        try:
            v = VslConfig()
            v.create_from_form(data=form.data, id_user=current_user.get_id())
            db.session.add(v)
            db.session.commit()
            flash(_('Visualization was added'), "info")
            return redirect(url_for('webvisualize.index'))
        except:
            db.session.rollback()
            abort(400)

    return render_template('webvisualize_new.html', form=form)

@blueprint.route('/navigate', methods=['GET'])
def navigate():
    """
    Simulates the navigation through the Collection Tree using an interactive
    BubbleTree tree
    """
    import json
    def generate_tree(root, level=0):
        if level < 4:
            tree = {
                'id': 'collection-bubble-' + str(root.id),
                'name': root.name,
                'label': root.name,
                'amount': root.nbrecs,
                'color': '#119ce2', # "invenio" blue as default color
                'children': [generate_tree(node, level+1) for node in root.collection_children]}
            if not len(tree['children']) or not tree['amount']:
                del(tree['children'])
            return tree

    tree = generate_tree(Collection.query.get(1)) # id=1 is the root of all collections
    return render_template('webvisualize_bubbletree_navigate.html', 
                                ds_tree=json.dumps(tree))
