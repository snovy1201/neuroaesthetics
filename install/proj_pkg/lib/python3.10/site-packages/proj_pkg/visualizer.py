import rclpy
from rclpy.node import Node
from mocap_optitrack_interfaces.msg import RigidBodyArray

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider
import time
from collections import deque

# CONFIG
TRACK_ID = 4  # rigid body ID to track
PROX_THRESH = 0.05 # 5 cm threshold for brush
MAX_POINTS = 1000

# SUBSCRIBER NODE
class MocapSubscriber(Node):
    def __init__(self):
        super().__init__('mocap_subscriber')
        self.subscription = self.create_subscription(
            RigidBodyArray,
            '/mocap_rigid_bodies',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        
        # Store coordinates
        self.xs = deque(maxlen=MAX_POINTS)
        self.zs = deque(maxlen=MAX_POINTS)
        
        # ADD THESE LINES - Current position for display
        self.current_x = 0.0
        self.current_z = 0.0
        self.current_time = 0.0
        
        # Optional: store additional info for debugging
        self.timestamps = deque(maxlen=MAX_POINTS)
        
        self.get_logger().info(f'Mocap subscriber initialized, tracking ID {TRACK_ID}')

    def listener_callback(self, msg):
        # Iterate through each rigid body in the array
        for rb in msg.rigid_bodies:
            # Extract the attributes you're interested in
            rigid_body_id = rb.id
            is_valid = rb.valid
            is_stroke = rb.is_stroke
            proximity = rb.proximity
            
            # Extract coordinates from pose_stamped
            x = rb.pose_stamped.pose.position.x
            y = rb.pose_stamped.pose.position.y
            z = rb.pose_stamped.pose.position.z
            
            # Extract the timestamp
            timestamp = rb.pose_stamped.header.stamp
            timestamp_float = timestamp.sec + timestamp.nanosec * 1e-9
            
            # Log the information
            self.get_logger().info(
                f'ID: {rigid_body_id}, Valid: {is_valid}, '
                f'Position: ({x:.3f}, {y:.3f}, {z:.3f}), '
                f'Stroke: {is_stroke}, Proximity: {proximity:.3f}'
            )
                    
            if is_valid and (rigid_body_id == TRACK_ID):
                # UPDATE THESE - Update current position
                self.current_x = x
                self.current_z = z
                self.current_time = timestamp_float
            
                if (y < PROX_THRESH) and (y > -PROX_THRESH):
                    self.xs.append(x)
                    self.zs.append(z)
                    self.timestamps.append(timestamp_float)


def main(args=None):
    rclpy.init(args=args)
    mocap_subscriber = MocapSubscriber()
    
    # Set up plot
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.15)
    scat = ax.scatter([], [], s=8, c='blue', alpha=0.6)
    ax.set_title(f"Mocap XZ Projection (Brush ID {TRACK_ID})")
    ax.set_xlabel("X (m)")
    ax.set_ylabel("Z (m)")
    ax.set_aspect("equal")
    ax.set_xlim(-2, 2)  # Adjust based on your workspace
    ax.set_ylim(-2, 2)
    ax.grid(True, alpha=0.3)
    
    # Add text annotations
    coord_text = ax.text(0.02, 0.98, '', transform=ax.transAxes,
                         verticalalignment='top',
                         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8),
                         fontsize=10)
    
    time_text = ax.text(0.02, 0.88, '', transform=ax.transAxes,
                        verticalalignment='top',
                        bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8),
                        fontsize=10)
    
    point_count_text = ax.text(0.98, 0.98, '', transform=ax.transAxes,
                               verticalalignment='top',
                               horizontalalignment='right',
                               bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8),
                               fontsize=10)
    
    def update_plot(frame):
        # Process ROS callbacks
        rclpy.spin_once(mocap_subscriber, timeout_sec=0.001)
        
        # Update scatter plot
        if len(mocap_subscriber.xs) > 0:
            scat.set_offsets(list(zip(mocap_subscriber.xs, mocap_subscriber.zs)))
            
            # Auto-adjust limits with margin
            if len(mocap_subscriber.xs) > 10:
                margin = 0.2
                x_min, x_max = min(mocap_subscriber.xs), max(mocap_subscriber.xs)
                z_min, z_max = min(mocap_subscriber.zs), max(mocap_subscriber.zs)
                
                ax.set_xlim(x_min - margin, x_max + margin)
                ax.set_ylim(z_min - margin, z_max + margin)
                
        # Update text displays
        coord_text.set_text(f'X: {mocap_subscriber.current_x:.4f} m\nZ: {mocap_subscriber.current_z:.4f} m')
        time_text.set_text(f'Time: {mocap_subscriber.current_time:.3f} s')
        point_count_text.set_text(f'Points: {len(mocap_subscriber.xs)}')
        
        return scat, coord_text, time_text, point_count_text
            
    # Animate at ~30 FPS
    ani = FuncAnimation(fig, update_plot, interval=33, blit=True)
    
    try:
        plt.show()
    except KeyboardInterrupt:
        pass
    finally:
        mocap_subscriber.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()