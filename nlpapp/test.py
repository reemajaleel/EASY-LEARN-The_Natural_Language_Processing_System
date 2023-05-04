# from transformers import pipeline
from nlpapp.pipelines import pipeline

g='''
    Paragraphs are the building blocks of papers. Many students define paragraphs in terms of length: a paragraph is a group of at least five sentences, a paragraph is half a page long, etc. In reality, though, the unity and coherence of ideas among sentences is what constitutes a paragraph. A paragraph is defined as “a group of sentences or a single sentence that forms a unit” (Lunsford and Connors 116). Length and appearance do not determine whether a section in a paper is a paragraph. For instance, in some styles of writing, particularly journalistic styles, a paragraph can be just one sentence long. Ultimately, a paragraph is a sentence or group of sentences that support one main idea. In this handout, we will refer to this as the “controlling idea,” because it controls what happens in the rest of the paragraph.
'''
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