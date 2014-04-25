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

"""FileManager helper methods"""

import hashlib
import zlib

from invenio.ext.cache import cache


class FileManagerCache(object):

    def __init__(self, engine=cache):
        self.engine = engine

    def _get_cache_key(self, params):
        """Calculates cache key from the parameters."""
        m = hashlib.md5()
        query = []
        for key in sorted(params.keys()):
            query.append(key)
            query.append(params[key])
        m.update(''.join(query))
        return m.hexdigest()

    def get(self, params):
        """Gets the element from the cache identified by parameters.

        Elements are stored compressed so it is necessary to decompress
        it before returning it.

        :param params: Parameters in the request.
        """
        try:
            cached = self.engine.get(self._get_cache_key(params))
            return zlib.decompress(cached) if cached else None
        except:
            return None

    def set(self, params, obj):
        """
        Store 'obj' in the cache.
        The key is calculated from the params

        :param params: Parameters in the request, for calculating the key.
        :param obj: Object to be stored.
        """
        try:
            self.engine.set(self._get_cache_key(params), zlib.compress((obj)))
        except:
            pass


class FileManagerAction(object):
    """File Manager Action"""

    def __init__(self, cache=FileManagerCache):
        self.cache = cache()

    def __call__(self, *args, **kwargs):
        params = kwargs.get('params')
        data = None
        data = self.cache.get(params)
        if data is None:
            data = self.action(*args, **kwargs)
            self.cache.set(params, data)
        return data, self.response_mimetype

    def action(self, *args, **kwargs):
        raise NotImplementedError()
