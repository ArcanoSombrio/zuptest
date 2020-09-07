import xlrd
from utils.get_current_folder import get_current_folder


# Método utilizado para carregar valores das linhas e colunas das abas de um arquivo excel
def get_excel_values(sheet, row, column):
    path = get_current_folder() + '/data/data.xlsx'
    print(path)
    if path is None or path == '':
        assert IOError('Arquivo não encontrado!')
    else:
        workbook = xlrd.open_workbook(path)
        worksheet = workbook.sheet_by_name(sheet)
        return worksheet.cell(row, column).value
