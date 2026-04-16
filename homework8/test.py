import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


# ==========================================
# 1. Mathematical Core
# ==========================================
def calculate_parabola(r):
    """Calculates the parabola y = r*x*(1-x) for the background."""
    x = np.linspace(0, 1, 500)
    y = r * x * (1 - x)
    return x, y

def calculate_cobweb(r, x0, iterations=50):
    """
    Generates the coordinates for the alternating vertical and 
    horizontal lines of the cobweb trajectory.
    """
    x_coords = [x0]
    y_coords = [0] # Start on the x-axis
    
    current_x = x0
    for _ in range(iterations):
        # Calculate the new output
        next_x = r * current_x * (1 - current_x)
        
        # Step 2: Go Vertical (to the parabola)
        x_coords.append(current_x)
        y_coords.append(next_x)
        
        # Step 3: Go Horizontal (to the y=x line)
        x_coords.append(next_x)
        y_coords.append(next_x)
        
        # Update current value for the next loop
        current_x = next_x
        
    return x_coords, y_coords

# ==========================================
# 2. Setup the Figure and Axes
# ==========================================
fig, ax = plt.subplots(figsize=(8, 8))
plt.subplots_adjust(bottom=0.25) # Make room for sliders

initial_r = 2.8
initial_x0 = 0.2

# Plot the diagonal 'Conveyor Belt' line (y = x)
ax.plot([0, 1], [0, 1], color='gray', linestyle='--', lw=1.5, label='y = x (Conveyor Belt)')

# Plot the 'Calculator' Parabola
x_parabola, y_parabola = calculate_parabola(initial_r)
parabola_line, = ax.plot(x_parabola, y_parabola, color='dodgerblue', lw=2, label='y = r \u00B7 x(1-x) (Calculator)')

# Plot the Cobweb trajectory
x_web, y_web = calculate_cobweb(initial_r, initial_x0)
web_line, = ax.plot(x_web, y_web, color='crimson', lw=1, alpha=0.8, marker='.', markersize=4, label='Cobweb Trajectory')

# Formatting
ax.set_title('Cobweb Plot')
ax.set_xlabel('Input State (x_n)')
ax.set_ylabel('Output State (x_n+1)')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.legend(loc='upper left')
ax.grid(True, alpha=0.3)

# ==========================================
# 3. Create Interactive Sliders
# ==========================================
# Define axes for sliders: [left, bottom, width, height]
ax_r = plt.axes([0.15, 0.10, 0.70, 0.03])
ax_x0 = plt.axes([0.15, 0.05, 0.70, 0.03])

slider_r = Slider(ax_r, 'Growth (r)', 0.0, 4.0, valinit=initial_r, color='dodgerblue')
slider_x0 = Slider(ax_x0, 'Start (x\u2080)', 0.0, 1.0, valinit=initial_x0, color='crimson')

# ==========================================
# 4. Define the Update Mechanism
# ==========================================
def update(val):
    """Recalculates the math and updates the plot when a slider moves."""
    r = slider_r.val
    x0 = slider_x0.val
    
    # Update the parabola
    _, y_parabola_new = calculate_parabola(r)
    parabola_line.set_ydata(y_parabola_new)
    
    # Update the cobweb
    x_web_new, y_web_new = calculate_cobweb(r, x0)
    web_line.set_data(x_web_new, y_web_new)
    
    # Redraw
    fig.canvas.draw_idle()

# Bind the update function to the sliders
slider_r.on_changed(update)
slider_x0.on_changed(update)

print("Cobweb Plot window...")
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# ==========================================
# 1. Mathematical Core
# ==========================================
def calculate_parabola(r):
    """Calculates the parabola y = r*x*(1-x) for the cobweb background."""
    x = np.linspace(0, 1, 500)
    y = r * x * (1 - x)
    return x, y

def calculate_system(r, x0, iterations=50):
    """
    Calculates both the Cobweb coordinates and the Time Series array
    in a single pass to ensure they are perfectly synced.
    """
    # Arrays for the Time Series
    time_steps = np.arange(iterations + 1)
    x_timeseries = np.zeros(iterations + 1)
    x_timeseries[0] = x0
    
    # Lists for the Cobweb Plot
    x_web = [x0]
    y_web = [0]
    
    current_x = x0
    for i in range(iterations):
        next_x = r * current_x * (1 - current_x)
        
        # Record for Time Series
        x_timeseries[i+1] = next_x
        
        # Record for Cobweb (Vertical then Horizontal)
        x_web.extend([current_x, next_x])
        y_web.extend([next_x, next_x])
        
        current_x = next_x
        
    return time_steps, x_timeseries, x_web, y_web

# ==========================================
# 2. Setup the Unified Dashboard Figure
# ==========================================
# Create a wide figure with 1 row and 2 columns
fig, (ax_web, ax_time) = plt.subplots(1, 2, figsize=(14, 6))

# Make room at the bottom for our interactive sliders
plt.subplots_adjust(bottom=0.25, wspace=0.25)

# Initial Parameters
initial_r = 2.8
initial_x0 = 0.1
n_iterations = 50

# Calculate initial data
x_p, y_p = calculate_parabola(initial_r)
t_steps, x_ts, x_w, y_w = calculate_system(initial_r, initial_x0, n_iterations)

# --- Subplot 1: The Cobweb Plot (Left) ---
ax_web.plot([0, 1], [0, 1], color='gray', linestyle='--', lw=1.5, label='y = x (Rest)')
parabola_line, = ax_web.plot(x_p, y_p, color='dodgerblue', lw=2, label='y = rx(1-x)')
web_line, = ax_web.plot(x_w, y_w, color='crimson', lw=1, alpha=0.7, marker='.', markersize=3)

ax_web.set_title('The Mechanism: Cobweb Plot')
ax_web.set_xlabel('Input State (x_n)')
ax_web.set_ylabel('Output State (x_{n+1})')
ax_web.set_xlim(0, 1)
ax_web.set_ylim(0, 1)
ax_web.legend(loc='upper left')
ax_web.grid(True, alpha=0.3)

# --- Subplot 2: The Time Series (Right) ---
time_line, = ax_time.plot(t_steps, x_ts, color='purple', lw=1.5, marker='o', markersize=4)

ax_time.set_title('The Rhythm: Time Series')
ax_time.set_xlabel('Iteration Step (n)')
ax_time.set_ylabel('Population Fraction (x_n)')
ax_time.set_xlim(0, n_iterations)
ax_time.set_ylim(0, 1.05)
ax_time.grid(True, alpha=0.3)

# ==========================================
# 3. Create Interactive Sliders
# ==========================================
# [left, bottom, width, height]
ax_r = plt.axes([0.15, 0.10, 0.70, 0.03])
ax_x0 = plt.axes([0.15, 0.04, 0.70, 0.03])

slider_r = Slider(ax_r, 'Growth (r)', 0.0, 4.0, valinit=initial_r, color='dodgerblue')
slider_x0 = Slider(ax_x0, 'Start (x\u2080)', 0.0, 1.0, valinit=initial_x0, color='crimson')

# ==========================================
# 4. Define the Update Mechanism
# ==========================================
def update(val):
    r = slider_r.val
    x0 = slider_x0.val
    
    # 1. Recalculate everything
    _, y_p_new = calculate_parabola(r)
    _, x_ts_new, x_w_new, y_w_new = calculate_system(r, x0, n_iterations)
    
    # 2. Update the Parabola
    parabola_line.set_ydata(y_p_new)
    
    # 3. Update the Cobweb trajectory
    web_line.set_data(x_w_new, y_w_new)
    
    # 4. Update the Time Series trajectory
    time_line.set_ydata(x_ts_new)
    
    # Redraw the canvas
    fig.canvas.draw_idle()

# Bind the sliders to the update function
slider_r.on_changed(update)
slider_x0.on_changed(update)

print("Launching Unified Non-linear Dynamics Simulator...")
plt.show()




import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# ==========================================
# 1. Mathematical Core
# ==========================================
def calculate_parabola(r):
    x = np.linspace(0, 1, 500)
    y = r * x * (1 - x)
    return x, y

def calculate_system(r, x0, iterations=100):
    time_steps = np.arange(iterations + 1)
    x_timeseries = np.zeros(iterations + 1)
    x_timeseries[0] = x0
    
    x_web = [x0]
    y_web = [0]
    
    current_x = x0
    for i in range(iterations):
        next_x = r * current_x * (1 - current_x)
        x_timeseries[i+1] = next_x
        x_web.extend([current_x, next_x])
        y_web.extend([next_x, next_x])
        current_x = next_x
        
    return time_steps, x_timeseries, x_web, y_web

def precalculate_bifurcation(n_r_points=1000, n_transients=500, n_plot=100):
    r_vals = np.linspace(2.5, 4.0, n_r_points)
    x = np.ones(n_r_points) * 0.1
    for _ in range(n_transients):
        x = r_vals * x * (1 - x)
    
    r_plot = []
    x_plot = []
    for _ in range(n_plot):
        x = r_vals * x * (1 - x)
        r_plot.extend(r_vals)
        x_plot.extend(x)
    return r_plot, x_plot

# ==========================================
# 2. Setup the Master Dashboard Layout
# ==========================================
print("Pre-calculating Bifurcation Background...")
r_bifur, x_bifur = precalculate_bifurcation()

fig, axes = plt.subplot_mosaic([['web', 'time'], ['map', 'map']], figsize=(14, 9))
plt.subplots_adjust(bottom=0.20, hspace=0.35, wspace=0.2)

initial_r = 2.8
initial_x0 = 0.1
n_iterations = 100

# --- Top Left: Cobweb ---
ax_web = axes['web']
x_p, y_p = calculate_parabola(initial_r)
ax_web.plot([0, 1], [0, 1], color='gray', linestyle='--', lw=1.5)
parabola_line, = ax_web.plot(x_p, y_p, color='dodgerblue', lw=2)
t_steps, x_ts, x_w, y_w = calculate_system(initial_r, initial_x0, n_iterations)
web_line, = ax_web.plot(x_w, y_w, color='crimson', lw=1, alpha=0.7, marker='.', markersize=3)
ax_web.set_title('The Engine (Cobweb Plot)')
ax_web.set_xlim(0, 1)
ax_web.set_ylim(0, 1)
ax_web.grid(True, alpha=0.3)

# --- Top Right: Time Series ---
ax_time = axes['time']
time_line, = ax_time.plot(t_steps, x_ts, color='purple', lw=1.5, marker='o', markersize=3)
ax_time.set_title('The Heartbeat (Time Series)')
ax_time.set_xlim(0, 50)
ax_time.set_ylim(0, 1.05)
ax_time.grid(True, alpha=0.3)

# --- Bottom: Bifurcation Map with DYNAMIC OVERLAY ---
ax_map = axes['map']
ax_map.plot(r_bifur, x_bifur, ',k', alpha=0.05) # Static background
tracker_line = ax_map.axvline(initial_r, color='gray', lw=1, linestyle='--')

# NEW: The dynamic dots representing the current steady state!
# We grab the last 20 iterations (assuming the transients have decayed)
live_dots, = ax_map.plot([initial_r]*20, x_ts[-20:], 'ro', markersize=4, alpha=0.5)

ax_map.set_title('The Map (Dynamic Attractor Overlay)')
ax_map.set_xlabel('Growth Rate Parameter (r)')
ax_map.set_xlim(2.5, 4.0)
ax_map.set_ylim(0, 1)
ax_map.grid(True, alpha=0.3)

# ==========================================
# 3. Create Interactive Sliders
# ==========================================
ax_r = plt.axes([0.15, 0.08, 0.70, 0.02])
ax_x0 = plt.axes([0.15, 0.03, 0.70, 0.02])
slider_r = Slider(ax_r, 'Gain (r)', 2.5, 4.0, valinit=initial_r, color='dodgerblue')
slider_x0 = Slider(ax_x0, 'Start (x\u2080)', 0.0, 1.0, valinit=initial_x0, color='crimson')

# ==========================================
# 4. Update Mechanism
# ==========================================
def update(val):
    r = slider_r.val
    x0 = slider_x0.val
    
    # Recalculate everything
    _, y_p_new = calculate_parabola(r)
    _, x_ts_new, x_w_new, y_w_new = calculate_system(r, x0, n_iterations)
    
    # Update Top Charts
    parabola_line.set_ydata(y_p_new)
    web_line.set_data(x_w_new, y_w_new)
    time_line.set_ydata(x_ts_new)
    
    # Update Bottom Chart (The Map)
    tracker_line.set_xdata([r, r])
    
    # MAGIC HAPPENS HERE: We feed the final settled values from the Time Series
    # directly into the scatter dots on the Bifurcation map!
    live_dots.set_data([r]*20, x_ts_new[-20:])
    
    fig.canvas.draw_idle()

slider_r.on_changed(update)
slider_x0.on_changed(update)

print("Launching Dynamic Master Dashboard...")
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from matplotlib.animation import FuncAnimation

# ==========================================
# 1. Mathematical Core
# ==========================================
def calculate_parabola(r):
    x = np.linspace(0, 1, 500)
    y = r * x * (1 - x)
    return x, y

def calculate_system(r, x0, iterations=100):
    time_steps = np.arange(iterations + 1)
    x_timeseries = np.zeros(iterations + 1)
    x_timeseries[0] = x0
    
    x_web = [x0]
    y_web = [0]
    
    current_x = x0
    for i in range(iterations):
        next_x = r * current_x * (1 - current_x)
        x_timeseries[i+1] = next_x
        x_web.extend([current_x, next_x])
        y_web.extend([next_x, next_x])
        current_x = next_x
        
    return time_steps, x_timeseries, x_web, y_web

# ==========================================
# 2. Setup the Master Dashboard Layout
# ==========================================
fig, axes = plt.subplot_mosaic([['web', 'time'], ['map', 'map']], figsize=(14, 9))
plt.subplots_adjust(bottom=0.25, hspace=0.35, wspace=0.2)
fig.canvas.manager.set_window_title("Dynamic Bifurcation Constructor")

initial_r = 2.5
initial_x0 = 0.1
n_iterations = 100
settled_points = 30 # How many points to "drip" onto the map per frame

# --- Top Left: Cobweb Plot ---
ax_web = axes['web']
x_p, y_p = calculate_parabola(initial_r)
ax_web.plot([0, 1], [0, 1], color='gray', linestyle='--', lw=1.5)
parabola_line, = ax_web.plot(x_p, y_p, color='dodgerblue', lw=2)
t_steps, x_ts, x_w, y_w = calculate_system(initial_r, initial_x0, n_iterations)
web_line, = ax_web.plot(x_w, y_w, color='crimson', lw=1, alpha=0.7, marker='.', markersize=3)
ax_web.set_title('The Engine (Cobweb Plot)')
ax_web.set_xlim(0, 1)
ax_web.set_ylim(0, 1)
ax_web.grid(True, alpha=0.3)

# --- Top Right: Time Series ---
ax_time = axes['time']
time_line, = ax_time.plot(t_steps, x_ts, color='purple', lw=1.5, marker='o', markersize=3)
ax_time.set_title('The Heartbeat (Time Series)')
ax_time.set_xlim(0, 50)
ax_time.set_ylim(0, 1.05)
ax_time.grid(True, alpha=0.3)

# --- Bottom: The Dynamic Bifurcation Canvas ---
ax_map = axes['map']

# 1. The Permanent Ink: This starts empty and accumulates dots over time
trace_r_data = []
trace_x_data = []
trace_line, = ax_map.plot([], [], ',k', alpha=0.3) # ',k' means black pixels

# 2. The Tracking Line
tracker_line = ax_map.axvline(initial_r, color='gray', lw=1, linestyle='--')

# 3. The Glowing Red Dots: Shows the current attractor jumping around
live_dots, = ax_map.plot([], [], 'ro', markersize=4, alpha=0.8)

ax_map.set_title('The Map (Drawing Live...)')
ax_map.set_xlabel('Growth Rate Parameter (r)')
ax_map.set_xlim(2.5, 4.0)
ax_map.set_ylim(0, 1)
ax_map.grid(True, alpha=0.3)

# ==========================================
# 3. Create Interactive Controls
# ==========================================
ax_r = plt.axes([0.15, 0.12, 0.70, 0.02])
ax_x0 = plt.axes([0.15, 0.08, 0.70, 0.02])
slider_r = Slider(ax_r, 'Gain (r)', 2.5, 4.0, valinit=initial_r, color='dodgerblue')
slider_x0 = Slider(ax_x0, 'Start (x\u2080)', 0.0, 1.0, valinit=initial_x0, color='crimson')

ax_play = plt.axes([0.4, 0.02, 0.1, 0.04])
ax_reset = plt.axes([0.55, 0.02, 0.1, 0.04])
btn_play = Button(ax_play, 'Play Sweep', color='lightgreen')
btn_reset = Button(ax_reset, 'Clear & Restart', color='lightcoral')

# ==========================================
# 4. The Master Update Engine
# ==========================================
def update(val):
    r = slider_r.val
    x0 = slider_x0.val
    
    # 1. Recalculate Physics
    _, y_p_new = calculate_parabola(r)
    _, x_ts_new, x_w_new, y_w_new = calculate_system(r, x0, n_iterations)
    
    # 2. Update Top Charts
    parabola_line.set_ydata(y_p_new)
    web_line.set_data(x_w_new, y_w_new)
    time_line.set_ydata(x_ts_new)
    
    # 3. Update Map Tracking Elements
    tracker_line.set_xdata([r, r])
    live_dots.set_data([r]*settled_points, x_ts_new[-settled_points:])
    
    # 4. PAINT THE INK: Add the settled points to our permanent memory
    trace_r_data.extend([r] * settled_points)
    trace_x_data.extend(x_ts_new[-settled_points:])
    trace_line.set_data(trace_r_data, trace_x_data)
    
    fig.canvas.draw_idle()

slider_r.on_changed(update)

# ==========================================
# 5. Animation and Button Logic
# ==========================================
is_playing = False

def toggle_play(event):
    global is_playing
    is_playing = not is_playing
    btn_play.label.set_text('Pause' if is_playing else 'Play Sweep')

def clear_and_reset(event):
    global is_playing
    # Stop the motor if it's running
    if is_playing:
        toggle_play(None)
    
    # Empty the ink bottle
    trace_r_data.clear()
    trace_x_data.clear()
    trace_line.set_data([], [])
    
    # Snap back to the beginning
    slider_r.set_val(2.5)

btn_play.on_clicked(toggle_play)
btn_reset.on_clicked(clear_and_reset)

def animation_loop(frame):
    """The internal motor that turns the slider when 'Play' is active."""
    if is_playing:
        new_r = slider_r.val + 0.005 # How fast the dial turns
        if new_r >= 4.0:
            toggle_play(None) # Auto-pause when we hit the end
        else:
            slider_r.set_val(new_r) # Physically move the slider

# Run the motor at 30 frames per second
ani = FuncAnimation(fig, animation_loop, interval=30, save_count=1)

print("Launching Live Bifurcation Constructor...")
plt.show()


import numpy as np
import matplotlib.pyplot as plt

def calculate_lyapunov():
    print("Calculating the Lyapunov spectrum...")
    
    # 1. Setup the r dial (Scan from 2.5 to 4.0)
    n_points = 2000
    r_vals = np.linspace(2.5, 4.0, n_points)
    
    # We will store the calculated exponents here
    lyapunov_exponents = np.zeros(n_points)
    
    # 2. Sweep through every r value
    for i, r in enumerate(r_vals):
        x = 0.5 # Start in the middle
        
        # Burn-in: Let transients decay (find the attractor)
        for _ in range(500):
            x = r * x * (1 - x)
            
        # Calculation phase: Sum the log of the derivative
        sum_log_deriv = 0
        n_iterations = 500
        
        for _ in range(n_iterations):
            # The feedback loop
            x = r * x * (1 - x)
            
            # The derivative: f'(x) = r - 2rx
            derivative = r - 2 * r * x
            
            # Avoid log(0) errors if the derivative happens to be exactly 0
            if derivative != 0:
                sum_log_deriv += np.log(abs(derivative))
                
        # Average the sum to get lambda
        lyapunov_exponents[i] = sum_log_deriv / n_iterations

    # 3. Plotting the result
    plt.figure(figsize=(10, 6))
    plt.title('Lyapunov Exponent (\u03BB) of the Logistic Map')
    
    # Draw the critical zero-line
    plt.axhline(0, color='black', lw=1, linestyle='--')
    
    # Plot the calculated data
    plt.plot(r_vals, lyapunov_exponents, color='purple', lw=1)
    
    plt.xlabel('Growth Rate (r)')
    plt.ylabel('Lyapunov Exponent (\u03BB)')
    plt.xlim(2.5, 4.0)
    plt.ylim(-2.5, 1.0)
    plt.grid(True, alpha=0.3)
    
    # Highlight the chaotic region (where lambda > 0)
    plt.fill_between(r_vals, 0, lyapunov_exponents, 
                     where=(lyapunov_exponents > 0), 
                     color='red', alpha=0.3, label='Chaos (\u03BB > 0)')
                     
    plt.legend()
    plt.show()

if __name__ == "__main__":
    calculate_lyapunov()
    
    
    import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def precalculate_chaos_universe(n_points=1500):
    """Calculates both the Bifurcation map and Lyapunov spectrum upfront."""
    r_vals = np.linspace(2.5, 4.0, n_points)
    
    # --- 1. Calculate Bifurcation Data ---
    x_bifur = np.ones(n_points) * 0.1
    # Burn-in (let transients decay)
    for _ in range(500):
        x_bifur = r_vals * x_bifur * (1 - x_bifur)
        
    # Record the settled points
    r_plot = []
    x_plot = []
    for _ in range(100):
        x_bifur = r_vals * x_bifur * (1 - x_bifur)
        r_plot.extend(r_vals)
        x_plot.extend(x_bifur)
        
    # --- 2. Calculate Lyapunov Data ---
    lyap_vals = np.zeros(n_points)
    x_lyap = np.ones(n_points) * 0.5
    
    # Burn-in
    for _ in range(500):
        x_lyap = r_vals * x_lyap * (1 - x_lyap)
        
    # Calculate running sum of the log of the derivative
    sum_log_deriv = np.zeros(n_points)
    for _ in range(500):
        x_lyap = r_vals * x_lyap * (1 - x_lyap)
        derivative = abs(r_vals - 2 * r_vals * x_lyap)
        
        # Avoid log(0) warnings by replacing 0 with a tiny number
        derivative[derivative == 0] = 1e-10 
        sum_log_deriv += np.log(derivative)
        
    lyap_vals = sum_log_deriv / 500
    
    return r_plot, x_plot, r_vals, lyap_vals

# ==========================================
# Build the Dashboard
# ==========================================
print("Calculating the Universe (This takes a few seconds)...")
r_bifur, x_bifur, r_lyap, y_lyap = precalculate_chaos_universe()

# Create a figure with 2 stacked subplots
fig, (ax_lyap, ax_bifur) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)
plt.subplots_adjust(bottom=0.20, hspace=0.1)
fig.canvas.manager.set_window_title("Lyapunov & Bifurcation Diagnostic")

initial_r = 3.5

# --- Top Chart: The Lyapunov Spectrum ---
ax_lyap.axhline(0, color='black', lw=1.5, linestyle='--') # The critical Zero Line
ax_lyap.plot(r_lyap, y_lyap, color='purple', lw=1.5)

# Color the chaotic regions red
ax_lyap.fill_between(r_lyap, 0, y_lyap, where=(y_lyap > 0), color='red', alpha=0.3)

# The Top Tracker Line & Text
tracker_lyap = ax_lyap.axvline(initial_r, color='crimson', lw=2)
text_lyap = ax_lyap.text(2.45, 1.3, '', fontsize=12, fontweight='bold', 
                         bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray'))

ax_lyap.set_title('Lyapunov Exponent (\u03BB)')
ax_lyap.set_ylabel('\u03BB Value')
ax_lyap.set_ylim(-2.5, 1.0)
ax_lyap.grid(True, alpha=0.3)

# --- Bottom Chart: The Bifurcation Map ---
ax_bifur.plot(r_bifur, x_bifur, ',k', alpha=0.05) # Black pixel dust
tracker_bifur = ax_bifur.axvline(initial_r, color='crimson', lw=2)

ax_bifur.set_title('Bifurcation Map')
ax_bifur.set_xlabel('Growth Rate Parameter (r)')
ax_bifur.set_ylabel('Population (x)')
ax_bifur.set_xlim(2.5, 4.0)
ax_bifur.set_ylim(0, 1)
ax_bifur.grid(True, alpha=0.3)

# ==========================================
# Interactive Slider Logic
# ==========================================
ax_slider = plt.axes([0.15, 0.08, 0.70, 0.03])
slider_r = Slider(ax_slider, 'Gain (r)', 2.5, 4.0, valinit=initial_r, color='dodgerblue')

def update(val):
    r_current = slider_r.val
    
    # 1. Move both vertical tracker lines
    tracker_lyap.set_xdata([r_current, r_current])
    tracker_bifur.set_xdata([r_current, r_current])
    
    # 2. Find the exact Lyapunov value for the current 'r'
    # We do this by finding the closest index in our pre-calculated array
    idx = (np.abs(r_lyap - r_current)).argmin()
    current_lambda = y_lyap[idx]
    
    # 3. Update the text readout
    status = "CHAOS" if current_lambda > 0 else "STABLE"
    color = "red" if current_lambda > 0 else "green"
    
    text_lyap.set_text(f"r = {r_current:.4f}\n\u03BB = {current_lambda:.4f}\nState: {status}")
    text_lyap.set_color(color)
    
    fig.canvas.draw_idle()

# Run the update function once to set the initial text
update(initial_r)

# Bind the slider to the update function
slider_r.on_changed(update)

print("Launching Diagnostic Tool...")
plt.show()


import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. Define Parameters (from the UI)
# ==========================================
f1 = 199            # Frequency in Hz
fs = 2703           # Sample Rate in Hz
N = 1024            # Number of Samples

# ==========================================
# 2. Generate the Signal
# ==========================================
# Create an array of sample indices (0 to 1023)
n = np.arange(N)    

# Convert sample index to physical time: t = n / fs
t = n / fs          

# Calculate angular frequency (w1 = 2 * Pi * f1)
w1 = 2 * np.pi * f1 

# Generate the function: Cos(w1 t)
x = np.cos(w1 * t)  

# ==========================================
# 3. Calculate Frequency Domain (FFT)
# ==========================================
# Perform the Fast Fourier Transform
X_fft = np.fft.fft(x)

# Create the x-axis for the frequency domain (0 to fs)
freqs = np.arange(N) * (fs / N)

# Convert magnitude to Decibels (dB)
magnitude = np.abs(X_fft)
# Prevent log(0) errors by setting a tiny floor
magnitude[magnitude < 1e-10] = 1e-10 
# Normalize so the peak sits at 0 dB, matching standard signal analyzers
power_db = 20 * np.log10(magnitude / np.max(magnitude))

# ==========================================
# 4. Build the Dashboard Plot
# ==========================================
# Set up a large figure to hold our windows
fig = plt.figure(figsize=(12, 8))
fig.suptitle(f'Dynamical System: Cosine Wave ($f_1$={f1} Hz, $F_s$={fs} Hz)', fontsize=14)

# --- Window 1: Time Domain (Bottom Left) ---
ax_time = plt.subplot(2, 2, 3)
ax_time.plot(n, x, color='black', linewidth=1.5)
ax_time.set_title('Time Domain')
ax_time.set_xlabel('Sample number')
ax_time.set_ylabel('Amplitude')
# Zoom in to match the specific x-axis window from your screenshot
ax_time.set_xlim(14, 82) 
ax_time.set_ylim(-1.1, 1.1)
ax_time.grid(True, linestyle='--', alpha=0.7)

# --- Window 2: Frequency Domain (Bottom Right) ---
ax_freq = plt.subplot(2, 2, 4)
ax_freq.plot(freqs, power_db, color='black', linewidth=1)
ax_freq.set_title('Frequency Domain')
ax_freq.set_xlabel('Hz')
ax_freq.set_ylabel('dB')
ax_freq.set_xlim(0, fs)
# Add a horizontal threshold line like in the UI
ax_freq.axhline(-50, color='gray', linewidth=1) 
ax_freq.grid(True, linestyle='--', alpha=0.7)

# --- Window 3: Return Map (Top Right) ---
ax_return = plt.subplot(2, 2, 2)
# The Return Map plots X_n against X_{n+1}
# We use array slicing: x[:-1] is X_n, and x[1:] is X_{n+1}
ax_return.plot(x[:-1], x[1:], 'k.', markersize=2)
ax_return.set_title('Return Map')
ax_return.set_xlabel('$X_n$')
ax_return.set_ylabel('$X_{n+1}$')
ax_return.set_xlim(-1.1, 1.1)
ax_return.set_ylim(-1.1, 1.1)
# Force the aspect ratio to be perfectly square to see the true ellipse
ax_return.set_aspect('equal', 'box')
ax_return.grid(True, linestyle='--', alpha=0.7)

# Adjust layout so labels don't overlap and display
plt.tight_layout()
plt.subplots_adjust(top=0.9)
plt.show()


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons

# ==========================================
# 1. Initial Parameters
# ==========================================
init_f1 = 199       # Frequency in Hz
init_fs = 2703      # Sample Rate in Hz
init_N = 1024       # Number of Samples
init_r = 2.8        # Quadratic Map Parameter

# ==========================================
# 2. Setup the Figure and Axes
# ==========================================
fig = plt.figure(figsize=(14, 8))
fig.canvas.manager.set_window_title('Dynamical Systems Dashboard')
plt.subplots_adjust(left=0.08, right=0.95, top=0.92, bottom=0.35, wspace=0.3, hspace=0.4)

# Create the main plot axes
ax_time = plt.subplot(2, 2, 3)
ax_return = plt.subplot(2, 2, 2)
ax_freq = plt.subplot(2, 2, 4)

# Create axes for the interactive widgets at the bottom
ax_radio = plt.axes([0.08, 0.05, 0.15, 0.15], facecolor='lightgoldenrodyellow')
ax_N = plt.axes([0.35, 0.20, 0.5, 0.03], facecolor='lightgoldenrodyellow')
ax_f1 = plt.axes([0.35, 0.15, 0.5, 0.03], facecolor='lightgoldenrodyellow')
ax_fs = plt.axes([0.35, 0.10, 0.5, 0.03], facecolor='lightgoldenrodyellow')
ax_r = plt.axes([0.35, 0.05, 0.5, 0.03], facecolor='lightgoldenrodyellow')

# ==========================================
# 3. Create the Widgets
# ==========================================
radio = RadioButtons(ax_radio, ('Cosine Wave', 'Quadratic Map'))
slider_N = Slider(ax_N, 'Samples (N)', 50, 5000, valinit=init_N, valstep=1)
slider_f1 = Slider(ax_f1, 'Freq f1 (Hz)', 1, 1000, valinit=init_f1)
slider_fs = Slider(ax_fs, 'Sample Rate Fs', 100, 5000, valinit=init_fs)
slider_r = Slider(ax_r, 'Quadratic r', 0.0, 4.0, valinit=init_r)

# ==========================================
# 4. The Core Update Function
# ==========================================
def update(val=None):
    """This function runs every time a slider or button is clicked."""
    
    # Grab current values from widgets
    func_type = radio.value_selected
    N = int(slider_N.val)
    f1 = slider_f1.val
    fs = slider_fs.val
    r = slider_r.val

    # Clear old plots
    ax_time.clear()
    ax_freq.clear()
    ax_return.clear()

    # --------------------------------------
    # MODE 1: Cosine Wave (Continuous Time)
    # --------------------------------------
    if func_type == 'Cosine Wave':
        fig.suptitle(f'Cosine Wave ($f_1$={f1:.0f} Hz, $F_s$={fs:.0f} Hz)', fontsize=16)
        
        n = np.arange(N)
        t = n / fs
        x = np.cos(2 * np.pi * f1 * t)
        
        # Time Domain
        ax_time.plot(n, x, 'k-', lw=1)
        ax_time.set_xlim(0, min(100, N)) # Zoom in on first 100 samples
        ax_time.set_ylim(-1.1, 1.1)
        ax_time.set_title('Time Domain')
        ax_time.set_xlabel('Sample number')
        
        # Return Map
        ax_return.plot(x[:-1], x[1:], 'k.', markersize=2)
        ax_return.set_xlim(-1.1, 1.1)
        ax_return.set_ylim(-1.1, 1.1)
        ax_return.set_aspect('equal', 'box')
        ax_return.set_title('Return Map')
        ax_return.set_xlabel('$X_n$')
        ax_return.set_ylabel('$X_{n+1}$')
        
        # Frequency Domain
        X_fft = np.fft.fft(x)
        freqs = np.arange(N) * (fs / N)
        mag = np.abs(X_fft)
        mag[mag < 1e-10] = 1e-10 # Prevent log(0)
        db = 20 * np.log10(mag / np.max(mag))
        
        # Plot only up to the Nyquist limit (fs/2)
        half_N = N // 2
        ax_freq.plot(freqs[:half_N], db[:half_N], 'k-', lw=1)
        ax_freq.set_xlim(0, fs/2)
        ax_freq.set_ylim(-100, 5)
        ax_freq.set_title('Frequency Domain (dB)')
        ax_freq.set_xlabel('Hz')

    # --------------------------------------
    # MODE 2: Quadratic Map (Discrete Steps)
    # --------------------------------------
    elif func_type == 'Quadratic Map':
        fig.suptitle(f'Quadratic Map ($r$={r:.3f})', fontsize=16)
        
        x = np.zeros(N)
        x[0] = 0.1 # Initial condition
        for i in range(1, N):
            x[i] = r * x[i-1] * (1 - x[i-1])
            
        n = np.arange(N)
        
        # Time Domain
        ax_time.plot(n, x, 'k-', lw=1, marker='.', markersize=3)
        ax_time.set_xlim(0, min(100, N))
        ax_time.set_ylim(0, 1)
        ax_time.set_title('Time Domain (Iterations)')
        ax_time.set_xlabel('Iteration n')
        
        # Return Map
        # Draw the underlying parabola and y=x line for context!
        xs = np.linspace(0, 1, 200)
        ys = r * xs * (1 - xs)
        ax_return.plot(xs, ys, color='blue', alpha=0.3, label='y = r*x*(1-x)')
        ax_return.plot([0,1], [0,1], color='gray', linestyle='--', alpha=0.5, label='y = x')
        
        # Plot the actual Return Map dots
        ax_return.plot(x[:-1], x[1:], 'k.', markersize=5)
        ax_return.set_xlim(0, 1)
        ax_return.set_ylim(0, 1)
        ax_return.set_aspect('equal', 'box')
        ax_return.set_title('Return Map')
        ax_return.set_xlabel('$X_n$')
        ax_return.set_ylabel('$X_{n+1}$')
        ax_return.legend(loc='upper left', fontsize=8)
        
        # Frequency Domain (FFT of the discrete sequence)
        # We subtract the mean so the giant DC spike at 0Hz doesn't drown out the chaos
        X_fft = np.fft.fft(x - np.mean(x)) 
        mag = np.abs(X_fft)
        mag[mag < 1e-10] = 1e-10
        db = 20 * np.log10(mag / np.max(mag))
        
        half_N = N // 2
        ax_freq.plot(n[:half_N], db[:half_N], 'k-', lw=1)
        ax_freq.set_xlim(0, half_N)
        ax_freq.set_ylim(-80, 5)
        ax_freq.set_title('Frequency Domain (Periodicity)')
        ax_freq.set_xlabel('Frequency bin')

    # Re-draw the grids for the newly created plots
    ax_time.grid(True, linestyle='--', alpha=0.5)
    ax_return.grid(True, linestyle='--', alpha=0.5)
    ax_freq.grid(True, linestyle='--', alpha=0.5)

    fig.canvas.draw_idle()

# ==========================================
# 5. Connect Widgets and Initialize
# ==========================================
# Link the update function to all widgets
radio.on_clicked(update)
slider_N.on_changed(update)
slider_f1.on_changed(update)
slider_fs.on_changed(update)
slider_r.on_changed(update)

# Run it once to generate the initial graphs
update()

plt.show()


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons

# ==========================================
# 1. Initial Parameters
# ==========================================
init_N = 1024
init_f1 = 199       # Cosine Freq
init_fs = 2703      # Cosine Sample Rate
init_r = 2.8        # Quadratic Map Parameter
init_a = 1.4        # Henon parameter a
init_b = 0.3        # Henon parameter b

# ==========================================
# 2. Setup the Figure and Axes
# ==========================================
fig = plt.figure(figsize=(15, 9))
fig.canvas.manager.set_window_title('Ultimate Dynamical Systems Dashboard')
# Make room at the bottom for all the new sliders
plt.subplots_adjust(left=0.06, right=0.96, top=0.92, bottom=0.40, wspace=0.25, hspace=0.35)

# Create the 4 quadrants!
ax_bifurc = plt.subplot(2, 2, 1) # Top Left
ax_return = plt.subplot(2, 2, 2) # Top Right
ax_time   = plt.subplot(2, 2, 3) # Bottom Left
ax_freq   = plt.subplot(2, 2, 4) # Bottom Right

# Create axes for the interactive widgets (stacked neatly)
ax_radio = plt.axes([0.05, 0.05, 0.15, 0.25], facecolor='lightgoldenrodyellow')
ax_N  = plt.axes([0.30, 0.28, 0.6, 0.02], facecolor='lightcyan')
ax_f1 = plt.axes([0.30, 0.23, 0.6, 0.02], facecolor='lavender')
ax_fs = plt.axes([0.30, 0.18, 0.6, 0.02], facecolor='lavender')
ax_r  = plt.axes([0.30, 0.13, 0.6, 0.02], facecolor='honeydew')
ax_a  = plt.axes([0.30, 0.08, 0.6, 0.02], facecolor='mistyrose')
ax_b  = plt.axes([0.30, 0.03, 0.6, 0.02], facecolor='mistyrose')

# ==========================================
# 3. Create the Widgets
# ==========================================
radio = RadioButtons(ax_radio, ('Cosine Wave', 'Quadratic Map', 'Hénon Map'))
slider_N  = Slider(ax_N,  'Samples (N) [All]', 50, 5000, valinit=init_N, valstep=1)
slider_f1 = Slider(ax_f1, 'Freq f1 [Cosine]', 1, 1000, valinit=init_f1)
slider_fs = Slider(ax_fs, 'Sample Rate [Cosine]', 100, 5000, valinit=init_fs)
slider_r  = Slider(ax_r,  'Param r [Quad]', 2.0, 4.0, valinit=init_r)
slider_a  = Slider(ax_a,  'Param a [Henon]', 0.0, 1.45, valinit=init_a)
slider_b  = Slider(ax_b,  'Param b [Henon]', 0.0, 0.4, valinit=init_b)

# ==========================================
# 4. Fast Vectorized Bifurcation Generators
# ==========================================
def get_quad_bifurcation():
    R = np.linspace(2.5, 4.0, 600)
    X = np.ones(600) * 0.1
    for _ in range(200): # throw away transients
        X = R * X * (1 - X)
    R_plot, X_plot = [], []
    for _ in range(100): # collect stable points
        X = R * X * (1 - X)
        R_plot.extend(R)
        X_plot.extend(X)
    return R_plot, X_plot

def get_henon_bifurcation(b_val):
    A = np.linspace(0.0, 1.45, 600)
    X = np.zeros(600)
    Y = np.zeros(600)
    for _ in range(200): 
        X_new = 1 - A * X**2 + Y
        Y = b_val * X
        X = X_new
    A_plot, X_plot = [], []
    for _ in range(100): 
        X_new = 1 - A * X**2 + Y
        Y = b_val * X
        X = X_new
        A_plot.extend(A)
        X_plot.extend(X)
    return A_plot, X_plot

# Pre-calculate to save processing time
quad_R, quad_X = get_quad_bifurcation()

# ==========================================
# 5. The Core Update Function
# ==========================================
def update(val=None):
    func_type = radio.value_selected
    N = int(slider_N.val)
    f1, fs = slider_f1.val, slider_fs.val
    r = slider_r.val
    a, b = slider_a.val, slider_b.val

    for ax in [ax_bifurc, ax_time, ax_freq, ax_return]:
        ax.clear()

    # --------------------------------------
    # MODE 1: Cosine Wave
    # --------------------------------------
    if func_type == 'Cosine Wave':
        fig.suptitle(f'Cosine Wave ($f_1$={f1:.0f} Hz, $F_s$={fs:.0f} Hz)', fontsize=16)
        
        n = np.arange(N)
        t = n / fs
        x = np.cos(2 * np.pi * f1 * t)
        
        ax_bifurc.text(0.5, 0.5, 'Bifurcation N/A\nfor Continuous Systems', 
                       ha='center', va='center', fontsize=14, color='gray')
        ax_bifurc.set_xticks([])
        ax_bifurc.set_yticks([])

        ax_time.plot(n, x, 'k-', lw=1)
        ax_time.set_xlim(0, min(100, N)) 
        ax_time.set_title('Time Domain')
        ax_time.set_xlabel('Sample number')
        
        ax_return.plot(x[:-1], x[1:], 'k.', markersize=2)
        ax_return.set_xlim(-1.1, 1.1)
        ax_return.set_ylim(-1.1, 1.1)
        ax_return.set_title('Return Map ($X_n$ vs $X_{n+1}$)')
        
        X_fft = np.fft.fft(x)
        freqs = np.arange(N) * (fs / N)
        mag = np.abs(X_fft)
        mag[mag < 1e-10] = 1e-10 
        db = 20 * np.log10(mag / np.max(mag))
        
        ax_freq.plot(freqs[:N//2], db[:N//2], 'k-', lw=1)
        ax_freq.set_xlim(0, fs/2)
        ax_freq.set_ylim(-100, 5)
        ax_freq.set_title('Frequency Domain (dB)')

    # --------------------------------------
    # MODE 2: Quadratic Map
    # --------------------------------------
    elif func_type == 'Quadratic Map':
        fig.suptitle(f'Quadratic Map ($r$={r:.3f})', fontsize=16)
        
        x = np.zeros(N)
        x[0] = 0.1 
        for i in range(1, N):
            x[i] = r * x[i-1] * (1 - x[i-1])
            
        ax_bifurc.plot(quad_R, quad_X, 'k.', markersize=0.1, alpha=0.5)
        ax_bifurc.axvline(r, color='red', lw=2, alpha=0.7)
        ax_bifurc.set_title('Bifurcation Diagram (X vs r)')
        ax_bifurc.set_xlim(2.5, 4.0)
        ax_bifurc.set_ylim(0, 1)

        n = np.arange(N)
        ax_time.plot(n, x, 'k-', lw=1, marker='.', markersize=3)
        ax_time.set_xlim(0, min(100, N))
        ax_time.set_ylim(0, 1)
        ax_time.set_title('Time Domain (Iterations)')
        
        xs = np.linspace(0, 1, 200)
        ax_return.plot(xs, r * xs * (1 - xs), 'b-', alpha=0.3)
        ax_return.plot([0,1], [0,1], 'g--', alpha=0.3)
        ax_return.plot(x[:-1], x[1:], 'k.', markersize=5)
        ax_return.set_xlim(0, 1)
        ax_return.set_ylim(0, 1)
        ax_return.set_title('Return Map / Cobweb Space')
        
        X_fft = np.fft.fft(x - np.mean(x)) 
        mag = np.abs(X_fft)
        mag[mag < 1e-10] = 1e-10
        db = 20 * np.log10(mag / np.max(mag))
        ax_freq.plot(n[:N//2], db[:N//2], 'k-', lw=1)
        ax_freq.set_xlim(0, N//2)
        ax_freq.set_ylim(-80, 5)
        ax_freq.set_title('Frequency Domain (Periodicity)')

    # --------------------------------------
    # MODE 3: Hénon Map
    # --------------------------------------
    elif func_type == 'Hénon Map':
        fig.suptitle(f'Hénon Map ($a$={a:.3f}, $b$={b:.3f})', fontsize=16)
        
        x, y = np.zeros(N), np.zeros(N)
        for i in range(1, N):
            x[i] = 1 - a * x[i-1]**2 + y[i-1]
            y[i] = b * x[i-1]
            
        henon_A, henon_X = get_henon_bifurcation(b)
        ax_bifurc.plot(henon_A, henon_X, 'k.', markersize=0.1, alpha=0.5)
        ax_bifurc.axvline(a, color='red', lw=2, alpha=0.7)
        ax_bifurc.set_title(f'Bifurcation Diagram (X vs a) at b={b:.2f}')
        ax_bifurc.set_xlim(0, 1.45)
        ax_bifurc.set_ylim(-1.5, 1.5)

        n = np.arange(N)
        ax_time.plot(n, x, 'b-', lw=1, alpha=0.7, label='X')
        ax_time.plot(n, y, 'r-', lw=1, alpha=0.7, label='Y')
        ax_time.set_xlim(0, min(100, N))
        ax_time.set_title('Time Domain (X and Y)')
        ax_time.legend(loc='upper right', fontsize=8)
        
        # For 2D systems, plotting X vs Y reveals the Strange Attractor
        ax_return.plot(x, y, 'k.', markersize=1, alpha=0.5)
        ax_return.set_title('Phase Space / Strange Attractor (X vs Y)')
        
        X_fft = np.fft.fft(x - np.mean(x)) 
        mag = np.abs(X_fft)
        mag[mag < 1e-10] = 1e-10
        db = 20 * np.log10(mag / np.max(mag))
        ax_freq.plot(n[:N//2], db[:N//2], 'k-', lw=1)
        ax_freq.set_xlim(0, N//2)
        ax_freq.set_ylim(-80, 5)
        ax_freq.set_title('Frequency Domain (X sequence)')

    for ax in [ax_bifurc, ax_time, ax_freq, ax_return]:
        if func_type != 'Cosine Wave' or ax != ax_bifurc:
            ax.grid(True, linestyle='--', alpha=0.5)

    fig.canvas.draw_idle()

# ==========================================
# 6. Connect Widgets and Run
# ==========================================
radio.on_clicked(update)
slider_N.on_changed(update)
slider_f1.on_changed(update)
slider_fs.on_changed(update)
slider_r.on_changed(update)
slider_a.on_changed(update)
slider_b.on_changed(update)

update()
plt.show()


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons

# ==========================================
# 1. Initial Parameters
# ==========================================
init_N = 1024
init_f1 = 199       # Cosine Freq
init_fs = 2703      # Cosine Sample Rate
init_r = 2.8        # Quadratic Map Parameter
init_a = 1.4        # Henon parameter a
init_b = 0.3        # Henon parameter b

# ==========================================
# 2. Setup the Figure and Axes
# ==========================================
fig = plt.figure(figsize=(15, 9))
fig.canvas.manager.set_window_title('Ultimate Dynamical Systems Dashboard')
# Make room at the bottom for all the sliders
plt.subplots_adjust(left=0.06, right=0.96, top=0.92, bottom=0.40, wspace=0.25, hspace=0.35)

# Create the 4 quadrants
ax_bifurc = plt.subplot(2, 2, 1) # Top Left
ax_return = plt.subplot(2, 2, 2) # Top Right
ax_time   = plt.subplot(2, 2, 3) # Bottom Left
ax_freq   = plt.subplot(2, 2, 4) # Bottom Right

# Create axes for the interactive widgets (stacked neatly)
ax_radio = plt.axes([0.05, 0.05, 0.15, 0.25], facecolor='lightgoldenrodyellow')
ax_N  = plt.axes([0.30, 0.28, 0.6, 0.02], facecolor='lightcyan')
ax_f1 = plt.axes([0.30, 0.23, 0.6, 0.02], facecolor='lavender')
ax_fs = plt.axes([0.30, 0.18, 0.6, 0.02], facecolor='lavender')
ax_r  = plt.axes([0.30, 0.13, 0.6, 0.02], facecolor='honeydew')
ax_a  = plt.axes([0.30, 0.08, 0.6, 0.02], facecolor='mistyrose')
ax_b  = plt.axes([0.30, 0.03, 0.6, 0.02], facecolor='mistyrose')

# ==========================================
# 3. Create the Widgets
# ==========================================
radio = RadioButtons(ax_radio, ('Cosine Wave', 'Quadratic Map', 'Hénon Map'))
slider_N  = Slider(ax_N,  'Samples (N) [All]', 50, 5000, valinit=init_N, valstep=1)
slider_f1 = Slider(ax_f1, 'Freq f1 [Cosine]', 1, 1000, valinit=init_f1)
slider_fs = Slider(ax_fs, 'Sample Rate [Cosine]', 100, 5000, valinit=init_fs)
slider_r  = Slider(ax_r,  'Param r [Quad]', 2.0, 4.0, valinit=init_r)
slider_a  = Slider(ax_a,  'Param a [Henon]', 0.0, 1.45, valinit=init_a)
slider_b  = Slider(ax_b,  'Param b [Henon]', 0.0, 0.4, valinit=init_b)

# ==========================================
# 4. Fast Vectorized Bifurcation Generators
# ==========================================
def get_quad_bifurcation():
    R = np.linspace(2.5, 4.0, 600)
    X = np.ones(600) * 0.1
    for _ in range(200): # throw away transients
        X = R * X * (1 - X)
    R_plot, X_plot = [], []
    for _ in range(100): # collect stable points
        X = R * X * (1 - X)
        R_plot.extend(R)
        X_plot.extend(X)
    return R_plot, X_plot

def get_henon_bifurcation(b_val):
    A = np.linspace(0.0, 1.45, 600)
    X = np.zeros(600)
    Y = np.zeros(600)
    for _ in range(200): 
        X_new = 1 - A * X**2 + Y
        Y = b_val * X
        X = X_new
    A_plot, X_plot = [], []
    for _ in range(100): 
        X_new = 1 - A * X**2 + Y
        Y = b_val * X
        X = X_new
        A_plot.extend(A)
        X_plot.extend(X)
    return A_plot, X_plot

# Pre-calculate to save processing time
quad_R, quad_X = get_quad_bifurcation()

# ==========================================
# 5. The Core Update Function
# ==========================================
def update(val=None):
    func_type = radio.value_selected
    N = int(slider_N.val)
    f1, fs = slider_f1.val, slider_fs.val
    r = slider_r.val
    a, b = slider_a.val, slider_b.val

    for ax in [ax_bifurc, ax_time, ax_freq, ax_return]:
        ax.clear()

    # --------------------------------------
    # MODE 1: Cosine Wave
    # --------------------------------------
    if func_type == 'Cosine Wave':
        fig.suptitle(f'Cosine Wave ($f_1$={f1:.0f} Hz, $F_s$={fs:.0f} Hz)', fontsize=16)
        
        n = np.arange(N)
        t = n / fs
        x = np.cos(2 * np.pi * f1 * t)
        
        ax_bifurc.text(0.5, 0.5, 'Bifurcation N/A\nfor Continuous Systems', 
                       ha='center', va='center', fontsize=14, color='gray')
        ax_bifurc.set_xticks([])
        ax_bifurc.set_yticks([])

        ax_time.plot(n, x, 'k-', lw=1)
        ax_time.set_xlim(0, min(100, N)) 
        ax_time.set_title('Time Domain')
        ax_time.set_xlabel('Sample number')
        
        ax_return.plot(x[:-1], x[1:], 'k.', markersize=2)
        ax_return.set_xlim(-1.1, 1.1)
        ax_return.set_ylim(-1.1, 1.1)
        ax_return.set_title('Return Map ($X_n$ vs $X_{n+1}$)')
        
        # FFT for continuous time (measured in Hz)
        X_fft = np.fft.fft(x)
        half_N = N // 2
        freqs = np.arange(half_N + 1) * (fs / N)
        mag = np.abs(X_fft)
        mag[mag < 1e-10] = 1e-10 
        db = 20 * np.log10(mag / np.max(mag))
        
        ax_freq.plot(freqs, db[:half_N + 1], 'k-', lw=1)
        ax_freq.set_xlim(0, fs/2)
        ax_freq.set_ylim(-100, 5)
        ax_freq.set_title('Frequency Domain (dB)')
        ax_freq.set_xlabel('Hz')

    # --------------------------------------
    # MODE 2: Quadratic Map
    # --------------------------------------
    elif func_type == 'Quadratic Map':
        fig.suptitle(f'Quadratic Map ($r$={r:.3f})', fontsize=16)
        
        x = np.zeros(N)
        x[0] = 0.1 
        for i in range(1, N):
            x[i] = r * x[i-1] * (1 - x[i-1])
            
        ax_bifurc.plot(quad_R, quad_X, 'k.', markersize=0.1, alpha=0.5)
        ax_bifurc.axvline(r, color='red', lw=2, alpha=0.7)
        ax_bifurc.set_title('Bifurcation Diagram (X vs r)')
        ax_bifurc.set_xlim(2.5, 4.0)
        ax_bifurc.set_ylim(0, 1)

        n = np.arange(N)
        ax_time.plot(n, x, 'k-', lw=1, marker='.', markersize=3)
        ax_time.set_xlim(0, min(100, N))
        ax_time.set_ylim(0, 1)
        ax_time.set_title('Time Domain (Iterations)')
        ax_time.set_xlabel('Iteration Step')
        
        xs = np.linspace(0, 1, 200)
        ax_return.plot(xs, r * xs * (1 - xs), 'b-', alpha=0.3)
        ax_return.plot([0,1], [0,1], 'g--', alpha=0.3)
        ax_return.plot(x[:-1], x[1:], 'k.', markersize=5)
        ax_return.set_xlim(0, 1)
        ax_return.set_ylim(0, 1)
        ax_return.set_title('Return Map / Cobweb Space')
        ax_return.set_xlabel('$X_n$')
        ax_return.set_ylabel('$X_{n+1}$')
        
        # FFT for discrete sequence (Normalized Frequency)
        X_fft = np.fft.fft(x - np.mean(x)) 
        mag = np.abs(X_fft)
        mag[mag < 1e-10] = 1e-10
        db = 20 * np.log10(mag / np.max(mag))
        
        half_N = N // 2
        norm_freq = np.arange(half_N + 1) / N  
        
        ax_freq.plot(norm_freq, db[:half_N + 1], 'k-', lw=1)
        ax_freq.set_xlim(0, 0.5)
        ax_freq.set_ylim(-80, 5)
        ax_freq.set_title('Frequency Domain (Periodicity)')
        ax_freq.set_xlabel('Normalized Frequency (cycles/step)')

    # --------------------------------------
    # MODE 3: Hénon Map
    # --------------------------------------
    elif func_type == 'Hénon Map':
        fig.suptitle(f'Hénon Map ($a$={a:.3f}, $b$={b:.3f})', fontsize=16)
        
        x, y = np.zeros(N), np.zeros(N)
        for i in range(1, N):
            x[i] = 1 - a * x[i-1]**2 + y[i-1]
            y[i] = b * x[i-1]
            
        henon_A, henon_X = get_henon_bifurcation(b)
        ax_bifurc.plot(henon_A, henon_X, 'k.', markersize=0.1, alpha=0.5)
        ax_bifurc.axvline(a, color='red', lw=2, alpha=0.7)
        ax_bifurc.set_title(f'Bifurcation Diagram (X vs a) at b={b:.2f}')
        ax_bifurc.set_xlim(0, 1.45)
        ax_bifurc.set_ylim(-1.5, 1.5)

        n = np.arange(N)
        ax_time.plot(n, x, 'b-', lw=1, alpha=0.7, label='X')
        ax_time.plot(n, y, 'r-', lw=1, alpha=0.7, label='Y')
        ax_time.set_xlim(0, min(100, N))
        ax_time.set_title('Time Domain (X and Y)')
        ax_time.set_xlabel('Iteration Step')
        ax_time.legend(loc='upper right', fontsize=8)
        
        ax_return.plot(x, y, 'k.', markersize=1, alpha=0.5)
        ax_return.set_title('Phase Space / Strange Attractor (X vs Y)')
        ax_return.set_xlabel('X')
        ax_return.set_ylabel('Y')
        
        # FFT for discrete sequence (Normalized Frequency)
        X_fft = np.fft.fft(x - np.mean(x)) 
        mag = np.abs(X_fft)
        mag[mag < 1e-10] = 1e-10
        db = 20 * np.log10(mag / np.max(mag))
        
        half_N = N // 2
        norm_freq = np.arange(half_N + 1) / N  
        
        ax_freq.plot(norm_freq, db[:half_N + 1], 'k-', lw=1)
        ax_freq.set_xlim(0, 0.5)
        ax_freq.set_ylim(-80, 5)
        ax_freq.set_title('Frequency Domain (X sequence)')
        ax_freq.set_xlabel('Normalized Frequency (cycles/step)')

    # Add grids to active plots
    for ax in [ax_bifurc, ax_time, ax_freq, ax_return]:
        if func_type != 'Cosine Wave' or ax != ax_bifurc:
            ax.grid(True, linestyle='--', alpha=0.5)

    fig.canvas.draw_idle()

# ==========================================
# 6. Connect Widgets and Run
# ==========================================
radio.on_clicked(update)
slider_N.on_changed(update)
slider_f1.on_changed(update)
slider_fs.on_changed(update)
slider_r.on_changed(update)
slider_a.on_changed(update)
slider_b.on_changed(update)

# Initialize
update()
plt.show()



import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# ==========================================
# 1. Initial Parameters (The Frequencies)
# ==========================================
# These are the exact frequencies that build a Period-8 cycle
f_nyquist = 0.500      # Period-2 Ghost (Nyquist)
f_p4      = 0.250      # Period-4 Ghost
f_p8_fund = 0.125      # Period-8 Fundamental
f_p8_harm = 0.375      # Period-8 3rd Harmonic

# Initial Amplitudes (Start with just the pure Period-2 Nyquist wave)
init_A_nyquist = 1.0
init_A_p4      = 0.0
init_A_p8_fund = 0.0
init_A_p8_harm = 0.0

# Discrete time steps (n = 0 to 24, giving us exactly three 8-step blocks)
n = np.arange(25)

# ==========================================
# 2. Setup the Figure and Axes
# ==========================================
fig = plt.figure(figsize=(12, 9))
fig.canvas.manager.set_window_title('Period-8 Wave Synthesizer')
plt.subplots_adjust(left=0.1, right=0.95, top=0.92, bottom=0.35, hspace=0.4)

# Create the top chart (Frequency Domain) and bottom chart (Time Domain)
ax_freq = plt.subplot(2, 1, 1)
ax_time = plt.subplot(2, 1, 2)

# Create axes for the 4 sliders at the bottom
ax_s1 = plt.axes([0.15, 0.20, 0.75, 0.03], facecolor='lightcyan')
ax_s2 = plt.axes([0.15, 0.15, 0.75, 0.03], facecolor='lavender')
ax_s3 = plt.axes([0.15, 0.10, 0.75, 0.03], facecolor='honeydew')
ax_s4 = plt.axes([0.15, 0.05, 0.75, 0.03], facecolor='mistyrose')

# ==========================================
# 3. Create the Widgets
# ==========================================
s_nyquist = Slider(ax_s1, 'Amp: 0.500 (Period-2)', 0.0, 2.0, valinit=init_A_nyquist)
s_p4      = Slider(ax_s2, 'Amp: 0.250 (Period-4)', 0.0, 2.0, valinit=init_A_p4)
s_p8_fund = Slider(ax_s3, 'Amp: 0.125 (Period-8 Fund)', 0.0, 2.0, valinit=init_A_p8_fund)
s_p8_harm = Slider(ax_s4, 'Amp: 0.375 (Period-8 Harm)', 0.0, 2.0, valinit=init_A_p8_harm)

# ==========================================
# 4. The Core Update Function
# ==========================================
def update(val=None):
    # Grab current amplitudes from sliders
    A1 = s_nyquist.val
    A2 = s_p4.val
    A3 = s_p8_fund.val
    A4 = s_p8_harm.val

    ax_freq.clear()
    ax_time.clear()

    # --- TOP CHART: Frequency Spectrum ---
    frequencies = [f_p8_fund, f_p4, f_p8_harm, f_nyquist]
    amplitudes = [A3, A2, A4, A1]
    labels = ['1/8\n(0.125)', '1/4\n(0.250)', '3/8\n(0.375)', '1/2\n(0.500)']

    # We use a bar chart to clearly show the "spikes"
    bars = ax_freq.bar(frequencies, amplitudes, width=0.015, color=['green', 'blue', 'red', 'black'], alpha=0.7)
    
    ax_freq.set_xlim(0, 0.55)
    ax_freq.set_ylim(0, 2.2)
    ax_freq.set_xticks(frequencies)
    ax_freq.set_xticklabels(labels)
    ax_freq.set_title('Frequency Domain (The Ingredients)')
    ax_freq.set_ylabel('Amplitude')
    ax_freq.grid(True, linestyle='--', alpha=0.5, axis='y')

    # --- BOTTOM CHART: Time Domain (Sum of Cosines) ---
    # Mathematically sum the 4 discrete cosine waves
    y = (A1 * np.cos(2 * np.pi * f_nyquist * n) + 
         A2 * np.cos(2 * np.pi * f_p4 * n) + 
         A3 * np.cos(2 * np.pi * f_p8_fund * n) + 
         A4 * np.cos(2 * np.pi * f_p8_harm * n))

    ax_time.plot(n, y, 'k-', linewidth=1.5, marker='o', markersize=6, markerfacecolor='orange')
    
    # Draw vertical lines to explicitly bracket the "8-step containers"
    for i in range(0, 25, 8):
        ax_time.axvline(i, color='gray', linestyle='--', alpha=0.8, linewidth=2)
        if i < 24:
            ax_time.text(i + 4, 3.5, f'8-Step Block', ha='center', va='center', color='gray', fontsize=10)

    ax_time.set_xlim(0, 24)
    ax_time.set_ylim(-4, 4)
    ax_time.set_xticks(n)
    ax_time.set_title('Time Domain (The Resulting Period-8 Shape)')
    ax_time.set_xlabel('Discrete Step (n)')
    ax_time.set_ylabel('Total Amplitude')
    ax_time.grid(True, linestyle='--', alpha=0.3)

    fig.canvas.draw_idle()

# ==========================================
# 5. Connect Widgets and Run
# ==========================================
s_nyquist.on_changed(update)
s_p4.on_changed(update)
s_p8_fund.on_changed(update)
s_p8_harm.on_changed(update)

# Run once to initialize the plots
update()

plt.show()


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons

# ==========================================
# 1. Setup Time and Frequencies
# ==========================================
# We need TWO time arrays: 
# One very dense array to draw the smooth, continuous waves
t_cont = np.linspace(0, 8, 500) 
# One integer array to draw the discrete, step-by-step math
n_disc = np.arange(9)           

# The four frequencies of a Period-8 cycle
f1 = 0.125 # 1/8 (Fundamental)
f2 = 0.250 # 1/4 (2nd Harmonic / Period-4 Ghost)
f3 = 0.375 # 3/8 (3rd Harmonic)
f4 = 0.500 # 1/2 (Nyquist / Period-2 Ghost)

# Calculate the continuous waves for the top chart
w1_c = np.cos(2 * np.pi * f1 * t_cont)
w2_c = np.cos(2 * np.pi * f2 * t_cont)
w3_c = np.cos(2 * np.pi * f3 * t_cont)
w4_c = np.cos(2 * np.pi * f4 * t_cont)

# Calculate the discrete points for the bottom chart
w1_d = np.cos(2 * np.pi * f1 * n_disc)
w2_d = np.cos(2 * np.pi * f2 * n_disc)
w3_d = np.cos(2 * np.pi * f3 * n_disc)
w4_d = np.cos(2 * np.pi * f4 * n_disc)

# ==========================================
# 2. Setup Figure and Subplots
# ==========================================
fig = plt.figure(figsize=(12, 8))
fig.canvas.manager.set_window_title('Harmonics in an 8-Step Window')
# Make room on the left for the checkboxes
plt.subplots_adjust(left=0.25, right=0.95, top=0.9, bottom=0.1, hspace=0.35)

ax_top = plt.subplot(2, 1, 1)
ax_bot = plt.subplot(2, 1, 2)

# ==========================================
# 3. Plot Top Chart (Continuous Waves)
# ==========================================
# We save the line objects (l1, l2...) so we can hide/show them later
l1, = ax_top.plot(t_cont, w1_c, color='green', lw=2, label='1/8 (1 cycle)')
l2, = ax_top.plot(t_cont, w2_c, color='blue', lw=2, label='1/4 (2 cycles)')
l3, = ax_top.plot(t_cont, w3_c, color='red', lw=2, label='3/8 (3 cycles) <- The 3rd Harmonic')
l4, = ax_top.plot(t_cont, w4_c, color='black', lw=2, label='1/2 (4 cycles)')

ax_top.set_xlim(0, 8)
ax_top.set_ylim(-1.2, 1.2)
ax_top.set_title('Individual Continuous Harmonics (0 to 8 steps)')
ax_top.grid(True, linestyle='--', alpha=0.6)
ax_top.legend(loc='upper right', fontsize=9)

# ==========================================
# 4. Plot Bottom Chart (Discrete Sum)
# ==========================================
# Initial state: start with all waves active
sum_d = w1_d + w2_d + w3_d + w4_d
line_sum, = ax_bot.plot(n_disc, sum_d, 'k-', marker='o', markersize=8, markerfacecolor='orange', lw=2)

ax_bot.set_xlim(0, 8)
ax_bot.set_ylim(-4.5, 4.5)
ax_bot.set_title('The Resulting Shape (Discrete Sum of Active Waves)')
ax_bot.set_xlabel('Discrete Step (n)')
ax_bot.grid(True, linestyle='--', alpha=0.6)
ax_bot.set_xticks(n_disc)

# ==========================================
# 5. Create the Checkbox Widget
# ==========================================
ax_check = plt.axes([0.02, 0.45, 0.16, 0.2], facecolor='lightgoldenrodyellow')
labels = ['1/8 (Fund)', '1/4 (2nd Harm)', '3/8 (3rd Harm)', '1/2 (Nyquist)']
# Initialize checkboxes to 'True' (checked)
visibility = [True, True, True, True] 
check = CheckButtons(ax_check, labels, visibility)

# ==========================================
# 6. The Update Logic
# ==========================================
def update(label):
    # Toggle the visibility of the continuous lines in the top graph
    if label == '1/8 (Fund)': l1.set_visible(not l1.get_visible())
    elif label == '1/4 (2nd Harm)': l2.set_visible(not l2.get_visible())
    elif label == '3/8 (3rd Harm)': l3.set_visible(not l3.get_visible())
    elif label == '1/2 (Nyquist)': l4.set_visible(not l4.get_visible())
    
    # Recalculate the discrete sum based ONLY on what is currently visible
    new_sum = np.zeros(9)
    if l1.get_visible(): new_sum += w1_d
    if l2.get_visible(): new_sum += w2_d
    if l3.get_visible(): new_sum += w3_d
    if l4.get_visible(): new_sum += w4_d
    
    # Update the bottom plot data
    line_sum.set_ydata(new_sum)
    fig.canvas.draw_idle()

check.on_clicked(update)

plt.show()


import numpy as np
import matplotlib.pyplot as plt

# 1. Setup the parameters
N_steps = 1000         # How many steps to analyze
N_transients = 200     # How many initial steps to throw away
r_values = np.linspace(2.5, 4.0, 1000) # The 'energy pedal' from stable to chaos
lyapunov = np.zeros(len(r_values))     # Array to store our error analysis results

# 2. Loop through every single r value
for j, r in enumerate(r_values):
    x = 0.1 # Starting point
    
    # Let the marble settle into the bowl (discard transients)
    for _ in range(N_transients):
        x = r * x * (1 - x)
        
    # 3. THE ERROR ANALYSIS (The Calculus Method)
    # We will accumulate the logarithmic stretch factor here
    log_derivative_sum = 0.0 
    
    for _ in range(N_steps):
        # Move the system forward one step
        x = r * x * (1 - x)
        
        # Calculate the derivative: f'(x) = r - 2rx
        derivative = r - 2 * r * x
        
        # Prevent math errors if the derivative is exactly 0
        if derivative == 0:
            derivative = 1e-10 
            
        # Add the log of the stretch factor to our running total
        log_derivative_sum += np.log(abs(derivative))
        
    # 4. Calculate the average exponent for this specific r value
    lyapunov[j] = log_derivative_sum / N_steps

# 5. Plot the Error Analysis
plt.figure(figsize=(10, 5))
plt.plot(r_values, lyapunov, 'k-', lw=1)
plt.axhline(0, color='red', linestyle='--', lw=2) # The Chaos Threshold!
plt.title('Error Analysis: Lyapunov Exponent of the Quadratic Map')
plt.xlabel('Parameter r (Energy)')
plt.ylabel('Lyapunov Exponent (λ)')
plt.grid(True, alpha=0.3)
plt.fill_between(r_values, lyapunov, 0, where=(lyapunov > 0), color='red', alpha=0.3, label='Chaos (Error Explodes)')
plt.fill_between(r_values, lyapunov, 0, where=(lyapunov <= 0), color='blue', alpha=0.3, label='Stable (Error Forgiven)')
plt.legend()
plt.show()



import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. Math for the 1D Quadratic Map
# ==========================================
print("Calculating Quadratic Map Lyapunov Exponents...")
N_steps = 1000
N_transients = 200

# Sweep energy parameter 'r' from 2.5 to 4.0
r_vals = np.linspace(2.5, 4.0, 1500)
lyap_quad = np.zeros(len(r_vals))

for i, r in enumerate(r_vals):
    x = 0.1 # Starting point
    
    # Discard transients
    for _ in range(N_transients):
        x = r * x * (1 - x)
        
    log_derivative_sum = 0.0
    for _ in range(N_steps):
        x = r * x * (1 - x)
        deriv = r - 2 * r * x
        
        # Prevent log(0)
        if deriv == 0: deriv = 1e-10 
            
        log_derivative_sum += np.log(abs(deriv))
        
    lyap_quad[i] = log_derivative_sum / N_steps

# ==========================================
# 2. Math for the 2D Hénon Map (Maximal Lyapunov)
# ==========================================
print("Calculating Hénon Map Lyapunov Exponents...")
b = 0.3
# Sweep chaotic parameter 'a' from 0.0 to 1.4
a_vals = np.linspace(0.0, 1.4, 1500)
lyap_henon = np.zeros(len(a_vals))

for i, a in enumerate(a_vals):
    x, y = 0.1, 0.1 # Starting coordinates
    
    # The "Tangent Vector" (a virtual arrow to measure stretching)
    u, v = 1.0, 0.0 
    
    # Discard transients
    for _ in range(N_transients):
        x_next = 1 - a * x**2 + y
        y_next = b * x
        x, y = x_next, y_next
        
    log_stretch_sum = 0.0
    for _ in range(N_steps):
        # 1. Multiply the Tangent Vector by the Jacobian Matrix at the current point
        # J = [[-2ax, 1], [b, 0]]
        u_next = (-2 * a * x * u) + (1.0 * v)
        v_next = (b * u) + (0.0 * v)
        
        # 2. Measure how much the arrow stretched (its length)
        stretch = np.sqrt(u_next**2 + v_next**2)
        
        if stretch > 0:
            log_stretch_sum += np.log(stretch)
            # 3. Normalize the arrow back to length 1 to prevent memory overflow!
            u = u_next / stretch
            v = v_next / stretch
        else:
            u, v = 1.0, 0.0
            
        # 4. Move the actual Hénon math forward one step
        x_next = 1 - a * x**2 + y
        y_next = b * x
        x, y = x_next, y_next
        
    lyap_henon[i] = log_stretch_sum / N_steps

print("Calculations complete. Drawing graphs...")

# ==========================================
# 3. Plotting the Graphs
# ==========================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
fig.canvas.manager.set_window_title('Global Error: Lyapunov Exponents')

# --- Plot 1: Quadratic Map ---
ax1.plot(r_vals, lyap_quad, 'k-', lw=0.8)
ax1.axhline(0, color='red', linestyle='--', lw=2, label="Chaos Threshold (λ=0)")
ax1.fill_between(r_vals, lyap_quad, 0, where=(lyap_quad > 0), color='red', alpha=0.3)
ax1.fill_between(r_vals, lyap_quad, 0, where=(lyap_quad <= 0), color='blue', alpha=0.3)

ax1.set_xlim(2.5, 4.0)
ax1.set_ylim(-3, 1)
ax1.set_title('Quadratic Map: Lyapunov Exponent', fontsize=14)
ax1.set_xlabel('Parameter r (Energy)', fontsize=12)
ax1.set_ylabel('Lyapunov Exponent (λ)', fontsize=12)
ax1.grid(True, alpha=0.3)
ax1.legend(loc='lower left')

# --- Plot 2: Hénon Map ---
ax2.plot(a_vals, lyap_henon, 'k-', lw=0.8)
ax2.axhline(0, color='red', linestyle='--', lw=2, label="Chaos Threshold (λ=0)")
ax2.fill_between(a_vals, lyap_henon, 0, where=(lyap_henon > 0), color='red', alpha=0.3)
ax2.fill_between(a_vals, lyap_henon, 0, where=(lyap_henon <= 0), color='blue', alpha=0.3)

# Add a marker for the classic chaotic parameters
ax2.plot(1.4, lyap_henon[-1], 'ro', markersize=8, label='Classic Hénon (a=1.4)')

ax2.set_xlim(0.0, 1.4)
ax2.set_ylim(-1.5, 0.6)
ax2.set_title('Hénon Map (b=0.3): Max Lyapunov Exponent', fontsize=14)
ax2.set_xlabel('Parameter a', fontsize=12)
ax2.set_ylabel('Lyapunov Exponent (λ₁)', fontsize=12)
ax2.grid(True, alpha=0.3)
ax2.legend(loc='lower left')

plt.tight_layout()
plt.show()


