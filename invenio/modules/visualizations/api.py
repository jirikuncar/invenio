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
    invenio.modules.visualizations.api
    ----------------------------------

    Visualizations API

    Following example shows how to handle visualizations metadata::

        >>> from flask import g
        >>> from invenio.base.factory import create_app
        >>> app = create_app()
        >>> ctx = app.test_request_context()
        >>> ctx.push()
        >>> from invenio.modules.visualizations import api
        >>> from invenio.modules.jsonalchemy.jsonext.engines import memory
        >>> app.config['VISUALIZATIONS_ENGINE'] = \
        "invenio.modules.jsonalchemy.jsonext.engines.memory:MemoryStorage"
        >>> d = api.Visualization.create({'title': 'Title 1'})
        >>> d['title']
        'Title 1'
        >>> d['creator']
        0
        >>> d['title'] = 'New Title 1'
        >>> d = d.update()
        >>> api.Visualization.get_visualization(d['_id'])['title']
        'New Title 1'
        >>> ctx.pop()
"""

from datetime import datetime

from invenio.modules.jsonalchemy.wrappers import SmartJson
from invenio.modules.jsonalchemy.reader import Reader

from . import signals, errors


class Visualization(SmartJson):
    """Visualization"""

    __storagename__ = 'visualizations'

    @classmethod
    def create(cls, data, model='visualization_base', master_format='json',
               **kwargs):
        visualization = Reader.translate(
            data, cls, master_format=master_format, model=model,
            namespace='visualizationext', **kwargs)
        cls.storage_engine.save_one(visualization.dumps())
        signals.visualization_created.send(visualization)
        return visualization

    @classmethod
    def get_visualization(cls, uuid, include_deleted=False):
        """Returns visualization instance identified by UUID.

        :returns: a :class:`Visualization` instance.
        :raises: :class:`~.invenio.modules.visualizations.errors.\
            VisualizationNotFound`
            or :class:`~invenio.modules.visualizations.errors.\
            DeletedVisualization`
        """
        try:
            visualization = cls(cls.storage_engine.get_one(uuid))
        except:
            raise errors.VisualizationNotFound

        if not include_deleted and visualization['deleted']:
            raise errors.DeletedVisualization
        return visualization

    def _save(self):
        try:
            return self.__class__.storage_engine.update_one(self.dumps(),
                                                            id=self['_id'])
        except:
            return self.__class__.storage_engine.save_one(self.dumps(),
                                                          id=self['_id'])

    def update(self):
        """Update visualization object."""
        #FIXME This should be probably done in model dump.
        self['modification_date'] = datetime.now()
        return self._save()

    def delete(self):
        """Deletes the instance of visualization."""
        self['deleted'] = True
        self._save()
