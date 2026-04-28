from filefifo import Filefifo
import matplotlib.pyplot as plt
data = Filefifo(10, name='capture_250Hz_01.txt')

samples = []


for i in range(2571):
    samples.append(data.get())

min_value = min(samples)
max_value = max(samples)

print(min_value, max_value)
scaled_samples = [(x - min_value) / (max_value - min_value) * 100 for x in samples]

min_scaled = min(scaled_samples[:500])
max_scaled = max(scaled_samples[:500])

peaks = []
# print peaks in 10-sec frame
for i in range(500, len(scaled_samples)):
    if scaled_samples[i] > scaled_samples[i - 1] and scaled_samples[i] > scaled_samples[i]:
        peaks.append(i)  # store index of peak

plt.plot(scaled_samples)
plt.scatter(peaks, [scaled_samples[i] for i in peaks], color='red', label='Peaks', marker='x')
plt.show()