class BowlingGame(object):
    def __init__(self):
        self.throw = []
        self.score = 0

    # define throw one time method
    def throw_one(self, pins):
        self.throw.append(pins)

    # adding many throws function to the prototype
    def throw_many(self, number_of_times, pins):
        for _ in range(number_of_times):
            self.throw.append(pins)

    # method that calculates the score
    def calculate_score(self):
        ball = 0
        for frames in range(10):
            if self.throw[ball] == 10:
                self.score += 10 + self.throw[ball+1] + self.throw[ball + 2]
                ball += 1
            elif self.throw[ball] + self.throw[ball+1] == 10:
                self.score += 10 + self.throw[ball + 2]
                ball += 2
            else:
                self.score += self.throw[ball] + self.throw[ball + 1]
                ball += 2