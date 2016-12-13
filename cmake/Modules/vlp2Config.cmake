INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_VLP2 vlp2)

FIND_PATH(
    VLP2_INCLUDE_DIRS
    NAMES vlp2/api.h
    HINTS $ENV{VLP2_DIR}/include
        ${PC_VLP2_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    VLP2_LIBRARIES
    NAMES gnuradio-vlp2
    HINTS $ENV{VLP2_DIR}/lib
        ${PC_VLP2_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(VLP2 DEFAULT_MSG VLP2_LIBRARIES VLP2_INCLUDE_DIRS)
MARK_AS_ADVANCED(VLP2_LIBRARIES VLP2_INCLUDE_DIRS)

