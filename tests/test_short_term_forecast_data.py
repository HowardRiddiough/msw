from msw import ShortTermForecastData


def test_retrieve_data(sample_location_data):
    expected_cols = [
        "fadedRating", "solidRating", "timestamp", "spot", "longitude",
        "latitude", "speed", "direction",  "maxBreakingHeight",  "period"
    ]
    stf = ShortTermForecastData(sample_location_data)
    assert sorted(stf.data.columns) == sorted(expected_cols)
    assert len(stf.data) == 3
