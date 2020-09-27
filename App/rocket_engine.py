# NOTES:
# fuel rate is per sec
# fuel for these purposes is assumed to be RP-1 (rocket propellant-1) and LOX (liquid oxygen)
#

class Engine:
    def __init__(self, thrust, fuel_burn_rt):
        self.thrust = thrust
        self.fuel_burn_rt = fuel_burn_rt
