from math import radians, degrees, cos, sin, asin, acos, sqrt, atan2

def haversine(lat1, lon1, lat2, lon2, r = 6371):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    Radius of earth in kilometers. Use r = 3956 for miles
    """

    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1;
    dlon = lon2 - lon1;

    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    d = r * c;

    return d;


def bearing(lat1, lon1, lat2, lon2):
    """
    Initial bearing (sometimes referred to as forward azimuth) which if
    followed in a straight line along a great-circle arc will take you from
    the point 1 to the point 2
    """
    # convert decimal degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    x = sin(lon2-lon1)*cos(lat2)
    y = cos(lat1)*sin(lat2)-sin(lat1)*cos(lat2)*cos(lon2-lon1)

    return degrees(atan2(x, y))

def cross_track_distance(lat1, lon1, lat_start, lon_start, lat_end, lon_end, r = 6371):
    """
    Distance of a point A from a great-circle path (sometimes called cross track error).
    lat1, lon1: coordinates of point A
    """
    # # d13 is (angular) distance from start point to point A
    d13 = haversine(lat_start, lon_start, lat1, lon1, r) / r
    # # t13 is (initial) bearing from start point to point
    t13 = radians(bearing(lat_start, lon_start, lat1, lon1))
    # # t12 is (initial) bearing from start point to end point
    t12 = radians(bearing(lat_start, lon_start, lat_end, lon_end))

    return asin(sin(d13) * sin(t13-t12)) * r;

def along_track_distance(lat1, lon1, lat_start, lon_start, lat_end, lon_end, r = 6371):
    """
    The along-track distance is the distance from the start point to the
    closest point to point A, on the path to the end point.
    """

    # d13 is (angular) distance from start point to point A
    d13 = haversine(lat_start, lon_start, lat1, lon1, r) / r
    # dxt is (angular) cross-track distance
    dxt = cross_track_distance(lat1, lon1, lat_start, lon_start, lat_end, lon_end, r) / r

    dat = acos(cos(d13)/cos(dxt)) * r

    return dat;
