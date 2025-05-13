import math
import random
import time

class FakeSensor:
    def __init__(self):
        self.values = [55.0]
        self._start_time = time.time()

    def clear(self):
        pass

    def update_value(self):
    # Simulate changing sensor voltage between 55 and 60 with decimal precision
        change = random.uniform(-0.2, 0.2)  # Small delta each step
        self.values[0] = round(min(60.0, max(55.0, self.values[0] + change)), 5)

class FakeDevice:
    def __init__(self):
        self.name = "FakeDevice"

    def read(self):
        return True

    def stop(self):
        print("Fake device stopped.")

    def close(self):
        print("Fake device closed.")

    def start(self, period=1000):
        print(f"Fake device started with period {period} ms.")

    def get_enabled_sensors(self):
        return [FakeSensor()]
    
    def open(self): 
        print("Fake device opened")
        return True
    
class FakeGoDirect:
    def __init__(self, use_ble=False):
        pass

    def get_device(self):
        return FakeDevice()

    def quit(self):
        print("Fake GoDirect quit.")

def cl_startup(period=1000):
    device = FakeDevice()
    device.open()
    device.start(period)
    return device  # return a non-zero object to mean success

# sensor.py
import time
import math
import random

class BaseSensor:
    """Common interface both real and fake sensors expose."""
    def start(self, period_ms: int) -> bool: ...
    def read(self) -> float: ...
    def close(self) -> None: ...

# ----------------------------------------------------------------------
# Real hardware --------------------------------------------------------
# ----------------------------------------------------------------------
class RealSensor(BaseSensor):
    def __init__(self):
        # the vendor DLL / godirect setup lives here
        import cl_sensor                           # or `from godirect import xxx`
        self._lib = cl_sensor

    def start(self, period_ms: int) -> bool:
        return bool(self._lib.cl_startup(period_ms))

    def read(self) -> float:
        return self._lib.cl_read()

    def close(self):
        self._lib.cl_close()
