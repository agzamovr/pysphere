from math import radians, degrees, cos, sin, asin, acos, sqrt, atan2

def convert2radians(p):
    return map(radians, p)

def haversine(p1, p2, r = 6371):
    """
    Calculate the great circle distance between two points
    on the earth: p1 and p2 (specified in decimal degrees)
    Points must be passed as (lat, lon)
    r is the radius of earth (default radius in kms)
    Use r = 3956 for miles
    """
    ((lat1, lon1), (lat2, lon2))    = map(convert2radians, (p1, p2))
    dlat, dlon                      = (lat2 - lat1, lon2 - lon1)
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    return r * c;


def bearing(p1, p2):
    """
    Initial bearing (sometimes referred to as forward azimuth) which if followed
    in a straight line along a great-circle arc will take you from p1 to p2
    """
    ((lat1, lon1), (lat2, lon2))    = map(convert2radians, (p1, p2))
    x = sin(lon2-lon1)*cos(lat2)
    y = cos(lat1)*sin(lat2)-sin(lat1)*cos(lat2)*cos(lon2-lon1)
    return degrees(atan2(x, y))

def cross_track_distance(p_start, p_end, p, r = 6371):
    """
    Distance of a point p from a great-circle path (sometimes called cross track error).
    """
    # d13 is (angular) distance from start point to point A
    # t13 is (initial) bearing from start point to point
    # t12 is (initial) bearing from start point to end point
    d13 = haversine(p_start, p, r) / r
    t13 = radians(bearing(p_start, p))
    t12 = radians(bearing(p_start, p_end))
    return asin(sin(d13) * sin(t13-t12)) * r;

def along_track_distance(p_start, p_end, p, r = 6371):
    """
    The along-track distance is the distance from the start point to the
    closest point to point A, on the path to the end point.
    """
    # d13 is (angular) distance from start point to point A
    # dxt is (angular) cross-track distance
    d13 = haversine(p_start, p, r) / r
    dxt = cross_track_distance(p_start, p_end, p, r) / r
    return acos(cos(d13)/cos(dxt)) * r;

def line_length(line):
    return sum([haversine(p, line[i+1]) for i, p in enumerate(line[:-1])])

def distance_to_segment(p_start, p_end, p, r = 6371):
    """
    Distance of a point p from a segment p_start, p_end
    """
    segment_length      = haversine(p_start, p_end)
    along_p_start_end   = along_track_distance(p_start, p_end, p)
    along_p_end_start   = along_track_distance(p_end, p_start, p)

    if (along_p_start_end > segment_length):
        if (along_p_start_end > along_p_end_start):
            return haversine(p_end, p)
        else:
            return haversine(p_start, p)
    else:
        return cross_track_distance(p_start, p_end, p, r)
