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

"""Users who can perform changes to their own paper attributions without the need for an operator's approval"""

definition = "allow any"

authorizations = [{"action": "claimpaper_view_pid_universe", "arguments": {}},
                  {"action": "claimpaper_claim_own_papers", "arguments": {}},
                  {"action": "claimpaper_change_own_data", "arguments": {}},
                  ]
