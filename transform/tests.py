import json
import os
import pytest
from transform import CSV

@pytest.fixture
def csv_instance():
    """
    Fixture that creates a CSV instance for testing purposes.

    Returns:
    CSV: An instance of the CSV class.
    """
    in_file = 'test_input.csv'
    out_file = 'test_output.json'

    with open(in_file, 'w', encoding='utf-8') as file:
        file.write('Title,Author,Veröffentlichungsjahr\n')
        file.write('Book1,Author1,2020\n')
        file.write('Book2,Author2,2018\n')

    csv = CSV(in_file, out_file)
    yield csv

    if os.path.exists(in_file):
        os.remove(in_file)
    if os.path.exists(out_file):
        os.remove(out_file)

def test_read(csv_instance):
    """
    Test function for CSV reading.

    Args:
    csv_instance (CSV): An instance of the CSV class.

    Returns:
    None
    """
    csv_instance.read()
    assert csv_instance.headers == ['Title', 'Author', 'Veröffentlichungsjahr']
    assert csv_instance.data == [['Book1', 'Author1', '2020'], ['Book2', 'Author2', '2018']]

def test_transform(csv_instance):
    """
    Test function for CSV transformation.

    Args:
    csv_instance (CSV): An instance of the CSV class.

    Returns:
    None
    """
    result = json.loads(csv_instance.transform())
    assert 'Buecher' in result
    assert len(result['Buecher']) == 2

    for book in result['Buecher']:
        assert 'Title' in book
        assert 'Author' in book
        assert 'Veroeffentlichungsjahr' in book

        assert isinstance(book['Title'], str)
        assert isinstance(book['Author'], str)
        assert isinstance(book['Veroeffentlichungsjahr'], str)

def test_export(csv_instance):
    """
    Test function for CSV export.

    Args:
    csv_instance (CSV): An instance of the CSV class.

    Returns:
    None
    """
    csv_instance.export()

    assert os.path.exists('test_output.json')

    with open('test_output.json', 'r', encoding='utf-8') as file:
        content = file.read()
        result = json.loads(content)

    assert 'Buecher' in result
    assert len(result['Buecher']) == 2

    for book in result['Buecher']:
        assert 'Title' in book
        assert 'Author' in book
        assert 'Veroeffentlichungsjahr' in book

        assert isinstance(book['Title'], str)
        assert isinstance(book['Author'], str)
        assert isinstance(book['Veroeffentlichungsjahr'], str)
