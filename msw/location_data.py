import os
import logging

import pandas as pd

from .utils import DATA_PATH

logger = logging.getLogger(__file__)

MSW_API_KEY = os.environ["MSW_API_KEY"]
MSW_API_URL_STUB = f"http://magicseaweed.com/api/{MSW_API_KEY}/forecast/?spot_id="
FIELDS = [
    "timestamp",
    "fadedRating",
    "solidRating",
    "wind.direction",
    "wind.speed",
    "swell.maxBreakingHeight",
    "swell.components.combined.period"
]


class LocationData:
    def __init__(self, location_data: pd.DataFrame=None):
        """Given some 'location_data' an object is created that includes the information contained within
        location_data in addition to a 'target_url' field. 'target_url' is unique to each location and
        corresponds to the Magicseaweed short term forecast API endpoint.

        Args:
            location_data: DataFrame with the following columns: spot, longitude, latitude & spot_id
        """
        self._fields_for_url = "&fields=" + ",".join(FIELDS)

        if location_data is None:
            self.data = pd.read_csv(os.path.join(DATA_PATH, "surf_spots.csv"))
        else:
            self.data = location_data

        self.data = self._process_data(self.data)

        logger.info(f"Loaded {len(self)} spots")

    def _process_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Sorts 'df' by 'spot' and adds a column with a target url for the Magicseaweed short term forecast
        API endpoint.

        Args:
            df: DataFrame with at least the following columns: with the following columns: spot & spot_id
        """
        df = (df
              .sort_values("spot")
              .reset_index(drop=True)
              )

        df["target_url"] = MSW_API_URL_STUB + df.spot_id.astype(str) + self._fields_for_url

        return df

    def __iter__(self):
        for row in self.data.itertuples():
            yield row

    def __len__(self):
        return len(self.data)
