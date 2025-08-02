"""
Twin Paradox Example

This example demonstrates the twin paradox, showing why the traveling twin
ages less than the Earth-bound twin.
"""

from special_relativity_grapher import Simulation
from special_relativity_grapher.visualization import RelatavisticAnimation
from special_relativity_grapher.utils import trueCond
import numpy as np


def twin_paradox_demo():
    """
    Demonstrate the twin paradox.
    
    Two twins start together. One stays on Earth, the other travels to a distant
    star and returns. Each twin sends signals at regular intervals in their own
    frame. The number of signals received shows who ages more.
    
    Returns:
        tuple: (earth_signals_animation, spaceship_signals_animation)
    """
    # Parameters
    D = 8  # Distance to target in light-years
    speed_of_rocket = 0.8  # Velocity as fraction of c
    gamma_rocket = 1 / np.sqrt(1 - speed_of_rocket**2)  # Lorentz factor
    L = D / speed_of_rocket * 2  # Total trip time in ground frame

    # Simulation 1: Signals sent by Earth twin
    TwinParadoxSim1 = Simulation()
    
    # Stationary twin on Earth
    TwinParadoxSim1.addPt([0.0, 0.0, 0.0], [0, 1], [0, 0])
    
    # Earth twin sends signals every time unit
    for i in range(int(L)):
        TwinParadoxSim1.addLine([0, i+1], 0.01, [1, 1], [0, 0], True, i+1)

    # Moving twin's path (out and back)
    TwinParadoxSim1.addPt([0.0, D, L/2], [0, 0], [0, 0])  # Target planet
    TwinParadoxSim1.addLine([0, 0], 0.01, [speed_of_rocket, 1], [0, 0], True, 0)  # Outbound
    TwinParadoxSim1.addLine([D, L/2], 0.01, [-speed_of_rocket, 1], [0, 0], True, L/2)  # Return

    # Simulation 2: Signals sent by traveling twin
    TwinParadoxSim2 = Simulation()
    
    # Stationary twin on Earth  
    TwinParadoxSim2.addPt([0.0, 0.0, 0.0], [0, 1], [0, 0])
    
    # Traveling twin sends fewer signals due to time dilation
    iter_count = int(L / gamma_rocket) + 1
    for i in range(iter_count):
        # Signals sent at dilated rate
        time_coord = (i + 1) * gamma_rocket
        x_coord = speed_of_rocket * (-abs(-iter_count/2 + i + 1) + iter_count/2)
        TwinParadoxSim2.addLine([x_coord, time_coord], 0.01, [-1, 1], [0, 0], True, time_coord)

    # Moving twin's path (same as before)
    TwinParadoxSim2.addPt([0.0, D, L/2], [0, 0], [0, 0])  # Target planet
    TwinParadoxSim2.addLine([0, 0], 0.01, [speed_of_rocket, 1], [0, 0], True, 0)  # Outbound
    TwinParadoxSim2.addLine([D, L/2], 0.01, [-speed_of_rocket, 1], [0, 0], True, L/2)  # Return

    # Run simulations in ground frame
    _, earth_signals = TwinParadoxSim1.runSimulation([0, 0.0], 0.1, 0, L, trueCond)
    _, spaceship_signals = TwinParadoxSim2.runSimulation([0, 0.0], 0.1, 0, L, trueCond)

    # Create animations
    plot_limits = [-1, D+1, -1, L+1]
    
    ani_earth = RelatavisticAnimation([earth_signals], plot_limits,
                                    "Twin Paradox: Signals from Earth Twin (More signals = older)")
    
    ani_spaceship = RelatavisticAnimation([spaceship_signals], plot_limits,
                                        "Twin Paradox: Signals from Traveling Twin (Fewer signals = younger)")
    
    return ani_earth, ani_spaceship


def explain_twin_paradox():
    """
    Print explanation of the twin paradox resolution.
    """
    explanation = """
    Twin Paradox Explanation:
    ========================
    
    Setup:
    - Twin A stays on Earth
    - Twin B travels to a distant star at high speed and returns
    - Both send signals at regular intervals in their own reference frames
    
    The Paradox:
    - From A's perspective: B's clocks run slow (time dilation)
    - From B's perspective: A's clocks run slow (time dilation)  
    - Who is younger when they reunite?
    
    The Resolution:
    The situation is NOT symmetric! Twin B experiences acceleration:
    1. Acceleration when leaving Earth
    2. Deceleration/acceleration when turning around at the star
    3. Deceleration when returning to Earth
    
    Twin A remains in an inertial frame throughout the journey.
    Twin B does NOT remain in an inertial frame due to the turnaround.
    
    Result: Twin B (the traveler) is younger when they reunite.
    
    Evidence in the simulation:
    - Count the signals: Earth twin sends more signals total
    - More signals = more time elapsed = older
    - The traveling twin ages less due to time dilation effects
    
    Key insight: The asymmetry comes from the acceleration phases,
    not just the constant-velocity travel phases.
    """
    print(explanation)


if __name__ == "__main__":
    print("Twin Paradox Demonstration")
    print("==========================")
    
    explain_twin_paradox()
    
    print("Running twin paradox simulation...")
    earth_ani, spaceship_ani = twin_paradox_demo()
    
    print("Animations created!")
    print("- Earth signals: Shows many signals sent by stationary twin")
    print("- Spaceship signals: Shows fewer signals sent by traveling twin")
    print("The difference in signal count shows the age difference!")
    print("Use .save() to export as gif files.")
