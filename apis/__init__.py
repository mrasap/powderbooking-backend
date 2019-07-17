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
from flask_restplus import Api

from .resort import api as resort
from .weather import api as weather
from .forecast import api as forecast
from .overview import api as overview

api = Api(
    title='Powderbooking',
    version='0.1.0',
    description='Application to show the best hotels with the weather',
    # All API metadatas
)

api.add_namespace(resort)
api.add_namespace(weather)
api.add_namespace(forecast)
api.add_namespace(overview)
