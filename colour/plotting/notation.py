# -*- coding: utf-8 -*-
"""
Colour Notation Systems Plotting
================================

Defines the colour notation systems plotting objects:

-   :func:`colour.plotting.single_munsell_value_function_plot`
-   :func:`colour.plotting.multi_munsell_value_function_plot`
"""

from __future__ import division

import numpy as np

from colour.notation import MUNSELL_VALUE_METHODS
from colour.plotting import artist, override_style, render

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013-2018 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = [
    'single_munsell_value_function_plot', 'multi_munsell_value_function_plot'
]


@override_style()
def single_munsell_value_function_plot(function='ASTM D1535-08', **kwargs):
    """
    Plots given *Lightness* function.

    Parameters
    ----------
    function : unicode, optional
        *Munsell* value function to plot.

    Other Parameters
    ----------------
    \**kwargs : dict, optional
        {:func:`colour.plotting.artist`, :func:`colour.plotting.render`},
        Please refer to the documentation of the previously listed definitions.

    Returns
    -------
    tuple
        Current figure and axes.

    Examples
    --------
    >>> single_munsell_value_function_plot('ASTM D1535-08')  # doctest: +SKIP

    .. image:: ../_static/Plotting_Single_Munsell_Value_Function_Plot.png
        :align: center
        :alt: single_munsell_value_function_plot
    """

    settings = {'title': '{0} - Munsell Value Function'.format(function)}
    settings.update(kwargs)

    return multi_munsell_value_function_plot((function, ), **settings)


@override_style()
def multi_munsell_value_function_plot(functions=None, **kwargs):
    """
    Plots given *Munsell* value functions.

    Parameters
    ----------
    functions : array_like, optional
        *Munsell* value functions to plot.

    Other Parameters
    ----------------
    \**kwargs : dict, optional
        {:func:`colour.plotting.artist`, :func:`colour.plotting.render`},
        Please refer to the documentation of the previously listed definitions.

    Returns
    -------
    tuple
        Current figure and axes.

    Raises
    ------
    KeyError
        If one of the given *Munsell* value function is not found in the
        factory *Munsell* value functions.

    Examples
    --------
    >>> multi_munsell_value_function_plot(['ASTM D1535-08', 'McCamy 1987'])
    ... # doctest: +SKIP

    .. image:: ../_static/Plotting_Multi_Munsell_Value_Function_Plot.png
        :align: center
        :alt: multi_munsell_value_function_plot
    """

    if functions is None:
        functions = ('ASTM D1535-08', 'McCamy 1987')

    settings = {'uniform': True}
    settings.update(kwargs)

    figure, axes = artist(**settings)

    samples = np.linspace(0, 100, 1000)
    for function in functions:
        function, name = MUNSELL_VALUE_METHODS.get(function), function
        if function is None:
            raise KeyError(
                ('"{0}" "Munsell" value function not found in '
                 'factory "Munsell" value functions: "{1}".').format(
                     name, sorted(MUNSELL_VALUE_METHODS.keys())))

        axes.plot(
            samples, [function(x) for x in samples], label=u'{0}'.format(name))

    settings = {
        'axes': axes,
        'aspect': 10,
        'bounding_box': (0, 100, 0, 10),
        'legend': True,
        'title': '{0} - Munsell Functions'.format(', '.join(functions)),
        'x_label': 'Luminance Y',
        'y_label': 'Munsell Value V',
    }
    settings.update(kwargs)

    return render(**settings)
