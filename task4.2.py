from filefifo import Filefifo
data1 = Filefifo(10, name='capture01_250Hz.txt')

samples = []
sample_rate = 250

for i in range(45000):
    samples.append(data1.get())


scaled_samples = []

for i in range(0, len(samples), sample_rate):
    chunk = samples[i:i+sample_rate]
    if i == 0:
        scaled_chunk = chunk
    else:
        prev_chunk = samples[i-sample_rate:i]
        prev_min = min(prev_chunk)
        prev_max = max(prev_chunk)
        current_min = min(chunk)
        current_max = max(chunk)
        if current_max == current_min:
            scaled_chunk = chunk 
        else:
            scaled_chunk = [(x-current_min)/(current_max-current_min)*(prev_max-prev_min)+prev_min for x in chunk]
    scaled_samples.extend(scaled_chunk)



