from execute_scrap import keys, definitions, words
from clean_def import clean_def
from cut_text import cut_text
from make_dict__suppr_list import make_dict, suppr_list_type

result = []
clean_def(definitions,result)

text=[]
cut_text(result, text)

text_dict = []
make_dict(text, text_dict)
suppr_list_type(text_dict)