# Govee Lights Controller CLI

Control your Govee lights from the command line with this simple and interactive CLI app!

## Features

- List all connected Govee devices.
- Turn a selected Govee device ON or OFF interactively.
- Friendly user interface with an interactive menu.

## Prerequisites

- Python 3.x
- `requests` and `click` Python packages
- Govee API key

## Installation

1. **Clone the repository:**
    ```shell
    git clone https://github.com/your_username/govee-controller.git
    cd govee-controller
    ```

    Replace `your_username` and repository name as per your actual GitHub URL.

2. **Install required Python packages:**
    ```pip install requests click```

3. **Set up your Govee API key:**
    Replace `YOUR_GOVEE_API_KEY` in the script with your actual Govee API key.

## Usage

Navigate to the script's directory and run:
```app.py```

Follow the interactive menu to control your Govee lights.

## Options
List Devices: Enumerates and displays all Govee devices linked to your account.

Control Device: Interactively choose and control a device state (ON/OFF).

Exit: Ends the application.

## Contributions
Feel free to submit pull requests, create issues, or request additional features to enhance the Govee Lights Controller CLI app.

## License
This project is licensed under the GNU General Public License v3.0 - see the LICENSE file for details.

## Disclaimer
This application is developed independently and is not endorsed by Govee. Always secure your API keys and sensitive data.
