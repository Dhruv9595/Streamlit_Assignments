import streamlit as st
import datetime

with st.form("Food"):
    st.title("Food Application", text_alignment="center")
    Name = st.text_input(label="Name", placeholder="Enter your Name")
    City = st.selectbox(label="City", options=["Vadodara", "Surat", "Ahmedabad", "Godhra"])
    Food_Pref = st.multiselect(label="Food Preference", options=("Punjabi", "Chienese", "South Indian", "Gujarati"))
    Orders = st.slider("How many times you have order the food", min_value=0, max_value=10)
    Gender = st.radio("Gender", options=("Male", "Female"), horizontal=True)
    Dob = st.date_input("Date of Birth")

    c1,c2 = st.columns(2)
    Food_Items = c1.multiselect(label="Food Items", options=("Paneer Chilli", "Kabab", "Pizza", "Burger", "Dosa", "Khichadi", "Chienese Bhel"))
    Beverages = c2.multiselect(label="Beverage", options=("Coca-Cola", "Thumpsups", "Moctails", "Fanta"))
    
    Audio = st.audio_input("Record your foods items and beverages you want.")

    Feedback = st.text_area("Share your review",placeholder="Enter your feedback", height=50)

    Agreement = st.checkbox("I agree")

    
    Submit = st.form_submit_button("Submit", use_container_width="center")

    if(Submit):
        if(Agreement==False):
            st.error("You have to accept terms and condition")
        else:
            st.balloons()    
            st.success("Your order has been placed")
            st.toast("You have registered successfully 🎉")


            st.write("Name :", Name)
            st.write("City :", City)
            st.write(f"Food Preference {Food_Pref}")
            st.write(f"Food : {Food_Items}")
            st.write(f"Berverages : {Beverages}")
            
            if(Audio):
                st.write("Message recorded successfully")
                st.audio(Audio)


            if(Feedback):
                st.write("Thanks for your feedback.")





