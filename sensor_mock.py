import random
import time

class SensorData:
    def __init__(self):
        self.water_level = 100
        self.battery_level = 100
        self.water_drunk = 0
        self.refills = 0
        self.waste_saved = 0
        self.last_update = time.time()
        
    def update(self):
        current_time = time.time()
        if current_time - self.last_update >= 1:  # Update every second
            # Simulate water consumption
            if self.water_level > 0:
                consumed = random.uniform(0, 2)
                self.water_level = max(0, self.water_level - consumed)
                self.water_drunk += consumed * 5  # Convert to ml
                
                # Calculate waste saved (1 bottle = 12g plastic)
                self.waste_saved = (self.water_drunk / 500) * 12  # 500ml bottle equivalent
            
            # Simulate refills
            if self.water_level <= 0:
                self.water_level = 100
                self.refills += 1
            
            # Simulate battery drain
            self.battery_level = max(0, self.battery_level - random.uniform(0, 0.1))
            
            self.last_update = current_time
        
        # Round values for display
        self.water_level = round(self.water_level, 1)
        self.battery_level = round(self.battery_level, 1)
        self.water_drunk = round(self.water_drunk, 1)
        self.waste_saved = round(self.waste_saved, 1)
