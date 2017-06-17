#coding:utf-8
import json
import csv

def json_data(filename_json):
    with open(filename_json,'r') as jsonfile:
        return json.load(jsonfile)

def csv_data(filename_json,filename_csv):
    content_list = json_data(filename_json)
    sheet = content_list[0].keys()
    data = []
    for content in content_list:
        data.append(content.values())
    csvfile = file(filename_csv,'w')
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(sheet)
    csvwriter.writerows(data)
    csvfile.close()

if __name__ == "__main__":
    filename_json = raw_input("请输入json文件名,(如test.json):")
    filename_csv = raw_input("请输入要保存为csv的文件名,(如test.csv):")
    csv_data(filename_json,filename_csv)
