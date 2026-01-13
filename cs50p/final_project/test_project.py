import project
from unittest.mock import mock_open, patch

def test_validated_input(monkeypatch):
    #test single input
    monkeypatch.setattr('builtins.input', lambda _: "1")
    result = project.validated_input("any_prompt",[{"id":"1", "name":"any_value"}])
    assert result == [1]

    #test multiple inputs
    monkeypatch.setattr('builtins.input', lambda _: "1,2,3")
    result = project.validated_input("any_prompt",[{"id":"1"},{"id":"2"},{"id":"3"}])
    assert result == [1,2,3]

    #test faulty inputs
    input = iter(["cat", "4", "", "1"])
    monkeypatch.setattr('builtins.input', lambda _: next(input))
    result = project.validated_input("any_prompt",[{"id":"1"},{"id":"2"},{"id":"3"}])
    assert result == [1]

@patch("builtins.open", new_callable=mock_open)
@patch("json.load")
def test_get_areas(mock_json_load, mock_file):
    sample_areas = [
        {"id":"1", "name": "Portugal"},
        {"id":"2", "name": "Iceland"},
        {"id":"3", "name": "Netherlands"},
        {"id":"4", "name": "Luxembourg"},
        {"id":"5", "name": "Other regions"}
    ]
    mock_json_load.return_value = sample_areas
    result = project.get_areas()
    # Should filter out "Other regions" and sort by name
    assert len(result) == 4
    assert all(area["name"] != "Other regions" for area in result)
    assert result[1]["name"] == "Luxembourg"
    mock_file.assert_called_once_with("data/areas.json", "r", encoding="utf-8")


@patch("builtins.open", new_callable=mock_open)
@patch("json.load")
def test_get_roles(mock_json_load, mock_file):
    sample_roles = {
        "categories": [
            {
                "id": "1",
                "name": "Automotive business",
                "roles": [
                    {"id": "1", "name": "Car washer"},
                    {"id": "2", "name": "Auto mechanic, automotive technician"}
                ]
            },
            {
                "id": "2",
                "name": "Information technology",
                "roles": [
                    {"id": "1", "name": "Data scientist"},
                    {"id": "2", "name": "Developer"}
                ]
            }
        ]
    }
    mock_json_load.return_value = sample_roles
    result = project.get_roles()
    # Should filter by "Information technology" category
    assert len(result) == 2
    assert result[0] == {"id": "1", "name": "Data scientist"}
    assert result[1] == {"id": "2", "name": "Developer"}
    mock_file.assert_called_once_with("data/job_roles.json", "r", encoding="utf-8")
