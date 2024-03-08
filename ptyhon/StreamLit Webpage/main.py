import streamlit as st

from streamlit_option_menu import option_menu

import Home,Experiences,projects,Resources

st.set_page_config(
    page_title="SumitaPathak"
) #setting page title

class multiApp:
    def __init__(self):
        self.apps=[]
    def add_app(self,title,function):
        self.apps.append({
            "title":title,
            "function": function
        })
    def run():
        with st.sidebar: #creatin side bar
            app= option_menu(
                menu_title="Sumita Pathak",
                options=['Home','Experience','Resources','Projects'],
                icons=['house-fill','battery-full','battery-full','battery-full'],
                menu_icon='circle-square',
                default_index=1,




            )
        if app=='Home':
            Home.app()
        if app=='Experience':
            Experiences.app()
        if app=='Resources':
            Resources.app()
        if app=='Projects':
            projects.app()
    run()