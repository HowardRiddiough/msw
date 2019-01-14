import os

import pytest
import pandas as pd

from msw.utils import DATA_PATH


@pytest.fixture
def sample_location_data():
    return pd.DataFrame(
        {
            "spot": ["Thurso", "Fistral", "Easkey"],
            "longitude": [58.60, 50.41, 54.29],
            "latitude": [-3.51, -5.10, -8.95],
            "spot_id": [47, 1, 1501]
        }
    )


@pytest.fixture
def number_of_locations_in_data():
    return len(pd.read_csv(os.path.join(DATA_PATH, "surf_spots.csv")))
