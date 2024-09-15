## 🌤️ Weather Forecast App with Streamlit

The **Weather Forecast App** provides real-time current weather conditions and 5-day weather forecasts for cities worldwide. Built using Python, Streamlit, and OpenWeatherMap API, this application displays dynamic weather data and allows users to visualize forecasts through interactive bar and line graphs.

---

### 🚀 Features

- **Current Weather**: Displays temperature, weather conditions, humidity, and wind speed for the selected city.
- **5-Day Forecast**: Visualizes weather predictions using bar and line charts for easy interpretation.
- **Custom Graphs**: Choose between bar and line graphs for forecast data visualization.
- **Interactive UI**: Intuitive and simple interface for entering city names and switching between graph types.
- **Responsive Design**: Built for desktop and mobile devices.
- **Contact Information**: Easy-to-access contact details with social media links in the sidebar.

---

### 🛠️ Technologies Used

- **Python**: Backend logic and data processing.
- **Streamlit**: Framework for creating an interactive web app.
- **Matplotlib & Seaborn**: For plotting weather forecast graphs.
- **OpenWeatherMap API**: Source for real-time weather data.
- **dotenv**: For environment variable management.

---

### 🧑‍💻 How to Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/AkramUllahKhan/weather-forecast-app-streamlit.git
   ```

2. Navigate to the project directory:

   ```bash
   cd weather-forecast-app-streamlit
   ```

3. Create and activate a virtual environment:

   ```bash
   python -m venv env
   source env/bin/activate  # For Windows: env\Scripts\activate
   ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Set up your environment variable for the API key by creating a `.env` file:

   ```bash
   echo "WEATHER_API_KEY=your_openweather_api_key" > .env
   ```

6. Run the app:

   ```bash
   streamlit run app.py
   ```

---

### 🌍 API Integration

The app fetches real-time weather data from [OpenWeatherMap API](https://openweathermap.org/). You need an API key to access weather data, which should be stored in a `.env` file as shown above.

---

### 📝 Future Enhancements

- Add more weather data visualizations.
- Implement location-based weather fetching.
- Improve UI/UX with more customizable features.

---

### 📬 Contact

For any inquiries, feel free to reach out:

- **Email**: [akramullahkhan05@gmail.com](mailto:akramullahkhan05@gmail.com)
- **GitHub**: [AkramUllahKhan](https://github.com/AkramUllahKhan)
- **LinkedIn**: [AkramUllah](https://www.linkedin.com/in/akram-ullah-97122014b/)

---

### ⚖️ License

This project is open-source and available under the [MIT License](LICENSE).

---