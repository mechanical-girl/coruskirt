import time
import json
start_time = time.time()

capture_data = []

class NeoPixel:
    def __init__(self, pin, count):
        self.count = count
        self.values = [(255, 255, 255)]*count
        self.name = pin.pin

    def __setitem__(self, key, value):
        self.values[key] = value

    def __getitem__(self, key):
        return self.values[key]

    def write(self):
        for i, val in enumerate(self.values):
            print(f'{time.time()-start_time} {self.name} {i} {val[0]} {val[1]} {val[2]}', flush=True)
            with open("output.json", 'w') as f:
                this_step = [time.time()-start_time, self.name, i, val]
                capture_data.append(this_step)
                f.write(json.dumps(capture_data))
