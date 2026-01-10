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
                elements = ','.join(element['name'].split(',')[:2])
                summary.update({elements: element['count']})
            else:
                summary.update({element['name']: element['count']})
        summary_list.append(summary)
    elif cluster["name"] in ["Work experience", "Professional role", "Type of employment", "Work format"]:
        for element in cluster["items"]:
            summary.update({element['name']: element['count']})
        summary_list.append(summary)

print(summary_list)


# [{'Minsk': 400, 'Gomel': 23, 'Vitebsk': 23, 'Brest': 16, 'Mogilev': 11},
#  {'IT, System Integration': 356, 'Retail': 35, 'Financial Sector': 25, 'Electronics, Tool Engineering': 19, 'Media, Marketing': 15},
#  {'Between 3 and 6 years': 201, 'Between 1 and 3 years': 181, 'No experience': 72, 'More than 6 years': 41},
#  {'Programmer, developer': 476, 'Development team leader': 19},
#  {'Full employment': 467, 'Part-time employment': 16, 'Project work': 12},
#  {"At the employer's location": 269, 'Remote': 134, 'Hybrid': 117, 'Travel': 2}]
