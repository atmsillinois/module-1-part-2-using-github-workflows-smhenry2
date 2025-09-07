import numpy as np

absolute_vorticity = 1.e-5  # 1/s
relative_humidity = 90.  # %
potential_intensity = 100.  # m/s
vertical_wind_shear = 5.  # m/s


def GPI_EN2004(
        absolute_vorticity,
        relative_humidity,
        potential_intensity,
        vertical_wind_shear
        ):
    """This function calculates and returns the genesis potential index for a
    tropical cyclone according to Emanuel and Nolan 2004
    Ref: Emanuel and Nolan 2004, Camagaro et al. 2006

    Args:
        absolute_vorticity (float): absolute vorticity at 850 hPa in 1/s
        relative_humidity (float): relative humidity at 600 hPa in percent
        potential_intensity (float): potential intensity in m/s
        vertical_wind_shear (float): VWS between 850 hPa and 200 hPa in m/s
    """

    GPI = (
            np.abs(10**5*absolute_vorticity)**(3/2)
            * (relative_humidity/50)**3
            * (potential_intensity/70)**3
            * (1+0.1*vertical_wind_shear)**(-2)
        )

    return GPI
