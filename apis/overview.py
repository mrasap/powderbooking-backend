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
from flask_restplus import Namespace, Resource, Model

from utils.convert_models import filter_restplus_columns
from database import db
from database.query import Query

from apis.forecast import forecast
from apis.resort import resort

api = Namespace('overview', description='Overview of all resorts with aggregate forecast data')

filtered_resort = filter_restplus_columns(model=resort, mask=['id', 'lat', 'lng'])
# TODO: Create an overview table in the database with rain_total_mm and snow_total_mm
filtered_forecast = filter_restplus_columns(model=forecast, mask=['rain_total_mm', 'snow_total_mm'])

overview = Model('overview', {**filtered_resort, **filtered_forecast})  # pythonic way to union two dicts
api.add_model(name=overview.name, definition=overview)


@api.route('/')
class OverviewList(Resource):
    @api.doc('list_overview')
    @api.marshal_list_with(overview)
    def get(self):
        """List all resorts with aggregate forecast data of today"""
        return db.execute_query(Query.select_overview).fetchall()
