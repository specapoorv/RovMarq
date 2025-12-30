

import cv2
import numpy as np
import os

# ======================
# CONFIG
# ======================
NEEDLE_PATH = "/home/specapoorv/RovMarq/offline_map/rover_vector.png"
OUTER_PATH  = "/home/specapoorv/RovMarq/offline_map/compass.png"
OUTPUT_DIR  = "/home/specapoorv/RovMarq/offline_map/output2"
STEP_DEG    = 10          # 0,10,20..360
NEEDLE_SCALE = 1.0    # <-- CHANGE THIS (0.3, 0.5, 1.0, etc)

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ======================
# LOAD IMAGES
# ======================
needle = cv2.imread(NEEDLE_PATH, cv2.IMREAD_UNCHANGED)
outer  = cv2.imread(OUTER_PATH,  cv2.IMREAD_UNCHANGED)

assert needle is not None and outer is not None
assert needle.shape[2] == 4 and outer.shape[2] == 4

H, W = outer.shape[:2]

# ======================
# SCALE NEEDLE (NO STRETCH)
# ======================
nh, nw = needle.shape[:2]
new_w = int(nw * NEEDLE_SCALE)
new_h = int(nh * NEEDLE_SCALE)

needle = cv2.resize(needle, (new_w, new_h), interpolation=cv2.INTER_AREA)
nh, nw = needle.shape[:2]

needle_center = (nw // 2, nh // 2)
outer_center  = (W // 2, H // 2)

# ======================
# ROTATE NEEDLE (NO CLIP)
# ======================
def rotate_needle(img, angle):
    diag = int(np.ceil(np.sqrt(nw*nw + nh*nh)))
    canvas = np.zeros((diag, diag, 4), dtype=np.uint8)

    cx = cy = diag // 2
    canvas[cy-nh//2:cy+nh//2, cx-nw//2:cx+nw//2] = img

    M = cv2.getRotationMatrix2D((cx, cy), -angle, 1.0)
    return cv2.warpAffine(
        canvas, M, (diag, diag),
        flags=cv2.INTER_LINEAR,
        borderMode=cv2.BORDER_TRANSPARENT
    )

# ======================
# GENERATE OUTPUT
# ======================
for angle in range(0, 361, STEP_DEG):
    rotated = rotate_needle(needle, angle)

    out = outer.copy()

    rh, rw = rotated.shape[:2]
    y = outer_center[1] - rh // 2
    x = outer_center[0] - rw // 2

    out[y:y+rh, x:x+rw] = rotated

    cv2.imwrite(f"{OUTPUT_DIR}/rover_{angle:03d}.png", out)
    print("saved", angle)

print("done.")

