import numpy as np

absolute_vorticity = 1.e-5  # 1/s
relative_humidity = 90.  # %
potential_intensity = 100.  # m/s
vertical_wind_shear = 5.  # m/s
omega_vert_velocity = -0.15  # Pa/s
du_dy = -1e-6  # 1/s


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


def GPI_MW2020(
        absolute_vorticity,
        vertical_wind_shear,
        omega_vert_velocity,
        du_dy
        ):
    """This function calculates and returns the dynamic genesis potential
    index for a tropical cyclone according to Murakami and Wang 2022
    Ref: Wang and Murakami 2020, Murakami and Wang 2022

    Args:
        absolute_vorticity (float): absolute vorticity at 850 hPa in 1/s
        vertical_wind_shear (float): VWS between 850 hPa and 200 hPa in m/s
        omega_vert_velocity (float): vertical velocity 500 hPa in Pa/s
        du_dy (float): meridional gradient of zonal wind at 500 hPa in 1/s
    """

    DGPI = (
            (2.0+.0*vertical_wind_shear)**(-1.7)
            * (5.5-du_dy*10**5)**(2.5)
            * (5.0-20*omega_vert_velocity)**(3.4)
            * (5.5 + abs(absolute_vorticity*10**5))**(2.4)
            * np.exp(-11.8) - 1.0
        )

    return DGPI


GPI = GPI_EN2004(
        absolute_vorticity,
        relative_humidity,
        potential_intensity,
        vertical_wind_shear
        )
print(GPI)

DGPI = GPI_MW2020(
        absolute_vorticity,
        vertical_wind_shear,
        omega_vert_velocity,
        du_dy
        )
print(DGPI)
