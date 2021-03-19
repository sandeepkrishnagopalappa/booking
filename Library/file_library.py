import xlrd

class xl_data:

    def read_locators(self,file_name,sheet_name):

        with xlrd.open_workbook(file_name) as workbook:
            worksheet=workbook.sheet_by_name(sheet_name)
            rows=worksheet.get_rows()
            next(rows)
            Readline={row[0].value:(row[1].value,row[2].value) for row in rows}
            return Readline,Readline.keys()


