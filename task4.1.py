from filefifo import Filefifo

SAMPLE_RATE = 250
SAMPLES = 250*20

ff = Filefifo(1, name="capture_250Hz_02.txt")

data = [ff.get() for _ in range(SAMPLES)]

# threshold
threshold = sum(data) / len(data) # simple average as threshold, can be improved with more sophisticated methods

# detect peaks
peaks = []
for i in range(1, len(data)-1):
    if data[i] > threshold and data[i] > data[i-1] and data[i] > data[i+1]:
        peaks.append(i) # store index of peak, can also store time or value if needed

# compute BPM
bpm_values = []
for i in range(1, len(peaks)):
    interval = peaks[i] - peaks[i-1] # number of samples between peaks
    if interval > 0:
        # bpm = 60 * SAMPLE_RATE / interval
        samples_per_minute = 60 * SAMPLE_RATE
        bpm = samples_per_minute / interval
        bpm_values.append(bpm)

# print at least 20
for i in range(min(20, len(bpm_values))):
    print("BPM:", int(bpm_values[i]))