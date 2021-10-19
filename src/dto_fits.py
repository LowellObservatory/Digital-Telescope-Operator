

# Subscribe to messaging system

on_message (message) {
  # Do the task requested, usually update header, write FITS file.
  # Send a "task complete" message when done.
}

# Main Loop
run = True
while(run) {
  # Update dictionary of current values of keywords, get from Redis.
  # async sleep 1 second (so other processes can run)
}