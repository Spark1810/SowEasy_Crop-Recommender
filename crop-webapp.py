import streamlit as st
import pandas as pd
import random
import pickle
from PIL import Image

LogReg_model=pickle.load(open('LogReg_model.pkl','rb'))
DecisionTree_model=pickle.load(open('DecisionTree_model.pkl','rb'))
NaiveBayes_model=pickle.load(open('NaiveBayes_model.pkl','rb'))
RF_model=pickle.load(open('RF_model.pkl','rb'))

data = {
    'Nitrogen': [37, 12, 7, 22, 35, 12, 9, 41, 21, 9, 13, 14, 36, 24, 14, 10, 38, 21, 39, 13, 10, 12, 11, 36, 13, 23, 9, 38, 12, 14, 24, 12, 39, 7, 23, 41, 8, 12, 15, 15, 13, 10, 22, 35, 10, 8, 12, 24, 41, 5, 23, 13, 40, 12, 11, 23, 38, 8, 11, 15, 36, 13, 24, 5, 37, 15, 9, 8, 6, 10, 21, 39, 23, 42, 13, 9, 22, 10, 7, 14, 10, 41, 14, 11, 21, 8, 13, 35, 12, 11, 8, 6, 41, 9, 24, 4, 39, 15, 12],
    'Potassium': [0, 0, 9, 0, 0, 10, 0, 0, 0, 7, 0, 15, 0, 0, 0, 13, 0, 0, 0, 0, 0, 14, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 9, 0, 0, 10, 0, 14, 0, 0, 7, 0, 0, 0, 8, 0, 0, 0, 9, 0, 0, 0, 0, 12, 0, 0, 0, 13, 0, 0, 0, 0, 18, 0, 0, 0, 8, 19, 0, 0, 0, 0, 0, 0, 10, 0, 0, 16, 0, 8, 0, 0, 7, 0, 17, 0, 0, 0, 18, 0, 9, 19, 0, 10, 0, 17, 0, 0],
    'Phosphorous': [0, 36, 30, 20, 13, 10, 0, 18, 30, 40, 12, 0, 22, 41, 14, 0, 19, 0, 36, 9, 12, 37, 0, 10, 20, 29, 0, 39, 13, 23, 40, 0, 30, 19, 0, 31, 41, 11, 37, 13, 32, 24, 0, 35, 28, 8, 18, 0, 29, 21, 14, 0, 42, 15, 24, 0, 15, 15, 37, 0, 9, 20, 15, 0, 40, 13, 33, 16, 14, 23, 0, 19, 0, 39, 22, 21, 15, 20, 38, 29, 0, 35, 9, 28, 31, 16, 0, 19, 38, 30, 21, 17, 0, 30, 19, 17, 0, 41, 10],
    'Fertilizer Name': ['Urea', 'DAP', 'Fourteen-Thirty Five-Fourteen', 'DAP', 'Twenty Eight-Twenty Eight', 'Urea', 'Seventeen-Seventeen-Seventeen', 'Twenty-Twenty', 'Urea', 'Twenty Eight-Twenty Eight', 'Fourteen-Thirty Five-Fourteen', 'DAP', 'Seventeen-Seventeen-Seventeen', 'Urea', 'Twenty Eight-Twenty Eight', 'DAP', 'Seventeen-Seventeen-Seventeen', 'Urea', 'Twenty Eight-Twenty Eight', 'Urea', 'DAP', 'Twenty-Twenty', 'Seventeen-Seventeen-Seventeen', 'DAP', 'Urea', 'Twenty-Twenty', 'Twenty Eight-Twenty Eight', 'Fourteen-Thirty Five-Fourteen', 'Urea', 'DAP', 'Twenty-Twenty', 'Twenty Eight-Twenty Eight', 'DAP', 'Urea', 'Fourteen-Thirty Five-Fourteen', 'Twenty Eight-Twenty Eight', 'Urea', 'Fourteen-Thirty Five-Fourteen', 'DAP', 'Seventeen-Seventeen-Seventeen', 'DAP', 'Twenty-Twenty', 'Fourteen-Thirty Five-Fourteen', 'Twenty Eight-Twenty Eight', 'Urea', 'DAP', 'Fourteen-Thirty Five-Fourteen', 'Twenty-Twenty', 'Twenty Eight-Twenty Eight', 'Urea', 'Fourteen-Thirty Five-Fourteen', 'Twenty Eight-Twenty Eight', 'Twenty-Twenty', 'Urea', 'DAP', 'Seventeen-Seventeen-Seventeen', 'Twenty Eight-Twenty Eight', 'Urea', 'Twenty-Twenty', 'Seventeen-Seventeen-Seventeen', 'DAP', 'Urea', 'Twenty-Twenty', 'Twenty Eight-Twenty Eight', 'Ten-Twenty Six-Twenty Six', 'Urea', 'DAP', 'Twenty-Twenty', 'Fourteen-Thirty Five-Fourteen', 'Ten-Twenty Six-Twenty Six', 'Twenty-Twenty', 'Twenty Eight-Twenty Eight', 'Urea', 'Twenty Eight-Twenty Eight', 'Urea', 'DAP', 'Fourteen-Thirty Five-Fourteen', 'Twenty Eight-Twenty Eight', 'Ten-Twenty Six-Twenty Six', 'DAP', 'Fourteen-Thirty Five-Fourteen', 'Urea', 'DAP', 'Twenty-Twenty', 'Twenty Eight-Twenty Eight', 'Fourteen-Thirty Five-Fourteen', 'Ten-Twenty Six-Twenty Six', 'Urea', 'Ten-Twenty Six-Twenty Six', 'DAP', 'Fourteen-Thirty Five-Fourteen', 'Ten-Twenty Six-Twenty Six', 'Urea', 'Fourteen-Thirty Five-Fourteen', 'Twenty Eight-Twenty Eight', 'Ten-Twenty Six-Twenty Six', 'Urea', 'DAP', 'Twenty-Twenty']
}

# Convert to DataFrame
df = pd.DataFrame(data)

def classify(answer):
    return answer[0]+" is the best crop for cultivation here."


def main():
    st.title("SowEasy - Smart Fertilizer And Crop Recommender System")
    image=Image.open('cc.jpg')
    st.image(image)
    html_temp = """
    <div style="background-color:teal; padding:10px">
    <h2 style="color:white;text-align:center;">Find The Most Suitable Fertilizer and Crop for Your Land</h2>
    </div>
    """

    st.markdown(html_temp, unsafe_allow_html=True)
    activities=['Naive Bayes (The Best Model)','Logistic Regression','Decision Tree','Random Forest']
    option=st.sidebar.selectbox("Which Model would you like to use?",activities)
    st.subheader(option)
    sn=st.slider('NITROGEN (N)', 0, 50)
    sp=st.slider('PHOSPHOROUS (P)', 0, 50)
    pk=st.slider('POTASSIUM (K)', 0, 20)
    pt=st.slider('TEMPERATURE', 0, 50)
    phu=st.slider('HUMIDITY', 0, 100)
    pPh=st.slider('Ph', 0, 14)
    pr=st.slider('RAINFALL', 0, 300)
    inputs=[[sn,sp,pk,pt,phu,pPh,pr]]
    if st.button('Predict'):
        nitrogen = sn
        potassium = pk
        phosphorous = sp

        # Find matching fertilizer
        matching_fertilizer = df[(df['Nitrogen'] == nitrogen)]

        if not matching_fertilizer.empty:
            fertilizer_name = matching_fertilizer['Fertilizer Name'].values[0]
        else:
            fertilizer_name = (df['Fertilizer Name'].values[20])

        st.success(f'The Recommended Fertilizer is {fertilizer_name}')



        if option=='Logistic Regression':
            st.info(classify(LogReg_model.predict(inputs)))
        elif option=='Decision Tree':
            st.info(classify(DecisionTree_model.predict(inputs)))
        elif option=='Naive Bayes':
            st.info(classify(NaiveBayes_model.predict(inputs)))
        else:
            st.info(classify(RF_model.predict(inputs)))   


if __name__=='__main__':
    main()
