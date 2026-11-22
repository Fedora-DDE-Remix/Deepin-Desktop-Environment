Name:           deepin-terminal
Version:        6.5.42
Release:        3%{?dist}
Summary:        Terminal emulator for the Deepin desktop environment
License:        GPL-3.0-or-later AND BSD-3-Clause
URL:            https://github.com/linuxdeepin/deepin-terminal
Source0:        %{url}/archive/%{version}/deepin-terminal-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6GuiPrivate)
BuildRequires:  cmake(Qt6CorePrivate)
BuildRequires:  cmake(Qt6WidgetsPrivate)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Dtk6Widget)
BuildRequires:  cmake(lxqt2-build-tools)
BuildRequires:  qt6-linguist
BuildRequires:  pkgconfig(atspi-2)
BuildRequires:  pkgconfig(chardet)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(libutf8proc)
BuildRequires:  uchardet-devel

Requires:       hicolor-icon-theme
Recommends:     deepin-manual

%description
Deepin Terminal is a terminal emulator with workspace, multiple windows,
remote management and quake mode support.

%prep
%autosetup -n deepin-terminal-%{version} -p1
sed -i 's|SHARED|STATIC|' 3rdparty/terminalwidget/CMakeLists.txt
sed -i 's|/lib|%{_libdir}|' cmake/translation-generate.cmake
sed -i 's|DDE;||' src/deepin-terminal.desktop

%build
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake -GNinja -DQT_VERSION_MAJOR=6 -DDTK_VERSION_MAJOR=6
%cmake_build

%install
%cmake_install
rm -r %{buildroot}%{_includedir}/terminalwidget6/ \
      %{buildroot}%{_libdir}/libterminalwidget6.a \
      %{buildroot}%{_libdir}/cmake/terminalwidget6/ \
      %{buildroot}%{_libdir}/pkgconfig/terminalwidget6.pc \
      %{buildroot}%{_datadir}/terminalwidget6/

%files
%license LICENSE
%doc README.md
%{_bindir}/deepin-terminal
%{_datadir}/applications/deepin-terminal.desktop
%{_datadir}/deepin-terminal/
%{_datadir}/deepin-manual/manual-assets/application/deepin-terminal/
%{_datadir}/deepin-debug-config/deepin-debug-config.d/org.deepin.terminal.json
%{_datadir}/deepin-log-viewer/deepin-log.conf.d/org.deepin.terminal.json
%{_datadir}/dsg/configs/org.deepin.terminal/
%{_datadir}/icons/hicolor/scalable/apps/deepin-terminal.svg

%changelog
* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 6.5.42-3
- Add cmake(Qt6CorePrivate), required by Qt6 private components.

* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 6.5.42-2
- Use Fedora's pkgconfig(libutf8proc) name.

* Sat Nov 21 2026 mozixun <mozixun@fedoraproject.org> - 6.5.42-1
- Initial Fedora package.
