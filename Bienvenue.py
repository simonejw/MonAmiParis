import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Bienvenue")

def show_welcome_message():
    """
    Shows the welcome message based on the selected language.

    """
    # Language selection
    language = st.sidebar.selectbox(
        'Language:',
        ('Français', 'English')
    )

    caption_fr = "La Tour Eiffel vue du septième arrondissement"
    caption_en = "The Eiffel Tower as seen from the seventh district"

    image_file = 'Data/paris4.png'
    if language == 'Français':
        # Show the welcome message in French
        st.header("Bienvenue à Mon Ami Paris!")
        st.image(image_file, caption=caption_fr)

        st.markdown(
            """
            Mon Ami Paris est une application qui propose un plan interactif de Paris avec plusieurs vues pour vous aider à naviguer dans la ville de Paris. Toutes les données proviennent de Paris Open Data - https://opendata.paris.fr/
            """
        )
    elif language == 'English':
        # Show the welcome message in English
        st.header("Welcome to Mon Ami Paris!")
        st.image(image_file, caption=caption_en, width=725)

        st.markdown(
            """
            Mon Ami Paris is an app that offers an interactive map of Paris with multiple views to help you navigate the city of Paris. All data is from Paris Open Data - https://opendata.paris.fr/
            """
        )

# Call the function to show the welcome message
show_welcome_message()

