import nltk


def sentence_read(path):
    """
    读取txt文件中的内容
    :param path: txt文件所对应的路径
    :return: txt文件中的内容
    """
    file = open(path)
    content_str = file.read()
    return content_str


def result_save(result_path, data):
    """
    将词性标注的结果保存为txt文件
    :param result_path: 词性标注结果txt文件所对应的路径
    :param data: 词性标注的结果
    """
    file = open(result_path, 'a')
    for i in range(len(data)):
        s = str(data[i]).replace('[', '').replace(']', '')
        s = s.replace('(', '').replace(')', '')
        s = s.replace("'", '').replace(",", '------') + '\n'
        file.write(s)
    file.close()
    print('词性标注文本保存成功')


# 读取对应txt文件中的内容
path = input("请输入希望进行词性标注的txt文件路径: ")
content = sentence_read(path)
#print(content)


# 分词
text_list = nltk.word_tokenize(content)
#print(text_list)


# 去除列表中的符号
english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%',' ']
text_list = [word for word in text_list if word not in english_punctuations]


# 打标签
label_list = nltk.pos_tag(text_list)
#print(label_list)


# 保存结果为txt文件
result_path = input("请输入词性标注结果文件的保存路径: ")
result_save(result_path, label_list)
