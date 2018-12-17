from phue import Bridge

bridge = Bridge("192.168.2.119")
# If the app is not registered and the button is not pressed, press the button and call connect()
# (this only needs to be run a single time)
bridge.connect()
# Get the bridge state (This returns the full dictionary that you can explore)
bridge.get_api()

bridge.set_group("radioRaspi", 'on', True)

bridge.run_scene("radioRaspi","hue_pause")