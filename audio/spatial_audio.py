import math


def itd(head_radius, azimuth, speed):
    """双耳时间差：球头模型 2r·sin(az)/c，量化到微秒以保证双耳对称。"""
    value = (2.0 * head_radius / speed) * math.sin(azimuth)
    return math.floor(value * 1e6) / 1e6


def ild(azimuth, strength):
    """双耳强度差：头部遮挡使背侧耳衰减，随方位角正弦变化。"""
    return strength * abs(math.sin(azimuth))


def hrtf_length(sample_rate, milliseconds):
    """HRTF 长度（采样点数），统一由采样率换算，避免 48k/44.1k 路径不一致。"""
    return int(round(sample_rate * milliseconds / 1000.0))


def azimuth_shortest_arc(current, target):
    """方位最短弧增量（度），结果落在 (-180, 180]，避免 ±180° 处绕远路。"""
    return (target - current + 180.0) % 360.0 - 180.0


def distance_gain(distance, reference):
    """距离增益：反比衰减，近处不超过参考增益。"""
    return reference / max(distance, reference)


def occlusion_gain(blocked):
    """遮挡增益：被遮挡时保留 0.3（绕射残余），否则 1.0。"""
    return 0.3 if blocked else 1.0


def reverb_fade(room_a, room_b, t):
    """混响跨房间淡出：旧房间尾音随 t 线性交叉淡入新房间，不硬截断。"""
    t = min(max(t, 0.0), 1.0)
    return room_a * (1.0 - t) + room_b * t


def channel_matrix(center, left, right):
    """声道矩阵：按 (center, left, right) 分配，中置不混入单侧耳。"""
    return (center, left, right)


def hrtf_ready(loaded, total):
    """HRTF 就绪屏障：全部加载完成前主线程不得读取缓冲。"""
    return total > 0 and loaded >= total


def dynamic_occlusion(static_hit, dynamic_hit):
    """动态遮挡：静态几何与动态几何（门等）任一命中即遮挡。"""
    return bool(static_hit or dynamic_hit)


def resample_length(length, source_rate, target_rate):
    """重采样后的长度，四舍五入保证双耳两侧对称。"""
    return int(round(length * target_rate / source_rate))


def tap_count(quality, base):
    """卷积 tap 数：按质量等级缩放，降级也不低于 base。"""
    return base * max(1, quality)


def binaural_delay(samples, sample_rate):
    """双耳延迟（秒）：采样数 / 采样率。"""
    return samples / sample_rate


def azimuth_key(azimuth, elevation):
    """方位缓存键。"""
    return f"{azimuth}:{elevation}"


def degrade_cues(azimuth):
    """降级保留声像：性能降级时仍保留方位 cues，不塌到中间。"""
    return azimuth
