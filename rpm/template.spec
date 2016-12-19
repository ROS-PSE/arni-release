Name:           ros-indigo-arni-rqt-overview-plugin
Version:        1.1.4
Release:        0%{?dist}
Summary:        ROS arni_rqt_overview_plugin package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/arni
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-arni-gui
Requires:       ros-indigo-rospy
Requires:       ros-indigo-rqt-gui
Requires:       ros-indigo-rqt-gui-py
BuildRequires:  ros-indigo-arni-gui
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-rospy
BuildRequires:  ros-indigo-rqt-gui
BuildRequires:  ros-indigo-rqt-gui-py

%description
The ARNI rqt_gui overview plugin.

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
* Mon Dec 19 2016 Matthias Hadlich <matthiashadlich@yahoo.de> - 1.1.4-0
- Autogenerated by Bloom

