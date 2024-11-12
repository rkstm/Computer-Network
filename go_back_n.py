import random
import time

# Simulated Go-Back-N sliding window protocol
def go_back_n(sender_window_size, total_frames):
    sent_frames = 0
    ack_frames = 0
    while sent_frames < total_frames:
        # Send frames within the window
        for i in range(sender_window_size):
            if sent_frames < total_frames:
                print(f"Sender: Sending frame {sent_frames}")
                sent_frames += 1

        # Simulate receiver ACKs
        for i in range(sender_window_size):
            if ack_frames < sent_frames:
                # Randomly introduce an error
                if random.random() > 0.8:  # 20% chance of error
                    print(f"Receiver: Error detected at frame {ack_frames}")
                    sent_frames = ack_frames  # Resend from last ACKed frame
                    break
                else:
                    print(f"Receiver: Acknowledging frame {ack_frames}")
                    ack_frames += 1

        # Simulate delay
        time.sleep(1)
    print("All frames successfully sent and acknowledged.")

# Example usage
go_back_n(sender_window_size=4, total_frames=10)
