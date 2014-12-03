# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2014 CERN.
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

"""Relationship API."""

import six

from uuid import uuid4
from sqlalchemy.orm.util import identity_key

from invenio.ext.sqlalchemy import db, utils

from .models import Relationship as Model


class NodeInterfaceMeta(type):

    """Define graph node interface."""

    def __init__(cls, name, bases, dct):
        if not hasattr(cls, 'registry'):
            cls.registry = {}
        else:
            interface_id = getattr(cls, '__nodename__', name)
            if interface_id in cls.registry:
                raise RuntimeError(
                    "Node registry already contains {}".format(name))
            cls.registry[interface_id] = cls
            cls.class_map[cls] = interface_id

        super(NodeInterfaceMeta, cls).__init__(name, bases, dct)


@six.with_metaclass(NodeInterfaceMeta)
class Node(object):

    """Base class for graph vertex."""

    def get_node_model(self):
        """Return model name this node."""
        return self.__class__.class_map[self.__class__]

    def get_node_id(self):
        """Return model id of this node."""
        if not isinstance(self, db.Model):
            raise NotImplemented
        dummy, pks_ = identity_key(self)
        assert len(pks_) == 1
        return pks_[0]

    def source_for(self, link_type=None):
        """Return nodes for which this node is source."""
        raise NotImplemented

    def destination_for(self, link_type=None):
        """Return nodes for which this node is destination."""
        raise NotImplemented


class Relationship(object):

    """Base class for graph edge."""

    def __init__(self, from_node, link_type, to_node):
        self.data = {}
        self.data['uuid'] = uuid4()
        self.data['link_type'] = link_type
        if from_node is not None:
            self.data['model_from'] = from_node.get_node_model()
            self.data['id_from'] = from_node.get_node_id()
        if to_node is not None:
            self.data['model_to'] = to_node.get_node_model()
            self.data['id_to'] = to_node.get_node_id()

    @utils.session_manager
    def save(self):
        db.session.add(Model(**self.data))

    @classmethod
    @utils.session_manager
    def save_all(cls, data, *args):
        if data is isinstance(cls):
            args = [data]
        else:
            args = [data] + list(args)
        for data in args:
            db.session.add(Model(**data.data))
