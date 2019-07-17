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
from powderbooking.models import model_resort
from sqlalchemy import MetaData

from database import db

from utils.convert_models import convert_sqlalchemy_to_restplus_model

api = Namespace('resort', description='Details of the resorts')

resort = convert_sqlalchemy_to_restplus_model(table=model_resort(metadata=MetaData()))
api.add_model(name=resort.name, definition=resort)


@api.route('/<int:id>')
@api.param('id', 'The overview identifier')
@api.response(404, 'Resort not found')
class Resort(Resource):
    @api.doc('get_resort')
    @api.marshal_with(resort)
    def get(self, id: int):
        """Get overview details given its identifier"""
        result = db.execute(db.get_table('resort').select().where(db.get_table_column('resort', 'id') == id))

        if result.rowcount == 1:
            return result.fetchone()
        api.abort(404)
