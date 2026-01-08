

titles = ['Top 5 cities', 'Top 5 industries', 'Work experience', 'Professional roles', 'Type of employment', 'Work format']
data = [{'Almaty': 16, 'Astana': 3, 'Shymkent': 1, 'Kazakhstan': 0}, {'Financial Sector': 9, 'IT, System Integration, Internet': 5, 'Telecommunications, Communications': 4, 'Retail': 4, 'Medicine, Pharmaceuticals, Pharmacies': 1}, {'Between 1 and 3 years': 9, 'Between 3 and 6 years': 9, 'No experience': 2}, {'Product analyst': 0}, {'Full employment': 20}, {"At the employer's location": 13, 'Hybrid': 3, 'Remote': 1}]
dict = {'Almaty': 16, 'Astana': 3, 'Shymkent': 1, 'Kazakhstan': 0}
tpl = [('the', 1143), ('and', 966), ('to', 762), ('of', 669), ('i', 631),
 ('you', 554),  ('a', 546), ('my', 514), ('hamlet', 471), ('in', 451)]

for i in tpl:
    print(f"{i[0]}: {i[1]}")
