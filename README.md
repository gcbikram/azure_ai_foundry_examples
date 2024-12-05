# ai_foundary_examples

## Overview
This project demonstrates examples for using Azure AI Foundry (previously known as Azure AI Studio). It includes various models and their deployment processes.

## Prerequisites
1. **Azure AI Foundry Project**: Create a new project in Azure AI Foundry.
2. **Deploy Models**: Deploy the necessary models to the project.
3. **Connection String**: From the overview page of the project, obtain the connection string and add it to the `.env` file in the root directory of this project.

## Setup Instructions
1. **Clone the Repository**:
    ```sh
    git clone <repository-url>
    cd ai_foundary_examples
    ```

2. **Create a Python Virtual Environment**:
    ```sh
    py -3 -m venv .venv
    .venv\scripts\activate
    ```

3. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the Project**:
    - Open the project in Visual Studio.
    - Run the azure cli command to login to azure and get authenticated with the project
    ```sh
    az login --use-device-code
    ````
    - Press `F5` to run the project.

## Notes
- Ensure that the `.env` file contains the correct connection string from your Azure AI Foundry project.
- The `requirements.txt` file includes all necessary dependencies for the project.

## Troubleshooting
- If you encounter any issues, verify that the connection string in the `.env` file is correct.
- Ensure that all dependencies are installed correctly by checking the output of the `pip install` command.