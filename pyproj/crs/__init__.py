# -*- coding: utf-8 -*-
"""
This module interfaces with PROJ to produce a pythonic interface
to the coordinate reference system (CRS) information through the CRS
class.

Original Author: Alan D. Snow [github.com/snowman2] (2019)
"""

from pyproj._crs import (  # noqa: F401
    CoordinateOperation,
    CoordinateSystem,
    Datum,
    Ellipsoid,
    PrimeMeridian,
    is_proj,
    is_wkt,
)
from pyproj.crs.crs import (  # noqa: F401
    CRS,
    BoundCRS,
    CompoundCRS,
    GeographicCRS,
    ProjectedCRS,
    VerticalCRS,
)
from pyproj.exceptions import CRSError  # noqa: F401
