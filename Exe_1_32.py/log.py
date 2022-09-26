from datetime import datetime 

def print_result(result):
    with open ('result.txt', 'a+', encoding='UTF-8') as file:
        file.write(f'{result} --- {datetime.now()}\n')
