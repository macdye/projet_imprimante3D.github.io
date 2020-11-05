def cut_text(list_element = list, empty_list = list):
    for thing in list_element:
        try:
            n = thing.index('Pages de glossaire connexes')
            pass
        except ValueError:
            pass
        empty_list.append(thing[:n])
        