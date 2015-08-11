#! python3
# carSim.py - Traffic light simulation to show where to add assertion to debug program quickly.

# ns = north south, ew = east west
market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}

def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'

        # added to debug the virtual cars crashing issue....
        assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)
switchLights(market_2nd)
