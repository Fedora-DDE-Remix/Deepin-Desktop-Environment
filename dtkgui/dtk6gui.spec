%global srcname dtkgui

Name:           dtk6gui
Version:        6.7.54
Release:        1%{?dist}
Summary:        Deepin Toolkit, GUI module for DDE look and feel
License:        LGPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dtkgui
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6ToolsTools)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6CorePrivate)
BuildRequires:  cmake(Qt6GuiPrivate)
BuildRequires:  cmake(Qt6WaylandClientPrivate)
BuildRequires:  cmake(Dtk6Core) >= %{version}
BuildRequires:  cmake(DtkBuildHelper)
BuildRequires:  cmake(TreelandProtocols)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(x11)
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel

%description
Deepin Tool Kit (DtkGui) is the development graphical user interface library
for all C++/Qt development on Deepin.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains development files for %{name}.

%prep
%autosetup -n %{srcname}-%{version} -p1 -C

%build
%cmake -GNinja -DDTK5=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_libdir}/libdtk6gui.so.6*
%{_libexecdir}/dtk6/DGui/

%files devel
%{_libdir}/libdtk6gui.so
%{_includedir}/dtk6/DGui/
%{_libdir}/cmake/Dtk6Gui/
%{_libdir}/pkgconfig/dtk6gui.pc
%{_qt6_archdatadir}/mkspecs/modules/*.pri

%changelog
* Sat Nov 21 2026 mozixun <mozixun@fedoraproject.org> - 6.7.54-1
- Initial Fedora package (DTK 6.7.54, Qt 6 only).
