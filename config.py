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
import os


def build_database_url(project: str = os.environ.get('PROJECT_NAME', 'powderbooking')) -> str:
    """
    Build the database url.
    Credentials are built from environmental variables.

    :return: the database url
    """
    username = os.environ.get('POSTGRESQL_USER', 'postgres')
    password = os.environ.get('POSTGRESQL_PASSWORD', 'password')
    host = os.environ.get(f'{project}_POSTGRESQL_SERVICE_HOST'.upper(), 'localhost')
    port = os.environ.get(f'{project}_POSTGRESQL_SERVICE_PORT'.upper(), '8001')
    database = os.environ.get('POSTGRESQL_DB', 'powderbooking')
    return f'postgresql://{username}:{password}@{host}:{port}/{database}'
