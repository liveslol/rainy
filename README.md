# rainy
What's the weather? Aesthetic and minimalistic weather fetching tool.

<img src="assets/preview.png">

## Dependencies
* ```python```
* ```requests```
* ```make```

You can install both from your distros repositories (usually they're named ```python```, ```python-requests``` and ```make```)

## Installation & Configuration
To install rainy, clone or download the repo, ```cd``` into it and just run ```make install``` (you can run ```make uninstall to uninstall it```)

**Before usage, you need to configure it**
First create an [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) account, go to [API keys](https://home.openweathermap.org/api_keys) and get your key.
Then edit ```/usr/local/bin/rainy``` and set the API key in the config section.
In the config section, also update your city and the timezone (you can add or subtract hours)

## Usage
If you set it up correctly, you can just go to your terminal and type ```rainy```

### Thanks
* [wego](https://github.com/schachmat/wego) for providing ASCII weather icons