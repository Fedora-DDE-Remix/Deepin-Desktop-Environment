%global debug_package %{nil}

Name:           deepin-wayland-protocols
Version:        1.10.0.33
Release:        1%{?dist}
Summary:        Wayland protocol definitions for the Deepin desktop
License:        LGPL-2.1-or-later
URL:            https://github.com/linuxdeepin/deepin-wayland-protocols
Source0:        %{url}/archive/%{version}/deepin-wayland-protocols-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  pkgconfig(wayland-protocols)

%description
Wayland protocol XML definitions shared by Deepin desktop components.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains CMake and pkg-config files for %{name}.

%prep
%autosetup -n deepin-wayland-protocols-%{version} -p1

%build
%cmake -GNinja
%cmake_build

%install
%cmake_install

%files
%license COPYING.LIB
%doc README.md
%{_datadir}/deepin-wayland-protocols/

%files devel
%{_libdir}/cmake/DeepinWaylandProtocols/

%changelog
* Sat Nov 21 2026 mozixun <mozixun@fedoraproject.org> - 1.10.0.33-1
- Initial Fedora package.
