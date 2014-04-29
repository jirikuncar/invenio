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

from wtforms import validators

from invenio.base.i18n import _
from invenio.modules.deposit.form import WebDepositForm
from invenio.modules.deposit import fields
from invenio.modules.deposit.field_widgets import \
    ExtendedListWidget, \
    ColumnInput, ItemWidget
from invenio.modules.deposit.validation_utils import list_length


from .visualization_base import (visualization_base, VisualizationForm,
                                 filter_empty_helper)


class ColumnInlineForm(WebDepositForm):
    """Column inline form"""

    id = fields.TextField(
        placeholder="Column name",
        widget_classes='form-control',
        widget=ColumnInput(class_="col-xs-4"),
    )

    label = fields.TextField(
        placeholder="Label",
        widget_classes='form-control',
        widget=ColumnInput(class_="col-xs-6"),
    )


class D3BarChartForm(VisualizationForm):
    """D3 Bar Chart visualization form"""
    #
    # Fields
    #

    columns = fields.DynamicFieldList(
        fields.FormField(
            ColumnInlineForm,
            widget=ExtendedListWidget(
                item_widget=ItemWidget(),
                html_tag='div',
            ),
        ),
        label=_('Columns'),
        add_label=_('Add another column'),
        icon='fa fa-columns fa-fw',
        min_entries=2,
        widget_classes='',
        validators=[validators.Required(), list_length(
            min_num=2, max_num=2, element_filter=filter_empty_helper(['id']),
        )],
    )

    resource = fields.TextField(
        placeholder="URL",
        widget_classes='form-control',
        label=_('Resource'),
        icon='fa fa-globe fa-fw',
        export_key='resource',
        validators=[validators.Required(), ],
    )
    #
    # Form configuration
    #
    _title = _('New D3 Bar Chart View')

    @property
    def groups(self):
        return super(D3BarChartForm, self).groups + [
            (_('Configuration'), ['resource', 'columns', ], {
                'indication': 'required'
            }),
        ]


#
# Workflow
#
class d3_bar_chart(visualization_base):
    """D3 Bar Chart visualization"""

    name = "D3 Bar Chart View"
    name_plural = "D3 Bar Chart Views"
    draft_definitions = {
        'default': D3BarChartForm,
    }
