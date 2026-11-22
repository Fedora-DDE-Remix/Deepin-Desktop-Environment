Name:           deepin-scanner
Version:        0.1.26
Release:        1%{?dist}
Summary:        Document scanner for the Deepin desktop environment

License:        GPL-3.0-or-later AND MIT
URL:            https://github.com/linuxdeepin/deepin-scanner
Source0:        %{url}/archive/%{version}/deepin-scanner-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  qt6-linguist
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(Dtk6Widget)
BuildRequires:  cmake(Dtk6Gui)
BuildRequires:  pkgconfig(quazip1-qt6)
BuildRequires:  pkgconfig(sane-backends)
BuildRequires:  pkgconfig(libpng)

Requires:       dtk6widget
Requires:       qt6-qt5compat
Requires:       hicolor-icon-theme
Recommends:     sane-backends-drivers-scanners
Recommends:     deepin-manual

%description
Deepin Scanner is a scanning application that supports flatbed and
automatic document feeder scanners through SANE, webcams, and
PDF/JPEG/PNG/TIFF/OFD output.

%prep
%autosetup -n deepin-scanner-%{version} -p1
sed -i 's|/lib/qt${QT_VERSION_MAJOR}/bin/|%{_qt6_bindir}/|g' \
  cmake/translation-generate.cmake

%build
%cmake -GNinja \
  -DVERSION=%{version} \
  -DQT_VERSION_MAJOR=6 \
  -DDTK_VERSION_MAJOR=6
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/deepin-scanner
%{_datadir}/applications/deepin-scanner.desktop
%{_datadir}/deepin-scanner/
%{_datadir}/deepin-log-viewer/deepin-log.conf.d/org.deepin.scanner.json
%{_datadir}/deepin-manual/manual-assets/application/deepin-scanner/
%{_datadir}/dsg/configs/org.deepin.scanner/
%{_datadir}/icons/hicolor/scalable/apps/deepin-scanner.svg

%changelog
* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 0.1.26-1
- Initial Fedora package.
