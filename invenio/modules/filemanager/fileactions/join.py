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

"""FileManager join action."""

import csv
import requests

from six import StringIO

from ..utils import FileManagerAction


class FileAction(FileManagerAction):
    """File Action plugin implementation."""

    accepted_mimetypes = ['text/plain', 'text/csv']
    response_mimetype = 'text/csv'

    def action(self, *args, **kwargs):
        """Merges several csv files in one.

        :note: All files must have the same header.
        """
        files = kwargs.get('files')
        if not files or len(files) < 2:
            raise Exception('Two o more files needed to join!')

        data = StringIO()
        result = csv.writer(data, quoting=csv.QUOTE_MINIMAL)
        previous_header = None
        for filename in files:
            response = requests.get(filename)
            # Check if mimetype is accepted
            mimetype = response.headers.get('content-type')
            if mimetype not in self.accepted_mimetypes:
                raise Exception('%s has not a valid mimetype', filename)

            # check headers
            csvreader = csv.reader(StringIO(response.content))
            header = csvreader.next()
            if previous_header is not None:
                if header != previous_header:
                    raise Exception('Different Header!')
            else:
                result.writerow(header)
            for line in csvreader:
                result.writerow(line)

        return data.getvalue()
