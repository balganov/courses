import json
import os

data = [{"id":1,"name":"test"},{"id":2, "name":"test2"}]

os.makedirs("data2",exist_ok=True)

with open("data2/test.json","w", encoding="utf-8") as f:
    json.dump(data, f,ensure_ascii=False,indent=4)
