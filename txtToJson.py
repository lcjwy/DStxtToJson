import os
import json
import re


# qrid date time qqname qglvlname qqname qqid qgrecord
# 字符串分离，解析为一个个小字符串，每一个集合字符串为一个切片字典。

f1 = "q1.txt"
f2 = 'write_data2.txt'
keys = ['qrid', 'date', 'time', 'qglvlname', 'qqname', 'qqid', 'qgrecord']
sstr = []
records = []

def clearSpace(f1, f2):
    # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！:
    with open(f1, "r", encoding='UTF-8') as fr:
        l1 = []

        lines = fr.readlines()
        # print(lines)
        for i in range(len(lines)):
            if lines[i] != '\n':
                l1.append(lines[i].replace('\n', ''))
                # print(l1)
            else:
                if l1 != []:
                    sstr.append(l1)
                l1 = []
        # print(sstr)
        sstr.append(l1)
    fr.close()
    print('ok')

def writeToTxt(sstr):
    for i in range(len(sstr)):
        line = sstr[i]
        # print(type(line[0]))
        # print(line)
        # if line[0]:
            # print('1')
        lenLine = len(line)
        if lenLine > 1:
            for j in range(2, lenLine):
                line[1] = line[1]+ ',' + line[j]
                line[j] = ''
        else:
            line.append(' ')
        while '' in line:
            line.remove('')
        # print(line)
        qgrecord = line[1]
        # print(i)
        string = ''.join(line[0])
        a = r'【(.*?)】'
        b = r'】(.*?)\('
        b2 = r'】(.*?)<'
        c = r'\((.*?)\)'
        c2 = r'<(.*?)>'
        qglvlname = ''.join(re.findall(a, line[0]))
        if re.findall(b2, line[0]) != [] and re.findall(c2, line[0]) != []:
            qqname= ''.join(re.findall(b2, line[0]))
            qqid = ''.join(re.findall(c2, line[0]))
        else:
            qqname= ''.join(re.findall(b, line[0]))
            qqid = ''.join(re.findall(c, line[0]))
        # print(qglvlname, qqname, qqid)
        datetimeStr = string.replace('【' + qglvlname + '】'+ qqname + '(' + qqid + ')', '').strip().split(' ')
        dateStr = datetimeStr[0]
        timeStr = datetimeStr[1]
        # timeStr = ' '
        # print(dateStr, timeStr)
        # keys = ['qrid', 'date', 'time', 'qglvlname', 'qqname', 'qqid', 'qgrecord']
        line[0] = str(i+1)
        line[1] = dateStr
        line.append(timeStr)
        if qglvlname == '':
            qglvlname = ' '
        line.append(qglvlname)
        if qqname == '':
            qqname = ' '
        line.append(qqname)
        if qqid == '':
            qqid= ' '
        line.append(qqid)
        line.append(qgrecord)
        sstr[i] = line
        record = {}
        record = dict(zip(keys, sstr[i]))
        # print(record)
        records.append(record)
        # print(records)
        # print(sstr[i])
    with open(f2, 'w', encoding='utf-8') as fw:
        fw.write('[')
        for d in records:
            fw.write(str(d))
            fw.write(',\n')
        fw.write(']')
        fw.close()
        print('ok2')
if __name__ == '__main__':
    clearSpace(f1, f2)
    writeToTxt(sstr)


    # for cntx in lines:
    #     if cntx == '\n':
    #         if line[line+1] == '\n':
    #             cnt = 0
    #         line = 0
    #         d = dict(zip(keys, sstr))
    #         records.append(str(d))
    #         f.write(str(d))
    #         f.write('\n')
    #     if line == 1:
    #         print(cntx)
    #         cntx1 = cntx.replace('\n', '')
    #         s1 = re.compile('【')
    #         cntx1 = s1.sub('', cntx1)
    #         s2 = re.compile('】')
    #         cntx1 = s2.sub(' ', cntx1)
    #         s3 = re.compile('\(')
    #         cntx1 = s3.sub(' ', cntx1)
    #         s4 = re.compile('\)')
    #         cntx1 = s4.sub('', cntx1)
    #         sstr = cntx1.split(' ')
    #         sstr.insert(0, cnt)
    #         cnt = cnt + 1
    #         # print(type(str))
    #     if line!= 0 and line != 1:
    #         print(cntx)
    #         cntx2 = cntx.replace('\n', '')
    #         s5 = re.compile('\[')
    #         cntx2 = s5.sub('', cntx2)
    #         s6 = re.compile('\]')
    #         cntx2 = s6.sub('', cntx2)
    #         sstr.append(cntx2)
    #         # print(str)
    #         #     records.append(sstr)
    #         # print(d)
    #     line = line + 1
    # # print(d)
    # # records.append(d)
    # # print('a')
    # f.write(']')
    # # print(records)

