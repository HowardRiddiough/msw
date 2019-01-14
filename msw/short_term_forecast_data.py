import logging

from tqdm import tqdm
import pandas as pd

from . import LocationData
from .utils import process_json

logger = logging.getLogger(__file__)
logger.setLevel(logging.INFO)


class ShortTermForecastData(LocationData):
    def __init__(self, location_data: pd.DataFrame=None):
        """Inherits state from 'msw.LocationData' in order to download short term forecast data for each
        spot listed in 'location_data'.

        Args:
            location_data: DataFrame with the following columns: spot, longitude, latitude & spot_id
        """
        super().__init__(location_data=location_data)

        self.data = self._retrieve_forecast_data()

    def _retrieve_forecast_data(self) -> pd.DataFrame:
        """Downloads short term forecast data for each spot in 'location_data'. Spots were no json data is
        found will be skipped.
        """
        df = pd.DataFrame([])

        logger.info("Downloading forecast data")
        for row in tqdm(list(self.data.itertuples())):
            if not self._json_error(row.target_url):
                df = pd.concat([df, process_json(row.target_url, row.spot, row.longitude, row.latitude)])

        df = df.reset_index(drop=True)

        return df

    @staticmethod
    def _json_error(target_url):
        df = pd.read_json(target_url).reset_index()
        return "error_response" in df.reset_index().columns
