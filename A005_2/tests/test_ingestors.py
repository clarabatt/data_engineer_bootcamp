import datetime
import pytest

from ingestors import DataIngestor
from unittest.mock import mock_open, patch
from writer import DataWriter


@pytest.fixture
@patch("ingestors.DataIngestor.__abstractmethods__", set())
def data_ingestor_fixture():
    return DataIngestor(
        writer=DataWriter,
        coins=["TESTE", "TESTANDO"],
        default_start_date=datetime.datetime(2021, 6, 21),
    )


@patch("ingestors.DataIngestor.__abstractmethods__", set())
class TestIngestors:
    def test_checkpoint_filename(self, data_ingestor_fixture):
        actual = data_ingestor_fixture._checkpoint_filename
        expected = "DataIngestor.checkpoint"
        assert actual == expected

    def test_load_checkpoint_without_checkpoint(self, data_ingestor_fixture):
        actual = data_ingestor_fixture._load_checkpoint()
        expected = datetime.datetime(2021, 6, 21)
        assert actual == expected

    @patch("builtins.open", new_callable=mock_open, read_data="2021-06-25")
    def test_load_checkpoint_existing_checkpoint(self, mock, data_ingestor_fixture):
        actual = data_ingestor_fixture._load_checkpoint()
        expected = datetime.datetime(2021, 6, 25)
        assert actual == expected

    @patch("ingestors.DataIngestor._save_checkpoint", return_value=None)
    def test_update_checkpoint_checkpoint_updated(self, mock, data_ingestor_fixture):
        data_ingestor = data_ingestor_fixture
        data_ingestor._update_checkpoint(value=datetime.datetime(2019, 1, 1))
        actual = data_ingestor._checkpoint
        expected = datetime.datetime(2019, 1, 1)
        assert actual == expected

    @patch("ingestors.DataIngestor._save_checkpoint", return_value=None)
    def test_update_checkpoint_checkpoint_written(self, mock, data_ingestor_fixture):
        data_ingestor = data_ingestor_fixture
        data_ingestor._update_checkpoint(value=datetime.datetime(2019, 1, 1))
        mock.assert_called_once()

    @patch("builtins.open", new_callable=mock_open, read_data="2021-06-25")
    @patch(
        "ingestors.DataIngestor._checkpoint_filename", return_value="foobar.chackpoint"
    )
    def test_save_checkpoint(
        self, mock_checkpoint_filename, mock_open_file, data_ingestor_fixture
    ):
        data_ingestor = data_ingestor_fixture
        data_ingestor._save_checkpoint()
        mock_open_file.assert_called_with(mock_checkpoint_filename, "w")
