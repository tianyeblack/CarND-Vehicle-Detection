class BoundingBox:
    start_point = (None, None)
    stop_point = (None, None)

    def __init__(self, start_point, stop_point):
        if start_point[0] >= stop_point[0] or start_point[1] >= stop_point[1]:
            raise Exception("Stopping point should have greater coordinates than starting point")
        self.start_point = start_point
        self.stop_point = stop_point

    def get_span(self):
        return self.stop_point[0] - self.start_point[0], self.stop_point[1] - self.start_point[1]
