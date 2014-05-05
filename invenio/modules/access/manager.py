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

"""
    invenio.modules.access.manager
    ------------------------------

    Access control list manager.
"""

from __future__ import print_function, absolute_import

from six import itervalues

from invenio.ext.sqlalchemy import db
from invenio.ext.script import Manager


manager = Manager(usage="Perform access controll list operations")


@manager.option("-v", "--verbose", dest="verbose",
                action="store_true", default=False)
def init(verbose=False):
    """Initializes actions, roles and authorizations."""
    print(">>> Going to create access controll list ...")
    from . import models
    from . import registry

    for action in itervalues(registry.actions):
        if verbose:
            print(">>> adding action:", action.name, "-",
                  action.description)
        db.session.add(models.AccACTION(
            name=action.name, description=action.description,
            optional=getattr(action, "optional", "no"),
            allowedkeywords=getattr(action, "allowedkeywords", list())
        ))

    for role in itervalues(registry.roles):
        if verbose:
            print(">>> adding role:", role.name, "-", role.description)
        db.session.add(models.AccROLE(
            name=role.name, description=role.description,
            definition=getattr(role, "definition", "")
        ))

    db.session.commit()
    print(">>> Access control list filled successfully.")


def main():
    from invenio.base.factory import create_app
    app = create_app()
    manager.app = app
    manager.run()

if __name__ == "__main__":
    main()
