import pyexcel
from datetime import datetime, date, time


second_array_dictionary = {'Sheet 1': [
                                   ['ID', 'AGE', 'SCORE'],
                                   [1, 22, 5],
                                   [2, 15, 6],
                                   [3, 28, 9]
                                  ],
                       'Sheet 2': [
                                    ['X', 'Y', 'Z'],
                                    [1, 2, 3],
                                    [4, 5, 6],
                                    [7, 8, 9]
                                  ],
                       'Sheet 3': [
                                    ['M', 'N', 'O', 'P'],
                                    [10, 11, 12, 13],
                                    [14, 15, 16, 17],
                                    [18, 19, 20, 21]
                                   ]}

pyexcel.save_book_as(bookdict=second_array_dictionary, dest_file_name="second_array_data.xls")

records = pyexcel.get_records(file_name='second_array_data.xls')
print(records)

now = datetime.utcnow()

print(now)