from airbyte_cdk.destinations import Destination
from airbyte_cdk.models import ConfiguredAirbyteCatalog, Type
from typing import List, Mapping, Tuple, Any

class DestinationPostgres(Destination):
    def check_connection(self, logger, config) -> Tuple[bool, any]:
        try:
            # PostgreSQL veritabanı bağlantısını kontrol et
            connection = psycopg2.connect(
                host=config["host"],
                user=config["user"],
                password=config["password"],
                dbname=config["dbname"]
            )
            connection.close()
            return True, None
        except Exception as e:
            return False, str(e)

    def write(self, logger, config, catalog: ConfiguredAirbyteCatalog, input):
        # PostgreSQL veritabanına veri yaz
        connection = psycopg2.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            dbname=config["dbname"]
        )
        cursor = connection.cursor()
        for message in input:
            if message.type == Type.RECORD:
                # Veriyi tabloya ekle
                cursor.execute(f"INSERT INTO {message.record.stream} (data) VALUES (%s)", (message.record.data,))
        connection.commit()
        cursor.close()
        connection.close()
