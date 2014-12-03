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

"""Database model for persisting relationships."""

from invenio.ext.sqlalchemy import db

from sqlalchemy_utils import UUIDType


class Relationship(db.Model):

    """Represent a graph edge."""

    uuid = db.Column(UUIDType(binary=False), primary_key=True)
    model_from = db.Column(db.String(255), nullable=True, index=True)
    id_from = db.Column(db.Integer(unsigned=True), nullable=True, index=True)
    link_type = db.Column(db.String(255), nullable=True, index=True)
    model_to = db.Column(db.String(255), nullable=True, index=True)
    id_to = db.Column(db.Integer(unsigned=True), nullable=True, index=True)

    confidence = db.Column(db.Float, nullable=True)
