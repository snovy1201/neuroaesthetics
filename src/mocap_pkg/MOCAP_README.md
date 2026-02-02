# MoCap OptiTrack Package

This package provides ROS2 integration for OptiTrack motion capture system using the NatNet protocol.

## Quick Start

**Run the MoCap publisher:**

```bash
cd ~/Documents/aura_code
source install/setup.bash
ros2 run mocap_optitrack_client mocap_optitrack_client --ros-args --params-file src/mocap_pkg/mocap_optitrack_client/config/natnetclient.yaml
```

## Published Topics

- `/mocap_rigid_bodies` - Motion capture rigid body data

## Prerequisites

1. **Motive OptiTrack software** running on the mocap computer
2. **Network connection** to the mocap system (default: 192.168.1.59)
3. **Firewall disabled** or ports 1510/1511 open
4. **Data streaming enabled** in Motive with correct axis configuration (Z-up)

## Configuration

Edit configuration file: `mocap_optitrack_client/config/natnetclient.yaml`

Key settings:
- `server_address`: IP of the Motive computer (default: "192.168.1.59")
- `connection_type`: 0 = multicast, 1 = unicast
- `pub_topic`: "mocap_rigid_bodies"

## Verify It's Working

```bash
# Check if topic is publishing
ros2 topic list | grep mocap

# Echo the data
ros2 topic echo /mocap_rigid_bodies

# Check publishing rate
ros2 topic hz /mocap_rigid_bodies
```

## Rebuild
```bash
colcon build --symlink-install --packages-select mocap_optitrack_client
```

## Integration with Training Data Collection

Once the mocap publisher is running, the training data collection system will automatically record mocap data in each batch.
