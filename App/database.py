# !!!UNCOMMENT FOR DATABASE CREATION!!!

# import sqlite3

# conn = sqlite3.connect("rocket_data.db")
# # creates cursor
# c = conn.cursor()
# # c.execute('''CREATE TABLE rocket_values (thrust REAL, fuel_burn_rate REAL, name TEXT, spec_impulse REAL,
# #           stage1_burn_time INT, stage2_burn_time INT, stage1_structural_mass REAL, stage2_structural_mass REAL,
# #           diameter REAL, height REAL, fuel_mass REAL)''')
#
# c.execute('''CREATE TABLE rocket_calculations (name TEXT, wet_mass REAL, exhaust_velocity REAL, area REAL,
#             lift_off_weight REAL, resultant_force REAL, acceleration REAL,
#             stage1_burnout_velocity REAL, stage2_burnout_velocity REAL, stage1_burnout_height REAL,
#             stage2_burnout_height REAL)''')
# # commit changes
# conn.commit()
# conn.close()
