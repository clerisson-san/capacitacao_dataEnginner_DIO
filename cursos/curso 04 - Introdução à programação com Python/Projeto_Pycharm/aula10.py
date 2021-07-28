# Utilizando a função DATE (timedelta : serve para subtração e soma de data)
from datetime import date, time, datetime, timedelta

def trabalhando_com_date():

    data_atual = date.today()
    # utilizando diretivas python para esta função
    data_atual_str = data_atual.strftime('%A %B %d-%m-%Y')

    print(data_atual)
    print(type(data_atual))
    print(type(data_atual_str))

def trabalhando_com_time():
    horario = time(hour=15, minute=10, second=30)
    #print(horario.strftime('%H:%M:%S'))
    horario_str = horario.strftime('%H:%M:%S')
    print(horario)
    print(horario_str)
    print(type(horario))
    print(type(horario_str))

# Trabalhado com data e hora diretamente e diretivas
def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y'))
    print(data_atual.strftime(('%H:%M:%S')))
    print(data_atual.strftime('%c'))
    print(data_atual.day)
    print(data_atual.year)
    print(data_atual.hour)
    print(data_atual.minute)
    print(data_atual.weekday())
    print(data_atual.month)
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2018, 6, 20, 15, 30, 20)
    print(data_criada)
    print(data_criada.strftime('%d/%m/%Y %H:%M:%S'))
    #ou
    print(data_criada.strftime('%c'))
    #Convertendo data em string para datetime
    data_string = '01/01/2019 12:20:22'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)
    print(type(data_convertida))
    #Subtração de data ou soma
    #nova_data = data_convertida - timedelta(days=365, hours=2, minutes=10, seconds=5)
    nova_data = data_convertida + timedelta(days=365, hours=2, minutes=10, seconds=5)
    print(nova_data)
    print(datetime.weekday())

if __name__ == '__main__':
    #trabalhando_com_date()
    #trabalhando_com_time()
    trabalhando_com_datetime()