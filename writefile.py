from globalf import resource_path
import os
import csv

def writef(data):
    filename1='sensor_output.csv'
    filename=resource_path(os.path.join('src', filename1))
    try:
        file_add = open(filename, "a")
        print("Open file " + filename)
        try:
            fwriter=csv.writer(file_add)
            fwriter.writerow(data)
        except Exception as ex:
            print(ex)
        finally:
            file_add.close()
    except:
        print('error File')
    finally:
        pass