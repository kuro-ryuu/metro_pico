from filefifo import Filefifo

SAMPLE_RATE = 250  # samples per second
data = Filefifo(10, name='capture_250Hz_01.txt')

samples = []

# Read data into a list
for _ in range(1000):
    samples.append(data.get())

# --- Peak Detection ---
peaks = []

for i in range(1, len(samples) - 1):
    if samples[i] > samples[i - 1] and samples[i] > samples[i + 1]:
        peaks.append(i)  # store index of peak

# --- Peak-to-Peak Intervals (PPI) ---
intervals_samples = []
intervals_seconds = []

for i in range(1, len(peaks)):
    interval = peaks[i] - peaks[i - 1]  # distance between peaks (in samples)
    intervals_samples.append(interval)

    time_sec = interval / SAMPLE_RATE  # convert samples → seconds
    intervals_seconds.append(time_sec)

# Print first 3 intervals
print("Peak-to-Peak Intervals:")
for i in range(min(3, len(intervals_samples))):
    print(intervals_samples[i], "samples |", round(intervals_seconds[i], 3), "seconds")

# --- Frequency ---
if intervals_seconds:
    avg_period = sum(intervals_seconds) / len(intervals_seconds)  # average time for one wave
    frequency = 1 / avg_period  # frequency = 1 / period

    print("\nEstimated Frequency:", round(frequency, 2), "Hz")