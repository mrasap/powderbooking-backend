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
from sqlalchemy import Table, Column, Integer, String, Float, MetaData

from utils.convert_models import convert_sqlalchemy_to_restplus_model, filter_restplus_columns


def test_convert_sqlalchemy_to_restplus_model():
    table: Table = Table('overview', MetaData(),
                         Column('id', Integer, primary_key=True,
                                comment='The identifier of the overview'),
                         Column('continent', String, comment='The continent where the overview is located'),
                         Column('lat', Float, comment='The latitudinal coordinate of the geolocation of the overview'),
                         Column('altitude_min_m', Integer, comment='The lowest altitude of the overview (in metres)'),
                         Column('altitude_max_m', Integer),
                         )

    expected: Model = Model('overview', {
        'id': fields.Integer(description='The identifier of the overview'),
        'continent': fields.String(description='The continent where the overview is located'),
        'lat': fields.Float(description='The latitudinal coordinate of the geolocation of the overview'),
        'altitude_min_m': fields.Integer(description='The lowest altitude of the overview (in metres)'),
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


def test_filter_restplus_columns():
    model: Model = Model('overview', {
        'id': fields.Integer(description='The identifier of the overview'),
        'continent': fields.String(description='The continent where the overview is located'),
        'lat': fields.Float(description='The latitudinal coordinate of the geolocation of the overview'),
        'altitude_min_m': fields.Integer(description='The lowest altitude of the overview (in metres)'),
        'altitude_max_m': fields.Integer(description=None),
    })

    mask = ['continent', 'lat']

    expected: Model = Model('overview', {
        'continent': fields.String(description='The continent where the overview is located'),
        'lat': fields.Float(description='The latitudinal coordinate of the geolocation of the overview'),
    })

    result: Model = filter_restplus_columns(model, mask)

    assert isinstance(result, type(expected))
    assert result.name == expected.name
    assert len(result.items()) == len(expected.items())
    for key in expected.keys():
        assert key in result.keys()
        assert isinstance(result[key], type(expected[key]))
        assert expected[key].description == result[key].description
