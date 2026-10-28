
import cv2
import numpy as np


def detect_changes(image_before, image_after, threshold_value=30):
    if image_before.shape != image_after.shape:
        raise ValueError("Images must have matching dimensions and channels.")

    gray_before = cv2.cvtColor(image_before, cv2.COLOR_RGB2GRAY)
    gray_after = cv2.cvtColor(image_after, cv2.COLOR_RGB2GRAY)

    diff = cv2.absdiff(gray_before, gray_after)

    _, change_mask = cv2.threshold(
        diff, threshold_value, 255, cv2.THRESH_BINARY
    )

    kernel = np.ones((3, 3), np.uint8)

    cleaned_mask = cv2.morphologyEx(
        change_mask, cv2.MORPH_OPEN, kernel
    )

    change_percentage = (
        np.count_nonzero(cleaned_mask == 255) / cleaned_mask.size
    ) * 100

    highlighted = image_after.copy()
    highlighted[cleaned_mask == 255] = [255, 0, 0]

    overlay = cv2.addWeighted(
        image_after, 0.7, highlighted, 0.3, 0
    )

    return diff, cleaned_mask, overlay, change_percentage

