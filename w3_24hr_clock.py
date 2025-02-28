def calculate_alarm_time():
    # Get the current time in hours (0-23)
    current_time = int(input("Enter the current time (in hours 0-23): "))

    # Validate current time input
    if current_time < 0 or current_time > 23:
        print("Error: Current time must be between 0 and 23.")
        return

    # Get the number of hours to wait
    hours_to_wait = int(input("Enter the number of hours to wait for the alarm: "))

    # Validate hours to wait input
    if hours_to_wait < 0:
        print("Error: Hours to wait must be non-negative.")
        return

    # Calculate the time when the alarm will go off
    alarm_time = (current_time + hours_to_wait) % 24

    # Display the result
    print(f"The alarm will go off at {alarm_time} on a 24-hour clock.")


# Run the program
if __name__ == "__main__":
    calculate_alarm_time()