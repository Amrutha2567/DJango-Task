from django.dispatch import Signal, receiver

# Define a simple signal
my_signal = Signal()

@receiver(my_signal)
def my_receiver(sender, **kwargs):
    print("Signal received!")

# Emitting the signal
print("Before sending signal.")
my_signal.send(sender=None)
print("After sending signal.")