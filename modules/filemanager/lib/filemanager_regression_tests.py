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
from invenio.config import CFG_SITE_SECURE_URL
from urllib import urlencode
from invenio.config import CFG_WEBDIR 
from invenio.testutils import make_test_suite, run_test_suite, \
    InvenioTestCase, test_web_page_content, test_web_page_existence
import os

class FileManagerRegressionTests(InvenioTestCase):

    def setUp(self):
        self.path = CFG_WEBDIR + '/static'
        self.csv_file_content = '''\
paid_by,date,transaction_id,currency,amount,paid_to,spending_area,unique_rowid
"London Borough of Hammersmith and Fulham",2010-01-01,405869,GBP,898.64,"ADT FIRE & SECURITY PLC","Childrens Services",1
"London Borough of Hammersmith and Fulham",2010-01-01,405870,GBP,517.85,"ADT FIRE & SECURITY PLC","Resident Services",2
"London Borough of Hammersmith and Fulham",2010-01-01,405871,GBP,1215.97,"ADT FIRE & SECURITY PLC","Regeneration and Housing Services",3
"London Borough of Hammersmith and Fulham",2010-01-01,417742,GBP,112.5,"ALARM LTD","Finance and Corporate Services",4
"London Borough of Hammersmith and Fulham",2010-01-01,417742,GBP,562.5,"ALARM LTD","Finance and Corporate Services",5
"London Borough of Hammersmith and Fulham",2010-01-01,391746,GBP,1665.62,"ASCOM TELE NOVA LTD","Childrens Services",6
"London Borough of Hammersmith and Fulham",2010-01-01,396062,GBP,1500,"BIW TECHNOLOGIES LIMITED","Community Services",7
"London Borough of Hammersmith and Fulham",2010-01-01,392463,GBP,560,"CAPITAL CITY COMMUNICATIONS LTD","Resident Services",8
"London Borough of Hammersmith and Fulham",2010-01-01,393998,GBP,1296,"CAPITAL CITY COMMUNICATIONS LTD","Environment Services",9
"London Borough of Hammersmith and Fulham",2010-01-01,395696,GBP,171.39,"CAR HIRE (DAY OF SWANSEA)LTD","Resident Services",10
"London Borough of Hammersmith and Fulham",2010-01-01,395696,GBP,180.68,"CAR HIRE (DAY OF SWANSEA)LTD","Resident Services",11
"London Borough of Hammersmith and Fulham",2010-01-01,395696,GBP,182.82,"CAR HIRE (DAY OF SWANSEA)LTD","Resident Services",12
"London Borough of Hammersmith and Fulham",2010-01-01,395696,GBP,185.6,"CAR HIRE (DAY OF SWANSEA)LTD","Resident Services",13
"London Borough of Hammersmith and Fulham",2010-01-01,395696,GBP,244.84,"CAR HIRE (DAY OF SWANSEA)LTD","Resident Services",14
"London Borough of Hammersmith and Fulham",2010-01-01,395696,GBP,265.49,"CAR HIRE (DAY OF SWANSEA)LTD","Resident Services",15
"London Borough of Hammersmith and Fulham",2010-01-01,395696,GBP,384.65,"CAR HIRE (DAY OF SWANSEA)LTD","Resident Services",16
"London Borough of Hammersmith and Fulham",2010-01-01,395696,GBP,148.1,"CAR HIRE (DAY OF SWANSEA)LTD","Resident Services",17
"London Borough of Hammersmith and Fulham",2010-01-01,395696,GBP,168.85,"CAR HIRE (DAY OF SWANSEA)LTD","Resident Services",18
"London Borough of Hammersmith and Fulham",2010-01-01,417549,GBP,32641.84,"CB RICHARD ELLIS LTD CLIENT ACCOUNT","Environment Services",19
"London Borough of Hammersmith and Fulham",2010-01-01,417550,GBP,8106.18,"CB RICHARD ELLIS LTD CLIENT ACCOUNT","Environment Services",20
"London Borough of Hammersmith and Fulham",2010-01-01,395936,GBP,527,"CHESTERFIELD ASSOCIATES","Childrens Services",21
"London Borough of Hammersmith and Fulham",2010-01-01,407426,GBP,525.52,"CHESTERFIELD ASSOCIATES","Community Services",22
"London Borough of Hammersmith and Fulham",2010-01-01,460450,GBP,136.97,"CONSULTUS SERVICES AGENCY LTD","Community Services",23
"London Borough of Hammersmith and Fulham",2010-01-01,460450,GBP,1431.85,"CONSULTUS SERVICES AGENCY LTD","Community Services",24
"London Borough of Hammersmith and Fulham",2010-01-01,409072,GBP,522.1,"COYLE PERSONNEL PLC","Community Services",25
"London Borough of Hammersmith and Fulham",2010-01-01,405998,GBP,7009.96,"CRANSTOUN DRUG SERVICES","Community Services",26
"London Borough of Hammersmith and Fulham",2010-01-01,409318,GBP,-1156.27,"EDF ENERGY 1 LIMITED","Resident Services",27
"London Borough of Hammersmith and Fulham",2010-01-01,409319,GBP,-826.32,"EDF ENERGY 1 LIMITED","Resident Services",28
"London Borough of Hammersmith and Fulham",2010-01-01,483559,GBP,2950,"e-MENTORING LIMITED","Childrens Services",29
'''
        self.CERN1_file_content = '''\
MEMBER STATES,6939
Austria,137
Belgium,110
Bulgaria,87
Czech Republic,199
Denmark,67
Finland,96
France,830
Germany,1281
Greece,177
Hungary,74
Italy,1802
Netherlands,152
Norway,69
Poland,278
Portugal,126
Slovakia,91
Spain,386
Sweden,79
Switzerland,214
United Kingdom,684
'''
        self.CERN2_file_content = '''\
OBSERVERS,2590
India,228
Japan,259
Russia,998
Turkey,127
USA,978
'''
        self.csv_file_name = 'filemanager_regression_tests_basic.csv'
        self.CERN1_file_name = 'filemanager_regression_tests_CERN1.csv'
        self.CERN2_file_name = 'filemanager_regression_tests_CERN2.csv'

        self.files = {
            self.csv_file_name: self.csv_file_content,
            self.CERN1_file_name: self.CERN2_file_content,
            self.CERN2_file_name: self.CERN2_file_content
        }
        for name, content in self.files.iteritems(): 
            with open(os.path.join(self.path, name), 'w') as file_url:
                file_url.write(content) 

        self.csv_file = CFG_SITE_SECURE_URL + '/static/' + self.csv_file_name
        self.CERN1_file = CFG_SITE_SECURE_URL + '/static/' + self.CERN1_file_name
        self.CERN2_file = CFG_SITE_SECURE_URL + '/static/' + self.CERN2_file_name

    def tearDown(self):
        for name in self.files.iterkeys():
            os.remove(os.path.join(self.path, name))

    def test_no_valid_action(self):
        url = url_for('filemanager.perform', action='anything', _external=True)
        errors  = test_web_page_content(url)
        print errors
        assert 'HTTP Error 406' in errors[0]

    def test_join_files(self):
        url = url_for('filemanager.perform', action='join', 
                                            file=[self.csv_file, self.csv_file], 
                                            _external=True)
        test_web_page_existence(url)
        expected =('London Borough of Hammersmith and Fulham,2010-01-01,483559,GBP,2950'
                   ',e-MENTORING LIMITED,Childrens Services,29\nLondon Borough of Hammer'
                   'smith and Fulham,2010-01-01,405869,GBP,898.64,ADT FIRE & SECURITY PLC'
                   ',Childrens Services,1')

        errors  = test_web_page_content(url, expected_text=expected)
        self.assertEquals([], errors)

    def test_csv_to_json_files(self):
        url = url_for('filemanager.perform', action='csvtojson', 
                                             file=self.csv_file, 
                                             _external=True)        
        test_web_page_existence(url)
        expected = ('"paid_to": "EDF ENERGY 1 LIMITED", "currency": "GBP", "'
                    'amount": "-1156.27", "date": "2010-01-01", "paid_by": "London '
                    'Borough of Hammersmith and Fulham", "transaction_id": "409318"},'
                    ' {"unique_rowid": "28", "spending_area": "Resident Services", "paid_to"'
                    ': "EDF ENERGY 1 LIMITED", "currency": "GBP", "amount": "-826.32", "date"'
                    ': "2010-01-01", "paid_by": "London Borough of Hammersmith and Fulham", '
                    '"transaction_id": "409319"}, {"unique_rowid": "29", "spending_area": "Ch'
                    'ildrens Services", "paid_to": "e-MENTORING LIMITED", "currency": "GBP", '
                    '"amount": "2950", "date": "2010-01-01", "paid_by": "London Borough of '
                    'Hammersmith and Fulham", "transaction_id": "483559"}]')
        errors  = test_web_page_content(url, expected_text=expected)
        self.assertEquals([], errors)

    def test_cut_files(self):
        url = url_for('filemanager.perform', action='cut', 
                                             file=self.csv_file,
                                             field=['paid_by', 'amount', 'spending_area'], 
                                             _external=True)
        test_web_page_existence(url)
        expected = ('paid_by,amount,spending_area\nLondon Borough of Hammers'
                    'mith and Fulham,898.64,Childrens Services\nLondon Boroug'
                    'h of Hammersmith and Fulham,517.85,Resident Services\nLon'
                    'don Borough of Hammersmith and Fulham,1215.97,Regeneration'
                    ' and Housing Services')
        errors  = test_web_page_content(url, expected_text=expected)
        self.assertEquals([], errors)

    def test_CERN_staff_to_bubbletree_files(self):
        print self.CERN1_file
        print self.CERN2_file
        url = url_for('filemanager.perform', action='cernstafftobubbletree', 
                                             file=[self.CERN1_file, self.CERN2_file], 
                                             _external=True)
        print url
        test_web_page_existence(url)
        expected = ('{"amount": 11146, "children": [{"amount": "6939", "children": '
            '[{"amount": "137", "name": "Austria", "label": "Austria"}, {"amount": "'
            '110", "name": "Belgium", "label": "Belgium"}, {"amount": "87", "name": '
            '"Bulgaria", "label": "Bulgaria"}, {"amount": "199", "name": "Czech Repub'
            'lic", "label": "Czech Republic"}, {"amount": "67", "name": "Denmark", "la'
            'bel": "Denmark"}, {"amount": "96", "name": "Finland", "label": "Finland"},'
            ' {"amount": "830", "name": "France", "label": "France"}, {"amount": "1281",'
            ' "name": "Germany", "label": "Germany"}, {"amount": "177", "name": "Greece'
            '", "label": "Greece"}, {"amount": "74", "name": "Hungary", "label": "Hunga'
            'ry"}, {"amount": "1802", "name": "Italy", "label": "Italy"}, {"amount": "1'
            '52", "name": "Netherlands", "label": "Netherlands"}, {"amount": "69", "na'
            'me": "Norway", "label": "Norway"}, {"amount": "278", "name": "Poland", "la'
            'bel": "Poland"}, {"amount": "126", "name": "Portugal", "label": "Portugal"'
            '}, {"amount": "91", "name": "Slovakia", "label": "Slovakia"}, {"amount": "'
            '386", "name": "Spain", "label": "Spain"}, {"amount": "79", "name": "Sweden'
            '", "label": "Sweden"}, {"amount": "214", "name": "Switzerland", "label": "'
            'Switzerland"}, {"amount": "684", "name": "United Kingdom", "label": "Unit'
            'ed Kingdom"}], "name": "MEMBER STATES", "label": "MEMBER STATES"}, {"amount'
            '": "2590", "children": [{"amount": "228", "name": "India", "label": "India'
            '"}, {"amount": "259", "name": "Japan", "label": "Japan"}, {"amount": "998'
            '", "name": "Russia", "label": "Russia"}, {"amount": "127", "name": "Turkey'
            '", "label": "Turkey"}, {"amount": "978", "name": "USA", "label": "USA"}], '
            '"name": "OBSERVERS", "label": "OBSERVERS"}], "name": "CERN Staff", "label"'
            ': "CERN Staff"}')


TEST_SUITE = make_test_suite(FileManagerRegressionTests)

if __name__ == "__main__":
    run_test_suite(TEST_SUITE)
