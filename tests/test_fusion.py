from src.fusion import fuse

def test_fusion_confirms_with_thermal():
    rgb = [[0, 0, 100, 100]]
    thermal = [[5, 5, 95, 95]]
    out = fuse(rgb, thermal)
    assert out[0]["thermal"] is True

def test_fusion_no_thermal():
    rgb = [[0, 0, 100, 100]]
    thermal = [[200, 200, 300, 300]]
    out = fuse(rgb, thermal)
    assert out[0]["thermal"] is False
