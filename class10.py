from datetime import date, time, datetime, timedelta

def working_with_datetime():
    actual_date = datetime.now()
    print(actual_date)
    data_convertida = actual_date.strftime('%d/%m/%Y %H:%M:%S')
    print(actual_date.strftime('%c'))
    print(actual_date.date().strftime('%d/%m/%Y'))
    data_nova = actual_date - timedelta(days=365, hours=2)
    print(data_nova)


def working_with_date():
    actual_date = date.today()
    print(actual_date)
    actual_date_str = actual_date.strftime('%d/%m/%Y')
    print(actual_date_str)
    #letra maiscula muda para dias da semana, por escrito e etc

def working_with_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario)
    horario_str = horario.strftime('%H:%M:%S')
    print(horario_str)



if __name__ == '__main__':
    working_with_time()
    working_with_date()
    working_with_datetime()