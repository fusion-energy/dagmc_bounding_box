import os
import tarfile
import unittest
import urllib.request
from pathlib import Path

from dagmc_bounding_box import DagmcBoundingBox


class TestPythonApi(unittest.TestCase):
    """Tests the neutronics utilities functionality and use cases"""

    def setUp(self):

        if not Path("tests/v0.0.2.tar.gz").is_file():
            url = "https://github.com/fusion-energy/neutronics_workflow/archive/refs/tags/v0.0.2.tar.gz"
            urllib.request.urlretrieve(url, "tests/v0.0.2.tar.gz")

            tar = tarfile.open("tests/v0.0.2.tar.gz", "r:gz")
            tar.extractall("tests")
            tar.close()

        self.h5m_filename_smaller = "tests/neutronics_workflow-0.0.2/example_01_single_volume_cell_tally/stage_2_output/dagmc.h5m"
        self.h5m_filename_bigger = "tests/neutronics_workflow-0.0.2/example_02_multi_volume_cell_tally/stage_2_output/dagmc.h5m"

    def test_corners_returns_correct_type(self):
        dagmc_filename = "tests/neutronics_workflow-0.0.2/example_01_single_volume_cell_tally/stage_2_output/dagmc.h5m"
        my_bb = DagmcBoundingBox(dagmc_filename).corners()
        assert isinstance(my_bb, tuple)
        assert isinstance(my_bb[0], tuple)
        assert isinstance(my_bb[1], tuple)
        assert isinstance(my_bb[0][0], float)
        assert isinstance(my_bb[0][1], float)
        assert isinstance(my_bb[0][2], float)
        assert isinstance(my_bb[1][0], float)
        assert isinstance(my_bb[1][1], float)
        assert isinstance(my_bb[1][2], float)
        assert len(my_bb) == 2
        assert len(my_bb[0]) == 3
        assert len(my_bb[1]) == 3


# TODO add a test to check the correct values are found

# TODO add a test to check that extend increases the values correctly
