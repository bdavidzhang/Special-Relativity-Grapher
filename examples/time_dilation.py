"""
Time Dilation Example

This example demonstrates time dilation by showing a moving train with a clock
that pulses at regular intervals. The pulse rate appears different when viewed
from different reference frames.
"""

from special_relativity_grapher import Simulation
from special_relativity_grapher.visualization import RelatavisticAnimation
from special_relativity_grapher.utils import trueCond
from IPython.display import HTML
import numpy as np


def time_dilation_demo():
    """
    Demonstrate time dilation with a moving train and clock.
    
    Creates a train moving at 0.8c with a clock that pulses every 3 time units.
    Shows the simulation from both the train frame and the ground frame.
    
    Returns:
        tuple: (ground_frame_animation, train_frame_animation)
    """
    # Create simulation
    TDsim = Simulation()
    pt = np.array([0, 0])
    frame_velo = np.array([0.8, 0])
    
    # Add a pulse (clock) and train
    TDsim.addPulse(pt, 3, 5, 15, frame_velo)
    TDsim.addTrain([-1, -1], 2, 2, [0, 0], frame_velo, 0)

    # Run simulation in train frame (moving with the train)
    TDtimes_train, TDout_train = TDsim.runSimulation(frame_velo, 0.1, 0, 20, trueCond)
    
    # Run simulation in ground frame (stationary)
    TDtimes_ground, TDout_ground = TDsim.runSimulation([0, 0], 0.1, 0, 20, trueCond)

    # Create animations
    plot_limits = [-20, 20, -5, 5]
    
    ani_train = RelatavisticAnimation([TDout_train], plot_limits, 
                                    "Time Dilation: Train Frame (Clock appears normal)")
    
    ani_ground = RelatavisticAnimation([TDout_ground], plot_limits,
                                     "Time Dilation: Ground Frame (Clock appears slow)")
    
    return ani_train, ani_ground


def light_clock_demo():
    """
    Demonstrate time dilation with a light clock bouncing between mirrors.
    
    Shows light bouncing vertically between y = -1 and y = 1 inside a train.
    The light path appears longer in the ground frame, demonstrating time dilation.
    
    Returns:
        tuple: (train_frame_animation, ground_frame_animation)
    """
    # Train frame simulation
    TDsim_train = Simulation()
    pt = np.array([0, -1])
    frame_velo = np.array([0.0, 0.0])
    TDsim_train.addLightBounce(pt, 0.1, 0, 12, frame_velo)
    TDsim_train.addTrain([-1, -1], 2, 2, [0, 0], frame_velo, 0)

    TDtimes_train, TDout_train = TDsim_train.runSimulationLight([0.0, 0.0], 0.1, 0, 12, trueCond)
    
    # Ground frame simulation
    TDsim_ground = Simulation()
    pt = np.array([0, -1])
    frame_velo = np.array([0.0, 0.0])
    TDsim_ground.addLightBounce(pt, 0.1, 0, 20, frame_velo)
    TDsim_ground.addTrain([-1, -1], 2, 2, [0, 0], frame_velo, 0)

    TDtimes_ground, TDout_ground = TDsim_ground.runSimulationLight([0.8, 0.0], 0.1, 0, 20, trueCond)

    plot_limits = [-20, 20, -5, 5]
    
    ani_train = RelatavisticAnimation([TDout_train], plot_limits,
                                    "Light Clock: Train Frame")
    
    ani_ground = RelatavisticAnimation([TDout_ground], plot_limits,
                                     "Light Clock: Ground Frame (Time Dilated)")
    
    return ani_train, ani_ground


if __name__ == "__main__":
    print("Time Dilation Examples")
    print("======================")
    
    print("Running standard time dilation demo...")
    train_ani, ground_ani = time_dilation_demo()
    
    print("Running light clock demo...")
    light_train_ani, light_ground_ani = light_clock_demo()
    
    print("Animations created. Use .save() to export as gif files.")
    print("Example: train_ani.save('time_dilation_train.gif', writer='pillow', fps=30)")
