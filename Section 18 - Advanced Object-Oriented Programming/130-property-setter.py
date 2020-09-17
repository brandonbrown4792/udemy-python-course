"""
Flight Leg:

GLA -> LHR -> CAN
2 segments (GLA -> LHR, LHR -> CAN)
"""
from typing import List


class Segment:
    def __init__(self, departure, destination):
        self.departure = departure  # GLA
        self.destination = destination  # LHR


class Flight:
    def __init__(self, segments: List[Segment]):
        self.segments = segments

    def __repr__(self):
        stops = [self.segments[0].departure]
        for segment in self.segments:
            stops.append(segment.destination)
        return f'<Flight: {"->".join(stops)}>'

    @property
    def departure_point(self) -> str:
        return self.segments[0].departure

    @departure_point.setter
    def departure_point(self, val):
        dest = self.segments[0].destination
        self.segments[0] = Segment(departure=val, destination=dest)


flight = Flight([Segment('GLA', 'LHR'), Segment('LHR', 'JFK')])
print(flight.departure_point)
flight.departure_point = 'MIA'
print(flight.departure_point)
print(flight)
