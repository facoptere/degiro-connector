# IMPORTATION STANDARD
import json

# IMPORTATION THIRD PARTY

from degiro_connector.trading.models.trading_pb2 import Credentials

# IMPORTATION INTERNAL
from degiro_connector.trading.relay import Relay as TradingRelay

# SETUP CONFIG DICT
with open("config/config.json") as config_file:
    config_dict = json.load(config_file)

# SETUP CREDENTIALS
int_account = config_dict.get("int_account")
username = config_dict.get("username")
password = config_dict.get("password")
totp_secret_key = config_dict.get("totp_secret_key")
one_time_password = config_dict.get("one_time_password")

credentials = Credentials(
    int_account=int_account,
    username=username,
    password=password,
    totp_secret_key=totp_secret_key,
    one_time_password=one_time_password,
)

relay = TradingRelay(credentials=None)
relay.serve()