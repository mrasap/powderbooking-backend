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
