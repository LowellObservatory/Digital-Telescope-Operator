# DTO main

# most of this is pseudocode and comments

# Turn on hardware (this is remote control via smart plugs, Power Distribution Units (PDU))
#    Mount
#    Dome
#    Camera + Filter Wheel
#    Focuser, De-rotator (do these need to be turned on seperately?)
#    All Sky Camera (? on all the time ?)
#    Cloud monitor (? on all the time ?)

# Initialize services
# Check to see if Database/Messaging services are running.  Start if not
# Check to see if hardware services are running (they shouldn't be), stop them if they are.
# Start up needed services:
#    Weather Checker service
#    Telescope Status Checker service
#    Mount Control service (PWI4 in our prototype)
#    Camera + Filter Wheel Control service (Indigo based in our prototype)
#    Image Statictics service
#    Focus Loop service
#    External Request Listener service
#    FITS File Writer service
#    UPS monitor service
#    Diskspace monitor (?)
#    All Sky Camera service (checks for clouds)
#    Cloud monitor service (checks for clouds)

# Set up communications
#    Make connections to all services via subscriptions, etc.

# Main Loop
run = True
while(run) {
  # Check events
  #    Various events will trigger dome closure, shutdown, updates to database,
  #      changes to observing plans, and etc.  We'll need to handle these events.
  #    Another class of events includes the arrival of new FITS files from the
  #      camera.  These must be sent off to the FITS file writer service.
  # Get next command
  #    This is either read from a script file or requested from the scheduler.
  #    If the command is DONE or EXIT, set "run" to False
  # Check command and execute
  #    Make sure all the requirement for the command are met (time, airmass, etc.)
  # async sleep 1 second (so other processes can run)
}

# Terminate communications

# End Services

# Turn off hardware

# Exit

