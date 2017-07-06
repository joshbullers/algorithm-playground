class Node():
    def __init__(self, value, next_val = None, prior = None):
        self.value = value
        self.next = next_val
        self.prior = prior

    def set_next(self, next_connect):
        self.next = next_connect

    def delete_next(self):
        self.next = None

    def set_prior(self, prior_val):
        self.prior = prior_val

    def delete_prior(self):
        self.prior = None
