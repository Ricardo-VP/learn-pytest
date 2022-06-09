from main import calculator
def test_class_monkey(monkeypatch):
    monkeypatch.setattr(calculator, "suma", lambda x: 4)
    c = calculator()
    assert c.suma() == 4