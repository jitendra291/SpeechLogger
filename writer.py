from openpyxl import Workbook


class WorksheetWriter:

    def __init__(self):
        self.wb = Workbook()

    def write(self, audio_string):
        default_worksheet = "test.xlsx"
        print("You said: " + audio_string)
        # grab the active worksheet
        ws = self.wb.active
        # Data can be assigned directly to cells
        ws['A1'] = audio_string
        self.wb.save(default_worksheet)
