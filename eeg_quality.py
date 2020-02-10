from scipy.stats import kurtosis
import numpy as np


def compute_quality_index(data_eeg, samp_rate=250, ref_krt=5.0,
                          ref_std=20.0, ref_max=100.0, ref_med=20.0,
                          buf=1.0, sliding_step=1.0):
    """
    Compute quality index sec by sec

    Parameters
    ----------
    data_eeg: np.ndarray
        Matrix containing EEG data
    samp_rate: int (optional, default 250)
        Sampling rate
    ref_krt: float (optional, default 4.0)
        Kurtosis reference
    ref_std: float (optional, default 15.0)
        Std reference
    ref_max: float (optional, default 50.0)
        Maximum reference
    ref_med: float (optional, default 15.0)
        Median reference
    buf: float (optional, default 1.0)
        Buffer to divide the EEG data (in seconds)
    sliding_step: float (optional, default 1.0)
        Sliding step used for the buffer (in seconds)

    Returns
    -------
    quality_index_array: np.ndarray
        Array of quality index
    """
    assert sliding_step <= buf, 'The sliding step should be lower or equal ' \
                                'to the buffer'

    # for channel in range(nb_channels):
    nb_steps = int((len(data_eeg) - (buf - sliding_step)
                    * samp_rate) / (samp_rate * sliding_step))

    eeg_array = []
    for index in range(nb_steps):
        eeg_array.append(data_eeg[
                         int(index * sliding_step * samp_rate): int(
                             (index * sliding_step + buf) * samp_rate)])

    if int(((nb_steps - 1) * sliding_step + buf) * samp_rate) < len(
            data_eeg):
        eeg_array.append(
            data_eeg[
            int(((nb_steps - 1) * sliding_step + buf) * samp_rate):len(
                data_eeg)])

    kurt_array = kurtosis(eeg_array, fisher=False, bias=True, axis=1)
    std_array = np.std(eeg_array, ddof=1, axis=1)
    max_array = np.amax(np.abs(eeg_array), axis=1)
    median_array = np.median(np.abs(eeg_array), axis=1)

    quality_array = (1.0 / 4.0) * (
            1.0 / np.exp(np.abs(kurt_array - ref_krt) / ref_krt)) + (
                            1.0 / 4.0) * \
                    (1.0 / np.exp(np.abs(std_array - ref_std) / ref_std)) + (
                            1.0 / 4.0) * \
                    (1.0 / np.exp(np.abs(max_array - ref_max) / ref_max)) + (
                            1.0 / 4.0) * \
                    (1.0 / np.exp(np.abs(median_array - ref_med) / ref_med))

    quality_array = [el if el > 0 else 0.0 for el in quality_array]
    quality_index_array = np.asarray(quality_array)

    return quality_index_array


if __name__ == "__main__":
    data_eeg = np.asarray([1, 2, 3])
    print(compute_quality_index(data_eeg))
