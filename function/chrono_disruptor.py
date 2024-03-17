import numpy as np

def chrono_disruptor(target_time, target_event, disruptor_power):
    """
    Function to disrupt the fabric of spacetime and manipulate time and temporal events.
    
    Parameters:
    target_time (int): The target time in seconds.
    target_event (str): The target event to be manipulated.
    disruptor_power (float): The power of the disruptor in range [0, 1].
    
    Returns:
    dict: A dictionary containing the manipulated time and event.
    """
    
    # Check if the disruptor power is within the valid range
    if not (0 <= disruptor_power <= 1):
        raise ValueError("Disruptor power must be in range [0, 1]")
    
    # Calculate the time displacement and event manipulation based on the disruptor power
    time_displacement = target_time * disruptor_power
    event_manipulation = target_event + " (manipulated)"
    
    # Return the manipulated time and event
    return {"time": target_time + time_displacement, "event": event_manipulation}
