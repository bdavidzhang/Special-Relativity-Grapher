"""
Length Contraction Example

This example demonstrates length contraction by showing multiple rods
of the same proper length moving at different velocities.
"""

from special_relativity_grapher import Simulation
from special_relativity_grapher.visualization import RelatavisticAnimation
from special_relativity_grapher.utils import trueCond


def length_contraction_demo():
    """
    Demonstrate length contraction with rods at different velocities.
    
    Creates three rods with the same proper length (5 units) moving at
    different velocities: 0.99c, 0.5c, and -0.5c.
    
    Returns:
        tuple: (stationary_frame_animation, moving_frame_animation)
    """
    # Create simulation with multiple rods
    LCsim = Simulation()
    
    # All rods have proper length = 5 units
    proper_length = 5
    
    # Rod 1: Moving at 0.99c (highly relativistic)
    LCsim.addLine([0, 0], proper_length, [0, 0], [-0.99, 0], True, 0)
    
    # Rod 2: Moving at 0.5c  
    LCsim.addLine([0, 1], proper_length, [0, 0], [-0.5, 0], True, 0)
    
    # Rod 3: Moving at -0.5c (opposite direction)
    LCsim.addLine([0, 2], proper_length, [0, 0], [0.5, 0], True, 0)

    # Run simulation in ground frame
    LCtimes_ground, LCoutput_ground = LCsim.runSimulation([0, 0], 0.1, 0, 10, trueCond)
    
    # Run simulation in frame moving at 0.5c
    LCtimes_moving, LCoutput_moving = LCsim.runSimulation([0.5, 0], 0.1, 0, 10, trueCond)

    # Create animations
    plot_limits = [-5, 10, -2, 3]
    
    ani_ground = RelatavisticAnimation([LCoutput_ground], plot_limits,
                                     "Length Contraction: Ground Frame")
    
    ani_moving = RelatavisticAnimation([LCoutput_moving], plot_limits,
                                     "Length Contraction: Frame Moving at 0.5c")
    
    return ani_ground, ani_moving


def transverse_length_demo():
    """
    Demonstrate that transverse length contraction does not occur.
    
    Shows rods oriented perpendicular to the direction of motion,
    which should maintain their proper length in all frames.
    
    Returns:
        matplotlib.animation.FuncAnimation: Animation showing no transverse contraction
    """
    # Create simulation with vertical rods
    LCsim = Simulation()
    
    # Rod 1: Stationary vertical rod
    LCsim.addLine([0, 0], 5, [0, 0], [0, 0], False, 0)  # False = vertical
    
    # Rod 2: Moving vertical rod at 0.5c
    LCsim.addLine([1, 0], 5, [0, 0], [-0.5, 0], False, 0)

    # Run simulation in ground frame
    LCtimes, LCoutput = LCsim.runSimulation([0, 0], 0.1, 0, 10, trueCond)

    # Create animation
    plot_limits = [-5, 10, -2, 7]
    ani = RelatavisticAnimation([LCoutput], plot_limits,
                              "No Transverse Length Contraction")
    
    return ani


if __name__ == "__main__":
    print("Length Contraction Examples")
    print("===========================")
    
    print("Running length contraction demo...")
    ground_ani, moving_ani = length_contraction_demo()
    
    print("Running transverse length demo...")
    transverse_ani = transverse_length_demo()
    
    print("Animations created. Use .save() to export as gif files.")
    print("Note: The rod moving at 0.99c will appear significantly contracted!")
    print("The contracted length = proper_length * sqrt(1 - v²/c²)")
