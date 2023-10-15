import requests
import click

API_KEY = 'YOURAPIKEYHERE'  # Replace with your actual API key
BASE_URL = 'https://developer-api.govee.com/v1/devices'

HEADERS = {
    'Govee-API-Key': API_KEY
}

def get_devices():
    try:
        response = requests.get(BASE_URL, headers=HEADERS)
        response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code
        return response.json().get('data', {}).get('devices', [])
    except requests.RequestException as e:  # Catching requests' exceptions, which include HTTPError if status is not successful
        click.echo(f"Error: Unable to retrieve devices - {str(e)}", err=True)
        return None
    except Exception as e:  # General exception handling for unforeseen errors
        click.echo(f"An unexpected error occurred: {str(e)}", err=True)
        return None

def list_devices():
    devices = get_devices()
    if not devices:
        click.echo("No devices found.")
    else:
        for idx, device in enumerate(devices):
            click.echo(f"{idx+1}. Name: {device['deviceName']}, Model: {device['model']}, Address: {device['device']}")

def control_device():
    devices = get_devices()
    if not devices:
        return  # Exit the function if no devices are found
    
    list_devices()
    
    # Ensuring user input is valid
    while True:
        try:
            selected = click.prompt("Select a device number", type=int)
            device = devices[selected-1]
            break  # Exit the loop if input is valid
        except IndexError:
            click.echo("Invalid selection. Please choose a valid device number.")
        except Exception as e:
            click.echo(f"An unexpected error occurred: {str(e)}")

    state = click.prompt("Enter state (on/off)", type=click.Choice(['on', 'off']))

    url = f"{BASE_URL}/control"
    payload = {
        'device': device['device'],
        'model': device['model'],
        'cmd': {
            'name': 'turn',
            'value': state
        }
    }
    try:
        response = requests.put(url, json=payload, headers=HEADERS)
        response.raise_for_status()
        click.echo(f"Light turned {state}.")
    except requests.RequestException as e:
        click.echo(f"Error: Unable to change the light state - {str(e)}", err=True)
    except Exception as e:
        click.echo(f"An unexpected error occurred: {str(e)}", err=True)

def main_menu():
    click.echo("Welcome to the Govee Lights Controller!")
    while True:
        click.echo("1. List devices")
        click.echo("2. Control device")
        click.echo("3. Exit")
        
        choice = click.prompt("Select an option", type=int)
        
        if choice == 1:
            list_devices()
        elif choice == 2:
            control_device()
        elif choice == 3:
            click.echo("Goodbye!")
            break
        else:
            click.echo("Invalid option. Please select a number between 1 and 3.")
            
if __name__ == '__main__':
    main_menu()
