import os

from msw import GeographicViz


def test_init(sample_location_data):
    viz = GeographicViz(sample_location_data)

    assert len(viz.data["colors"]) == 3
    assert viz.data["colors"].empty is False

    assert len(viz.data["sizes"]) == 3
    assert viz.data["sizes"].empty is False


def test_save(tmpdir, sample_location_data):
    out_file_name = "index.html"
    out_path = os.path.join(tmpdir, out_file_name)
    viz = GeographicViz(sample_location_data)
    viz.save_and_open(out_path=out_path, open_in_browser=False)
    assert os.path.getsize(out_path) > 0
