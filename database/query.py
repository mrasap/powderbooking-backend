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

from enum import Enum

from sqlalchemy import text


class Query(Enum):
    """
    This Enum is used to store all the queries that are used by the application.

    source to execute raw sql with sqlalchemy:
    https://chartio.com/resources/tutorials/how-to-execute-raw-sql-in-sqlalchemy/
    """
    select_weather_recent = text("""
        SELECT *
        FROM weather
        WHERE weather.resort_id = :resort_id 
            AND NOW() - dt < INTERVAL '1 day'
        ORDER BY dt DESC
        LIMIT 1
    """)
