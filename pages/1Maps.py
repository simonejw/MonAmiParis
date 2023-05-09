import geopandas as gpd
import folium
import streamlit as st
from streamlit_folium import st_folium
import numpy as np
import pandas as pd


# Load Font Awesome CSS
st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/all.min.css">', unsafe_allow_html=True)     


#Define strings for colors
red= 'red'
orange = 'orange'
blue = 'blue'
pink = 'pink'
purple = 'purple'
gray = 'gray' 
lightblue = 'lightblue' 
lightgray = 'lightgray'
green = 'green' 
cadetblue = 'cadetblue' 
darkgreen = 'darkgreen' 
darkblue = 'darkblue'
white = 'white' 
beige = 'beige' 
lightgreen = 'lightgreen' 
darkpurple='darkpurple'
black = 'black'

# Folium map initialization (for both English and French)
visitormap_fr = folium.Map(location=[48.8566, 2.3522], zoom_start=12)
environmentmap_fr = folium.Map(location=[48.8566, 2.3522], zoom_start=12)
practicalmap_fr = folium.Map(location=[48.8566, 2.3522], zoom_start=12)
parismap = folium.Map(location=[48.8566, 2.3522], zoom_start=12)
balademap_fr = folium.Map(location=[48.8566, 2.3522], zoom_start=12)

visitormap_en = folium.Map(location=[48.8566, 2.3522], zoom_start=12)
environmentmap_en = folium.Map(location=[48.8566, 2.3522], zoom_start=12)
practicalmap_en = folium.Map(location=[48.8566, 2.3522], zoom_start=12)
parismap_en = folium.Map(location=[48.8566, 2.3522], zoom_start=12)
balademap_en = folium.Map(location=[48.8566, 2.3522], zoom_start=12)

# Language selection
language = st.sidebar.selectbox(
    'Language:',
    ('Français', 'English')
)

if language == 'Français': 
    st.title('Mon Ami Paris', help = "Ces plans prennent du temps pour rendre.")

    # Checkbox View
    visitor_fr = st.sidebar.checkbox('Visite')
    practical_fr = st.sidebar.checkbox('Services de la ville')
    balade_fr = st.sidebar.checkbox('Balades')
                                  
    
    # Set names for each dataset
    lgd_txt = '<span style="color: {col};">{icon} {txt}</span >'
    name_sanisettes = lgd_txt.format(col='black', icon='<i class="fa fa-user"></i>', txt='Sanisettes')
    name_wifi = lgd_txt.format(col='darkblue', txt='Wifi Hotspots', icon = '<i class="fa fa-wifi"></i>')
    name_ascenseurs = lgd_txt.format(col='red', txt='Ascenseurs', icon = '<i class="fa fa-wheelchair"></i>')
    name_fontaines = lgd_txt.format(col='blue', txt='Fontaines', icon = '<i class="fa fa-tint"></i>')
    name_defibrillateurs = lgd_txt.format(col='gray', txt='Défibrillateurs', icon = '<i class="fa fa-heartbeat"></i>')

    # Set markercluster names
    sanisettes_markers = 'sanisettes_cluster'
    ascenseurs_markers = 'ascenseurs_cluster'
    fontaines_markers = 'fontaines_cluster'
    defibrillateurs_markers = 'defibrillateurs_cluster'
    wifi_markers = 'wifi_cluster'
    
    # Set names for icons
    user = 'user'
    bicycle = 'bicycle'
    volume = 'volume-up'
    lift = 'triangle-top'
    wifi_icon = 'wifi'
    tint = 'tint'
    heartbeat = 'heartbeat'
    prefix = 'fa'
    sp = 'superpowers'
    unlock = 'unlock'
    wheelchair = 'wheelchair'

    def markercluster(name, data, markername, mapversion, iconcolor, icon, prefix='glyphicon'):
        """
        A function that creates a marker cluster and adds it to a folium map.

        Parameters:
        -----------
        name : str
            The name of the marker cluster.
        data : dict or GeoDataFrame
            The data to be added to the marker cluster.
        markername : str
            The name of the marker.
        mapversion : folium.Map
            The folium map object to which the marker cluster should be added.
        iconcolor : str
            The color of the marker icon.
        icon : str
        The name of the marker icon.
        prefix : str, optional
            The prefix of the marker icon. Default is 'glyphicon'.

        Returns:
        --------
        None

        Description:
        ------------
        This function creates a marker cluster with the given name and adds it to the folium map object. It also creates a GeoJSON layer with the given data, and adds it to the marker cluster with the specified icon color, icon name, and prefix. If no prefix is given, the default prefix 'glyphicon' is used.
        """
        markername = folium.plugins.MarkerCluster(name=name).add_to(mapversion)
        folium.GeoJson(data, name=name, marker=folium.Marker(icon=folium.Icon(color=iconcolor, icon=icon, prefix=prefix)), embed=True).add_to(markername)

   
   # Define the GitHub repository URL and file names
    fontaines = 'Data/fontaines-a-boire.geojson'
    wifi = 'Data/sites-disposant-du-service-paris-wi-fi.geojson'
    ascenseurs = 'Data/ascenseurs-escalators-tele-surveillance-temps-reel.geojson'
    sanisettes = 'Data/sanisettesparis.geojson'
    defibrillateurs = 'Data/defibrillateurs.geojson'

    # Create the folium.GeoJson objects for the practical map
    markercluster(name_sanisettes, sanisettes, sanisettes_markers, practicalmap_fr, black, user)
    markercluster(name_wifi, wifi, wifi_markers, practicalmap_fr, darkblue, wifi_icon, prefix='fa')
    markercluster(name_ascenseurs, ascenseurs, ascenseurs_markers, practicalmap_fr, red, wheelchair, prefix='fa')
    markercluster(name_fontaines, fontaines, fontaines_markers, practicalmap_fr, blue, tint, prefix = 'fa')
    markercluster(name_defibrillateurs, defibrillateurs, defibrillateurs_markers, practicalmap_fr, red, heartbeat, prefix='fa')
    folium.LayerControl(collapsed=False,
                        position='topright',
                        autoZIndex=True,
                        hideSingleBase=True,
                        overlay=True,
                        control=True,
                        show=True,
                        name='Layers',
                        ).add_to(practicalmap_fr)

    # Visitor Mapping
    tournage = "Data/lieux-de-tournage-a-paris.geojson"
    marches = "Data/marches-decouverts.geojson"
    plaques = "Data/plaques_commemoratives_1939-1945.geojson"
    activites = "Data/que-faire-a-paris-.geojson"
    seniors = "Data/seniors-a-paris-loisirs-et-citoyennete.geojson"
    portraits = "Data/femmes-illustres-a-paris-portraits.geojson"
    arbres = "Data/arbresremarquablesparis.geojson"

    plaques_df = gpd.read_file("Data/plaques_commemoratives_1939-1945.geojson")
    plaques = gpd.GeoDataFrame(plaques_df)

    arr = [p is None for p in plaques['geometry']]
    np.isfinite(arr)
    plaques = plaques[~pd.isnull(plaques['geometry'])]

    # Define marker names
    tournage_markers = 'tournage_markers'
    marches_markers = 'marches_markers'
    plaques_markers = 'plaques_markers'
    activites_markers = 'activites_markers'
    seniors_markers = 'seniors_markers'
    portraits_markers = 'portraits_markers'
    arbres_markers = 'arbres_markers'


    # Add text and icons for layer control
    lgd_txt = '<span style="color: {col};">{icon} {txt}</span >'
    name_tournage = lgd_txt.format(col='black', icon='<i class="fa fa-video-camera"></i>', txt='Lieux de tournage')
    name_marches = lgd_txt.format(col='darkblue', txt='Marchés Découverts', icon = '<i class="fa fa-shopping-basket"></i>')
    name_plaques = lgd_txt.format(col='black', txt='Plaques commémoratives 1939-1945', icon = '<i class="fa fa-bars"></i>')
    name_seniors = lgd_txt.format(col='darkgreen', txt='Activités à destination des seniors parisiens', icon = '<i class="fa fa-user-plus"></i>')
    name_portraits = lgd_txt.format(col='gray', txt='Femmes illustres à Paris', icon = '<i class="fa fa-image"></i>')
    name_arbres = lgd_txt.format(col='red', txt='Arbres Remarquables', icon = '<i class="fa fa-tree"></i>')

    # Set names for icons
    film_icon = 'video-camera'
    marche_icon = 'shopping-basket'
    plaque_icon = 'bars'
    activites_icon = 'book'
    seniors_icon = 'user-plus'
    portraits_icon = 'image'
    arbres_icon = 'tree'
    

    # Create folium.GeoJson objects for the visitor map
    markercluster(name_tournage, tournage, tournage_markers, visitormap_fr, black, film_icon, prefix='fa')
    markercluster(name_plaques, plaques, plaques_markers, visitormap_fr, beige, plaque_icon, prefix='fa')
    markercluster(name_seniors, seniors, seniors_markers, visitormap_fr, red, seniors_icon, prefix='fa')
    markercluster(name_portraits, portraits, portraits_markers, visitormap_fr, red, portraits_icon, prefix='fa')
    markercluster(name_arbres, arbres, arbres_markers, visitormap_fr, red, arbres_icon, prefix='fa')
    folium.LayerControl(collapsed=False,
                        position='topright',
                        autoZIndex=True,
                        hideSingleBase=True,
                        overlay=True,
                        control=True,
                        show=True,
                        name='Layers',
                        ).add_to(visitormap_fr)


    # Balades mapping
    balades = "Data/paris-autrement-balades-dans-les-arrondissements-peripheriques-parcours.geojson"
    arrondissements = "Data/arrondissements.geojson"
    bois = "Data/plu-voies-dans-les-bois.geojson"

    arr = gpd.read_file(arrondissements)
    arr_df = gpd.GeoDataFrame(arr)

    arrondissements_name = 'Arrondissements'
    balades_name = 'Balades'
    bois_name = 'Voies dans les bois'

    balademap = folium.Map(location=[48.8566, 2.3522], zoom_start=12)
    lgd_txt = '<span style="color: {col};">{txt}</span>'

    # Create folium.GeoJson objects for the balade map
    folium.GeoJson(data = bois, style_function = lambda feature: {'color': darkgreen,'weight': 3}, name=lgd_txt.format(col='black', txt='Voies dans les bois'), embed =True).add_to(balademap_fr)
    folium.GeoJson(data=balades, style_function=lambda feature: {'color': 'black', 'weight': 3}, name=lgd_txt.format(col='green', txt='Balades'), embed=True).add_to(balademap_fr)
    folium.GeoJson(data = arrondissements, name=lgd_txt.format(col='blue', txt='Arrondissements'), embed=True).add_to(balademap_fr)

    # add the layer control to the map and set the legend HTML
    folium.LayerControl(collapsed=False,
                        position='topright',
                        autoZIndex=True,
                        hideSingleBase=True,
                        overlay=True,
                        control=True,
                        show=True,
                        name='Layers',
                        ).add_to(balademap_fr)

    

    
    if visitor_fr:
        st_data = st_folium(visitormap_fr, width=725)
         # Checkbox for more information
        voir_plus_fr = st.checkbox("Voir plus d'informations sur les jeux de données")
       
        if voir_plus_fr:
            st.markdown("**Lieux de tournage:** Lieux de tournage de scène en extérieur à Paris depuis 2016. Les données de l'année en cours ne sont pas publiées.Les tournages désignent les longs métrages, les séries et les téléfilms, réalisés à l’extérieur.Les lieux de tournage de l’année en cours ne sont pas diffusés. Depuis 2017, les informations sont issues de l’application AGATE, application d'instruction des demandes de tournage utilisée par la Mission Cinéma.")
            st.markdown("La liste des plaques commémoratives des personnes et des organisations qui se sont illustrées durant la période 1939-1945 par arrondissement.")
            st.markdown("**Activités de loisirs:** Pour favoriser l’autonomie des seniors parisiens, la Ville de Paris soutient les initiatives locales contribuant au bien vieillir. Avec le concours de la Conférence des Financeurs de la prévention de la perte d’autonomie de Paris, la Ville déploie sur le territoire parisien une offre variée d’ateliers destinés au plus de 60 ans.")
            st.markdown("**Femmes illustres:** A l’occasion de la coupe féminine du monde de la FIFA 2019, partez sur les traces des parisiennes illustres à travers les lieux emblématiques de leurs vies.")
            st.markdown("**Arbres Remarquables:** Géo-localisation des arbres remarquables d'alignement, des jardins, des cimetières parisiens, des écoles, des établissements de la petite enfance")
            st.markdown("Source de données : Paris Open Data - https://opendata.paris.fr/") 
        else: 
            st.markdown("Source de données : Paris Open Data - https://opendata.paris.fr/") 
    
    elif practical_fr:
        st_data = st_folium(practicalmap_fr, width=725)
        voir_plus_fr = st.checkbox("Voir plus d'informations sur les jeux de données")
        
        if voir_plus_fr:
            st.markdown("**Sanisettes:** Les toilettes publiques présentes sur l'espace public, dans les parcs et jardins et sur les quais de Seine. AVERTISSEMENT : L'actualité du jeu de données prend en compte la période de confinement lié au COVID-19 et donc la fermeture d'un certain nombre d'équipements publics. Ce jeu de données montre des toilettes publiques gratuites et des toilettes à accès payant déléguées à un prestataire de service.")
            st.markdown("**Hotspots wifi:** Liste des sites municipaux disposant d'un hotspot Paris Wi-Fi permettant une connexion à Internet limitée. L'accès au service internet Wi-Fi de la Ville de Paris est ouvert aux usagers dans la limite de la tranche horaire de 7h à minuit.. Les connexions sont limités à 2h, sans limitation de reconnexion. Les Conditions Générales d'Utilisation du service sont disponibles en pièce jointe. Ce jeu de données est directement lié celui des usages : Paris Wi-Fi - Utilisation des hotspots Paris Wi-Fi. Paris Wi-Fi est un service mis en place par la Ville de Paris. Il vous permet de vous connecter gratuitement, sans fil et en haut débit, à Internet. Il est ouvert à tous: Parisiens, Franciliens et visiteurs de Paris.")
            st.markdown("**Défibrillateurs:** Localisation des défibrillateurs automatiques gérés par la Ville de Paris.")
            st.markdown("**Fontaines:** Localisation des fontaines à boire Eau de Paris sur les espaces gérés par la Ville de Paris.")
            st.markdown("Source de données : Paris Open Data - https://opendata.paris.fr/") 
        else: 
            st.markdown("Source de données : Paris Open Data - https://opendata.paris.fr/") 
    
    elif balade_fr:
        st_data = st_folium(balademap_fr, width=725)
        voir_plus_fr = st.checkbox("Voir plus d'informations")
        
        if voir_plus_fr:
            st.markdown("**Balades:** Balades insolites au cœur des 12, 13 et 14ème arrondissements - Jeu de données présentant des parcours et des points d’intérêts sur les trésors cachés de ces arrondissements.")
            st.markdown("**Voies dans ls bois:** Voies dans les Bois indiquées sur les plans du PLU de Paris.") 
            st.markdown("Source de données : Paris Open Data - https://opendata.paris.fr/") 
        else: 
            st.markdown("Source de données : Paris Open Data - https://opendata.paris.fr/") 
            
    # Set the default map option to display a clean map of Paris
    else: 
        st_data = st_folium(parismap, width=725)
    
    
# English version

elif language == 'English': 
    st.title('Mon Ami Paris', help = "These maps take some time to render.")
    # Checkbox View
    visitor_en = st.sidebar.checkbox('Visiting')
    #environment_en = st.sidebar.checkbox('Sustainable Resources') 
    practical_en = st.sidebar.checkbox('City Services')
    balade_en = st.sidebar.checkbox('Walks through the city')
                                  
    
    # Set names for each dataset
    name_sanisettes = 'Public restrooms'
    name_ascenseurs = 'Elevators'
    name_fontaines = 'Water refill stations'
    name_defibrillateurs = 'Defibrillators'
    name_wifi = 'Wifi Hotspots'
    name_velib = 'Vélib'

    #markercluster names

    sanisettes_markers = 'sanisettes_cluster'
    ascenseurs_markers = 'ascenseurs_cluster'
    fontaines_markers = 'fontaines_cluster'
    defibrillateurs_markers = 'defibrillateurs_cluster'
    wifi_markers = 'wifi_cluster'

    #Define strings for colors
    red= 'red'
    orange = 'orange'
    blue = 'blue'
    pink = 'pink'
    purple = 'purple'
    gray = 'gray' 
    lightblue = 'lightblue' 
    lightgray = 'lightgray'
    green = 'green' 
    cadetblue = 'cadetblue' 
    darkgreen = 'darkgreen' 
    darkblue = 'darkblue'
    white = 'white' 
    beige = 'beige' 
    darkred = 'darkred' 
    lightred= 'lightred' 
    lightgreen = 'lightgreen' 
    darkpurple='darkpurple'
    black = 'black'

    # Set names for icons
    user = 'user'
    bicycle = 'bicycle'
    volume = 'volume-up'
    lift = 'triangle-top'
    wifi_icon = 'wifi'
    tint = 'tint'
    heartbeat = 'heartbeat'
    prefix = 'fa'
    sp = 'superpowers'
    unlock = 'unlock'
    wheelchair = 'wheelchair'
   

    def markercluster(name, data, markername, mapversion, iconcolor, icon, prefix = 'glyphicon'):
        markername = folium.plugins.MarkerCluster(name=name).add_to(mapversion)
        folium.GeoJson(data, marker = folium.Marker(icon = folium.Icon(color = iconcolor, icon=icon, prefix = prefix)), embed=True).add_to(markername)
    
    
    fontaines = "Data/fontaines-a-boire.geojson"
    wifi = "Data/sites-disposant-du-service-paris-wi-fi.geojson"
    ascenseurs = "Data/ascenseurs-escalators-tele-surveillance-temps-reel.geojson"
    sanisettes = "Data/sanisettesparis.geojson"
    defibrillateurs = "Data/defibrillateurs.geojson"
    
    # Set names for each dataset
    lgd_txt = '<span style="color: {col};">{icon} {txt}</span >'
    name_sanisettes = lgd_txt.format(col='black', icon='<i class="fa fa-user"></i>', txt='Public restroooms')
    name_wifi = lgd_txt.format(col='darkblue', txt='Wifi Hotspots', icon = '<i class="fa fa-wifi"></i>')
    name_ascenseurs = lgd_txt.format(col='red', txt='Elevators', icon = '<i class="fa fa-wheelchair"></i>')
    #name_activites = lgd_txt.format(col='black', txt='Activités', icon ='<i class="fa fa-video"></i>')
    name_fontaines = lgd_txt.format(col='blue', txt='Water refill stations', icon = '<i class="fa fa-tint"></i>')
    name_defibrillateurs = lgd_txt.format(col='gray', txt='Defibrillators', icon = '<i class="fa fa-heartbeat"></i>')

    markercluster(name_sanisettes, sanisettes, sanisettes_markers, practicalmap_en, black, user)
    markercluster(name_wifi, wifi, wifi_markers, practicalmap_en, darkblue, wifi_icon, prefix='fa')
    markercluster(name_ascenseurs, ascenseurs, ascenseurs_markers, practicalmap_en, red, wheelchair, prefix='fa')
    markercluster(name_fontaines, fontaines, fontaines_markers, practicalmap_en, blue, tint, prefix = 'fa')
    markercluster(name_defibrillateurs, defibrillateurs, defibrillateurs_markers, practicalmap_en, red, heartbeat, prefix='fa')
    folium.LayerControl(collapsed=False,
                        position='topright',
                        autoZIndex=True,
                        hideSingleBase=True,
                        overlay=True,
                        control=True,
                        show=True,
                        name='Layers',
                        ).add_to(practicalmap_en)

    #Visitor Mapping
    tournage = "Data/lieux-de-tournage-a-paris.geojson"
    marches = "Data/marches-decouverts.geojson"
    plaques = "Data/plaques_commemoratives_1939-1945.geojson"
    activites = "Data/que-faire-a-paris-.geojson"
    seniors = "Data/seniors-a-paris-loisirs-et-citoyennete.geojson"
    portraits = "Data/femmes-illustres-a-paris-portraits.geojson"
    arbres = "Data/arbresremarquablesparis.geojson"

    plaques_df = gpd.read_file("Data/plaques_commemoratives_1939-1945.geojson")
    plaques = gpd.GeoDataFrame(plaques_df)

    arr = [p is None for p in plaques['geometry']]
    np.isfinite(arr)
    plaques = plaques[~pd.isnull(plaques['geometry'])]

    #define marker names
    tournage_markers = 'tournage_markers'
    marches_markers = 'marches_markers'
    plaques_markers = 'plaques_markers'
    activites_markers = 'activites_markers'
    seniors_markers = 'seniors_markers'
    portraits_markers = 'portraits_markers'
    arbres_markers = 'arbres_markers'


    #define function to add markercluster data
    lgd_txt = '<span style="color: {col};">{icon} {txt}</span>'
    name_tournage = lgd_txt.format(col='black', icon='<i class="fa fa-video-camera"></i>', txt='Filming sites')
    name_marches = lgd_txt.format(col='darkblue', txt='Markets', icon = '<i class="fa fa-shopping-basket"></i>')
    name_plaques = lgd_txt.format(col='orange', txt='Commemorative plaques', icon = '<i class="fa fa-image"></i>')
    name_activites = lgd_txt.format(col='black', txt='Activities', icon ='<i class="fa fa-video"></i>')
    name_seniors = lgd_txt.format(col='darkgreen', txt='Activities for seniors', icon = '<i class="fa fa-user-plus"></i>')
    name_portraits = lgd_txt.format(col='gray', txt='Portraits of famous women', icon = '<i class="fa fa-camera"></i>')
    name_arbres = lgd_txt.format(col='red', txt='Remarkable trees', icon = '<i class="fa fa-tree"></i>')


    #Define strings for colors
    red= 'red'
    orange = 'orange'
    blue = 'blue'
    pink = 'pink'
    purple = 'purple'
    gray = 'gray' 
    lightblue = 'lightblue' 
    lightgray = 'lightgray'
    green = 'green' 
    cadetblue = 'cadetblue' 
    darkgreen = 'darkgreen' 
    darkblue = 'darkblue'
    white = 'white' 
    beige = 'beige' 
    darkred = 'darkred' 
    lightred= 'lightred' 
    lightgreen = 'lightgreen' 
    darkpurple='darkpurple'
    black = 'black'

    #define icons

    film_icon = 'video-camera'
    marche_icon = 'shopping-basket'
    plaque_icon = 'image'
    activites_icon = 'book'
    seniors_icon = 'user-plus'
    portraits_icon = 'camera'
    arbres_icon = 'tree'

    markercluster(name_tournage, tournage, tournage_markers, visitormap_en, black, film_icon, prefix='fa')
    markercluster(name_marches, marches, marches_markers, visitormap_en, darkblue, marche_icon, prefix='fa')
    markercluster(name_plaques, plaques, plaques_markers, visitormap_en, orange, plaque_icon, prefix='fa')
    markercluster(name_seniors, seniors, seniors_markers, visitormap_en, red, seniors_icon, prefix='fa')
    markercluster(name_portraits, portraits, portraits_markers, visitormap_en, red, portraits_icon, prefix='fa')
    markercluster(name_arbres, arbres, arbres_markers, visitormap_en, red, arbres_icon, prefix='fa')
    folium.LayerControl(collapsed=False,
                        position='topright',
                        autoZIndex=True,
                        hideSingleBase=True,
                        overlay=True,
                        control=True,
                        show=True,
                        name='Layers',
                        ).add_to(visitormap_en)


    #Balade mapping
    balades = "Data/paris-autrement-balades-dans-les-arrondissements-peripheriques-parcours.geojson"
    arrondissements = "Data/arrondissements.geojson"
    bois = "Data/plu-voies-dans-les-bois.geojson"

    arr = gpd.read_file(arrondissements)
    arr_df = gpd.GeoDataFrame(arr)

    arrondissements_name = 'Parisian districts'
    balades_name = 'Walks through the city'
    bois_name = 'Walks through the woods of Paris'

    balademap = folium.Map(location=[48.8566, 2.3522], zoom_start=12)
    lgd_txt = '<span style="color: {col};">{txt}</span>'


    folium.GeoJson(data = bois, style_function = lambda feature: {'color': darkgreen,'weight': 3}, name=lgd_txt.format(col='black', txt='Forest walks'), embed =True).add_to(balademap_en)
    folium.GeoJson(data=balades, style_function=lambda feature: {'color': 'black', 'weight': 3}, name=lgd_txt.format(col='green', txt='City walks'), embed=True).add_to(balademap_en)
    folium.GeoJson(data = arrondissements, name=lgd_txt.format(col='blue', txt='Districts'), embed=True).add_to(balademap_en)

    # add the layer control to the map and set the legend HTML
    folium.LayerControl(collapsed=False,
                        position='topright',
                        autoZIndex=True,
                        hideSingleBase=True,
                        overlay=True,
                        control=True,
                        show=True,
                        name='Layers',
                        ).add_to(balademap_en)

    if visitor_en:
        st_data = st_folium(visitormap_en, width=725)
        
        voir_plus_en = st.checkbox("See more information")
            
        if voir_plus_en:
            st.markdown("**Sites of filming:** Displays sites of filming in Paris since 2016. The data for the current year has not been updated. Since 2017, this information has been accessed through the app AGATE.")
            st.markdown("**Open air markets:** Displays food markets or other specialized markets. A market est composed of mostly of Un marché de plein vent ou découvert est composé en majorité de commerçants non sédentaires, alimentaires ou non, auxquels s’ajoutent des producteurs locaux.")
            st.markdown("**Commemorative Plaques** Commemorative plaques of people and organizations that were erected during the period of 1939-1945.")
            st.markdown("**Activities for seniors:** The city of Paris supports local initiative that contribute to the wellbeing of those in retirement age. This dataset displays a variety of activities for those 60 years of age or older.")
            st.markdown("**Portraits of famous women:** Upon the women's world cup in 2019, the city of Paris traced the locations of several portraits of famous women in Paris.")
            st.markdown("**Remarkable Trees:** Remarkable trees in parisian gardens, cemeteries, schools, and other spots.")
            st.markdown("Data source: Paris Open Data - https://opendata.paris.fr/") 
        else: 
            st.markdown("Data source: Paris Open Data - https://opendata.paris.fr/") 

    elif practical_en:
        st_data = st_folium(practicalmap_en, width=725)
        voir_plus_en = st.checkbox("See more information")
        
        if voir_plus_en: 
            st.markdown("**Public restrooms:** Public restrooms in parks, gardins, and on the Seine river.This dataset shows free public restrooms as well as those with entry fees.")
            st.markdown("**Elevators:** Displays sites of filming in Paris since 2016. The data for the current year has not been updated. Since 2017, this information has been accessed through the app AGATE.")
            st.markdown("**Wifi hotspots:** Sites of wifi offered by the city of Paris. Users are able to connect to the internet for free between the hours of 7am and midnight with a connection that is limited to 2 hours. Reconnections are unlimited. It is open to all: Parisians, French citizens, and visitors to Paris.")                       
            st.markdown("**Defibrillateurs:** Locations of defibrillators managed by the City of Paris.")
            st.markdown("**Water refill stations:** Locations of drinking water stations managed by the City of Paris.")
            st.markdown("Data source: Paris Open Data - https://opendata.paris.fr/") 
        else: 
            st.markdown("Data source: Paris Open Data - https://opendata.paris.fr/")
    
    elif balade_en:
        st_data = st_folium(balademap_en, width=725)
        voir_plus_en = st.checkbox("See more information")
        
        if voir_plus_en: 
            st.markdown("**City walks:** Walking paths found in the 12, 13, and 14th districts.")
            st.markdown("**Districts:** All 19 districts of Paris.")
            
            st.markdown("Data source: Paris Open Data - https://opendata.paris.fr/") 
        else: 
            st.markdown("Data source: Paris Open Data - https://opendata.paris.fr/")
            
    # Set the default map option to a clean map of Paris
    else: 
        st_data = st_folium(parismap, width=725)
