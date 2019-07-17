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
from typing import List

from sqlalchemy import Table, Column
from flask_restplus import fields, Model


def convert_sqlalchemy_to_restplus_model(table: Table) -> Model:
    """
    Convert an sqlalchemy table to a restplus model.
    Adds support for the field types defined in map_sqlalchemy_to_restplus_type, as well as description and required.

    :param table: The sqlalchemy table.
    :return: a restplus model derived from the table.
    """
    map_sqlalchemy_to_restplus_type = {
        'FLOAT': fields.Float,
        'INTEGER': fields.Integer,
        'VARCHAR': fields.String,
        'DATETIME': fields.DateTime,
        'DATE': fields.Date,
    }

    def _convert_sqlalchemy_to_restplus_column(column: Column) -> (str, fields):
        """
        Inner function used by the map to convert each column.

        :param column: the sqlalchemy column.
        :return: a tuple with the name and field, usable for restplus.
        """
        type: str = str(column.type)

        return column.name, map_sqlalchemy_to_restplus_type[type](description=column.comment,
                                                                  required=column.nullable)

    results = map(_convert_sqlalchemy_to_restplus_column, table.columns)

    return Model(table.name, {row[0]: row[1] for row in results})


def filter_restplus_columns(model: Model, mask: List[str]) -> Model:
    """
    Filter the columns to your desired list that are specified in the mask.
    I favored this option instead of the built-in mask possibilities, because the mask can be overridden by the user.

    :param model: the current restplus model.
    :param mask: a list of all columns that should be retained.
    :return: a restplus model with only the columns that are in the given mask.
    """
    return Model(model.name, {key: model[key] for key in model if key in mask})
