from test_defense_shield.alert.serial import Serial

def test_rescale():
    assert Serial().run() == 6
