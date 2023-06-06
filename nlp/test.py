from transformers import pipelines


def qa1():

    import os
    import docx
    g='Hello. How Are You?'
    qa=pipelines.pipeline('question-answering')
    # print(qa,"haiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    s=qa(g)
    d=""
    m=1
    print(s)
    for i in s:
        d = d + str(m) + "." + i['question'] + "\n" + "Answer: " + i['answer'] + "\n\n\n\n";
        m=m+1
        print(d)
    print(s)
qa1()