# rainy
Aesthetic and minimalistic weather fetching tool.

<img src="assets/preview.png">

## Dependencies
* ```python```
* ```requests```
* ```make```

You can install all of them from your distros repositories (usually they're named ```python```, ```python-requests``` and ```make```)

## Installation & Configuration
To install rainy, clone or download the repo, ```cd``` into it and just run ```make install``` (you can run ```make uninstall``` to uninstall it)

**Before usage, you need to configure it**

* First create an [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) account, go to [API keys](https://home.openweathermap.org/api_keys) and get your key.
* Then edit ```/usr/local/bin/rainy``` and set the API key, city and timezone in the config section.
* You can also set if you want to show city name or / and the current date if you want to.

## Usage
When set up correctly, you can just go to your terminal and type ```rainy```

What if there's an update? You can just update your local git clone and sudo make again (you can also edit the config of the git clone you you don't have to set it every time you sudo make)

If you like this tool, please consider starring as it helps the growth <3

### PS
This project seems pretty exciting, with plenty of room to grow. I've been on the lookout for a long-term project, and if anyone's interested in working on this with me, just message me (I'm not sure I'd be working on this alone) <<

### Thanks
* [1Codealot](https://github.com/1Codealot) and [Chirikumbrah](https://github.com/Chirikumbrah) for helping out with the code a lot :)
* [wego](https://github.com/schachmat/wego) for providing ASCII weather icons