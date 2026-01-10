import json

summary = {}
summary_list = []
with open("data/job_roles.json", "r", encoding="utf-8") as f:
    roles = json.load(f)

#Summary of regions, industries, work experience, roles, work format, employment type
for cat in roles["categories"]:
    print(f"{cat['id']}: {cat['name']}")

keys = ['id','name']
list = roles["categories"][7]["roles"]
print([{key: e[key] for key in keys} for e in list])
