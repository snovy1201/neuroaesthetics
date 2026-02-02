# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION ${CMAKE_VERSION}) # this file comes with cmake

# If CMAKE_DISABLE_SOURCE_CHANGES is set to true and the source directory is an
# existing directory in our source tree, calling file(MAKE_DIRECTORY) on it
# would cause a fatal error, even though it would be a no-op.
if(NOT EXISTS "/home/snovyang/neuroaesthetics/build/mocap_optitrack_client/_deps/natnet_sdk_content-src")
  file(MAKE_DIRECTORY "/home/snovyang/neuroaesthetics/build/mocap_optitrack_client/_deps/natnet_sdk_content-src")
endif()
file(MAKE_DIRECTORY
  "/home/snovyang/neuroaesthetics/build/mocap_optitrack_client/_deps/natnet_sdk_content-build"
  "/home/snovyang/neuroaesthetics/build/mocap_optitrack_client/_deps/natnet_sdk_content-subbuild/natnet_sdk_content-populate-prefix"
  "/home/snovyang/neuroaesthetics/build/mocap_optitrack_client/_deps/natnet_sdk_content-subbuild/natnet_sdk_content-populate-prefix/tmp"
  "/home/snovyang/neuroaesthetics/build/mocap_optitrack_client/_deps/natnet_sdk_content-subbuild/natnet_sdk_content-populate-prefix/src/natnet_sdk_content-populate-stamp"
  "/home/snovyang/neuroaesthetics/build/mocap_optitrack_client/_deps/natnet_sdk_content-subbuild/natnet_sdk_content-populate-prefix/src"
  "/home/snovyang/neuroaesthetics/build/mocap_optitrack_client/_deps/natnet_sdk_content-subbuild/natnet_sdk_content-populate-prefix/src/natnet_sdk_content-populate-stamp"
)

set(configSubDirs )
foreach(subDir IN LISTS configSubDirs)
    file(MAKE_DIRECTORY "/home/snovyang/neuroaesthetics/build/mocap_optitrack_client/_deps/natnet_sdk_content-subbuild/natnet_sdk_content-populate-prefix/src/natnet_sdk_content-populate-stamp/${subDir}")
endforeach()
if(cfgdir)
  file(MAKE_DIRECTORY "/home/snovyang/neuroaesthetics/build/mocap_optitrack_client/_deps/natnet_sdk_content-subbuild/natnet_sdk_content-populate-prefix/src/natnet_sdk_content-populate-stamp${cfgdir}") # cfgdir has leading slash
endif()
