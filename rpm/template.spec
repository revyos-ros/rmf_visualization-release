%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-rmf-visualization-schedule
Version:        2.4.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS rmf_visualization_schedule package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       eigen3-devel
Requires:       openssl-devel
Requires:       ros-rolling-builtin-interfaces
Requires:       ros-rolling-geometry-msgs
Requires:       ros-rolling-rclcpp
Requires:       ros-rolling-rclcpp-components
Requires:       ros-rolling-rmf-traffic
Requires:       ros-rolling-rmf-traffic-msgs
Requires:       ros-rolling-rmf-traffic-ros2
Requires:       ros-rolling-rmf-visualization-msgs
Requires:       ros-rolling-rosidl-default-generators
Requires:       ros-rolling-visualization-msgs
Requires:       websocketpp-devel
Requires:       ros-rolling-ros-workspace
BuildRequires:  boost-devel
BuildRequires:  eigen3-devel
BuildRequires:  openssl-devel
BuildRequires:  ros-rolling-ament-cmake
BuildRequires:  ros-rolling-builtin-interfaces
BuildRequires:  ros-rolling-geometry-msgs
BuildRequires:  ros-rolling-rclcpp
BuildRequires:  ros-rolling-rclcpp-components
BuildRequires:  ros-rolling-rmf-traffic
BuildRequires:  ros-rolling-rmf-traffic-msgs
BuildRequires:  ros-rolling-rmf-traffic-ros2
BuildRequires:  ros-rolling-rmf-visualization-msgs
BuildRequires:  ros-rolling-rosidl-default-generators
BuildRequires:  ros-rolling-visualization-msgs
BuildRequires:  websocketpp-devel
BuildRequires:  ros-rolling-ros-workspace
BuildRequires:  ros-rolling-rosidl-typesupport-fastrtps-c
BuildRequires:  ros-rolling-rosidl-typesupport-fastrtps-cpp
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}
Provides:       ros-rolling-rosidl-interface-packages(member)

%if 0%{?with_tests}
BuildRequires:  ros-rolling-ament-cmake-uncrustify
BuildRequires:  ros-rolling-ament-lint-auto
BuildRequires:  ros-rolling-ament-lint-common
BuildRequires:  ros-rolling-rmf-utils
%endif

%if 0%{?with_weak_deps}
Supplements:    ros-rolling-rosidl-interface-packages(all)
%endif

%description
A visualizer for trajectories in rmf schedule

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/rolling" \
    -DAMENT_PREFIX_PATH="/opt/ros/rolling" \
    -DCMAKE_PREFIX_PATH="/opt/ros/rolling" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Sat Jun 15 2024 Yadunund <yadunund@openrobotics.org> - 2.4.0-1
- Autogenerated by Bloom

* Thu Jun 06 2024 Yadunund <yadunund@openrobotics.org> - 2.3.1-1
- Autogenerated by Bloom

* Mon Jun 03 2024 Yadunund <yadunund@openrobotics.org> - 2.3.0-1
- Autogenerated by Bloom

* Wed Mar 06 2024 Yadunund <yadunund@openrobotics.org> - 2.2.1-2
- Autogenerated by Bloom

