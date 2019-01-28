<img src="https://raw.githubusercontent.com/Shadowsych/smart-rates/master/rsrc/icon_text.png" width="250" height="175" />

# Smart Rates
A mobile and web-application that analyzes the market value of a car using the Smart Car API.

# DevPost
https://devpost.com/software/safe-sound-hruj1p

# Developers
- Pravat Bhusal (Full-Stack Developer and API Solutions)
- Michael Kasman (Full-Stack Developer and Graphics Designer)

# Technologies
- HTML5, CSS3, JavaScript (ES6), Bootstrap
- Python 3.0+ (Flask Web-server)
- Smart Car API, Marketcheck API

# Configuration
- Within the `main.py` and `smart_rates.py` files inside the `server` directory must change these variables to your APIs
    - `client_id` from `main.py` for Smart Car API
    - `client_secret` from `main.py` for Smart Car API
    - `redirect_uri` from `main.py` for Smart Car API (must also add in the Smart Car dashboard)
    - `api_key` from `smart_rates.py` for Marketcheck API

# Installing Dependencies and Running The Server
- Run `pip install -r requirements.txt` in the `server` directory
- Run `python3 main.py` in the `server` directory

# Running The Client
To test your mobile and web-application on `localhost`, load up the `index.html` file within the `client` folder in your local web-browser and view it as a mobile application using `Inspect Element`.
- We implemented it as a mobile and web-application to allow flexibility for customers using a browser and a mobile phone to use
