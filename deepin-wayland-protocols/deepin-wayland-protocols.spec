%global debug_package %{nil}

Name:           deepin-wayland-protocols
Version:        1.10.0.33
Release:        3%{?dist}
Summary:        Wayland protocol definitions for the Deepin desktop
License:        LGPL-2.1-or-later
URL:            https://github.com/linuxdeepin/deepin-wayland-protocols
Source0:        %{url}/archive/%{version}/deepin-wayland-protocols-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
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
* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 1.10.0.33-3
- Require ninja-build for the Ninja CMake generator.

* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 1.10.0.33-2
- Add the missing C/C++ compiler and make build dependencies.

* Sat Nov 21 2026 mozixun <mozixun@fedoraproject.org> - 1.10.0.33-1
- Initial Fedora package.
