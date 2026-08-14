import numpy as np
from skyfield.api import Topos, load, EarthSatellite

class OrbitalDebrisMitigationEngine:
    def __init__(self, cubesat_tle_line1, cubesat_tle_line2):
        self.ts = load.timescale()
        self.ephemeris = load('de421.bsp')
        self.cubesat = EarthSatellite(cubesat_tle_line1, cubesat_tle_line2, 'Mitigation-CubeSat', self.ts)
        self.laser_coupling_efficiency = 5.6e-5  
        self.active_range_threshold_km = 150.0   

    def propagate_state(self, target_tle_1, target_tle_2, simulation_time_epoch):
        t = self.ts.utc(simulation_time_epoch.year, simulation_time_epoch.month, 
                        simulation_time_epoch.day, simulation_time_epoch.hour, 
                        simulation_time_epoch.minute, simulation_time_epoch.second)
        
        target = EarthSatellite(target_tle_1, target_tle_2, 'Debris-Target', self.ts)
        sub_sat_pos = self.cubesat.at(t).position.km
        sub_debris_pos = target.at(t).position.km
        
        distance_vector = sub_debris_pos - sub_sat_pos
        euclidean_distance = np.linalg.norm(distance_vector)
        
        return euclidean_distance, distance_vector

    def evaluate_interception_matrix(self, distance_km, mass_g, laser_power_watts):
        if distance_km <= self.active_range_threshold_km:
            pulse_duration = 2.5 
            total_energy_joules = laser_power_watts * pulse_duration
            mass_kg = mass_g / 1000.0
            delta_v = (total_energy_joules * self.laser_coupling_efficiency) / mass_kg
            return "ACTIVE_ENGAGEMENT_ABLATION_SEQUENCE", delta_v
        else:
            return "MONITORING_ORBITAL_PLANE", 0.0
