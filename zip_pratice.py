from zipfile import ZipFile, is_zipfile
from datetime import datetime
import os.path
import json
#1
def search_count_file():
    count = 0
    with ZipFile('zip/workbook.zip') as zip_file:
        for el in zip_file.infolist():
            if not el.is_dir():
                count+=1
    print(count)

# def search_count_file():
    count = 0

#2
def compress_file():
    with ZipFile('zip/workbook.zip') as zip_file:
        a= 0
        z = 0
        for el in zip_file.infolist():
            if not el.is_dir():
                a+=el.file_size
                z+=el.compress_size
        print(f"Объем исходных файлов: {a} байт(а)", f"Объем сжатых файлов: {z} байт(а)", sep='\n')

#3
def search_good_compr_file():
    with ZipFile('zip/workbook.zip') as zip_file:
        res = []
        for el in zip_file.infolist():
            if not el.is_dir():
                if "/" in list(el.filename):
                    res.append((el.compress_size/el.file_size*100, el.filename.split("/")[-1]))
                else:
                    res.append((el.compress_size / el.file_size * 100, el.filename))
        print(min(res)[1])

#4
def sort_files_by_date():
    with ZipFile('zip/workbook.zip') as zip_file:
        print(*sorted([el.filename if "/" not in list(el.filename) else el.filename.split("/")[-1]
                       for el in zip_file.infolist() if not el.is_dir()
                       and el.date_time > (2021, 11, 30, 14, 22)]), sep="\n")

#5
def grooming_files():
    with ZipFile('zip/workbook.zip') as zip_file:
        res = [el for el in zip_file.infolist()]
        for el in sorted(res, key=lambda x: x.filename.split("/")[-1]):
            if not el.is_dir():
                print(el.filename.split("/")[-1], f"  Дата модификации файла: "
                                                  f"{datetime(*el.date_time).strftime('%Y-%m-%d %H:%M:%S')}"
                      , f"  Объем исходного файла: {el.file_size} байт(а)",
                      f"  Объем сжатого файла: {el.compress_size} байт(а)", sep="\n")
                print()

#6
def record_files_to_zip():
    file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
                  'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
                  'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']

    with ZipFile("zip/files.zip", "a") as out:
        for el in file_names:
            out.write(el)

#7
def record_files_to_zip_condition():
    file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
                  'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
                  'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']

    with ZipFile("zip/files.zip", "w") as out:
        for el in file_names:
            if os.path.getsize(el)<=100:
                out.write(el)

#8
def extract_this(zip_name, *args):
    with ZipFile(zip_name) as out:
        if args:
            for el in args:
                try:
                    out.extract(el)
                except KeyError:
                    pass
        else:
            out.extractall()

#9
def select_json_from_zip():
    dct_res = []
    with ZipFile("zip/data.zip") as out:
        for el in out.namelist():
            if el[-1] != "/":
                if el.endswith("json") and el.split("/")[-1].startswith("player"):
                    with out.open(el) as file:
                        try:
                            tmp = file.read().decode("UTF-8")
                            dct_res.append(json.loads(tmp))
                        except:
                            pass
    for el in sorted([(el['first_name'], el['last_name']) for el in dct_res if el['team'] == 'Arsenal']):
        print(el[0],el[1])

# select_json_from_zip()

#10
def create_tree():
    def convert_bytes(size):
        if size < 1000:
            return f'{size} B'
        elif 1000 <= size < 1000000:
            return f'{round(size / 1024)} KB'
        elif 1000000 <= size < 1000000000:
            return f'{round(size / 1048576)} MB'
        else:
            return f'{round(size / 1073741824)} GB'

    dir_flag = False
    with ZipFile("zip/desktop.zip") as out:
        for el in out.infolist():
            if el.is_dir():
                dir_flag = True
            tmp = el.filename.rstrip("/")
            if len(tmp.split("/")) == 1 :
                print(tmp) if dir_flag else print(f"{tmp} {convert_bytes(el.file_size)}")
            elif len(tmp.split("/")) == 2:
                print(f"  {tmp.split('/')[1]}") if dir_flag else print(f"  {tmp.split('/')[1]} {convert_bytes(el.file_size)}")
            elif len(tmp.split("/")) == 3:
                print(f"    {tmp.split('/')[2]}") if dir_flag else print(f"    {tmp.split('/')[2]} {convert_bytes(el.file_size)}")
            else:
                print(f"      {tmp.split('/')[3]}") if dir_flag else print(f"      {tmp.split('/')[3]} {convert_bytes(el.file_size)}")
            dir_flag = False






