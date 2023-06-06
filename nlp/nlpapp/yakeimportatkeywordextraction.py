import yake

text_content = """
Sources tell us that Google is acquiring Kaggle, a platform that hosts data science and machine learning
competitions. Details about the transaction remain somewhat vague , but given that Google is hosting
its Cloud Next conference in San Francisco this week, the official announcement could come as early
as tomorrow. Reached by phone, Kaggle co-founder CEO Anthony Goldbloom declined to deny that the
acquisition is happening. Google itself declined 'to comment on rumors'.
"""

# # assuming default parameters
# simple_kwextractor = yake.KeywordExtractor()
# keywords = simple_kwextractor.extract_keywords(text_content)
#
# for kw in keywords:
#     print(kw)


custom_kwextractor = yake.KeywordExtractor(lan="en", n=1, dedupLim=0.8, windowsSize=2, top=20)
keywords = custom_kwextractor.extract_keywords(text_content)

for kw in keywords:
    print(kw)