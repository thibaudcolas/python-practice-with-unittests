kmh_mph = 1.60934


def kmh_to_mph(speed, ndigits):
    return round(speed / kmh_mph, ndigits)
    # return int((10 ** ndigits) * speed / kmh_mph) / (10 ** ndigits)


def mph_to_kmh(speed, ndigits):
    return round(speed * kmh_mph, ndigits)
