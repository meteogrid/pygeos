from ctypes import c_void_p
from types import NoneType
from .error import GEOSException

import _geos_gdal as gdal

# NumPy supported?
try:
    import numpy
except ImportError:
    numpy = False

class GEOSBase(object):
    """
    Base object for GEOS objects that has a pointer access property
    that controls access to the underlying C pointer.
    """
    # Initially the pointer is NULL.
    _ptr = None

    # Default allowed pointer type.
    ptr_type = c_void_p

    # Pointer access property.
    def _get_ptr(self):
        # Raise an exception if the pointer isn't valid don't
        # want to be passing NULL pointers to routines --
        # that's very bad.
        if self._ptr: return self._ptr
        else: raise GEOSException('NULL GEOS %s pointer encountered.' % self.__class__.__name__)

    def _set_ptr(self, ptr):
        # Only allow the pointer to be set with pointers of the
        # compatible type or None (NULL).
        if isinstance(ptr, (self.ptr_type, NoneType)):
            self._ptr = ptr
        else:
            raise TypeError('Incompatible pointer type')

    # Property for controlling access to the GEOS object pointers.  Using
    # this raises an exception when the pointer is NULL, thus preventing
    # the C library from attempting to access an invalid memory location.
    ptr = property(_get_ptr, _set_ptr)
