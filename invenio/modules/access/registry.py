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

from flask.ext.registry import ModuleAutoDiscoveryRegistry, RegistryProxy

from invenio.ext.registry import ModuleAutoDiscoverySubRegistry
from invenio.utils.datastructures import LazyDict


def wrap(module):
    """Checks module for attributes name and description."""
    if not hasattr(module, 'name'):
        setattr(module, 'name', module.__name__.split('.')[-1])
    if not hasattr(module, 'description'):
        setattr(module, 'description', module.__doc__ or '')
    return module


def create_mapping(proxy, wrapper=wrap):
    """Creates mapping for given proxy."""
    def generator():
        out = {}
        for obj in map(wrapper, proxy):
            if obj.name not in out:
                out[obj.name] = obj
        return out
    return LazyDict(generator)

aclext = RegistryProxy('aclext', ModuleAutoDiscoveryRegistry, 'aclext')

roles_proxy = RegistryProxy('aclext.roles', ModuleAutoDiscoverySubRegistry,
                            'roles', registry_namespace=aclext)

roles = create_mapping(roles_proxy)

actions_proxy = RegistryProxy('aclext.actions', ModuleAutoDiscoverySubRegistry,
                              'actions', registry_namespace=aclext)

actions = create_mapping(actions_proxy)
