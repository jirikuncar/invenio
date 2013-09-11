# -*- coding: utf-8 -*-
#
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
## 59 Temple Place, Suite 330, Boston, MA 02D111-1307, USA.

"""
WebVisualize database models.
"""

# General imports.
from invenio.sqlalchemyutils import db
from invenio.websession_model import User
from datetime import datetime
# Create your models here.

class VslConfig(db.Model):
	""" Represents a Visualization config record"""

	__tablename__ = 'VslConfig'
	id = db.Column(db.Integer(15, unsigned=True), primary_key=True,
                   autoincrement=True)
	name = db.Column(db.String(255), nullable=False,
                  server_default='', index=True, unique=True)
	title = db.Column(db.String(255), nullable=False,
                  server_default='', index=True)
	id_creator = db.Column(db.Integer(15, unsigned=True),
				           db.ForeignKey(User.id), nullable=True)
	graph_type = db.Column(db.String(255), nullable=False,
                     server_default='', index=True)
	visibility = db.Column(db.String(255), nullable=False, 
					 server_default='private', index=True)
	description = db.Column(db.Text)
	config = db.Column(db.Text)

	creator = db.relationship(User, backref='visualization_configs')

	@property
	def json_config(self):
		import json
		cfg = json.loads(self.config)
		cfg['name'] = self.name
		cfg['title'] = self.title
		cfg['description'] = self.description
		return cfg

	@property
	def fields(self):
		# only one element??
		import json
		return json.dumps([str(field['id']) for field in 
									self.json_config['resources'][0]['schema']['fields']])

	@property
	def is_public(self):
	    return self.visibility == 'public'

	@property
	def get_url_csv(self):
		url = self.json_config['resources'][0]['url']
		return url.replace('http://localhost', '')

	def create_from_form(self, data, id_user):
		def generate_config(csv_url):
			import json, urllib2
			config = {}
			config['licenses'] = []
			config['sources'] = []
			config['last_modified'] = str(datetime.now())

			# Read the first row in the CSV file to get the headers
			response = urllib2.urlopen(csv_url).read(10000) #FIX ME! maybe 10000 chars  is not enough
			if not len(response.split('\n')): # At least one line
				raise Exception('Fields missing!!')
			fields = response.split('\n')[0].split(',')
			formatted_fields = []
			for field in fields:
				formatted_fields.append({'id': field,
										'type': 'string'})
			config['resources'] = [{'url': csv_url,
						  			'path': '???',
						  			'format':'csv',
						  			'schema': {'fields': formatted_fields}
						  		   }]

			return json.dumps(config)

		self.name = data['name']
		self.title = data['title']
		self.id_creator = id_user
		self.graph_type = data['graph_type']
		self.description = data['description']
		self.visibility = data['visibility']
		self.config = generate_config(csv_url=data['csv_file'])