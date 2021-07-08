import pandas as pd
from utils import get_json
from utils import parse_json

response = get_json()

dic = parse_json(response)

print(dic)
