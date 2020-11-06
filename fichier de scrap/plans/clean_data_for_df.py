def clean_data_from_scrap(list_of_object = list,empty_list = list):
    for objet in list_of_object:
        obj = {}
        for element in objet:
            a = element.split(':',1)
            if len(a) == 2:
                key = str(a[0]).replace('"','')
                cont= str(a[1]).replace('"','')
                obj[key]=cont
        empty_list.append(obj)