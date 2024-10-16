import os
import shutil

# Get the current script path
current_script = __file__

# Define the destination where the script will replicate itself
destination = "replica.py"

# Replicate the script to the destination file
shutil.copy(current_script, destination)

# Output to inform the user about the replication process
print(f"The script '{current_script}' has successfully replicated itself as '{destination}'.")

# Check if the new file exists and print a message
if os.path.exists(destination):
    print(f"Replication confirmed! '{destination}' now exists in the same directory.")
else:
    print("Replication failed!")

