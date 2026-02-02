import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider
from rosbags.highlevel import AnyReader
from rosbags.typesys import get_typestore, Stores, get_types_from_msg
from pathlib import Path
import time

# ----------------------------
# CONFIG
# ----------------------------
BAG_FOLDER = Path("testHumanTrajectory")
TOPIC = "/mocap_rigid_bodies"
TRACK_ID = 4  # rigid body ID to track

# ----------------------------
# Load ROS 2 + custom msg types
# ----------------------------
typestore = get_typestore(Stores.ROS2_HUMBLE)
CUSTOM_MSG_DIR = Path("/home/snovyang/AURA/src/mocap_pkg/mocap_optitrack_interfaces/msg")
custom_msg_defs = {}

for msgfile in CUSTOM_MSG_DIR.glob("*.msg"):
    text = msgfile.read_text()
    typename = f"{msgfile.parent.parent.name}/msg/{msgfile.stem}"
    custom_msg_defs.update(get_types_from_msg(text, typename))

typestore.register(custom_msg_defs)

# ----------------------------
# Load rosbag
# ----------------------------
timestamps, xs, zs = [], [], []

with AnyReader([BAG_FOLDER], default_typestore=typestore) as reader:
    connections = [c for c in reader.connections if c.topic == TOPIC]
    if not connections:
        print("Topic not found!")
        exit()
    for conn, t, rawdata in reader.messages(connections=connections):
        msg = reader.deserialize(rawdata, conn.msgtype)
        for body in msg.rigid_bodies:
            if not body.valid or body.id != TRACK_ID:
                continue
            pos = body.pose_stamped.pose.position
            xs.append(pos.x)
            zs.append(pos.z)
            timestamps.append(t)

if len(xs) == 0:
    print("No points loaded for this rigid body")
    exit()

# Normalize timestamps to seconds
timestamps = np.array(timestamps)
timestamps = (timestamps - timestamps[0]) / 1e9
xs = np.array(xs)
zs = np.array(zs)

# ----------------------------
# Visualization
# ----------------------------
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.15)  # space for centered slider
scat = ax.scatter([], [], s=8)
ax.set_title(f"Mocap XZ Projection (RigidBody ID {TRACK_ID})")
ax.set_xlabel("X")
ax.set_ylabel("Z")
ax.set_aspect("equal")
ax.set_xlim(xs.min() - 0.1, xs.max() + 0.1)
ax.set_ylim(zs.min() - 0.1, zs.max() + 0.1)

# Playback controls
frame_idx = [0]

# ----------------------------
# Animation update
# ----------------------------
def update(_):
    i = frame_idx[0]
    scat.set_offsets(np.c_[xs[:i+1], zs[:i+1]])
    return scat,

# ----------------------------
# Slider callback
# ----------------------------
def slider_update(val):
    idx = (np.abs(timestamps - slider.val)).argmin()
    frame_idx[0] = idx
    scat.set_offsets(np.c_[xs[:idx+1], zs[:idx+1]])
    fig.canvas.draw_idle()

# ----------------------------
# Add centered slider
# ----------------------------
slider_width = 0.6  # 60% of figure width
slider_left = (1 - slider_width) / 2
ax_slider = plt.axes([slider_left, 0.05, slider_width, 0.03])
slider = Slider(ax_slider, 'Time (s)', timestamps[0], timestamps[-1], valinit=timestamps[0])
slider.on_changed(slider_update)

ani = FuncAnimation(fig, update, frames=len(timestamps), interval=1, repeat=False)
plt.show()
