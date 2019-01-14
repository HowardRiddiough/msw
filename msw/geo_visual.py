import os
import webbrowser
import logging

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.cm
import folium

from . import ShortTermForecastData

logger = logging.getLogger(__file__)
logger.setLevel(logging.INFO)


class GeographicViz(ShortTermForecastData):
    def __init__(self, location_data: pd.DataFrame=None, limit_data: int=None):
        """Inherits state from 'msw.ShortTermForecastData' in order to download short term forecast data for
        each spot listed in 'location_data'.

        Args:
            location_data: DataFrame with the following columns: spot, longitude, latitude & spot_id
            limit_data: Enables user to limit the number of spots included in visual
        """
        super().__init__(location_data=location_data)

        if limit_data:
            print("limit")
            self.data = self.data[:limit_data]

        self.data["colors"] = self._gen_color_map(self.data["solidRating"])
        self.data["sizes"] = self._calc_point_sizes(self.data["maxBreakingHeight"])

        self._geo_viz = self.gen_geo_viz()

    def gen_geo_viz(self):
        """A html map is created with a circle marker for each surf spot. The circle's size is determined
        by the max breaking wave height and the color intensity by the number of MSW solid stars of the swell.
        A popup marker is included providing further information: spot name, swell height, period and number
        of MSW solid stars.
        """
        logger.info("Creating visualisation")

        m = folium.Map([50, 0], zoom_start=3.5, tiles='cartodbpositron')

        for row in self.data.itertuples():
            popup = (
                    f"{row.spot} <br>msw stars: {row.solidRating}"
                    f"<br>wave height: {row.maxBreakingHeight}ft @ {row.period}s"
                    f"<br>wind speed: {row.speed}mph"
            )

            folium.CircleMarker(
                location=[row.longitude, row.latitude],
                radius=row.sizes,
                fill=True,
                popup=popup,
                fill_color=row.colors,
                color=None,
                fill_opacity=0.7
            ).add_to(m)

        return m

    def save_and_open(self, out_path: str=None, open_in_browser: bool=True):
        """Saves geographical visualisation as a .html file and opens that file in a web browser.

        Args:
            out_path: Path where to save geographical visualisation
            open_in_browser: If True the html will be opened in a web browser
        """
        if not out_path:
            out_path = "../index.html"

        self._geo_viz.save(out_path)

        if open_in_browser:
            webbrowser.open("file://" + os.path.realpath(out_path))

    @staticmethod
    def _gen_color_map(values) -> list:
        """For each value in a given iterable this function calculates an RGB color; larger numbers will be
        allocated a darker color.

        Args:
            values: an iterable containing integers or floats
        """
        return [
            "#%02x%02x%02x" % (int(r), int(g), int(b))
            for r, g, b, _
            in 255 * matplotlib.cm.OrRd(mpl.colors.Normalize()(values.tolist()))
        ]

    @staticmethod
    def _calc_point_sizes(values) -> list:
        """For each value in a given iterable provided, point size is calculated. Point size refers to the
        size of a point on a graphical plot. Larger numbers are given larger points. Values must contain
        integers or floats only.

        Args:
            values: an iterable containing integers or floats
        """
        return np.where(values < 16, ((values**3)**0.5)*1.3, ((17**3)**0.5)*1.3)
