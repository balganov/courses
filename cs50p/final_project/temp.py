import json

summary = {}
summary_list = []
with open("data/job_roles.json", "r", encoding="utf-8") as f:
    roles = json.load(f)

#Summary of regions, industries, work experience, roles, work format, employment type
for cat in roles["categories"]:
    print(f"{cat['id']}: {cat['name']}")

keys = ['id','name']
list = [cat["roles"] for cat in roles["categories"] if cat["name"] == "Information technology"]
print(list)
print([{key: e[key] for key in keys} for e in list])
