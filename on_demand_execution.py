"Synthetic Monitor - On Demand Execution"
import logging
import os
import json
import requests
import yaml

def load_config(file_path='on_demand_execution.yml'):
    """Load Config"""
    try:
        with open(file_path, 'r', encoding="utf-8") as config_file:
            return yaml.safe_load(config_file)
    except FileNotFoundError:
        logging.error("Config file '%s' not found.", file_path)
    except yaml.YAMLError as e:
        logging.error("Error loading config file: %s", e)
    return None

def make_api_request(api_url, api_token, tag, timeout=10):
    """Make a POST request to Dynatrace API"""
    headers = {
        'Accept': 'application/json; charset=utf-8',
        'Authorization': f'Api-Token {api_token}',
        'Content-Type': 'application/json; charset=utf-8',
    }

    json_data = {
        'group': {
            'tags': [tag],
        },
    }

    try:
        response = requests.post(api_url, headers=headers, json=json_data, timeout=timeout)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        logging.error("An error occurred during the API request: %s", e)
        return None

def print_response(response):
    """Print Status Code & Response Content in JSON format"""
    logging.info("Response:")
    logging.info("Status Code: %s", response.status_code)
    logging.info("Response Content:")
    try:
        response_json = response.json()
        logging.info(json.dumps(response_json, indent=2))
    except ValueError:
        logging.info(response.text)

def main():
    """ Configuring logging, loading the configuration, making an on-demand execution
        API request to Dynatrace, and logging relevant information or errors."""
    log_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'on_demand_execution.log'
    )
    logging.basicConfig(
        filename=log_file_path,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filemode='w'
    )

    config = load_config()
    if config:
        api_token = config.get('CONFIG', {}).get('API_TOKEN')
        api_dt_url = config.get('CONFIG', {}).get('URL_DT')
        api_dt_v2 = config.get('CONFIG', {}).get('URL_API_V2')
        tag = config.get('CONFIG', {}).get('TAG')

        if all((api_token, api_dt_url, api_dt_v2, tag)):
            api_url = api_dt_url + api_dt_v2
            response = make_api_request(api_url, api_token, tag)

            if response:
                print_response(response)
            else:
                logging.warning("API request did not return a valid response.")
        else:
            logging.error("Incomplete or missing configuration parameters.")
    else:
        logging.error("Configuration not loaded. Exiting.")

if __name__ == "__main__":
    main()
