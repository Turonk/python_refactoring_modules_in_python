c_sharp = 375
java = 546
java_script = 915
php = 288
python = 603

def analyze_jobs():
    total_jobs = c_sharp + java + java_script + php + python
    python_percent = round(python / total_jobs * 100, 2)
    print('Общее число исследованных вакансий, в тысячах:', total_jobs)
    print('Вакансии для Python-разработчиков, в %:', python_percent)

analyze_jobs()