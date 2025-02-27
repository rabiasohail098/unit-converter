import streamlit as st

# Set Streamlit page config
st.set_page_config(page_title="Unit Converter", layout="wide")
st.title("Professional Unit Converter")

# App Description
st.markdown(
    """
    ## About This App
    Welcome to the **Professional Unit Converter**, a versatile and user-friendly tool designed to seamlessly convert units across various categories. 
    
    ### Key Features:
    - **Multi-Category Conversion**: Convert Length, Weight, Temperature, Volume, Speed, and Pressure effortlessly.
    - **Accurate Calculations**: Uses scientifically accurate conversion formulas to ensure precision.
    - **Graphical Representation**: Each conversion page dynamically updates the graph based on selected units.
    - **Easy-to-Use Interface**: Simple navigation with a smooth user experience.
    - **FAQ Section**: Answers to commonly asked questions about unit conversion.
    
    ### How to Use:
    - Select the category of conversion from the sidebar.
    - Navigate to the respective page to input values and get results.
    - Each page contains a detailed explanation of how the conversion works.
    """
)

# FAQ Section
st.subheader("Frequently Asked Questions")
faq = {
    "What is this Unit Converter App?": "This app allows users to convert units across different categories such as Length, Weight, Speed, Temperature, and Pressure. The app provides accurate conversions, detailed explanations, and graphical representations of each conversion.",
    "How does unit conversion work?": "Each unit has a standard conversion factor based on global standards. Using these factors, the app calculates and converts the given input accurately.",
    "Why is the graph important?": "The graph visually represents the unit conversion, helping users understand how one unit compares to another. It updates dynamically based on the selected conversion.",
    "Can I convert between different unit categories?": "No, conversion is only allowed within the same category. For example, you can convert kilometers to miles but not kilometers to kilograms.",
    "How is the conversion formula derived?": "The formula follows a standardized approach based on the physical properties of each unit and their internationally accepted conversion factors.",
    "Is the conversion result accurate?": "Yes, the app uses the Pint library, ensuring precise and reliable unit conversions without errors.",
    "Why do some conversions show decimals while others don’t?": "Some units require precise decimal values to ensure accuracy, whereas others are represented as whole numbers depending on the scale.",
    "Can I add more unit categories in the future?": "Yes! The app is designed to be expandable. More unit categories and conversions can be added easily in future updates."
}

for question, answer in faq.items():
    with st.expander(question):
        st.write(answer)
