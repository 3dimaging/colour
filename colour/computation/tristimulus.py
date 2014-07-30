# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**tristimulus.py**

**Platform:**
    Windows, Linux, Mac Os X.

**Description:**
    Defines **Colour** package *tristimulus* values computation objects.

**Others:**

"""

from __future__ import unicode_literals

import numpy

import colour.algebra.matrix
import colour.computation.spectrum
import colour.dataset.cmfs
import colour.dataset.lefs
import colour.utilities.common
import colour.utilities.exceptions
import colour.utilities.decorators
import colour.utilities.verbose
from colour.algebra.interpolation import SpragueInterpolator
from colour.cache.runtime import RuntimeCache

__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2013 - 2014 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["spectral_to_XYZ",
           "wavelength_to_XYZ"]


def spectral_to_XYZ(spd,
                    cmfs=colour.dataset.cmfs.STANDARD_OBSERVERS_CMFS.get("CIE 1931 2 Degree Standard Observer"),
                    illuminant=None):
    """
    Converts given spectral power distribution to *CIE XYZ* colourspace using given colour
    matching functions and illuminant.

    Usage::

        >>> cmfs = colour.CMFS.get("CIE 1931 2 Degree Standard Observer")
        >>> spd = colour.SpectralPowerDistribution("Custom", {380: 0.0600, 390: 0.0600}).zeros(*cmfs.shape)
        >>> illuminant = colour.ILLUMINANTS_RELATIVE_SPDS.get("D50").zeros(*cmfs.shape)
        >>> spectral_to_XYZ(spd, cmfs, illuminant)
        array([[  4.57648522e-04],
               [  1.29648668e-05],
               [  2.16158075e-03]])

    :param spd: Spectral power distribution.
    :type spd: SpectralPowerDistribution
    :param cmfs: Standard observer colour matching functions.
    :type cmfs: XYZ_ColourMatchingFunctions
    :param illuminant: *Illuminant* spectral power distribution.
    :type illuminant: SpectralPowerDistribution
    :return: *CIE XYZ* colourspace matrix.
    :rtype: ndarray (3, 1)

    :note: Output *CIE XYZ* colourspace matrix is in domain [0, 1].

    References:

    -  **Wyszecki & Stiles**, *Color Science - Concepts and Methods Data and Formulae - Second Edition*, \
    Wiley Classics Library Edition, published 2000, ISBN-10: 0-471-39918-3, Page 158.
    """

    shape = cmfs.shape
    if spd.shape != cmfs.shape:
        spd = spd.clone().zeros(*shape)

    if illuminant is None:
        start, end, steps = shape
        range = numpy.arange(start, end + steps, steps)
        illuminant = colour.computation.spectrum.SpectralPowerDistribution(name="1.0",
                                                                           data=dict(zip(*(list(range),
                                                                                           [1.] * len(range)))))
    else:
        if illuminant.shape != cmfs.shape:
            illuminant = illuminant.clone().zeros(*shape)

    illuminant = illuminant.values
    spd = spd.values

    x_bar, y_bar, z_bar = cmfs.x_bar.values, cmfs.y_bar.values, cmfs.z_bar.values

    x_products = spd * x_bar * illuminant
    y_products = spd * y_bar * illuminant
    z_products = spd * z_bar * illuminant

    normalising_factor = 100. / numpy.sum(y_bar * illuminant)

    XYZ = numpy.array([normalising_factor * numpy.sum(x_products),
                       normalising_factor * numpy.sum(y_products),
                       normalising_factor * numpy.sum(z_products)])

    return XYZ.reshape((3, 1))


@colour.utilities.decorators.memoize(RuntimeCache.wavelength_to_XYZ)
def wavelength_to_XYZ(wavelength,
                      cmfs=colour.dataset.cmfs.STANDARD_OBSERVERS_CMFS.get("CIE 1931 2 Degree Standard Observer")):
    """
    Converts given wavelength to *CIE XYZ* colourspace using given colour matching functions, if the retrieved
    wavelength is not available in the colour matching function, its value will be calculated using *CIE* recommendations:
    The method developed by *Sprague* (1880) should be used for interpolating functions having a uniformly spaced
    independent variable and a *Cubic Spline* method for non-uniformly spaced independent variable.

    Usage::

        >>> wavelength_to_XYZ(480, colour.CMFS.get("CIE 1931 2 Degree Standard Observer"))
        array([[ 0.09564  ],
               [ 0.13902  ],
               [ 0.8129501]])

    :param wavelength: Wavelength in nm.
    :type wavelength: float
    :param cmfs: Standard observer colour matching functions.
    :type cmfs: XYZ_ColourMatchingFunctions
    :return: *CIE XYZ* colourspace matrix.
    :rtype: ndarray (3, 1)

    :note: Output *CIE XYZ* colourspace matrix is in domain [0, 1].
    :note: If *scipy* is not unavailable the *Cubic Spline* method will fallback to legacy *Linear* interpolation.
    """

    start, end, steps = cmfs.shape
    if wavelength < start or wavelength > end:
        raise colour.utilities.exceptions.ColourMatchingFunctionsError(
            "'{0} nm' wavelength not in '{1} - {2}' nm supported wavelengths range!".format(wavelength, start, end))

    wavelengths, values, = cmfs.wavelengths, cmfs.values

    if wavelength not in cmfs:
        if cmfs.is_uniform():
            interpolators = [SpragueInterpolator(wavelengths, values[:, i]) for i in range(values.shape[-1])]
        else:
            if colour.utilities.common.is_scipy_installed():
                from scipy.interpolate import interp1d

                interpolators = [interp1d(wavelengths, values[:, i], kind="cubic") for i in range(values.shape[-1])]
            else:
                colour.utilities.verbose.warning(
                    "!> {0} | 'scipy.interpolate.interp1d' interpolator is unavailable, using 'numpy.interp' interpolator!".format(
                        __name__))

                x_interpolator = lambda x: numpy.interp(x, wavelengths, values[:, 0])
                y_interpolator = lambda x: numpy.interp(x, wavelengths, values[:, 1])
                z_interpolator = lambda x: numpy.interp(x, wavelengths, values[:, 2])
                interpolators = (x_interpolator, y_interpolator, z_interpolator)

        return numpy.array([interpolator(wavelength) for interpolator in interpolators]).reshape((3, 1))
    else:
        return numpy.array(cmfs.get(wavelength)).reshape((3, 1))