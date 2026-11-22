Name:           deepin-compressor
Version:        6.5.38
Release:        3%{?dist}
Summary:        Archive manager for the Deepin desktop environment
License:        GPL-3.0-or-later AND GPL-2.0-or-later AND LGPL-2.1-or-later AND MPL-1.1
URL:            https://github.com/linuxdeepin/deepin-compressor
Source0:        %{url}/archive/%{version}/deepin-compressor-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(Dtk6Widget)
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  libarchive-devel
BuildRequires:  libzip-devel
BuildRequires:  minizip-ng-compat-devel
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(mount)

Requires:       libarchive
Requires:       p7zip
Requires:       unzip
Requires:       zip
Recommends:     deepin-manual

%description
Deepin Compressor is the archive manager of the Deepin desktop environment.
It supports common archive formats through libarchive and command-line
compressors.

%prep
%autosetup -n deepin-compressor-%{version} -p1
sed -i 's|/lib/qt${QT_VERSION_MAJOR}/bin/lrelease|%{_qt6_bindir}/lrelease|' cmake/translation-generate.cmake

%build
%cmake -GNinja \
  -DQT_VERSION_MAJOR=6 \
  -DDTK_VERSION_MAJOR=6 \
  -DCOMPRESSOR_PLUGIN_PATH=%{_libdir}/deepin-compressor/plugins
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/deepin-compressor
%{_prefix}/lib/deepin-compressor/pzip
%{_prefix}/lib/deepin-compressor/punzip
%{_libdir}/deepin-compressor/plugins/
%{_datadir}/applications/deepin-compressor.desktop
%{_datadir}/applications/context-menus/
%{_datadir}/dbus-1/interfaces/com.deepin.Compressor.xml
%{_datadir}/dbus-1/services/com.deepin.Compressor.service
%{_datadir}/deepin-compressor/
%{_datadir}/deepin-manual/manual-assets/application/deepin-compressor/
%{_datadir}/dsg/configs/org.deepin.compressor/
%{_datadir}/icons/hicolor/scalable/apps/deepin-compressor.svg
%{_datadir}/mime/packages/deepin-compressor.xml

%changelog
* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 6.5.38-3
- Add minizip-ng-compat-devel for the minizip plugin.

* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 6.5.38-2
- Add libzip-devel for the zip plugin.

* Sat Nov 21 2026 mozixun <mozixun@fedoraproject.org> - 6.5.38-1
- Initial Fedora package.
