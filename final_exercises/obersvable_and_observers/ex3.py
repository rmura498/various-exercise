from ex3_publisher import Publisher, Observer


class PiggyBank:
    def __init__(self, total_amount, threshold=10):

        self.threshold = threshold
        self.total_amount = total_amount
        self.publisher = Publisher(['too_low_amount'])

    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        if value < self.threshold:
            self.publisher.dispatch('too_low_amount', "The total amount is under the threshold")
        self._total_amount = value

    def retrieve(self, value):
        if value < self.total_amount:
            self.total_amount -= value
            return True
        else:
            return False

    def save(self, value):
        self.total_amount += value


# ----------------------main
if __name__ == '__main__':
    obs1 = Observer('obs1')
    savings = PiggyBank(30, 10)
    savings.publisher.register(obs1, 'too_low_amount')
    savings.retrieve(21)
