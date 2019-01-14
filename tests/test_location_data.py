from msw import LocationData


def test_init_with_dataframe(sample_location_data):
    locs = LocationData(sample_location_data)
    assert len(locs) == 3


def test_init_no_dataframe(number_of_locations_in_data):
    locs = LocationData()
    assert len(locs) == number_of_locations_in_data


def test_internal_iterator(number_of_locations_in_data):
    locs = LocationData()
    assert len([l for l in locs]) == number_of_locations_in_data


def test_columns():
    expected_cols = {"spot", "longitude", "latitude", "spot_id", "target_url"}
    locs = LocationData()
    assert sorted(locs.data.columns) == sorted(expected_cols)
