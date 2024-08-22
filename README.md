# dip_price_tracking



# Cryptocurrency Price Tracker

## Description

This Python script monitors the price of a specific cryptocurrency from the "crypto.com" website. It periodically fetches the current price and compares it to previously recorded prices. If a price drop is detected (i.e., the current price is lower than all previously recorded prices), the script prints a notification indicating the drop. Otherwise, it displays the current price.

## Features

- **Real-Time Tracking**: Fetches and monitors cryptocurrency price at regular intervals.
- **Price Drop Notification**: Alerts you if the current price drops below the minimum of previously recorded prices.
- **Customizable Interval**: Allows adjustment of the frequency of price checks.

## Installation

1. **Clone the repository** or download the script file.

2. **Create a `requirements.txt` file** with the following content:

    ```
    requests
    beautifulsoup4
    lxml
    ```

3. **Install the dependencies** by running:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the script**:

    ```bash
    python price_tracker.py
    ```

2. The script will start fetching prices from the specified URL and print updates to the console.

3. **Adjust the URL** if you need to track a different cryptocurrency by modifying the `url` variable in the script.

4. **Change the interval** by adjusting the `time.sleep(10)` value to set the frequency of price checks in seconds.


### user-agent you can find your current User-Agent string by searching for "my user agent" on Google.


