from mot_cle_df import *
import pandas as pd 

def join_table (empty_list=list):
    index_word = 0
    for each_name in df.name:
        print(each_name)
        index_key = 0
        for a in df_key.mots:
            test = {}
            mots = each_name.split()
            i=0
            while i < len(mots):
                if a == mots[i]:
                    print(each_name, 'mot clé trouvé =', a)
                    test['mot_index'] = df.index[index_word]
                    test[f'mot_clés_index'] = df_key.index[index_key]
                    empty_list.append(test)
                i +=1
            index_key+=1
        print("Nothing Find")
        index_word+=1

blah = []
join_table(blah)

jt_table = pd.DataFrame(blah)