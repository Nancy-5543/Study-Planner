from planner.storage import load_data


def test_data_structure():
    data = load_data()

    assert "tasks" in data
    assert "revisions" in data
    assert "sessions" in data