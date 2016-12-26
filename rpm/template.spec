Name:           ros-indigo-arni-core
Version:        1.1.6
Release:        0%{?dist}
Summary:        ROS arni_core package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/arni
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-arni-msgs
BuildRequires:  ros-indigo-arni-msgs
BuildRequires:  ros-indigo-catkin

%description
This package contains common ARNI functionality. Furthermore, generic launch
files and integration tests.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Dec 26 2016 Matthias Hadlich <matthiashadlich@yahoo.de> - 1.1.6-0
- Autogenerated by Bloom

* Mon Dec 26 2016 Matthias Hadlich <matthiashadlich@yahoo.de> - 1.1.5-0
- Autogenerated by Bloom

* Mon Dec 19 2016 Matthias Hadlich <matthiashadlich@yahoo.de> - 1.1.4-0
- Autogenerated by Bloom

* Mon Dec 12 2016 Matthias Hadlich <matthiashadlich@yahoo.de> - 1.1.3-0
- Autogenerated by Bloom

* Mon Dec 12 2016 Matthias Hadlich <matthiashadlich@yahoo.de> - 1.1.2-1
- Autogenerated by Bloom

* Sun Dec 11 2016 Matthias Hadlich <matthiashadlich@yahoo.de> - 1.1.2-0
- Autogenerated by Bloom

* Mon Dec 05 2016 Matthias Hadlich <matthiashadlich@yahoo.de> - 1.1.1-0
- Autogenerated by Bloom

