from alert.serial import Serial

def test_rescale():
    assert Serial().run() == 6
