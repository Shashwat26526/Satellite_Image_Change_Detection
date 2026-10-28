
import numpy as np
import pytest

from change_detection import detect_changes


def test_identical_images_produce_no_changes():
    image = np.zeros((100, 100, 3), dtype=np.uint8)

    diff, mask, overlay, percentage = detect_changes(image, image)

    assert np.count_nonzero(diff) == 0
    assert np.count_nonzero(mask) == 0
    assert percentage == 0.0
    assert overlay.shape == image.shape


def test_output_shapes_and_percentage_are_valid():
    image_before = np.zeros((100, 100, 3), dtype=np.uint8)
    image_after = image_before.copy()
    image_after[20:80, 20:80] = 255

    diff, mask, overlay, percentage = detect_changes(
        image_before, image_after
    )

    assert diff.shape == (100, 100)
    assert mask.shape == (100, 100)
    assert overlay.shape == image_after.shape
    assert 0 <= percentage <= 100
    assert np.count_nonzero(mask) > 0


def test_mismatched_image_shapes_raise_error():
    image_before = np.zeros((100, 100, 3), dtype=np.uint8)
    image_after = np.zeros((80, 100, 3), dtype=np.uint8)

    with pytest.raises(ValueError, match="matching dimensions"):
        detect_changes(image_before, image_after)
