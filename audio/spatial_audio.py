import math

def itd(head_radius, azimuth, speed):
    """双耳时间差。"""
    raise NotImplementedError("TODO: itd")

def ild(azimuth, strength):
    """双耳强度差。"""
    raise NotImplementedError("TODO: ild")

def hrtf_length(sample_rate, milliseconds):
    """HRTF 长度。"""
    raise NotImplementedError("TODO: hrtf_length")

def azimuth_shortest_arc(current, target):
    """方位最短弧。"""
    raise NotImplementedError("TODO: azimuth_shortest_arc")

def distance_gain(distance, reference):
    """距离增益。"""
    raise NotImplementedError("TODO: distance_gain")

def occlusion_gain(blocked):
    """遮挡增益。"""
    raise NotImplementedError("TODO: occlusion_gain")

def reverb_fade(room_a, room_b, t):
    """混响跨房间淡出。"""
    raise NotImplementedError("TODO: reverb_fade")

def channel_matrix(center, left, right):
    """声道矩阵。"""
    raise NotImplementedError("TODO: channel_matrix")

def hrtf_ready(loaded, total):
    """HRTF 就绪。"""
    raise NotImplementedError("TODO: hrtf_ready")

def dynamic_occlusion(static_hit, dynamic_hit):
    """动态遮挡。"""
    raise NotImplementedError("TODO: dynamic_occlusion")

def resample_length(length, source_rate, target_rate):
    """重采样长度。"""
    raise NotImplementedError("TODO: resample_length")

def tap_count(quality, base):
    """卷积 tap 数。"""
    raise NotImplementedError("TODO: tap_count")

def binaural_delay(samples, sample_rate):
    """双耳延迟。"""
    raise NotImplementedError("TODO: binaural_delay")

def azimuth_key(azimuth, elevation):
    """方位缓存键。"""
    raise NotImplementedError("TODO: azimuth_key")

def degrade_cues(azimuth):
    """降级保留声像。"""
    raise NotImplementedError("TODO: degrade_cues")
