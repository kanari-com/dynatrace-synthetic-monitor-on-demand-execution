# Synthetic Monitor - On Demand Execution

## Overview

This script, titled "Synthetic Monitor - On Demand Execution," facilitates on-demand executions through the Dynatrace API. 
It is designed to trigger synthetic monitors based on specified configuration parameters.

## Prerequisites

Before using this script, ensure the following prerequisites are met:

- Python 3.x installed
- Required Python libraries installed (`requests`, `yaml`,`os`,`json`,`logging`)
- Dynatrace Synthetic Monitor Enabled
- Dynatrace Api-Token:
  One of the following scopes is required:
    syntheticExecutions.write
    ExternalSyntheticIntegration

## Configuration
Ensure the configuration file is present in the same directory as the script.

The script relies on a YAML configuration file (`on_demand_execution.yml`) to specify essential parameters. 
The configuration file should be structured as follows:

```yaml
CONFIG:
  API_TOKEN: <Dynatrace_API_Token>
  URL_DT: <Dynatrace_URL>
  URL_API_V2: <Dynatrace_API_Version_2>
  TAG: <Tag_Name>
```

## Script Functions
load_config(file_path='on_demand_execution.yml')

    Loads the configuration from the specified YAML file.
    Parameters:
        file_path (optional): Path to the YAML configuration file (default is 'on_demand_execution.yml').
    Returns: Configuration data or None if unsuccessful.

make_api_request(api_url, api_token, tag, timeout=10)

    Sends a POST request to the Dynatrace API to trigger on-demand execution.
    Parameters:
        api_url: Full API URL for the Dynatrace instance.
        api_token: API token for authentication.
        tag: Monitor tag for identifying the synthetic monitor.
        timeout (optional): Request timeout in seconds (default is 10 seconds).
    Returns: Response object or None in case of an error.

print_response(response)

    Prints the status code and response content in JSON format.
    Parameters:
    response: Response object from the API request.

main()

    The main function that configures logging, loads the configuration, makes an on-demand execution 
    API request to Dynatrace, and logs relevant information or errors.

Logging

    The script logs information to a file named on_demand_execution.log in the script's directory. 
    The log file includes a timestamp, log level, and corresponding log message.

Important Note

    Incomplete or missing configuration parameters will result in an error.
    If the configuration is not loaded successfully, the script will exit.