# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2012, 2013, 2014 CERN.
#
# Invenio is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

from __future__ import absolute_import, print_function

from flask import url_for, redirect
from wtforms import validators, widgets

from invenio.base.i18n import _
from invenio.modules.deposit.form import WebDepositForm
from invenio.modules.deposit import fields
from invenio.modules.deposit.filter_utils import strip_string, sanitize_html
from invenio.modules.deposit.field_widgets import \
    ExtendedListWidget, CKEditorWidget, \
    ColumnInput, ItemWidget
from invenio.modules.deposit.validation_utils import list_length
from invenio.modules.deposit.processor_utils import set_flag
from invenio.modules.deposit.models import DepositionType
from invenio.modules.deposit.tasks import (
    render_form, prefill_draft, prepare_sip, process_sip_metadata)
from invenio.utils.text import slugify

from ..tasks import create_visualization


#
# Helpers
#
def filter_empty_helper(keys=None):
    """ Remove empty elements from a list"""

    def _inner(elem):
        if isinstance(elem, dict):
            for k, v in elem.items():
                if (keys is None or k in keys) and v:
                    return True
            return False
        else:
            return bool(elem)
    return _inner


def generate_slug(target_field):
    """Generate slug and store it to target field"""

    def generator(form, field, submit=False, fields=None):
        if not getattr(form, target_field).flags.touched:
            getattr(form, target_field).data = slugify(field.data.lower())
    return generator


#
# Forms
#
class VisualizationForm(WebDepositForm):
    """Visualization form"""
    #
    # Fields
    #

    title = fields.TextField(
        label=_('Title'),
        export_key='title',
        icon='fa fa-book fa-fw',
        widget_classes="form-control",
        processors=[generate_slug('name')]
        # validators=[validators.Required()],
    )

    description = fields.TextAreaField(
        label=_("Description"),
        description=_('Required.'),
        default='',
        icon='fa fa-pencil fa-fw',
        # validators=[validators.required(), ],
        widget=CKEditorWidget(
            toolbar=[
                ['PasteText', 'PasteFromWord'],
                ['Bold', 'Italic', 'Strike', '-',
                    'Subscript', 'Superscript', ],
                ['NumberedList', 'BulletedList'],
                ['Undo', 'Redo', '-', 'Find', 'Replace', '-', 'RemoveFormat'],
                ['SpecialChar', 'ScientificChar'], ['Source'], ['Maximize'],
            ],
            disableNativeSpellChecker=False,
            extraPlugins='scientificchar',
            removePlugins='elementspath',
        ),
        filters=[
            sanitize_html,
            strip_string,
        ],
    )

    name = fields.TextField(
        label=_('Name'),
        description=_('short url-usable (and preferably human-readable) '
                      'name of the package'),
        export_key='name',
        icon='fa fa-thumb-tack fa-fw',
        widget_classes="form-control",
        processors=[set_flag('touched')],
        # validators=[validators.Required()],
        validators=[validators.Required()],
    )

    license = fields.SelectField(
        choices=[('gpl', 'GNU/GPLv1'), ('xxx', 'XXX')],
        label=_('License'),
        icon='fa fa-certificate fa-fw',
        widget_classes="form-control",
    )


    #
    # Form configuration
    #
    _title = _('New Visualization View')
    _subtitle = 'Instructions: (i) Press "Save" to save your upload for '\
                'editing later, as many times you like. (ii) Upload or remove'\
                ' extra files in the bottom of the form. (iii) When ready, '\
                'press "Submit" to finalize your upload.'

    groups = [
        (_('Basic Information'), ['title', 'description', 'name', 'license', ], {
            'indication': 'required',
        }),
    ]


#
# Workflow
#
class visualization_base(DepositionType):
    """Visualization workflow"""

    group = "Visualizations"
    draft_definitions = {
        'default': VisualizationForm,
    }

    workflow = [
        # Pre-fill draft with values passed in from request
        prefill_draft(draft_id='default'),
        # Render form and wait for user to submit
        render_form(draft_id='default'),
        # Create the submission information package by merging form data
        # from all drafts (in this case only one draft exists).
        prepare_sip(),
        # Process metadata to match your JSONAlchemy model. This will
        # call process_sip_metadata() on your subclass.
        process_sip_metadata(),
        # Create visualization instance
        create_visualization(),
    ]

    @classmethod
    def render_completed(cls, d):
        """
        Page to render when deposition was successfully completed.
        """
        return redirect(url_for('visualizations.view',
                                uuid=d.get_latest_sip().package['_id']))

    @classmethod
    def process_sip_metadata(cls, deposition, metadata):
        """Custom sip processing"""
        if 'fft' in metadata:
            del metadata['fft']
