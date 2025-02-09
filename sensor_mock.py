import random
import time

class SensorData:
    def __init__(self):
        self.water_level = 100
        self.battery_level = 100
        self.water_drunk = 0
        self.refills_needed = None  # Will be set after weight input
        self.completed_refills = 0
        self.waste_saved = 0
        self.last_update = time.time()
        self.daily_target_liters = None
        self.all_refills_complete = False

    def calculate_daily_target(self, weight_lbs):
        # Convert weight to required water
        ounces = weight_lbs / 2
        self.daily_target_liters = round(ounces * 0.0295735, 1)  # Convert oz to L

        # Calculate refills needed based on target liters
        # If target is less than 1L, need 1 refill
        # If target is between 1-2L, need 2 refills
        # If target is between 2-3L, need 3 refills, and so on
        self.refills_needed = max(1, round(self.daily_target_liters + 0.5))

    def update(self):
        if self.refills_needed is None:
            return

        current_time = time.time()
        if current_time - self.last_update >= 1:  # Update every second
            # Simulate water consumption
            if self.water_level > 0:
                consumed = random.uniform(0, 2)
                self.water_level = max(0, self.water_level - consumed)
                self.water_drunk += consumed * 10  # Convert to ml (now 1000ml total)

                # Calculate waste saved (1 bottle = 12g plastic, based on 500ml bottles)
                self.waste_saved = (self.water_drunk / 500) * 12

            # Simulate refills (now 1000ml per refill)
            if self.water_level <= 0:
                self.water_level = 100
                self.completed_refills += 1
                if self.completed_refills >= self.refills_needed:
                    self.all_refills_complete = True

            # Simulate battery drain
            self.battery_level = max(0, self.battery_level - random.uniform(0, 0.1))

            self.last_update = current_time

        # Round values for display
        self.water_level = round(self.water_level, 1)
        self.battery_level = round(self.battery_level, 1)
        self.water_drunk = round(self.water_drunk, 1)
        self.waste_saved = round(self.waste_saved, 1)