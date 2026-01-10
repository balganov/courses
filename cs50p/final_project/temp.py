import json

summary_list = []
with open("data/vacancies.json", "r", encoding="utf-8") as f:
    vacancies = json.load(f)

#Summary of regions, industries, work experience, roles, work format, employment type
for cluster in vacancies["clusters"]:
    summary = {}
    if cluster["name"] in ["Region", "Company branch"]:
        for element in cluster["items"][:5]:
            if len(element['name'].split(',')) > 2:
                elements = element['name'].split(',')[:2]
                summary.update({elements: element['count']})
            else:
                summary.update({element['name']: element['count']})
        summary_list.append(summary)
    elif cluster["name"] in ["Work experience", "Professional role", "Type of employment", "Work format"]:
        for element in cluster["items"]:
            summary.update({element['name']: element['count']})
        summary_list.append(summary)

print(summary_list)
