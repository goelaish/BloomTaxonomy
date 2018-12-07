import pandas as pd
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from wup_sim import wup_sim_fun
from path_sim import path_sim_fun
from jcn_sim import jcn_sim_fun
from res_sim import res_sim_fun
from lin_sim import lin_sim_fun
from lch_sim import lch_sim_fun


clean_words_list=[]

def read_file(filepath):
    df=pd.read_csv(filepath,usecols=["QUESTIONS"])
    return df

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return ''

def read_ques_words(filepath="/home/aishgoel/MAJORVIIthsem/ques_words_unique.txt"):
    # file_handle = open(filepath,"r")
    # string=(file_handle.read())
    # li = list(string.split(","))
    file_handle=open(filepath,"r")
    file=file_handle.read()
    file=file.lower()
    # print file
    # print (type(file))
    return file


#create indiviual sentences and then tokenize words
def tokenize_fun(df,ques_words):
    for index,row in df.iterrows():
        #list of tokenized words
        # print index
        words=[]
        row=row.values[0]
        # print(type(row))
        row_tok=sent_tokenize(row)
        for sentence in row_tok:
            # print(sentence)
            word_tok=word_tokenize(sentence)
            words+=word_tok


        clean_words=words[:]
        punctuations_filepath="/home/aishgoel/MAJORVIIthsem/punctuations"
        stopwords_filepath="/home/aishgoel/MAJORVIIthsem/nltk_data/corpora/stopwords/english"
        punctuations=open(punctuations_filepath,"r")
        stopwords=open(stopwords_filepath,"r")
        punctuations=punctuations.read()
        stopwords=stopwords.read()
        # print ("1",type(punctuations))
        for token in words:
            if token in punctuations:
                clean_words.remove(token)
            else:
                if token in stopwords:
                    clean_words.remove(token)


        words=clean_words
        # print(index)
        # for word in clean_words:
        #     print(word)
        # input()


        pos_tag_list=pos_tag(words)
        # print (type(token_pos[0]))
        # for pos_tag in pos_tag_list:
        #     print pos_tag
        lemmatizer=WordNetLemmatizer()
        lem_list=[]
        for tuple in pos_tag_list:
            # print(tuple[0],tuple[1])
            wordnet_tag=get_wordnet_pos(tuple[1])
            try:
                tuple[0].decode('ascii')
            except UnicodeDecodeError:
                # print "Not a ascii"
                continue
            if(wordnet_tag==''):
                lemmatized_word= (lemmatizer.lemmatize(tuple[0]))
            else:
                # print wordnet_tag
                lemmatized_word= (lemmatizer.lemmatize(tuple[0],wordnet_tag))
            lemmatized_word=str(lemmatized_word)
            lem_list.append(lemmatized_word)
            # print (type(lemmatized_word))
            # print ("original word",tuple[0],"lemmatized_word",lemmatized_word)
        words=lem_list


        #***************************lemmatization done till here***********************************************


        clean_words=[]
        # print clean_words
        for token in words:
            token=token.lower()
            if token in ques_words:
                clean_words.append(token)
        # for word in clean_words:
            # print(word)
        clean_words_list.append(clean_words)
        # print (clean_words)


def read_file_for_level(filepath):
    df=pd.read_csv(filepath,usecols=["COGNITIVE LEVELS"])
    # for index,row in df.iterrows():
    #     print index,row.values[0]
    return df



filepath="/home/aishgoel/MAJORVIIthsem/Dataset/correct_dataset.csv"

ques_words=read_ques_words()
df=read_file(filepath)

def make_questions_list(df):
    questions_list=[]
    for index,row in df.iterrows():
        questions_list.append(row.values[0])
    # print questions_list
    return questions_list

tokenize_fun(df,ques_words)
# print clean_words_list
dict={'Knowledge':0,'Comprehension':1,'Application':2,'Analysis':3,'Synthesis':4,'Evaluation':5}
inv_dict={0:'Knowledge',1:'Comprehension',2:'Application',3:'Analysis',4:'Synthesis',5:'Evaluation'}

def predict_fun(wup=False,path=False,jcn=False,res=False,lin=False,lch=False):
    if wup:
        pred_cnt=[0 ,0, 0, 0, 0, 0]
        acc_cnt=0
        total_cnt=0
        actual_levels=read_file_for_level(filepath)
        actual_levels_list=[]
        for index,row in actual_levels.iterrows():
            # print row.values
            actual_levels_list.append(row.values[0])
        actual_levels=actual_levels_list
        # print actual_levels
        questions_list=make_questions_list(df)
        for index,question in enumerate(clean_words_list):
            # if index>10:
            #     break
            # level_pred=sim_algo_fun_path(question)
            level_pred=wup_sim_fun(question)
            # print level_pred
            pred_cnt[level_pred]+=1
            level_act=actual_levels[index]
            # print ("hi",level_pred,level_act)
            if level_pred==dict[level_act]:
                acc_cnt+=1
            total_cnt+=1
            # print(questions_list[index])
            # print('predicted',inv_dict[level_pred])
            # print('actual',level_act)

            # input()
        print("Wu palmer")
        print("total_cnt",total_cnt)
        print ("Accuracy",float(acc_cnt)/float(total_cnt))
        print("Acc count",acc_cnt)

    if path:
        pred_cnt=[0 ,0, 0, 0, 0, 0]
        acc_cnt=0
        total_cnt=0
        actual_levels=read_file_for_level(filepath)
        actual_levels_list=[]
        for index,row in actual_levels.iterrows():
            # print row.values
            actual_levels_list.append(row.values[0])
        actual_levels=actual_levels_list
        # print actual_levels
        questions_list=make_questions_list(df)
        for index,question in enumerate(clean_words_list):
            # if index>10:
            #     break
            # level_pred=sim_algo_fun_path(question)
            level_pred=path_sim_fun(question)
            # print level_pred
            pred_cnt[level_pred]+=1
            level_act=actual_levels[index]
            # print ("hi",level_pred,level_act)
            if level_pred==dict[level_act]:
                acc_cnt+=1
            total_cnt+=1
            # print(questions_list[index])
            # print('predicted',inv_dict[level_pred])
            # print('actual',level_act)

            # input()
        print("Path")
        print("total_cnt",total_cnt)
        print ("Accuracy",float(acc_cnt)/float(total_cnt))
        print("Acc count",acc_cnt)

    if jcn:
        pred_cnt=[0 ,0, 0, 0, 0, 0]
        acc_cnt=0
        total_cnt=0
        actual_levels=read_file_for_level(filepath)
        actual_levels_list=[]
        for index,row in actual_levels.iterrows():
            # print row.values
            actual_levels_list.append(row.values[0])
        actual_levels=actual_levels_list
        # print actual_levels
        questions_list=make_questions_list(df)
        for index,question in enumerate(clean_words_list):
            # if index>10:
            #     break
            # level_pred=sim_algo_fun_path(question)
            level_pred=jcn_sim_fun(question)
            # print level_pred
            pred_cnt[level_pred]+=1
            level_act=actual_levels[index]
            # print ("hi",level_pred,level_act)
            if level_pred==dict[level_act]:
                acc_cnt+=1
            total_cnt+=1
            # print(questions_list[index])
            # print('predicted',inv_dict[level_pred])
            # print('actual',level_act)

            # input()
        print("Jcn")
        print("total_cnt",total_cnt)
        print ("Accuracy",float(acc_cnt)/float(total_cnt))
        print("Acc count",acc_cnt)

    if res:
        pred_cnt=[0 ,0, 0, 0, 0, 0]
        acc_cnt=0
        total_cnt=0
        actual_levels=read_file_for_level(filepath)
        actual_levels_list=[]
        for index,row in actual_levels.iterrows():
            # print row.values
            actual_levels_list.append(row.values[0])
        actual_levels=actual_levels_list
        # print actual_levels
        questions_list=make_questions_list(df)
        # print ("actual_levels",actual_levels)
        for index,question in enumerate(clean_words_list):
            # if index>10:
            #     break
            # level_pred=sim_algo_fun_path(question)
            level_pred=res_sim_fun(question)
            # print level_pred
            pred_cnt[level_pred]+=1
            # print ("index",index)
            level_act=actual_levels[index]
            # print ("hi",level_pred,level_act)
            if level_pred==dict[level_act]:
                acc_cnt+=1
            total_cnt+=1
            # print(questions_list[index])
            # print('predicted',inv_dict[level_pred])
            # print('actual',level_act)

            # input()
        print("Res")
        print("total_cnt",total_cnt)
        print ("Accuracy",float(acc_cnt)/float(total_cnt))
        print("Acc count",acc_cnt)

    if lin:
        pred_cnt=[0 ,0, 0, 0, 0, 0]
        acc_cnt=0
        total_cnt=0
        actual_levels=read_file_for_level(filepath)
        actual_levels_list=[]
        for index,row in actual_levels.iterrows():
            # if index>10:
            #     break
            # print row.values
            actual_levels_list.append(row.values[0])
        actual_levels=actual_levels_list
        # print actual_levels
        questions_list=make_questions_list(df)
        for index,question in enumerate(clean_words_list):
            # if index>10:
            #     break
            # level_pred=sim_algo_fun_path(question)
            level_pred=lin_sim_fun(question)
            # print level_pred
            pred_cnt[level_pred]+=1
            level_act=actual_levels[index]
            # print ("hi",level_pred,level_act)
            if level_pred==dict[level_act]:
                acc_cnt+=1
            total_cnt+=1
            # print(questions_list[index])
            # print('predicted',inv_dict[level_pred])
            # print('actual',level_act)

            # input()
        print("lin")
        print("total_cnt",total_cnt)
        print ("Accuracy",float(acc_cnt)/float(total_cnt))
        print("Acc count",acc_cnt)

    if lch:
        pred_cnt=[0 ,0, 0, 0, 0, 0]
        acc_cnt=0
        total_cnt=0
        actual_levels=read_file_for_level(filepath)
        actual_levels_list=[]
        for index,row in actual_levels.iterrows():
            # if index>10:
            #     break
            # print row.values
            actual_levels_list.append(row.values[0])
        actual_levels=actual_levels_list
        # print actual_levels
        questions_list=make_questions_list(df)
        for index,question in enumerate(clean_words_list):
            # if(index>10):
            #     break
            # level_pred=sim_algo_fun_path(question)
            level_pred=lch_sim_fun(question)
            # print level_pred
            pred_cnt[level_pred]+=1
            level_act=actual_levels[index]
            # print ("hi",level_pred,level_act)
            if level_pred==dict[level_act]:
                acc_cnt+=1
            total_cnt+=1
            # print(questions_list[index])
            # print('predicted',inv_dict[level_pred])
            # print('actual',level_act)

            # input()
        print("LCH")
        print("total_cnt",total_cnt)
        print ("Accuracy",float(acc_cnt)/float(total_cnt))
        print("Acc count",acc_cnt)

predict_fun(True,True,True,True,True,True)
