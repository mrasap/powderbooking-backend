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


def build_database_url() -> str:
    """
    Build the database url.
    Credentials are built from environmental variables.

    :return: the database url
    """
    username = os.environ.get('POSTGRES_USERNAME', 'postgres')
    password = os.environ.get('POSTGRES_PASSWORD', 'password')
    host = os.environ.get('POSTGRES_HOST', 'localhost')
    port = os.environ.get('POSTGRES_PORT', '8001')
    database = os.environ.get('POSTGRES_DB', 'powderbooking')
    return f'postgresql://{username}:{password}@{host}:{port}/{database}'