from unittest.mock import patch

import numpy as np
import pytest

from napari_animation.frame_sequence import FrameSequence
from napari_animation.key_frame import ViewerState


def test_frame_seq(frame_sequence: FrameSequence):
    """Test basic indexing and length of FrameSequence."""
    # this fixture has two keyframes, with 15 steps in between
    assert len(frame_sequence) == 16

    # first and last frames are just the keyframes
    assert frame_sequence[0] == frame_sequence._key_frames[0].viewer_state
    # negative indexing works
    assert frame_sequence[-1] == frame_sequence._key_frames[-1].viewer_state

    with pytest.raises(IndexError):
        frame_sequence[1000]


def test_frame_seq_caching(frame_sequence: FrameSequence):
    """Test that we only interpolate on demand, and cache results."""
    fs = frame_sequence
    # index into the sequence and watch whether interpolate is called
    with patch.object(
        fs, "_interpolate_state", wraps=fs._interpolate_state
    ) as mock:
        frame_5 = fs[5]

    # it should have been called once, and a single frame cached
    mock.assert_called_once()
    assert isinstance(frame_5, ViewerState)
    assert len(fs._cache) == 1

    # indexing the same frame again will not require re-interpolation
    with patch.object(
        fs, "_interpolate_state", wraps=fs._interpolate_state
    ) as mock:
        frame_5 = fs[5]
        mock.assert_not_called()

    fs._rebuild_frame_index()
    assert len(fs._cache) == 0


def test_iterframes(animation_with_key_frames, frame_sequence: FrameSequence):
    """Test that we can render frames."""

    viewer = animation_with_key_frames.viewer
    fs = frame_sequence

    for n, i in enumerate(fs.iter_frames(viewer)):
        assert isinstance(i, np.ndarray)
        assert i.shape == (1200, 1600, 4)
        assert i.dtype == np.uint8
        if n > 4:
            break

    for n, i in enumerate(fs.iter_frames(viewer, scale_factor=0.5)):
        assert isinstance(i, np.ndarray)
        assert i.shape == (600, 800, 4)
        assert i.dtype == np.uint8
        if n > 4:
            break
