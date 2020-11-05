def make_dict(list_of_element = list, empty_list = list):
    for i in list_of_element:
        res = {}
        a = len(i)//2
        res['part01'] = i[:a]
        res['part02'] = i[a:]
        empty_list.append(res)
    
def suppr_list_type(liste = list):
    for i in liste:
        if type(i['part01']) == list:
            i['part01'] = ','.join(i['part01'])
            i['part02'] = ','.join(i['part02'])
        else:
            pass
