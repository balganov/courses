import matplotlib.pyplot as plt
import matplotlib as mpl
from wordcloud import WordCloud
from fpdf import FPDF

import numpy as np

data = [{'Almaty': 141, 'Astana': 53, 'Temirtau': 2, 'Shymkent': 2, 'Atyrau': 1},
        {'IT, System Integration, Internet': 67, 'Financial Sector': 59, 'Retail': 26, 'Telecommunications, Communications': 25, 'Business Services': 24},
        {'Between 3 and 6 years': 100, 'Between 1 and 3 years': 72, 'No experience': 24, 'More than 6 years': 13},
        {'BI analyst, data analyst': 118, 'Data scientist': 71, 'Product analyst': 20},
        {'Full employment': 192, 'Part-time employment': 13, 'Project work': 4},
        {"At the employer's location": 99, 'Hybrid': 53, 'Remote': 49, 'Travel': 1}
        ]
count_skills = {'SQL': 62, 'Python': 47, 'Power BI': 26, 'Анализ данных': 25, 'Big Data': 23, 'Аналитическое мышление': 22,'Data Analysis': 22, 'Английский язык': 20, 'Математическая статистика': 14, 'MS SQL': 13, 'Работа с большим объемом информации': 13, 'Databases': 13, 'Визуализация данных': 9, 'MS Excel': 9, 'PostgreSQL': 8, 'A/B тесты': 6, 'Tableau': 6, 'Бизнес-анализ': 6, 'Интерпретация данных': 6, 'MS PowerPoint': 6, 'Деловая коммуникация': 6, 'ORACLE': 6, 'ETL': 5, 'Git': 5, 'Базы данных': 5, 'pandas': 5, 'DWH': 5, 'Подготовка презентаций': 5, 'Работа с базами данных': 5, 'Исследовательский анализ данных': 4, 'Продуктовые метрики': 4, 'Основы баз данных': 4, 'Аналитические исследования': 4, 'Формирование аналитической отчетности': 4, 'Теория вероятностей': 4, 'Apache Airflow': 4, 'Qlik Sense': 3, 'ML': 3, 'Разработка бизнес-требований': 3, 'RAG': 3, 'Анализ требований': 3, 'Google Analytics': 3, 'DAX': 3, 'Анализ конкурентной среды': 3, 'Scikit-learn': 3, 'Numpy': 3, 'Управление проектами': 3, 'Аналитика': 3, 'LLM': 3, 'NLP': 3, 'C++': 3, 'Машинное обучение': 3, 'Линейная алгебра': 3, 'MySQL': 3, 'Docker': 3, 'Apache Kafka': 3, 'Azure': 3, 'Data Mining': 2, 'Маркетинговые метрики': 2, 'Product Led Growth': 2, 'VBA': 2, 'Риск-менеджмент': 2, '1C: ERP': 2, 'FastAPI': 2, 'PyTorch': 2, 'CI/CD': 2, 'Обучение и развитие': 2, 'Умение работать в коллективе': 2, 'Извлечение данных': 2, 'R': 2, 'Финансовая отчетность': 2, 'Оценка рисков': 2, 'Аудит': 2, 'TensorFlow': 2, 'Организаторские навыки': 2, 'MLflow': 2, 'Excel': 2, 'AI': 2, 'Информационные технологии': 2, 'Статистический анализ': 2, 'Computer Vision': 2, 'Clickhouse': 2, 'Power Query': 2, 'Прогнозирование': 2, 'Atlassian Confluence': 2, 'Data Analyst': 2, 'Сбор и анализ информации': 2, 'Oracle Pl/SQL': 2, 'Risk management': 2, 'Анализ бизнес показателей': 2, 'MS Word': 2, 'Linux': 2, 'Analysis': 2, 'PySpark': 2, 'Microsoft Fabric': 2, 'Статистика': 1, 'Сегментирование аудитории': 1, 'UX-исследования': 1, 'Управление организационными изменениями': 1, 'Анализ целевой аудитории': 1, 'Мобильная аналитика': 1, 'Анализ трафика': 1, 'Основы маркетинга': 1, 'Мотивация сотрудников': 1, 'Управление стейкхолдерами': 1, 'Стратегический менеджмент': 1, 'Регрессионный анализ': 1, 'Риски ликвидности': 1, 'кредитные риски': 1, 'Agentic': 1, 'API': 1, 'Проведение ревизий': 1, '1С: Торговля и склад': 1, 'Проведение инвентаризаций': 1, '1С: Бухгалтерия и склад': 1, 'Внутренний контроль': 1, 'Инвентаризация': 1, 'Точность и внимательность к деталям': 1, 'Навыки составления отчетности': 1, 'Складской Учет': 1, 'Учет остатков': 1, 'E-Commerce': 1, 'Администрирование сайтов': 1, 'Поисковая оптимизация сайтов': 1, 'Управление продажами': 1, 'Маркетинговый анализ': 1, 'CatBoost': 1, 'Jupyter Notebook': 1, 'Анализ рисков': 1, 'Анализ воронки продаж': 1, 'Unit-экономика': 1, 'Событийная аналитика': 1, 'Прогнозирование спроса': 1, 'JavaScript': 1, 'Machine Learning / Deep Learning': 1, 'Нейронные сети': 1, 'ASR': 1, 'AI-инженер': 1, 'MS SQL Server': 1, 'Моделирование бизнес-процессов': 1,
          'Автоматизация процессов': 1, 'Системное мышление': 1, 'Анализ бизнес-процессов': 1, 'Управление командой': 1, 'Управление бизнес процессами': 1, 'Kubernetes': 1, 'Deep Learning': 1, 'GitHub': 1, 'NLTK': 1, 'Аналитик': 1, 'ABC-анализ': 1, 'Анализ оборачиваемости товара': 1, 'Планирование ассортиментной матрицы': 1, 'ABC/XYZ анализы': 1, 'Fashion Trends': 1, 'Маркетинговая стратегия': 1, 'Многозадачность': 1, 'Ответственность': 1, 'informatica': 1, 'Бухгалтерская отчетность': 1, 'Деловая переписка': 1, 'Навыки переговоров': 1, 'Деловое общение': 1, 'analyst': 1, 'SDLC': 1, 'Software Development': 1, 'Payments': 1, 'Artificial intelligence': 1, 'Oracle DWH': 1, 'Hadoop': 1, 'JIRA': 1, 'Confluence': 1, 'Глубокий опыт в анализе и реорганизации таблиц БД (включая партиционирование)': 1, 'Навыки проектирования и оптимизации схем хранения данных.': 1, 'Опыт в разработке архитектуры DWH, нормализации и денормализации данных.': 1, 'Понимание принципов Data Vault / Star / Snowflake моделей.': 1, 'Приветствуется опыт построения OLAP-кубов и настройки отчётности': 1, '1С программирование': 1, 'Разработка и внедрение KPI': 1, 'SAP': 1, 'Предобработка данных': 1, 'Разработка технических заданий': 1, 'КХД': 1, 'REST API': 1, 'AppsFlyer': 1, 'Firebase': 1, 'Amplitude': 1, 'Atlassian Jira': 1, 'P&L': 1, 'Cash Flow': 1, 'Управленческая отчетность': 1, 'Java': 1, 'База данных: Olap': 1, 'Olap (online analytical processing)': 1, 'Постановка задач разработчикам': 1, 'Сбор требований': 1, 'Наставничество': 1, 'Резервное копирование': 1, 'SQL Server Profiler': 1, 'Perforce': 1, 'ASP.NET': 1, '.NET Core': 1, 'Финансовый анализ': 1, 'Financial Analysis': 1, 'МСФО': 1, 'Анализ рынка': 1, 'CFA': 1, 'ESG': 1, 'CFA ESG': 1, 'FRM': 1, 'PRM': 1, 'SCR': 1, 'Управление рисками': 1, 'Бизнес-моделирование': 1, 'Business Consulting': 1, 'Финансы': 1, 'OLAP': 1, 'Apache NiFi': 1, 'QlikView': 1, 'BI разработчик': 1, 'SSAS Tabular': 1, 'PBI Report Server': 1, 'витрины': 1, 'дашборды': 1, 'расчётные модули': 1, 'BI Developer': 1, 'Data Engineer': 1, 'Data Lake': 1, 'Machine Learning': 1, 'ONNXRuntime': 1, 'Snowflake': 1, 'AWS': 1, 'Amazon Web Services': 1, 'JSON API': 1, 'Product-market fit': 1, 'Roadmap': 1, 'Заключение договоров': 1, 'Проектный менеджмент': 1, 'Управление ожиданиями': 1, 'cloud data': 1, 'Алгоритмы и структуры данных': 1, 'Грамотная речь': 1, 'Fluent English': 1, 'Writing Skills': 1, 'Kafka': 1, 'Debezium': 1, 'Airflow': 1, 'S3': 1, 'Trino': 1, 'Spark': 1, 'Скоринговая карта': 1, 'LightGBM': 1, 'Мотивация персонала': 1, 'Пользовательские сценарии': 1, 'end-user layer': 1, 'CJM': 1, 'Use case': 1, 'Бенчмарки': 1, 'Гипотезы': 1, 'Google Tag Manager': 1, 'Access': 1, 'Статистическая обработка данных': 1, 'MS Office': 1, 'Dynamics 365 CRM': 1, 'Microsoft certification': 1, 'English': 1, 'MS Navision': 1, 'ERP': 1, '1C': 1, 'C/AL': 1, '1C: Зарплата и кадры': 1, 'Data Service': 1, 'Dynamics 365': 1, 'Power Apps': 1, 'PL/SQL': 1, 'Swift/ISO20022': 1, 'PL/SQL Tuning': 1, 'Регуляторная задолженность': 1, 'Бухгалтерский учет': 1, 'кредиты/депозиты': 1}
r = 2
c = 3
n = 0
f, ax = plt.subplots(r,c, figsize=(22,11))
colors = plt.get_cmap('viridis')(np.linspace(0.9, 0.4, len(data)))

print(colors)

titles = ['Top 5 industries','Work format', 'Work experience', 'Top 5 cities', 'Professional roles', 'Type of employment']

for i in range(r):
    for j in range(c):
        ax[i,j].set_title(titles[n], fontsize=20, fontweight='bold')
        n += 1

ax[0,0].pie(data[1].values(), labels=data[1].keys(), colors=colors, autopct='%.2f%%', textprops={'fontsize': 13})
ax[0,1].pie(data[5].values(), labels=data[5].keys(), colors=colors, autopct='%.2f%%', textprops={'fontsize': 13})
ax[0,2].pie(data[2].values(), labels=data[2].keys(), colors=colors, autopct='%.2f%%', textprops={'fontsize': 13})

ax[1,0].bar(data[0].keys(), data[0].values(), color=colors)
ax[1,1].bar(data[3].keys(), data[3].values(), color=colors)
ax[1,2].bar(data[4].keys(), data[4].values(), color=colors)

for i in range(3):
    ax[1,i].tick_params(axis='x', labelsize=12,rotation=45)

f.tight_layout()
plt.tight_layout()
plt.savefig("charts.png")

wcloud = WordCloud(background_color='white', width=2000,height=1200).generate_from_frequencies(count_skills)
wcloud.to_file("word_cloud.png")


try:
    pdf = FPDF(orientation='P', format='A4', unit='mm')
    pdf.add_page()
    pdf.image("charts.png", w=190, keep_aspect_ratio=True)
    pdf.set_font("Helvetica", style="B", size=9)
    pdf.cell(0, 35, "Required skills (Word Cloud)", align="C")
    pdf.set_xy(10,0)
    pdf.image("word_cloud.png", y=130, w=190, keep_aspect_ratio=True)
    pdf.output("summary.pdf")

except FileNotFoundError:
        print("Input does not exist")
