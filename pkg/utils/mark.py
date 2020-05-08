# coding = utf-8

import numpy as np
import pandas as pd
from snownlp import SnowNLP

from pkg.config import data_dir


def snow():
    result = []
    for index in doc_ids:
        s1 = SnowNLP(comments[index])
        mark = {
            'comment': comments[index],
            'score': s1.sentiments,
            'is_positive': True if s1.sentiments > 0.6 else False
        }
        result.append(mark)
        # print('评论：%s, 得分：%f, 是否是好评：%s' % (comments[index], s1.sentiments, '好评' if s1.sentiments > 0.6 else '差评'))
    df = pd.DataFrame(result)
    df.sort_values(['score'], ascending=[True], inplace=True)
    df.to_csv(data_dir + 'comments_result_snow.csv', encoding='utf_8_sig', index=False)


if __name__ == '__main__':
    comments = pd.read_csv(data_dir+'comments.csv')
    print(comments.head())
    idx = np.arange(len(comments))
    np.random.shuffle(idx)
    doc_ids = idx[:len(comments)]

    # snow()
