import streamlit as st
import pandas as pd
from joblib import load
from scipy.spatial.distance import cdist
import regex as re
import numpy as np
#from flair.data import Sentence
#from flair.models import SequenceTagger
#from flair.visual.ner_html import render_ner_html

multi_space = re.compile("[_ \t]+")
non_ascii = re.compile("[^\x00-\x7FåäöÅÄÖ\s\n\p{Punct}]+")
punct = re.compile('([\p{Punct}\n])+')
assignment_title_clean = re.compile(',?-? ? [Rr]ef')

def clean(text):
    t = non_ascii.sub('', text)
    t = punct.sub(' \g<1> ', t)
    t = multi_space.sub(' ', t)
    t = t.replace('\n', '.')
    t = t.lower()
    return t

def clean_title(text):
    return assignment_title_clean.split(text)[0]

def get_data():
    assignments = pd.read_csv('clean_assignments.csv')
    assignments['title'] = assignments['title'].apply(lambda x: clean_title(x))
    resumes = pd.read_csv('clean_resumes.csv')
    resumes['clean_resume'] = resumes['Resume'].apply(lambda x: clean(x))
    return assignments, resumes

def get_closest(query, resumes, k=5):
    return cdist(query, resumes, metric='cosine').argpartition(k, axis=1)[:,:k]

assignments, resumes = get_data()

tfidf = load('tfidf_on_updated_resumes.joblib')
x_resume = tfidf.transform(resumes['clean_resume']).toarray()
x_assignment = tfidf.transform(assignments['clean_text']).toarray()
dists = get_closest(x_assignment, x_resume)

# tagger = SequenceTagger.load('best-model.pt')


# ====== STREAMLIT =======


st.write("Hello and Welcome to CV Mix & Match!")
chosen = st.radio('Choose a task', ("Match Best Resume", "Search Profiles", "Find Keywords"))#, "Classify CV"))

if chosen == 'Match Best Resume':
    option = st.selectbox('What Assignment Should We Match?', assignments['title'])
    if st.button('Predict'):
        idx = assignments.index[assignments['title'].str.contains(option)]
        text = assignments.iloc[idx]['text']
        st.write()
        cvs = resumes.iloc[dists[idx].tolist()[0]]
        st.write("Assignment Information:")
        st.write(text)
        st.write("Matched Resumes:")
        st.write(cvs)
elif chosen == 'Search Profiles':
    text = st.text_input('Search Query', '')
    if text:
        vec = tfidf.transform([text]).toarray()
        st.write(resumes.iloc[get_closest(vec, x_assignment).tolist()[0]])
    st.write("SEARCHING!")
elif chosen == "Find Keywords":
    text = st.text_input('Search for keywords', '')
    st.write("Because of model size this can't be autodeployed")
    #if text:
    #    manual_sentence = Sentence(text.lower())
    #    tagger.predict(manual_sentence)
    #    st.markdown(render_ner_html(manual_sentence, wrap_page=False), unsafe_allow_html=True)
#elif chosen == "Classify CV":
#    
#    pass