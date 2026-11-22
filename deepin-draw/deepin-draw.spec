Name:           deepin-draw
Version:        6.5.44
Release:        1%{?dist}
Summary:        Lightweight drawing tool for the Deepin desktop environment

License:        GPL-3.0-or-later AND CC0-1.0 AND CC-BY-4.0 AND BSD-3-Clause
URL:            https://github.com/linuxdeepin/deepin-draw
Source0:        %{url}/archive/%{version}/deepin-draw-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  qt6-linguist
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6SvgWidgets)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(Dtk6Widget)
BuildRequires:  cmake(Dtk6Gui)
BuildRequires:  pkgconfig(dtk6widget)
BuildRequires:  pkgconfig(dtk6gui)
BuildRequires:  pkgconfig(dtk6core)

Requires:       dtk6widget
Requires:       qt6-qtsvg
Requires:       hicolor-icon-theme
Recommends:     deepin-manual

%description
Deepin Draw is a lightweight drawing tool that lets users freely draw and
edit images with shapes, text, layers and image adjustments.

%prep
%autosetup -n deepin-draw-%{version} -p1

%build
%cmake -GNinja -DQT_VERSION_MAJOR=6 -DDTK_VERSION_MAJOR=6 \
  -DDEEPINDRAW_TEST=OFF \
  -DDEEPINDRAW_AC_FUNC_ENABLE=ON
%cmake_build

%install
%cmake_install

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/deepin-draw
%{_datadir}/applications/deepin-draw.desktop
%{_datadir}/dbus-1/services/com.deepin.Draw.service
%{_datadir}/deepin-draw/
%{_datadir}/deepin-manual/manual-assets/application/deepin-draw/
%{_datadir}/dsg/configs/org.deepin.draw/
%{_datadir}/icons/deepin/apps/scalable/deepin-draw.svg
%{_datadir}/icons/hicolor/scalable/apps/deepin-draw.svg
%{_datadir}/mime/packages/deepin-draw.xml

%changelog
* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 6.5.44-1
- Initial Fedora package.
