"""
Pole-in-Barn Paradox Example

This example demonstrates the famous pole-in-barn paradox, showing how
the resolution depends on the relativity of simultaneity.
"""

from special_relativity_grapher import Simulation
from special_relativity_grapher.visualization import RelatavisticAnimation
from special_relativity_grapher.utils import trueCond


def pole_in_barn_demo():
    """
    Demonstrate the pole-in-barn paradox.
    
    A person runs with a pole at high speed into a barn. In the ground frame,
    the pole contracts and fits in the barn with both doors closing simultaneously.
    In the pole frame, the barn contracts but the doors don't close simultaneously.
    
    Returns:
        tuple: (ground_frame_animation, pole_frame_animation)
    """
    # Create the pole-in-barn simulation
    PoleInBarnSim = Simulation()
    
    # Add person carrying the pole
    PoleInBarnSim.addPerson([-10, 0], [0, 0], [-0.85, 0], 0.8, 0)
    
    # Add the pole (proper length = 6 units)
    PoleInBarnSim.addLine([-13, 0], 6, [0, 0], [-0.85, 0], True, 0)
    
    # Add barn structure (proper length = 6 units)
    # Bottom wall
    PoleInBarnSim.addLine([-3, -1], 6, [0, 0], [0, 0], True, 0)
    # Top wall  
    PoleInBarnSim.addLine([-3, 1], 6, [0, 0], [0, 0], True, 0)
    
    # Add barn doors (initially open, then close)
    # Left door
    PoleInBarnSim.addLine([-3, 5], 2, [0, -0.95], [0, 0], False, 0)
    # Right door
    PoleInBarnSim.addLine([3, 5], 2, [0, -0.95], [0, 0], False, 0)

    # Run simulation in ground frame
    _, ground_output = PoleInBarnSim.runSimulation([0, 0], 0.1, -10, 30, trueCond)
    
    # Run simulation in pole frame  
    _, pole_output = PoleInBarnSim.runSimulation([-0.85, 0], 0.1, -10, 30, trueCond)

    # Create animations
    plot_limits_ground = [-15, 15, -5, 5]
    plot_limits_pole = [-20, 15, -5, 5]
    
    ani_ground = RelatavisticAnimation([ground_output], plot_limits_ground,
                                     "Pole-in-Barn: Ground Frame (Pole fits!)")
    
    ani_pole = RelatavisticAnimation([pole_output], plot_limits_pole,
                                   "Pole-in-Barn: Pole Frame (Doors not simultaneous!)")
    
    return ani_ground, ani_pole


def explain_paradox():
    """
    Print explanation of the pole-in-barn paradox resolution.
    """
    explanation = """
    Pole-in-Barn Paradox Explanation:
    =================================
    
    Setup:
    - A pole and barn both have the same proper length L
    - The pole moves at high speed (0.85c) toward the barn
    
    Ground Frame Perspective:
    - The pole is length-contracted: L' = L * sqrt(1 - v²/c²) ≈ 0.53L
    - The barn has its proper length L
    - The contracted pole fits inside the barn
    - Both doors can close simultaneously
    
    Pole Frame Perspective:  
    - The pole has its proper length L
    - The barn is length-contracted: L' ≈ 0.53L
    - The pole is longer than the contracted barn
    - BUT the doors don't close simultaneously due to relativity of simultaneity!
    
    Resolution:
    The key is that "simultaneous" events in one frame are NOT simultaneous 
    in another frame. In the pole frame, the far door closes first, then opens 
    before the near door closes, allowing the pole to pass through.
    
    Both perspectives are physically consistent!
    """
    print(explanation)


if __name__ == "__main__":
    print("Pole-in-Barn Paradox Demonstration")
    print("===================================")
    
    explain_paradox()
    
    print("Running pole-in-barn simulation...")
    ground_ani, pole_ani = pole_in_barn_demo()
    
    print("Animations created!")
    print("- Ground frame: Shows the pole fitting in the barn")
    print("- Pole frame: Shows non-simultaneous door closing")
    print("Use .save() to export as gif files.")
