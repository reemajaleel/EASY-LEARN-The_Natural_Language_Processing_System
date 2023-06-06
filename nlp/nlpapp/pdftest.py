# from transformers import pipeline
from nlpapp.pipelines import pipeline

g='''
Question: What are the building blocks of papers?
Answer: Paragraphs
Question: What is a paragraph defined as a group of at least five sentences?
Answer: a paragraph is a group of at least five sentences, a paragraph is half a page long, etc
Question: What constitutes a paragraph?
Answer: unity and coherence of ideas among sentences
Question: What is a paragraph defined as?
Answer: a group of sentences or a single sentence that forms a unit
Question: What does not determine whether a section in a paper is a paragraph?
Answer: Length and appearance
Question: How long can a paragraph be in some writing styles?
Answer: one
Question: What is a paragraph defined as?
Answer: a sentence or group of sentences that support one main idea
Question: What does the handout refer to a paragraph as?
Answer: controlling ide'''
qa=pipeline('question-generation')
print(qa,"haiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
s=qa(g)
d=""
m=1
print(s)
for i in s:
    d = d + str(m) + "." + i['question'] + "\n" + "Answer: " + i['answer'] + "\n\n\n\n";
    m=m+1
    print(d)
    from fpdf import FPDF

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size=15)

    f = g

    for i, q in enumerate(s):
        pdf.cell(0, 10, f"{i+1}. {q['question']}", ln=1)
        pdf.cell(0, 10, f"Answer: {q['answer']}", ln=1)
        pdf.cell(0, 10, '', ln=1)  # add a blank line after each question-answer pair

    pdf.output("C://Users//Reema//PycharmProjects//nlp//media//pp1.pdf")