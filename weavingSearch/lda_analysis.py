import jieba
import json
from weavingSearch.models import Periodical_details, Periodicals, Patent
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer
from weavingSearch.settings import BASE_DIR
import os
import numpy as np
# from mongoengine.queryset.visitor import Q
from django.db.models import Q
from django.core import serializers

file_root = os.path.join(BASE_DIR, 'files')
stop_word_txt = os.path.join(file_root, 'stop_word.txt')


# 文本预处理
def process_text(keywords, category):
    abstract_list = []
    stopwords = [line.strip() for line in open(stop_word_txt, encoding='UTF-8').readlines()]
    text_list = []
    if category == "periodical":
        periodicals = Periodicals.objects.filter(Q(title__icontains=keywords) |
                                                 Q(keywords__icontains=keywords))
        periodicals_json = json.loads(serializers.serialize("json", periodicals))
        for periodical_json in periodicals_json:
            text_list.append(periodical_json["fields"])
        for periodical in text_list:
            abstract_list.append(periodical["abstract"])
    else:
        patent = Patent.objects.filter(Q(name__icontains=keywords))
        patents_json = json.loads(serializers.serialize("json", patent))
        for patent_json in patents_json:
            text_list.append(patent_json["fields"])
        for patent in text_list:
            abstract_list.append(patent["name"])
    jieba_list = []
    for abstract in abstract_list:
        jieba_list.append(jieba.cut(abstract))
    jieba_list_nonestop = []
    for cut_abstract in jieba_list:
        cut_none_stop = []
        for word in cut_abstract:
            if word not in stopwords:
                cut_none_stop.append(word)
        jieba_list_nonestop.append(cut_none_stop)
    return jieba_list_nonestop, len(text_list)


# 词向量统计
def count_vector(keywords, category):
    jieba_list_nonestop = process_text(keywords, category)[0]
    new_jieba_list_nonestop = []
    for word_cut in jieba_list_nonestop:
        new_jieba_list_nonestop.append(' '.join(word_cut).encode('utf-8'))
    count_vec = CountVectorizer()
    cntTf = count_vec.fit_transform(new_jieba_list_nonestop)
    return cntTf, count_vec


# 训练模型
def train_lad(keywords, category):
    word_vector = count_vector(keywords, category)
    cntTf = word_vector[0]
    n_topics = range(1, 8, 1)
    lda_models = []
    lda_docres = []
    perplexityLst = [1.0] * len(n_topics)
    for idx, n_topic in enumerate(n_topics):
        lda = LatentDirichletAllocation(n_components=n_topic,
                                        learning_offset=50,
                                        random_state=0, max_iter=10)
        docres = lda.fit_transform(cntTf)
        perplexityLst[idx] = lda.perplexity(cntTf)
        lda_docres.append(docres)
        lda_models.append(lda)
    best_index = perplexityLst.index(min(perplexityLst))
    best_n_topic = n_topics[best_index]
    best_docres = lda_docres[best_index]
    best_model = lda_models[best_index]
    best_topic = []
    for t in best_docres:
        best_topic.append(list(t).index(np.max(t)))
    return best_topic, best_n_topic, get_top_words(best_model, word_vector[1].get_feature_names(), 10)


# 得到主题关键词
def get_top_words(model, feature_names, n_top_words):
    tword = []
    for topic_idx, topic in enumerate(model.components_):
        topic_w = " ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]])
        tword.append(topic_w)
    return tword
