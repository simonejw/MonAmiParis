import streamlit as st

st.set_page_config(
    page_title="Bienvenue"
)

# Language selection
language = st.sidebar.selectbox(
    'Language:',
    ('Français', 'English')
)

caption_fr = "La Tour Eiffel vue du septième arrondissement"
caption_en = "The Eiffel Tower as seen from the seventh district"
if language == 'Français': 

    st.header("Bienvenue à Mon Ami Paris!")

    st.image("paris4.png", caption= caption_fr)
    
    st.markdown(
        """
        Mon Ami Paris est une application qui propose un plan interactif de Paris avec plusieurs vues pour vous aider à naviguer dans la ville de Paris. Toutes les données proviennent de Paris Open Data - https://opendata.paris.fr/
    
    """
)

elif language == 'English': 

    st.header("Welcome to Mon Ami Paris!")

    st.image("paris1.png", caption= caption_en, width = 725)


    st.markdown(
        """
        Mon Ami Paris is an app that offers an interactive map of Paris with multiple views to help you navigate the city of Paris. All data is from Paris Open Data - https://opendata.paris.fr/
    
    """
)