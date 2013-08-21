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

"""FileManager helper methods"""

from invenio.cache import cache
import zlib

class FileManagerCache(object):

    def __init__(self, engine=cache):
        self.engine = engine

    def _get_cache_key(self, params):
        """
        Calculates a string from the params, 
        to be used as a key in the cache

        """
        import hashlib
        m = hashlib.md5()
        query = []
        for key in sorted(params.keys()):
            query.append(key)
            query.append(params[key])
        m.update(''.join(query))
        return m.hexdigest()

    def get(self, params):
        """
        Get the element from the cache whose key is calculated from the params. 
        Elements are stored compressed so it is necessary to decompress 
        it before returning it.

        @param params: Params in the request
        
        """
        cached = self.engine.get(self._get_cache_key(params))
        return zlib.decompress(cached) if cached else None

    def set(self, params, obj):
        """
        Store 'obj' in the cache. 
        The key is calculated from the params

        @param params: Params in the request, for calculating the key
        @param obj: Object to be stored
        
        """
        self.engine.set(self._get_cache_key(params), zlib.compress((obj)))

class FileManagerAction(object):
    def __init__(self, cache=FileManagerCache):
        self.cache = cache()

    def __call__(self, *args, **kwargs):
        params = kwargs.get('params')
        data = self.cache.get(params)
        if not data:
            data = self.action(*args, **kwargs)
            self.cache.set(params, data)
        return data, self.response_mimetype
    
    def action(self, *args, **kwargs):
        raise 'Needs to be implemented'