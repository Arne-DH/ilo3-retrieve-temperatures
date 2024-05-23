import csv
import paramiko
import time

# Define the SSH credentials and target
hostname = "" # IP address of the server
username = "" # Username for the server
password = "" # Password for the server

# Create a new SSH client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname, username=username, password=password)

# Calculate the time
end_time = time.time() + 20 * 60  # 20 minutes

# Create a list of sensor names
sensor_names = ["Ambient", "CPU1", "CPU2", "Memory1", "Memory2", "Memory3", "Memory4", "System1", "System2", "System3", "System4", "System5", "N/T", "N/T", "N/T", "N/T", "N/T", "N/T", "System5", "System6", "System7", "System8", "System9", "System10", "System11", "System12", "N/T", "N/T", "Storage", "System13"]

sensor_nums = [f"sensor{i}" for i in range(1, 31)]

# Open the CSV file for writing
with open('Temperatures.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["Index"] + sensor_names)
    writer.writeheader()

    index = 1
    # Loop until the current time is greater than the end time
    while time.time() < end_time:
        readings = {"Index": index}
        # Loop over all the sensors
        for i in range(1, len(sensor_nums) + 1):
            # Run the command for the current sensor and get the output
            command = f"show /system1/{sensor_nums[i-1]}"
            stdin, stdout, stderr = client.exec_command(command)
            output = stdout.read().decode()

            # Parse the output to get the temperature data
            temperature_data = output.split("\n")

            for line in temperature_data:
                if "CurrentReading" in line:
                    reading = line.split("=")[1].strip()
                    readings[sensor_names[i-1]] = reading

        writer.writerow(readings)
        index += 1

        # Sleep for 30 seconds
        time.sleep(30)

    # Close the SSH connection
    client.close()