import math

from App.rocket_engine import Engine


# Notes: Measurements are in meters, kgs, and seconds
# Laundry list of features:
# Equations: Thrust, specific impulse, burn time.
# Count down simulation.


class Rocket(Engine):
    # assumed constants
    GRAVITY = 9.81

    def __init__(self, thrust, fuel_burn_rt, name, spec_impulse, stage1_burn_t, stage2_burn_t,
                 stage1_struct_mass, stage2_struct_mass, diameter, length, fuel_mass):
        super().__init__(thrust, fuel_burn_rt)
        self.name = name
        self.spec_impulse = spec_impulse
        self.stage1_burn_t = stage1_burn_t
        self.stage2_burn_t = stage2_burn_t
        self.stage1_struct_mass = stage1_struct_mass
        self.stage2_struct_mass = stage2_struct_mass
        self.diameter = diameter
        self.height = length
        self.fuel_mass = fuel_mass

    # starting rocket mass
    def initial_mass(self):
        return round(self.stage1_struct_mass + self.stage2_struct_mass + self.fuel_mass, 4)

    # exhaust velocity using specific impulse and the acceleration of gravity
    def exhaust_velocity(self):
        return round(self.spec_impulse * Rocket.GRAVITY, 4)

    # calculates rocket area
    def rocket_area(self):
        return round(math.pi * (self.diameter / 2 ** 2), 4)

    # liftoff weight in newtons
    def lift_off_weight(self):
        return round(self.initial_mass() * Rocket.GRAVITY, 4)

    # resultant force of rocket in newtons
    def resultant_force(self):
        return self.thrust - self.lift_off_weight()

    # rocket acceleration (m/s^2)
    def acceleration(self):
        return round(self.resultant_force() / self.initial_mass(), 4)

    # calculates burnout velocity of rocket under constant gravity

    def burn_velocity(self, stage):
        stage_mass = 0
        if stage == 2:
            stage_mass = self.stage2_struct_mass
        else:
            stage_mass = self.stage1_struct_mass

        velocity = self.exhaust_velocity() * math.log(1 + (stage_mass / self.fuel_mass)) - \
                   (Rocket.GRAVITY * self.fuel_mass) / self.fuel_burn_rt
        return round(velocity, 4)

    # calculates burnout height per rocket stage
    def burn_height(self, stage):
        stage_mass = 0
        if stage == 2:
            stage_mass = self.stage2_struct_mass
        else:
            stage_mass = self.stage1_struct_mass
        burnout_height = ((self.spec_impulse * Rocket.GRAVITY) / stage_mass *
                          (stage_mass * math.log(stage_mass / self.initial_mass()) +
                           self.initial_mass() - stage_mass))
        return round(burnout_height, 4)

    def rocket_name(self):
        return self.name