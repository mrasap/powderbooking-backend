#  Copyright 2019 Michael Kemna.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
from flask_restplus import fields, Model
from sqlalchemy import Table, Column, Integer, String, Float, Sequence, MetaData

from utils.convert_models import convert_sqlalchemy_to_restplus_model


def test_convert_sqlalchemy_to_restplus_model():
    table: Table = Table('resort', MetaData(),
                         Column('id', Integer, primary_key=True,
                                comment='The identifier of the resort'),
                         Column('continent', String, comment='The continent where the resort is located'),
                         Column('lat', Float, comment='The latitudinal coordinate of the geolocation of the resort'),
                         Column('altitude_min_m', Integer, comment='The lowest altitude of the resort (in metres)'),
                         Column('altitude_max_m', Integer),
                         )

    expected: Model = Model('resort', {
        'id': fields.Integer(description='The identifier of the resort'),
        'continent': fields.String(description='The continent where the resort is located'),
        'lat': fields.Float(description='The latitudinal coordinate of the geolocation of the resort'),
        'altitude_min_m': fields.Integer(description='The lowest altitude of the resort (in metres)'),
        'altitude_max_m': fields.Integer(description=None),
    })

    result: Model = convert_sqlalchemy_to_restplus_model(table)

    assert isinstance(result, type(expected))
    assert result.name == expected.name
    assert len(result.items()) == len(expected.items())
    for key in expected.keys():
        assert key in result.keys()
        assert isinstance(result[key], type(expected[key]))
        assert expected[key].description == result[key].description
