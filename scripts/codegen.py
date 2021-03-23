import os


def main():
    os.system("gql-compiler mauna_sdk/schema/ mauna_sdk/api/ --config_path mauna_sdk/schema_config/json_scalar.py")
