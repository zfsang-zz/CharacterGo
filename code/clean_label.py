import pandas as pd
import glob
import os
import json
from utils.file_io_helper import unicode_normalizer
import pickle
def read_label_files(path):
    names = ['character1','character2','relationship']
    label_dict = {}
    for file in  glob.glob('{}/*.xlsx'.format(path)):
        try:
            df = pd.read_excel(file, header=None, names=names)
            df = df.dropna().values.tolist() 
            # title = str(unicode_normalizer(os.path.basename(file).split('.')[1]))
            title = str(os.path.basename(file).split('.')[0])
            label_dict[title]={(unicode_normalizer(i1).lower().strip(),unicode_normalizer(i2).lower().strip()):unicode_normalizer(i3).lower().strip() for i1,i2,i3 in df}
        except:
            pass
    return label_dict

if __name__ == '__main__':
    label_dict = read_label_files('../data/label')
    pickle.dump( label_dict, open( "../data/all_label.p", "wb" ) )

    # r = json.dumps(label_dict)
    # with open('../data/all_label2.json','w') as file:
    #     file.write(r)