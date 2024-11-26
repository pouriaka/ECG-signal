import neurokit2 as nk
import matplotlib.pyplot as plt


simulated_ecg = nk.ecg_simulate(duration=2, sampling_rate=100, heart_rate=80)
nk.signal_plot(simulated_ecg, sampling_rate=200)  # Visualize the signal

plt.show()
