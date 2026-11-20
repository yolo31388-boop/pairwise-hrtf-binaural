import pytest
from audio import spatial_audio as mod

CASES = [
    ("itd", 'm.itd(0.09, 1.5707963267948966, 343) == approx(0.000524, rel=1e-3)'),
    ("ild", 'm.ild(1.5707963267948966, 1) == approx(1.0)'),
    ("length", 'm.hrtf_length(48000, 5) == 240'),
    ("arc", 'm.azimuth_shortest_arc(350, 10) == approx(20)'),
    ("gain", 'm.distance_gain(10, 1) == approx(0.1)'),
    ("occlusion", 'm.occlusion_gain(True) == approx(0.3)'),
    ("reverb", 'm.reverb_fade(0.2, 0.8, 0.5) == approx(0.5)'),
    ("matrix", 'm.channel_matrix(1.0, 2.0, 3.0) == (1.0, 2.0, 3.0)'),
    ("ready", 'm.hrtf_ready(10, 10) is True'),
    ("dynamic", 'm.dynamic_occlusion(True, False) is True'),
    ("resample", 'm.resample_length(480, 48000, 44100) == 441'),
    ("tap", 'm.tap_count(2, 64) == 128'),
    ("delay", 'm.binaural_delay(1, 48000) == approx(1 / 48000)'),
    ("key", 'm.azimuth_key(30, 10) == "30:10"'),
    ("degrade", 'm.degrade_cues(1) == 1')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
