def clean_def(list_element = list, empty_list = list):
    spliter = []
    for i in list_element:
        a = i.split('  ')
        spliter.append(a)
    for i in spliter:
        beh = []
        for a in i:
            if len(a) > 1:
                beh.append(a)
        empty_list.append(beh)
    