from supersuit.utils.basic_transforms.flatten import check_param, change_observation
from gym.spaces import Box
import numpy as np
import pytest

test_obs_space = Box(
    low=np.float32(0.0), high=np.float32(1.0), shape=(4, 4, 3), dtype=np.float32
)
test_obs = np.zeros([4, 4, 3], dtype=np.float64) + np.arange(3)


def test_param_check():
    check_param(test_obs_space, True)
    with pytest.raises(AssertionError):
        check_param(test_obs_space, 6)


def test_change_observation():
    new_obs = change_observation(test_obs, test_obs_space, True)
    assert new_obs.shape == (4 * 4 * 3,)
