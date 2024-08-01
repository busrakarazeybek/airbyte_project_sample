from airbyte_cdk.sources import Source
from airbyte_cdk.models import AirbyteStream, SyncMode
from typing import List, Mapping, Tuple, Any

class SourceMySQL(Source):
    def check_connection(self, logger, config) -> Tuple[bool, any]:
        try:
            # MySQL veritabanı bağlantısını kontrol et
            connection = pymysql.connect(
                host=config["host"],
                user=config["user"],
                password=config["password"],
                database=config["database"]
            )
            connection.close()
            return True, None
        except Exception as e:
            return False, str(e)

    def streams(self, config: Mapping[str, Any]) -> List[AirbyteStream]:
        # MySQL tablosunu bir AirbyteStream olarak döndür
        return [AirbyteStream(name="example_table", json_schema={}, supported_sync_modes=[SyncMode.full_refresh])]
