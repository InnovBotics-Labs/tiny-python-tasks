# tiny-python-tasks
Contains simple python programs

## Lamda
Syntax: lamda param : action(param)
Eg: lamda a,b : a + b
Eg: lamda mark : f"pass with {mark}" if mark > 50
Rules:
    - Only use them once.(onetime annoys function)

## List comprehension

Syntax: list = [item for item in items if condition]

Eg 1: Creating list of vowels in a given word  
list = [letter for letter in words if letter in vowels]

Eg 2: Creating list that contains a score greater than 50%
list = [score for score in scores if score > 50]

Eg 3: Capitalizing each letter in a word 
list = [letter.upper() for letter in words]

Rules:
    - Condition is optional.
    - You can perform an operation on the item    

## Dictionary comprehension

Syntax: dict = {key:value for key, value in dict.items() if condition}

Eg 1: Creating graduated student from all student list
graduated_student = { student: score for student, score in all_students.items() if score > 50 }


Rules:
    - Condition is optional.
    - You can perform an operation on the key and value    

## Modules / Packages

- [Pandas](https://pandas.pydata.org)
  - To handle table manipulation EXCEL, CSV, SQL database 
- [Pretty Table ](https://pypi.org/project/prettytable/)
  - Display a table in Console in prettier format 
- [Turtle](https://docs.python.org/3/library/turtle.html)
  - small animations, graphics and games
- [Tkinter](https://docs.python.org/3/library/tkinter.html#the-packer)
  - [GUI based](http://tcl.tk/man/tcl8.6/TkCmd/pack.htm)
- [re](https://www.w3schools.com/python/python_regex.asp)
  - for [regex string validation](https://regex101.com)
- SMTP ( to send mail)
  - https://docs.python.org/3/library/smtplib.html
- [datetime](https://docs.python.org/3/library/datetime.html) 
  - works with date and time.
  - [W3School](https://www.w3schools.com/python/python_datetime.asp)
- [requests](https://docs.python-requests.org/en/latest/)
  - [HTTP status codes ](https://www.webfx.com/web-development/glossary/http-status-codes/)
- HTML
  - to unpack a values from json files
  - [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
  - [Gify](https://giphy.com)
  
## Services:

To run python code to run on cloud services for free
    refer: https://www.pythonanywhere.com

## APIs

- [International Space Station Current Location ](http://open-notify.org/Open-Notify-API/ISS-Location-Now/)
  - Eg [API endpoint:http://api.open-notify.org/iss-now.json]
- Weather
  - [sign-up](https://home.openweathermap.org/users/sign_up)
  - [Home](https://openweathermap.org/current)
  - [sign](https://home.openweathermap.org/users/sign_in)
  - [Online JSON Viewer](https://jsonviewer.stack.hu)
  - [where its raining](https://www.ventusky.com/vancouver)
  - [Sheety google sheets and program](https://sheety.co)

## Extension for browser

- JSON VIEWER PRO
  - [Chrome Extension](https://chromewebstore.google.com/detail/json-viewer/gbmdgpbipfallnflgajpaliibnhdgobh)

## MISC reference
- [Find your latitude and longitude](https://www.latlong.net/Show-Latitude-Longitude.html)
- [HTML Entities](https://www.w3schools.com/html/html_entities.asp)
- [Named Color Color Hunt](https://developer.mozilla.org/en-US/docs/Web/CSS/named-color)
- [RGB Mixer](https://www.csfieldguide.org.nz/en/interactives/rgb-mixer/)

# WEB design Principles 
## color Theory
- [Adobe_color](https://color.adobe.com/create/color-wheel)
- [color_hunt](https://colorhunt.co)

## Typography
- 