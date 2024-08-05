import numpy as np
from scipy.io import wavfile
from scipy.signal import stft
import numpy as np
import matplotlib.pyplot as plt

def analyze_audio(file_path):
    # Read the audio file
    sample_rate, audio_data = wavfile.read(file_path)
    
    # Perform Short-Time Fourier Transform (STFT)
    f, t, Zxx = stft(audio_data, fs=sample_rate, nperseg=1024)
    
    return f, t, np.abs(Zxx)

# Example usage
file_path = "path/to/your/audio.wav"
frequencies, times, amplitudes = analyze_audio(file_path)

def solve_wave_equation(frequency, grid_size=(100, 100), time_steps=500, c=1):
    dx = 1 / grid_size[0]
    dy = 1 / grid_size[1]
    dt = 0.1 * min(dx, dy) / c

    u = np.zeros(grid_size)
    u_prev = np.zeros(grid_size)
    u_next = np.zeros(grid_size)

    # Initial condition: a point source at the center
    u[grid_size[0] // 2, grid_size[1] // 2] = 1

    for _ in range(time_steps):
        u_next[1:-1, 1:-1] = (
            2 * u[1:-1, 1:-1] - u_prev[1:-1, 1:-1]
            + c ** 2 * dt ** 2 / dx ** 2 * (u[2:, 1:-1] - 2 * u[1:-1, 1:-1] + u[:-2, 1:-1])
            + c ** 2 * dt ** 2 / dy ** 2 (u[1:-1, 2:] - 2 * u[1:-1, 1:-1] + u[1:-1, :-2])
        )

        u_prev, u, u_next = u, u_next, u_prev

    return u

# Example usage
frequency = 440  # Example frequency in Hz
pattern = solve_wave_equation(frequency)
plt.imshow(pattern, cmap='viridis')
plt.colorbar()
plt.show()

