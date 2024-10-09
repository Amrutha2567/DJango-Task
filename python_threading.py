import threading
from django.dispatch import Signal, receiver

# Define a signal
my_signal = Signal()

@receiver(my_signal)
def my_receiver(sender, **kwargs):
    print(f"Signal received in thread: {threading.current_thread().name}")

# Emitting the signal
print(f"Before sending signal in thread: {threading.current_thread().name}")
my_signal.send(sender=None)
print(f"After sending signal in thread: {threading.current_thread().name}")
