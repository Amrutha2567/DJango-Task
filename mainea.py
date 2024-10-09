from django.db import transaction
from django.dispatch import Signal, receiver

# Define a signal
my_signal = Signal()

@receiver(my_signal)
def my_receiver(sender, **kwargs):
    print("Signal received within a transaction!")

# Using a transaction
with transaction.atomic():
    print("Before sending signal within transaction.")
    my_signal.send(sender=None)
    print("After sending signal within transaction.")
