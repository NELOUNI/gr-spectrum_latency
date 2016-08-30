# Copyright 2011,2012,2016 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.

########################################################################
# Setup library
########################################################################
include(GrPlatform) #define LIB_SUFFIX

include_directories(${Boost_INCLUDE_DIR})
link_directories(${Boost_LIBRARY_DIRS})
list(APPEND spectrum_latency_sources
    bin_aggregator_impl.cc
    bin_statistics_impl.cc
    )

set(spectrum_latency_sources "${spectrum_latency_sources}" PARENT_SCOPE)
if(NOT spectrum_latency_sources)
	MESSAGE(STATUS "No C++ sources... skipping lib/")
	return()
endif(NOT spectrum_latency_sources)

add_library(gnuradio-spectrum_latency SHARED ${spectrum_latency_sources})
target_link_libraries(gnuradio-spectrum_latency ${Boost_LIBRARIES} ${GNURADIO_ALL_LIBRARIES})
set_target_properties(gnuradio-spectrum_latency PROPERTIES DEFINE_SYMBOL "gnuradio_spectrum_latency_EXPORTS")

if(APPLE)
    set_target_properties(gnuradio-spectrum_latency PROPERTIES
        INSTALL_NAME_DIR "${CMAKE_INSTALL_PREFIX}/lib"
    )
endif(APPLE)

########################################################################
# Install built library files
########################################################################
include(GrMiscUtils)
GR_LIBRARY_FOO(gnuradio-spectrum_latency RUNTIME_COMPONENT "spectrum_latency_runtime" DEVEL_COMPONENT "spectrum_latency_devel")

########################################################################
# Build and register unit test
########################################################################
include(GrTest)

include_directories(${CPPUNIT_INCLUDE_DIRS})
list(APPEND test_spectrum_latency_sources
    ${CMAKE_CURRENT_SOURCE_DIR}/test_spectrum_latency.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/qa_spectrum_latency.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/qa_bin_statistics.cc
)

add_executable(test-spectrum_latency ${test_spectrum_latency_sources})

target_link_libraries(
  test-spectrum_latency
  ${GNURADIO_RUNTIME_LIBRARIES}
  ${Boost_LIBRARIES}
  ${CPPUNIT_LIBRARIES}
  gnuradio-spectrum_latency
)

GR_ADD_TEST(test_spectrum_latency test-spectrum_latency)

########################################################################
# Print summary
########################################################################
message(STATUS "Using install prefix: ${CMAKE_INSTALL_PREFIX}")
message(STATUS "Building for version: ${VERSION} / ${LIBVER}")

