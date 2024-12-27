# StockFXBot

A Python-based stock tracking bot that monitors specified stocks and sends notifications based on price limits.

## Description

StockFXBot allows users to track stock prices and receive notifications when stocks reach specified thresholds. This bot is designed for users who want to stay updated on their investments effortlessly.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Requirements](#requirements)
- [Docker Usage](#docker-usage)

## Installation

To install and run the StockFXBot, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/StockFXBot.git
   cd StockFXBot
   ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the environment variables. Create a `.env` file in the root directory and add your API key:

    ```bash
    API_KEY=your_api_key_here
    ```

## Usage

To run the bot, use the following command:

    ```
    python3 bot_loop.py
    ```

Once the bot is activated, it will start tracking the stocks specified in `stocks.txt` and will log notifications to the `notifications.log` file based on the limits you set.

## Configuration

1. Modify `stocks.txt`: This file should contain the stocks you want to track and their respective price limits. Use the following format:

    ```yaml
    TICKER, lower_limit, upper_limit
    AAPL, 130, 150
    GOOGL, 2500, 2800
    ```

2. Logging Notifications: Notifications will be logged in `notifications.log`. You can check the `notifications.log` file for updates on stock price movements and any notifications logged by the bot.

## Requirements

• Python 3.9 or higher

• Required Python packages listed in `requirements.txt`

## Docker Usage

To run the StockFXBot in a Docker container, follow these steps:

1. Build the Docker image:

    ```bash
    docker build -t stockfxbot .
    ```

2. Run the Docker container:

    ```bash
    docker run --env-file .env stockfxbot
    ```

Make sure your `.env` file is located in the same directory as your Dockerfile to ensure that the environment variables are properly passed to the container.
