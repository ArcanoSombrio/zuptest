import datetime as datetime

datetime = datetime.datetime.now()


# Função que extraí a data e hora atual ou somente a data atual
def get_date_time(date_time):
    if date_time is False:
        return datetime.strftime("%d-%m-%Y %H_%M_%S")
    else:
        return datetime.strftime("%d-%m-%Y")
