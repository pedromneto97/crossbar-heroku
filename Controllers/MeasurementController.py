from Models.Measurement import Measurement


def get_last_measurement(sensor: str) -> Measurement or None:
    m = Measurement.objects(sensor=sensor).order_by('-timestamp').limit(1).first()
    return m.to_json() if m is not None else None
