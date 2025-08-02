"""
Loss of Simultaneity Example

This example demonstrates the relativity of simultaneity - events that are
simultaneous in one reference frame are not simultaneous in another.
"""

from special_relativity_grapher import Simulation
from special_relativity_grapher.visualization import RelatavisticAnimation
from special_relativity_grapher.utils import trueCond


def simultaneity_demo():
    """
    Demonstrate loss of simultaneity.
    
    Two events occur simultaneously at different locations in the ground frame.
    When viewed from a moving frame, they are no longer simultaneous.
    
    Returns:
        tuple: (ground_frame_animation, moving_frame_animations)
    """
    # Create simulation with simultaneous events
    LoSSim = Simulation()
    
    # Two events at the same time (t=1) but different locations
    LoSSim.addEvent([1, 1, 0], [0, 0])  # Event 1 at x=1
    LoSSim.addEvent([1, 5, 0], [0, 0])  # Event 2 at x=5
    
    # Add a train to show the reference frame
    LoSSim.addTrain([-1, -1], 7, 2, [0, 0], [0, 0], 0)

    # Run simulation in ground frame (events are simultaneous)
    _, ground_output = LoSSim.runSimulation([0, 0], 0.1, 0, 10, trueCond)
    
    # Run simulation in frame moving at 0.5c in x-direction
    _, moving_x_output = LoSSim.runSimulation([0.5, 0], 0.1, 0, 10, trueCond)
    
    # Run simulation in frame moving diagonally (both x and y)
    _, moving_diag_output = LoSSim.runSimulation([0.5, 0.5], 0.1, 0, 10, trueCond)

    # Create animations
    plot_limits = [-5, 10, -2, 2]
    plot_limits_diag = [-5, 10, -5, 5]
    
    ani_ground = RelatavisticAnimation([ground_output], plot_limits,
                                     "Simultaneity: Ground Frame (Events simultaneous)")
    
    ani_moving_x = RelatavisticAnimation([moving_x_output], plot_limits,
                                       "Simultaneity: Frame moving at 0.5c in x")
    
    ani_moving_diag = RelatavisticAnimation([moving_diag_output], plot_limits_diag,
                                          "Simultaneity: Frame moving diagonally at 0.5c")
    
    return ani_ground, ani_moving_x, ani_moving_diag


def explain_simultaneity():
    """
    Print explanation of the relativity of simultaneity.
    """
    explanation = """
    Relativity of Simultaneity:
    ==========================
    
    Key Principle:
    Events that are simultaneous in one reference frame are generally NOT 
    simultaneous when viewed from a different reference frame moving relative 
    to the first.
    
    Mathematical Basis:
    The Lorentz transformation shows that the time coordinate transforms as:
    t' = γ(t - vx/c²)
    
    This means that the new time t' depends on both the original time t 
    AND the spatial position x. Events at different positions (different x) 
    will have different times t' in the moving frame, even if they had the 
    same time t in the original frame.
    
    What you'll see in the simulation:
    1. Ground frame: Both events appear at the same time (simultaneous)
    2. Moving frame: Events appear at different times (not simultaneous)
    3. The event at larger x coordinate appears to happen first in the 
       moving frame (when frame moves in +x direction)
    
    Physical Implications:
    - There is no universal "now" that applies to all observers
    - The concept of simultaneity is relative to the observer
    - This is crucial for understanding paradoxes like the pole-in-barn problem
    - It's also why faster-than-light communication would violate causality
    
    This effect is purely due to the geometry of spacetime, not a limitation
    of measurement or communication delays.
    """
    print(explanation)


if __name__ == "__main__":
    print("Loss of Simultaneity Demonstration")
    print("==================================")
    
    explain_simultaneity()
    
    print("Running simultaneity simulation...")
    ground_ani, moving_x_ani, moving_diag_ani = simultaneity_demo()
    
    print("Animations created!")
    print("- Ground frame: Events happen simultaneously")
    print("- Moving x frame: Events are no longer simultaneous")  
    print("- Moving diagonal frame: Shows effect persists even with y-component")
    print("Notice how the right event happens first in the moving frames!")
    print("Use .save() to export as gif files.")
