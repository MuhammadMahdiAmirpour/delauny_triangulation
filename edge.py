class Edge(object):
    def __init__(self, v0, v1) -> None:
        self.v0 = v0
        self.v1 = v1

    def __eq__(self, __value: object) -> bool:
        return (self.v0 == __value.v0 and self.v1 == __value.v1) or \
                (self.v0 == __value.v1 and self.v1 == __value.v0)
        
