####################################################################################
#                                   测试词向量                                      #
####################################################################################

import spacy

nlp = spacy.load('zh_core_web_md')

a = nlp.vocab["铜器"]
print(a.vector)
b = nlp.vocab['铜']
print(a.similarity(b))