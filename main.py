
import requests
import pyttsx3
import re
import random

# Initialize pyttsx3 for text-to-speech
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for index, voice in enumerate(voices):
    print(f"{index}:{voice.name}-{voice.id}")
engine.setProperty('voice',voices[1].id)
engine.setProperty("rate",200)

def speak(text):
    text= re.sub(r'(?<!\d)\.(?!\d)','',text)
    engine.say(text)
    engine.runAndWait()

# WeatherAPI function to fetch weather based on city
def get_weather(city):
    # Replace 'YOUR_API_KEY' with your actual API key from WeatherAPI
    api_key = "0101e7ba804f408f86d111958251304"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200 and 'current' in data :
        temp_c = data['current']['temp_c']
        feels_like = data['current']['feelslike_c']
        humidity = data['current']['humidity']
        condition = data['current']['condition']['text']
        wind_speed = data['current']['wind_kph']
        return (
                f"The weather in {city} is currently {condition}.\n" 
                f"The temperature is {temp_c} degree Celsius," 
                f"but it feels like {feels_like} .\n"
                f"Humidity is {humidity} percent,\n"
                f"and wind speed is {wind_speed} kilometers per hour.\n"
            )
    else:
        return "CIty not found or Error fetching weather data!"


def goodbye_message():
    messages = [
        "Catch you later !Stay awesome, and take care !",
        "Goodbye for now ! and Keep the vibes High!",
        "take it easy bro , and stay fresh out there!",
        "I'll see you next time buddy. Until then, stay cool!",
        "Time to bounce! , Keep shining champ!"
    ]
    return random.choices(messages)

def speak_goodbye():
    message = goodbye_message()
    print(message)
    engine.say(message)
    engine.runAndWait()


# Main function for RoboSpeaker
def main():
    print("Welcome to RoboSpeaker 1.2 By Smit , currently i provide weather updates , enter any city to get the weather updates!")
    speak("Welcome to RoboSpeaker 1.2 By Smit , currently i provide weather updates , enter any city to get the weather updates!")
    while True:
        city = input("Enter city name (or type 'exit' to quit): ")
        if city.lower() == "exit":
            speak_goodbye()
            break
        weather_info = get_weather(city)
        print(weather_info)
        speak(weather_info)


# Run RoboSpeaker
if __name__ == "__main__":
    main()
