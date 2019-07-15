from powderbooking.database import DatabaseHandler

from config import build_database_url

if __name__ == '__main__':
    print('creating db handler')
    db = DatabaseHandler(database_url=build_database_url())
    print('successfully created db handler')
