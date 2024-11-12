import random
import time

# Simulated Selective Repeat sliding window protocol
def selective_repeat(sender_window_size, total_frames):
    sent_frames = 0
    ack_frames = [False] * total_frames
    while not all(ack_frames):
        # Send frames within the window
        for i in range(sender_window_size):
            if sent_frames < total_frames and not ack_frames[sent_frames]:
                print(f"Sender: Sending frame {sent_frames}")
                sent_frames += 1

        # Simulate receiver ACKs
        for i in range(sent_frames):
            if not ack_frames[i]:
                # Randomly introduce an error
                if random.random() > 0.8:  # 20% chance of error
                    print(f"Receiver: Error detected at frame {i}")
                else:
                    print(f"Receiver: Acknowledging frame {i}")
                    ack_frames[i] = True

        # Retransmit any unacknowledged frames within the window
        sent_frames = ack_frames.index(False) if False in ack_frames else total_frames
        time.sleep(1)
    print("All frames successfully sent and acknowledged.")

# Example usage
selective_repeat(sender_window_size=4, total_frames=10)
