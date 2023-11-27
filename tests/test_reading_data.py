from pathlib import Path

import pandas
import pandas as pd
import pytest

from src.reading_data import reading_data_from_file_csv, reading_data_from_file_xlsx


@pytest.fixture
def sample_csv(tmp_path: Path) -> Path:
    """
    Фикстура для создания временного файла CSV с примером данных.
    :param tmp_path: путь к временной директории, предоставляемой pytest.
    :type tmp_path: Path
    :return: путь к созданному временному файлу CSV.
    """
    data = {"Column1": [1, 2, 3], "Column2": ["A", "B", "C"]}
    df = pandas.DataFrame(data)
    file_path = tmp_path / "sample.csv"
    df.to_csv(file_path, index=False, encoding="utf-8")
    return file_path


def test_reading_data_from_file_csv(sample_csv: str) -> None:
    """
    Тестовая функция проверяющая корректность чтения данных из CSV файла.
    :param sample_csv: путь к временному файлу CSV, содержащему тестовые данные.
    :type sample_csv: Path
    :return: None
    """
    result = reading_data_from_file_csv(sample_csv)
    assert isinstance(result, pandas.DataFrame)
    expected_columns = ["Column1", "Column2"]
    assert result.columns.tolist() == expected_columns


@pytest.fixture
def sample_xlsx(tmp_path: Path) -> Path:
    """
    Фикстура для создания временного файла Excel (XLSX) с примером данных.
    :param tmp_path: путь к временной директории, предоставляемой pytest.
    :type tmp_path: Path
    :return: путь к созданному временному файлу Excel (XLSX).
    """
    data = {"Column1": [1, 2, 3], "Column2": ["A", "B", "C"], "Column3": ["City1", "City2", "City3"]}
    df = pd.DataFrame(data)
    file_path = tmp_path / "sample.xlsx"
    df.to_excel(file_path, index=False, na_rep="NA")
    return file_path


def test_reading_data_from_file_xlsx(sample_xlsx: str) -> None:
    """
    Тестовая функция проверяющая корректность чтения данных из файла Excel (XLSX).
    :param sample_xlsx: путь к временному файлу Excel (XLSX), содержащему тестовые данные.
    :type sample_xlsx: Path
    :return: None
    """
    result = reading_data_from_file_xlsx(sample_xlsx)
    assert isinstance(result, pd.DataFrame)
    expected_columns = ["Column1", "Column2", "Column3"]
    assert result.columns.tolist() == expected_columns
