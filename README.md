# Temperature Monitoring System

This repository contains a simple Python script that wil gather temperature readings from various sensors for a specified amount of time and write the data to a CSV file. The script is written for HPE DL380 G7 servers, but can form the baseline for newer ILO versions. The script can also be modified to monitor other parameters if need be.

### Prerequisites

You need to have Python installed on your machine. The script uses the `paramiko` library for SSH connections and `csv` for writing the data to a CSV file. You can install these with pip:

```bash
pip install paramiko
```

### Usage

The script connects to a server over SSH and runs a command to get the temperature readings from various sensors. It then writes these readings to a CSV file. The script runs for 20 minutes, taking a reading every 30 seconds.

You need to provide the IP address, username, and password of the server in the script, the time can also be adjusted in the script if need be.

Then, you can run the script with Python.

The script will create a CSV file named Temperatures.csv in the same directory.

### License
This project is licensed under the MIT License - see the LICENSE.md file for details
