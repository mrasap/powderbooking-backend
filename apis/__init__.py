from flask_restplus import Api

from .resort import api as resort

api = Api(
    title='Powderbooking',
    version='0.1.0',
    description='Application to show the best hotels with the weather',
    # All API metadatas
)

api.add_namespace(resort)
