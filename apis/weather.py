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
from powderbooking.models import model_weather
from sqlalchemy import MetaData

from database import db
from database.query import Query

from utils.convert_models import convert_sqlalchemy_to_restplus_model

api = Namespace('weather', description='Weather reports of a resort')

model = convert_sqlalchemy_to_restplus_model(table=model_weather(metadata=MetaData()))
api.add_model(name=model.name, definition=model)


@api.route('/')
class List(Resource):
    @api.doc('list_resorts')
    @api.marshal_list_with(model)
    def get(self):
        """List all weather reports"""
        return db.execute(db.get_table('weather').select()).fetchall()


@api.route('/<resort_id>')
@api.param('resort_id', 'The resort identifier')
@api.response(404, 'No weather report for given resort identifier found')
class Item(Resource):
    @api.doc('get_weather_report')
    @api.marshal_with(model)
    def get(self, resort_id):
        """Get the latest weather report for the given resort identifier"""
        result = db.execute_query(Query.select_weather_recent, resort_id=resort_id)

        if result.rowcount == 1:
            return result.fetchone()
        api.abort(404)
