# -*- coding: utf-8 -*-
##
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

from flask import url_for 
from invenio.testutils import make_test_suite, run_test_suite, \
    InvenioTestCase, test_web_page_content, test_web_page_existence

class WebVisualizeRegressionTests(InvenioTestCase):

    def test_bubbletree_navigation(self):
        url = url_for('webvisualize.navigate', _external=True)
        test_web_page_existence(url)

    def test_index_guest_visualization(self):
        url = url_for('webvisualize.index', _external=True)
        errors = test_web_page_content(url)
        assert 'HTTP Error 401' in errors[0]

    def test_index_authenticated_visualization(self):
        url = url_for('webvisualize.index', _external=True)
        errors = test_web_page_content(url, username='jekyll', 
                                            password='j123ekyll',
    									    expected_text='create visualization')
        self.assertEquals([], errors)

    def test_add_guest_visualization(self):
        url = url_for('webvisualize.new', _external=True)
        errors = test_web_page_content(url)
        assert 'HTTP Error 401' in errors[0]

    def test_add_authenticated_visualization(self):
        url = url_for('webvisualize.new', _external=True)
        errors = test_web_page_content(url, username='jekyll', 
                                            password='j123ekyll',
    									    expected_text='<select id="graph_type"')
        self.assertEquals([], errors)

TEST_SUITE = make_test_suite(WebVisualizeRegressionTests)

if __name__ == "__main__":
    run_test_suite(TEST_SUITE)
