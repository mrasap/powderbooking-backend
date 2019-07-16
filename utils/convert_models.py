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
from sqlalchemy import Table, Column
from flask_restplus import fields, Model

map_sqlalchemy_to_restplus_type = {
    'FLOAT': fields.Float,
    'INTEGER': fields.Integer,
    'VARCHAR': fields.String,
}


def _convert_sqlalchemy_to_restplus_column(column: Column) -> (str, fields):
    type: str = str(column.type)

    return column.name, map_sqlalchemy_to_restplus_type[type](description=column.comment,
                                                              required=column.nullable)


def convert_sqlalchemy_to_restplus_model(table: Table) -> Model:
    results = map(_convert_sqlalchemy_to_restplus_column, table.columns)

    return Model(table.name, {row[0]: row[1] for row in results})
