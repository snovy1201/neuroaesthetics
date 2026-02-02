# NeuroAesthetics
Local repository for motion capture and trajectory projection pipeline for neuroaesthetic project.

This project examines whether human‑made artwork can be reliably distinguished from robot‑generated art in an era where generative AI can closely imitate human creativity. The study tests the hypothesis that both the final painting and the underlying production process contain uniquely human signatures that trained art experts can recognize. To evaluate this, experts will view human and robot paintings, as well as movement‑only reconstructions of the painting process, and classify each as human or robotic.

## Features
- Motion capture ROS2 publisher (Optitrack)
- Real-time trajectory projection


# MoCap Real-Time Visualization

Real-time visualization of motion capture data from OptiTrack system, displaying brush position on an XZ plane with proximity-based stroke detection.

## Prerequisites

- ROS 2 Humble
- Python 3.10
- OptiTrack Motive streaming to network
- System packages:
```bash
  sudo apt update
  sudo apt install python3-matplotlib python3-numpy
```

## Installation

1. **Clone or navigate to your workspace:**
```bash
   cd ~/neuroaesthetics
```

2. **Build the packages:**
```bash
   colcon build --packages-select mocap_optitrack_client mocap_optitrack_interfaces proj_pkg
```

3. **Source the workspace:**
```bash
   source install/setup.bash
```

## Configuration

Edit the configuration file to match your OptiTrack setup:
```bash
nano src/mocap_pkg/mocap_optitrack_client/config/natnetclient.yaml
```

Key settings:
- **Server IP**: Set to your OptiTrack workstation IP (default: `192.168.1.59`)
- Make sure both devices (Linux and Windows running Motive) are connected to the AURA_Net network

### Visualizer Configuration

Edit `src/proj_pkg/proj_pkg/visualizer.py` to customize:
```python
TRACK_ID = 4          # Rigid body ID to track
PROX_THRESH = 0.05    # Proximity threshold in meters (5cm)
MAX_POINTS = 1000     # Maximum trajectory points to display
```

## Deployment

### Option 1: Launch Everything Together (Recommended)

If you've added the visualizer to your launch file:
```bash
cd ~/neuroaesthetics
source install/setup.bash
ros2 launch mocap_pkg launch_y_up.launch.py
```

### Option 2: Launch Components Separately

**Terminal 1 - Start MoCap Publisher:**
```bash
cd ~/neuroaesthetics/src/mocap_pkg
source ~/neuroaesthetics/install/setup.bash
ros2 launch launch/launch_y_up.py
```

**Terminal 2 - Start Visualizer:**
```bash
source /opt/ros/humble/setup.bash
source ~/neuroaesthetics/install/setup.bash
ros2 run proj_pkg mocap_visualizer
```

Or run directly:
```bash
~/neuroaesthetics/install/proj_pkg/bin/mocap_visualizer
```

## Verification

Check that data is flowing:
```bash
# List available topics
ros2 topic list

# Echo mocap data
ros2 topic echo /mocap_rigid_bodies

# Check topic info
ros2 topic info /mocap_rigid_bodies
```

## Troubleshooting

### Visualization window doesn't appear
- Ensure matplotlib is installed: `pip3 install --user matplotlib`
- Check for NumPy compatibility issues
- If using a virtual environment, deactivate it first

### No data appearing / Time stuck at 0.0
- Verify `TRACK_ID` matches an actual rigid body ID in Motive
- Check that rigid body is marked as valid in OptiTrack
- Temporarily remove proximity check to see all points:
```python
  # Comment out the proximity condition
  # if (y < PROX_THRESH) and (y > -PROX_THRESH):
  self.xs.append(x)
  self.zs.append(z)
```

### Package not found errors
- Ensure you've sourced the workspace: `source install/setup.bash`
- Rebuild packages: `colcon build`
- Check workspace structure matches:
```
  ~/neuroaesthetics/
  ├── src/
  │   ├── mocap_pkg/
  │   │   ├── mocap_optitrack_client/
  │   │   ├── mocap_optitrack_interfaces/
  │   │   └── launch/
  │   └── proj_pkg/
```

### Network connection issues
- Verify OptiTrack workstation IP: `ping 192.168.4.31`
- Check firewall settings (disable Windows Defender on OptiTrack machine)
- Ensure Motive is broadcasting on the correct network interface

## Display Information

The visualization shows:
- **Blue dots**: Brush trajectory (XZ plane)
- **Top-left box**: Current X, Y, Z coordinates
- **Middle-left box**: Timestamp
- **Top-right box**: Number of recorded points

Points are only recorded when the brush is within the proximity threshold (Y coordinate between -PROX_THRESH and +PROX_THRESH).

## Development

To modify and rebuild:
```bash
# Edit the visualizer
nano ~/neuroaesthetics/src/proj_pkg/proj_pkg/visualizer.py

# Rebuild
cd ~/neuroaesthetics
colcon build --packages-select proj_pkg

# Source and run
source install/setup.bash
ros2 run proj_pkg mocap_visualizer
```

## Authors

- Cindy Yang (@snovy1201)

## License

Apache License 2.0


