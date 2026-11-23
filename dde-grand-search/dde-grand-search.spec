Name:           dde-grand-search
Version:        6.1.3
Release:        1%{?dist}
Summary:        Global search service for the Deepin desktop environment
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dde-grand-search
Source0:        %{url}/archive/%{version}/dde-grand-search-%{version}.tar.gz
Patch0:         https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/dde-grand-search/01-fedora-libdir.patch
Patch1:         https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/dde-grand-search/02-readme-content.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconf-pkg-config
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  qt6-linguist
BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(Dtk6Gui)
BuildRequires:  cmake(Dtk6Widget)
BuildRequires:  cmake(DDEShell)
BuildRequires:  cmake(dfm6-search)
BuildRequires:  cmake(deepin-qdbus-service)
BuildRequires:  boost-devel
BuildRequires:  lucene++-devel
BuildRequires:  pkgconfig(dde-dock)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(taglib)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libffmpegthumbnailer)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(deepin-pdfium)
BuildRequires:  pkgconfig(libjpeg)

Requires:       dde-shell
Requires:       dde-tray-loader
Requires:       dde-daemon
Requires:       deepin-desktop-base
Requires:       deepin-desktop-schemas
Requires:       deepin-service-manager
Requires:       /usr/bin/glib-compile-schemas
Recommends:     dde-control-center

%description
dde-grand-search provides the DDE global search UI, the search daemon,
Treeland/dde-shell and dde-dock integration, and the file, media, PDF
and text preview plugins used by the desktop search experience.

%prep
%autosetup -n dde-grand-search-%{version} -p1

%build
export PATH=%{_qt6_bindir}:$PATH
%cmake -GNinja \
  -DQT_VERSION_MAJOR=6 \
  -DBUILD_OS_VERSION=25 \
  -DVERSION=%{version} \
  -DBUILD_TESTING=OFF
%cmake_build

%install
%cmake_install

%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :

%postun
glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :

%files
%license LICENSE.txt
%license LICENSES/
%doc README.md CHANGELOG.md
%{_bindir}/dde-grand-search
%{_bindir}/dde-grand-search-setting
%{_bindir}/dde-grand-search-daemon
%{_libdir}/dde-grand-search/
%{_libdir}/dde-grand-search-daemon/
%{_prefix}/lib/dde-dock/plugins/libddegrandsearch_dockplugin.so
%{_datadir}/dde-dock/icons/dcc-setting/dcc-search.dci
%{_libdir}/dde-shell/org.deepin.ds.dock.searchitem.so
%{_datadir}/dde-shell/org.deepin.ds.dock.searchitem/
%{_datadir}/glib-2.0/schemas/com.deepin.dde.dock.module.grand-search.gschema.xml
%{_datadir}/dbus-1/services/com.deepin.dde.GrandSearch.service
%{_datadir}/dbus-1/services/com.deepin.dde.GrandSearchSetting.service
%{_datadir}/dbus-1/services/org.deepin.dde.GrandSearchDaemon.service
%{_datadir}/dbus-1/interfaces/com.deepin.dde.GrandSearch.xml
%{_datadir}/dbus-1/interfaces/com.deepin.dde.GrandSearchSetting.xml
%{_datadir}/dde-grand-search/translations/
%{_datadir}/applications/dde-grand-search.desktop
%{_datadir}/deepin-manual/manual-assets/application/dde-grand-search/
%{_datadir}/deepin-service-manager/other/grand-search-daemon.json

%changelog
* Mon Nov 23 2026 mozixun <mozixun@fedoraproject.org> - 6.1.3-1
- Initial Fedora package for DDE 25/Treeland.
