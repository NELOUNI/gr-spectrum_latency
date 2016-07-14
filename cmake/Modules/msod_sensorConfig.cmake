INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_MSOD_SENSOR msod_sensor)

FIND_PATH(
    MSOD_SENSOR_INCLUDE_DIRS
    NAMES msod_sensor/api.h
    HINTS $ENV{MSOD_SENSOR_DIR}/include
        ${PC_MSOD_SENSOR_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    MSOD_SENSOR_LIBRARIES
    NAMES gnuradio-msod_sensor
    HINTS $ENV{MSOD_SENSOR_DIR}/lib
        ${PC_MSOD_SENSOR_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(MSOD_SENSOR DEFAULT_MSG MSOD_SENSOR_LIBRARIES MSOD_SENSOR_INCLUDE_DIRS)
MARK_AS_ADVANCED(MSOD_SENSOR_LIBRARIES MSOD_SENSOR_INCLUDE_DIRS)

