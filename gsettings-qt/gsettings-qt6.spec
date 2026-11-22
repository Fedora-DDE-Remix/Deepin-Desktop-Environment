%global srcname gsettings-qt

Name:           gsettings-qt6
Version:        1.1.1
Release:        1%{?dist}
Summary:        Qt 6 wrapper for GSettings
License:        LGPL-3.0-only
URL:            https://gitlab.com/ubports/development/core/gsettings-qt
Source0:        %{url}/-/archive/v%{version}/%{srcname}-v%{version}.tar.gz
Patch0:         https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/gsettings-qt/01-optional-qml-plugin.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  cmake-extras

%description
gsettings-qt6 provides a Qt-style API for GSettings.  It is required by
dde-appearance for reading and writing GNOME/GTK desktop settings.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains development files for %{name}.

%prep
%autosetup -n %{srcname}-v%{version} -p1
%build
%cmake -GNinja -DENABLE_QT6=ON -DBUILD_TESTING=OFF
%cmake_build

%install
%cmake_install

%files
%license COPYING
%doc AUTHORS ChangeLog
%{_libdir}/libgsettings-qt6.so.1*

%files devel
%{_includedir}/qt6/QGSettings/
%{_libdir}/libgsettings-qt6.so
%{_libdir}/pkgconfig/gsettings-qt6.pc

%changelog
* Sat Nov 21 2026 mozixun <mozixun@fedoraproject.org> - 1.1.1-1
- Initial Fedora package (Qt 6 build).
