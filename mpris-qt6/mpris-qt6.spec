Name:           mpris-qt6
Version:        1.0.0.1
Release:        1%{?dist}
Summary:        Qt 6 MPRIS interface and adaptor library
License:        LGPL-2.1-or-later
URL:            https://github.com/deepin-community/qt6mpris
Source0:        %{url}/archive/refs/tags/%{version}-1deepin2/qt6mpris-%{version}-1deepin2.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel

%description
mpris-qt6 implements the MPRIS 2 D-Bus media player interface and adaptor
for Qt 6.  It provides the MprisPlayer, MprisController and MprisManager
classes, plus the org.nemomobile.mpris QML module.

%package        devel
Summary:        Development files for mpris-qt6
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, CMake/qmake feature files and pkg-config metadata for mpris-qt6.

%prep
%autosetup -n qt6mpris-%{version}-1deepin2 -p1

%build
%qmake_qt6 VERSION=%{version}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%license COPYING
%{_libdir}/libmpris-qt6.so.*
%{_libdir}/qt6/qml/org/nemomobile/mpris/
%{_libdir}/qt6/mkspecs/features/mpris-qt6.prf

%files devel
%{_libdir}/libmpris-qt6.so
%{_libdir}/pkgconfig/mpris-qt6.pc
%{_includedir}/qt6/MprisQt/

%changelog
* Mon Nov 23 2026 mozixun <mozixun@fedoraproject.org> - 1.0.0.1-1
- Initial Fedora package for deepin-music.
