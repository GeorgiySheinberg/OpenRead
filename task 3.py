def create_result():
    dict_ = {}
    with open("1.txt", "r", encoding='utf-8') as txt1:
        lines_1 = txt1.readlines()
        dict_['1.txt'] = lines_1
    with open("2.txt", "r", encoding='utf-8') as txt2:
        lines_2 = txt2.readlines()
        dict_['2.txt'] = lines_2
    with open("3.txt", "r", encoding='utf-8') as txt3:
        lines_3 = txt3.readlines()
        dict_['3.txt'] = lines_3

    list_line = [lines_1, lines_2, lines_3]
    list_line.sort(key=len)
    with open('result.txt', "w", encoding='utf-8') as result:
        for line in list_line:
            for k, v in dict_.items():
                if v == line:
                    result.write(k)
            result.write('\n')
            result.write(str(len(line)))
            result.write('\n')
            for string in line:
                result.write(string)


create_result()
