import json
import pytest
import json
import pytest
from dotenv import  load_dotenv
import os
@pytest.fixture
def load_json_data():
    load_dotenv()
    file_name = os.getenv("load_env")
    print(str(file_name))
    with open(file_name, 'r') as f:
        data = json.load(f)
    return data


def test_make_req(load_json_data):
    print("this is the url",load_json_data["url"])