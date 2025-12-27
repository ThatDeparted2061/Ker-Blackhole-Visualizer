import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def run_black_hole_simulation():
    """
    Simulates and visualizes the extraction of energy from a Rotating (Kerr) Black Hole.
    
    1. Calculates the topology of the Event Horizon (Point of No Return).
    2. Calculates the topology of the Ergosphere (Region of Frame Dragging).
    3. Visualizes the Penrose Process particle split trajectory.
    """
    
    M = 1.0         # Mass of Black Hole
    a = 0.99        # Spin parameter (Extremal limit is 1.0)
    resolution = 80 # Mesh resolution

    print(f"Initializing Kerr Metric Simulation...")
    print(f"Mass (M): {M}")
    print(f"Spin (a): {a}")

    theta = np.linspace(0, np.pi, resolution)
    phi = np.linspace(0, 2 * np.pi, resolution)
    THETA, PHI = np.meshgrid(theta, phi)

    r_plus = M + np.sqrt(M**2 - a**2)
    
    r_ergo = M + np.sqrt(M**2 - a**2 * np.cos(THETA)**2)

    X_EH = r_plus * np.sin(THETA) * np.cos(PHI)
    Y_EH = r_plus * np.sin(THETA) * np.sin(PHI)
    Z_EH = r_plus * np.cos(THETA)

    X_ER = r_ergo * np.sin(THETA) * np.cos(PHI)
    Y_ER = r_ergo * np.sin(THETA) * np.sin(PHI)
    Z_ER = r_ergo * np.cos(THETA)

    
    r_in = np.linspace(4.0, 1.6, 100) 
    phi_in = np.linspace(0, 2.5*np.pi, 100)
    x_in = r_in * np.cos(phi_in)
    y_in = r_in * np.sin(phi_in)
    z_in = np.zeros_like(r_in)

    split_point = (x_in[-1], y_in[-1], z_in[-1])

    r_esc = np.linspace(1.6, 4.5, 80)
    phi_esc = np.linspace(2.5*np.pi, 3.2*np.pi, 80)
    x_esc = r_esc * np.cos(phi_esc)
    y_esc = r_esc * np.sin(phi_esc)
    z_esc = np.linspace(0, 0.8, 80) # Slight vertical kick

    r_fall = np.linspace(1.6, r_plus, 40)
    phi_fall = np.linspace(2.5*np.pi, 4.0*np.pi, 40) # Rapid spiral
    x_fall = r_fall * np.cos(phi_fall)
    y_fall = r_fall * np.sin(phi_fall)
    z_fall = np.linspace(0, -0.2, 40)

    print("Rendering 3D Spacetime Manifold...")
    fig = plt.figure(figsize=(14, 10), facecolor='black')
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('black')
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    ax.grid(False)

    ax.plot_wireframe(X_ER, Y_ER, Z_ER, color='cyan', alpha=0.15, 
                      rstride=4, cstride=4, linewidth=0.5, label='Ergosphere (Static Limit)')
    ax.plot_surface(X_EH, Y_EH, Z_EH, color='black', edgecolor='darkred', 
                    alpha=0.95, linewidth=0.5, zorder=1)

    ax.plot(x_in, y_in, z_in, color='yellow', linewidth=2.5, label='Inbound (E > 0)')
    ax.plot(x_esc, y_esc, z_esc, color='lime', linewidth=3, label='Escaping (E_out > E_in)')
    ax.plot(x_fall, y_fall, z_fall, color='red', linestyle='--', linewidth=1.5, label='Negative E (Consumed)')

    ax.scatter([split_point[0]], [split_point[1]], [split_point[2]], 
               color='white', s=200, marker='*', zorder=10, label='Particle Split Event')

    ax.set_title(f"General Relativity: Penrose Process Simulation\nKerr Spin Parameter a={a}", 
                 color='white', fontsize=16, pad=20)
    
    limit = 3.0
    ax.set_xlim(-limit, limit)
    ax.set_ylim(-limit, limit)
    ax.set_zlim(-limit, limit)
    
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])

    legend = ax.legend(loc='upper right', frameon=True, facecolor='black', edgecolor='white')
    for text in legend.get_texts():
        text.set_color("white")

    plt.tight_layout()
    
    print("Visualization generated successfully.")
    print("Displaying interactive window... (Close window to exit)")
    plt.show()

if __name__ == "__main__":
    run_black_hole_simulation()
