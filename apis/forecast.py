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
from flask_restplus import Namespace, Resource
from powderbooking.models import model_forecast
from sqlalchemy import MetaData

from database import db
from database.query import Query

from utils.convert_models import convert_sqlalchemy_to_restplus_model

api = Namespace('forecast', description='Weather reports of a overview')

forecast = convert_sqlalchemy_to_restplus_model(table=model_forecast(metadata=MetaData()))
api.add_model(name=forecast.name, definition=forecast)


@api.route('/current/<int:resort_id>')
@api.param('resort_id', 'The overview identifier')
@api.response(404, 'No current forecast report for given overview identifier found')
class ForecastCurrent(Resource):
    @api.doc('get_current_forecast_report')
    @api.marshal_list_with(fields=forecast)
    def get(self, resort_id: int):
        """Get the current forecast report from today for the given overview identifier"""
        result = db.execute_query(Query.select_forecast_current, resort_id=resort_id)

        if result.rowcount > 0:
            return result.fetchall()
        api.abort(404)


@api.route('/past/<int:resort_id>')
@api.param('resort_id', 'The overview identifier')
@api.response(404, 'No past forecast report for given overview identifier found')
class ForecastPast(Resource):
    @api.doc('get_past_forecast_report')
    @api.marshal_list_with(fields=forecast)
    def get(self, resort_id: int):
        """Get the past forecast reports of today for the given overview identifier"""
        result = db.execute_query(Query.select_forecast_past, resort_id=resort_id)

        if result.rowcount > 0:
            return result.fetchall()
        api.abort(404)
