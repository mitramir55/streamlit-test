import streamlit as st

def page1():
    st.write("This is page 1")

def page2():
    st.write("This is page 2")

# Create a dictionary to map page names to functions
pages = {
    "Page 1": page1,
    "Page 2": page2
}

# Create a menu with the page names
selection = st.sidebar.selectbox("Go to", list(pages.keys()))

# Get the function corresponding to the selected page
page = pages[selection]

# Call the selected page function with the Streamlit subpage function
with st.subheader(selection):
    page()