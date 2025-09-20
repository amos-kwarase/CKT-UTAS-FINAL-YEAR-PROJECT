import streamlit as st
import tensorflow as tf
import numpy as np



def predict(model, test_image):
    model = tf.keras.models.load_model("Adam.keras")
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(256,256))
    img_array = tf.keras.preprocessing.image.img_to_array(image)
    img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array)
    class_names= ['Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy']
    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = round(100 * (np.max(predictions[0])), 2)
    return predicted_class, confidence

def get_management_recommendations():
    management_practices = """
    **Management Practices for Bacterial Spot:**
    - Use disease-free seeds and transplants
    - Practice crop rotation (2-3 years without peppers/tomatoes)
    - Avoid overhead irrigation to reduce leaf wetness
    - Space plants properly for good air circulation
    - Remove and destroy infected plant debris
    - Work with plants when they are dry to prevent spread
    """
    
    recommended_chemicals = """
    **Recommended Chemicals:**
    - Orizon
    - Copper-based bactericides
    - Always follow label instructions and rotate chemicals to prevent resistance
    """
    
    return management_practices, recommended_chemicals


st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page", ["Home", "About", "Bacterial Spot Diagnos"])

if (app_mode=="Home"):
    st.header("Bacterial Spot Recognition System")
    image_path = "homepage_logo.jpg"
    st.image(image_path, width=350)
    st.markdown("""
                ### Get Started
                 
                Navrongo is a high densely populated farming community. Farmers lack access to diagnostic tools and modern solutions like laboratory testing, which is very expensive and time consuming. The rely on traditional disease detection techniques rely on visual assessment by old experienced farmers and agriculture expects.
                """
                """
                The primary objective of this project is to develop an automated deep learning-Based system for Bacterial spot detection in Bell pepper plant disease using CNN.
                """
                )
    
elif(app_mode=="About"):
    st.header("About")
    st.markdown("""
                ### About this Project
                This project is a Deep Learning tool that helps Pepper farmers quickly identify Bacterial Spot in Bell Pepper plants, enabling early detection and intervention.
                This helps reduce crop yield losses through timely accurate diagnosis and practical management recommendations.
                """)
    st.markdown("""
                ### Team
                - **DR. MOSES APAMBILA AGEBURE,PHD** - Supervisor, Senior Lecterer at CK Tedam UNiversity for Tecnology and Applied Sciences 
                - **Mr. Amos Kwarase** - Project Student
                
                """)
    
elif(app_mode=="Bacterial Spot Diagnos"):
    st.header("Bacterial Spot Diagnos")
    test_image = st.file_uploader("Choose an Image")
    if(st.button("Show Image")):
        st.image(test_image, use_column_width=True)

    if(st.button("Predict")):
        st.write("Model Prediction")
        predicted_class, confidence = predict(None, test_image)
        st.success("Prediction: {}".format(predicted_class))
        st.success("Confidence: {}%".format(confidence))

        if predicted_class == 'Pepper,_bell___Bacterial_spot':
            st.warning("⚠️ Bacterial Spot Detected - Management Recommendations")
            management, chemicals = get_management_recommendations()
            st.info(management)
            st.info(chemicals)
        else:
            st.success("Good Farming Practices Adopted, Your Farm is free from Bacterial Sopt Disease")




