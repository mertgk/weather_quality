from django.shortcuts import render

# Create your views here.

def home(request):
    import json
    import requests

    if request.method == "POST":
        zipcode = request.POST['zipcode']

        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=25&API_KEY=2BEB8C39-AB5D-4BD6-B2AC-053B599851CA")

        try:
            api =json.loads(api_request.content)

        except Exception as e:
            api = "Error"

        if api[0]['Category']['Name'] == "Good":
            category_description = "Air quality is satisfactory, and air pollution poses little or no risk. People of all ages and health conditions can be active outdoors on most days when the AQI is good."
            category_color = "Good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution. Active children and adults, and people with respiratory disease, such as asthma, should limit prolonged outdoor exertion."
            category_color = "Moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "Members of sensitive groups may experience health effects. The general public is not likely to be affected. Sensitive groups include children, older adults, and people with respiratory problems or heart disease."
            category_color = "USG"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "Everyone may begin to experience health effects. Active children and adults, and people with respiratory disease, should avoid prolonged outdoor exertion."
            category_color = "Unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "Health warnings of emergency conditions. Everyone may experience significant health effects. The elderly and people with heart or lung disease should stay indoors and avoid all physical activity."
            category_color = "Very Unhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = "Health alert: everyone may experience health effects. Stay indoors, especially if you are elderly, have heart or lung disease, or are a child."
            category_color = "Hazardous"
           


        return render(request, 'home.html', {'api': api, 'category_description' : category_description, 'category_color': category_color})


    else:


        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=25&API_KEY=2BEB8C39-AB5D-4BD6-B2AC-053B599851CA")

        try:
            api =json.loads(api_request.content)

        except Exception as e:
            api = "Error"

        if api[0]['Category']['Name'] == "Good":
            category_description = "Air quality is satisfactory, and air pollution poses little or no risk. People of all ages and health conditions can be active outdoors on most days when the AQI is good."
            category_color = "Good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution. Active children and adults, and people with respiratory disease, such as asthma, should limit prolonged outdoor exertion."
            category_color = "Moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "Members of sensitive groups may experience health effects. The general public is not likely to be affected. Sensitive groups include children, older adults, and people with respiratory problems or heart disease."
            category_color = "USG"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "Everyone may begin to experience health effects. Active children and adults, and people with respiratory disease, should avoid prolonged outdoor exertion."
            category_color = "Unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "Health warnings of emergency conditions. Everyone may experience significant health effects. The elderly and people with heart or lung disease should stay indoors and avoid all physical activity."
            category_color = "Very Unhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = "Health alert: everyone may experience health effects. Stay indoors, especially if you are elderly, have heart or lung disease, or are a child."
            category_color = "Hazardous"
           


        return render(request, 'home.html', {'api': api, 'category_description' : category_description, 'category_color': category_color})

def about(request):
    return render(request, 'about.html', {})

def about_aqi(request):
    return render(request, 'about_aqi.html', {})