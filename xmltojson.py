#coding:utf-8
import re
import json

#读取文件
def loadfile(filename):
    try:
        xml_file = open(filename,'r')
        return xml_file.read()
    except:
        print "读取文件失败"

# 抽取数据
def select_data(split):
    split = split_data(file)
    select_filter = re.compile(r'<filter\s.*?>.*?</filter>',re.S)
    select_id = re.compile(r'\sid="(\d+)"\s')
    select_name = re.compile(r'<name>(.*?)</name>')
    select_description = re.compile(r'<description>(.*?)</description>')
    select_category = re.compile(r'<category>(.*?)</category>')
    select_severity = re.compile(r'<severity>(.*?)</severity>')
    select_cve_id = re.compile(r'<cve\sid="(.*?)">')
    result_filter = select_filter.findall(split)
    list = []
    for item in result_filter:
        result_dic = {}
        result_dic['id'] =  select_id.search(item).group(1)
        result_dic['name'] = select_name.search(item).group(1)
        result_dic['description'] = select_description.search(item).group(1)
        result_dic['category'] = select_category.search(item).group(1)
        result_dic['severity'] = select_severity.search(item).group(1)
        result_dic['cve_id'] = select_cve_id.findall(item)
        list.append(result_dic)
    return list

# 处理数据
def split_data(file):
    xml_read = loadfile(filename)
    split_xml = re.compile(r'\n')
    split_nbsp1 = re.compile(r'\,\s{2,}')
    split_nbsp2 = re.compile(r'\.,,')
    result_sub = split_xml.sub(",",xml_read)
    result_nbsp1 = split_nbsp1.sub(",",result_sub)
    result_split = split_nbsp2.sub(",",result_nbsp1)
    return result_split

#保存成json文件
def py_json(py_data):
    result_list = select_data(py_data)
    content = json.dumps(result_list)
    filename = raw_input("请输入保存文件名,(如test):")+".json"
    with open(filename,'w') as f:
        f.write(content.encode('utf-8'))
    print "保存的json文件为"+filename
    print "执行完毕"

if __name__ == "__main__":
    filename = raw_input("请输入xml文件名,(如test.xml):")
    py_json(filename)
