import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from weather_service import get_weather_data, get_forecast_data, process_forecast_data
#from dotenv import load_dotenv
import os
import datetime  

# Load environment variables from .env file
#load_dotenv()

# Set page configuration
st.set_page_config(page_title="Weather Dashboard", page_icon=":sunny:")

# Sidebar setup
st.sidebar.title("Weather Dashboard")
st.sidebar.markdown("### A comprehensive app for current weather and 5-day forecasts.")


# Main function
def main():
    
    city_name = st.sidebar.text_input("Enter City Name", "New York")
    # Dropdown for selecting graph type
    graph_type = st.sidebar.radio("Select Graph Type", ["Bar Graph", "Line Graph"])
    
    api_key = st.secrets["general"]["WEATHER_API_KEY"]
    
    if city_name:
        try:
            weather_data = get_weather_data(city_name, api_key)
            forecast_data = get_forecast_data(city_name, api_key)
            if 'main' in weather_data:
                # Current Weather Details
                st.title(f"Current Weather in {city_name} :sunny:")
                st.subheader(f"**Temperature:** {weather_data['main']['temp']}°C :thermometer:")
                st.write(f"**Weather:** {weather_data['weather'][0]['description'].capitalize()} :cloud:")
                st.write(f"**Humidity:** {weather_data['main']['humidity']}% :droplet:")
                st.write(f"**Wind Speed:** {weather_data['wind']['speed']} m/s :wind_blowing_face:")
                
                # Next Day Prediction
                tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
                tomorrow_date = tomorrow.strftime('%Y-%m-%d')
                tomorrow_forecast = next_day_forecast(forecast_data, tomorrow_date)
                st.write(f"**Prediction for {tomorrow_date}:** {tomorrow_forecast} :chart_with_upwards_trend:")

                # Plot Graph
                forecast_by_day = process_forecast_data(forecast_data)
                plot_graph(graph_type, forecast_by_day)
            else:
                st.error("City not found or API limit exceeded.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

def plot_graph(graph_type, forecast_by_day):
    dates = list(forecast_by_day.keys())
    temps = [sum([data['temp'] for data in day_data]) / len(day_data) for day_data in forecast_by_day.values()]

    plt.figure(figsize=(10, 6))
    if graph_type == "Bar Graph":
        sns.barplot(x=dates, y=temps, palette="coolwarm")
        plt.xlabel('Date')
        plt.ylabel('Temperature (°C)')
        plt.title('Temperature Forecast')
    elif graph_type == "Line Graph":
        sns.lineplot(x=dates, y=temps, marker='o', color='b')
        plt.xlabel('Date')
        plt.ylabel('Temperature (°C)')
        plt.title('Temperature Forecast')

    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

def next_day_forecast(forecast_data, date):
    for entry in forecast_data['list']:
        if entry['dt_txt'].startswith(date):
            temp = entry['main']['temp']
            description = entry['weather'][0]['description']
            return f"{description.capitalize()} with a temperature of {temp}°C"
    return "No data available for the next day."

if __name__ == "__main__":
    main()

# Contact Information at the bottom with icons
st.sidebar.markdown("### Contact Me")
st.sidebar.markdown("[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/AkramUllahKhan)")
st.sidebar.markdown("[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:akramullahkhan05@gmail.com)")
st.sidebar.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/akram-ullah-97122014b/)")

st.markdown("""
    <footer style="
        text-align: center; 
        padding: 20px; 
        font-size: 14px; 
        color: #555; 
        background-color: #f9f9f9; 
        border-top: 1px solid #ddd; 
        margin-top: 30px; 
        position: relative; 
        bottom: 0; 
        width: 100%;
        ">
        <p style="margin: 0;">Made with ❤️ by <strong>Akram Ullah</strong></p>
        <p style="margin: 5px 0 0; font-size: 12px; color: #777;">For any inquiries, contact me at <a href="mailto:akramullahkhan05@gmail.com" style="color: #007bff;">akramullahkhan05@gmail.com</a></p>
    </footer>
    """, unsafe_allow_html=True)