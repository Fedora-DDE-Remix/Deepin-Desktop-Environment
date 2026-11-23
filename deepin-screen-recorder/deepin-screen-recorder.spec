Name:           deepin-screen-recorder
Version:        6.7.2
Release:        1%{?dist}
Summary:        Screen capture and recording tool for the Deepin desktop
License:        GPL-3.0-or-later AND LGPL-3.0-or-later AND MIT AND CC-BY-4.0 AND CC0-1.0
URL:            https://github.com/linuxdeepin/deepin-screen-recorder
Source0:        %{url}/archive/%{version}/deepin-screen-recorder-%{version}.tar.gz
Patch0:         https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/deepin-screen-recorder/01-use-qt-host-tools.patch
Patch1:         https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/deepin-screen-recorder/02-fix-ffmpeg-compat.patch
Patch2:         https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/deepin-screen-recorder/03-use-system-libs.patch
Patch3:         https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/deepin-screen-recorder/04-fix-desktop-entry.patch

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconf-pkg-config
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtmultimedia-devel
BuildRequires:  qt6-qtwayland-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-linguist
BuildRequires:  dtk6core-devel
BuildRequires:  dtk6gui-devel
BuildRequires:  dtk6widget-devel
BuildRequires:  libxcb-devel
BuildRequires:  xcb-util-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  libusb1-devel
BuildRequires:  ffmpeg-free-devel
BuildRequires:  ffmpegthumbnailer-devel
BuildRequires:  opencv-devel
BuildRequires:  portaudio-devel
BuildRequires:  libv4l-devel
BuildRequires:  systemd-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXtst-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libdrm-devel
BuildRequires:  mesa-libgbm-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  libepoxy-devel
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-2.0)

Requires:       dde-tray-loader
Requires:       deepin-desktop-base
Requires:       deepin-desktop-schemas
Requires:       ffmpeg-free
Requires:       gstreamer1-plugins-base
Requires:       gstreamer1-plugins-good
Requires:       gstreamer1-plugins-bad-free
Requires:       portaudio
Requires:       dbus-tools
Recommends:     gstreamer1-plugin-libav
Recommends:     deepin-ocr-plugin-manager

%description
deepin-screen-recorder provides full-screen and region screenshots, the
pinned screenshot viewer, screen recording on X11 and Treeland Wayland,
the screenshot D-Bus services and the corresponding dock plugins.

%prep
%autosetup -n deepin-screen-recorder-%{version} -p1

%build
export PATH=%{_qt6_bindir}:$PATH
%qmake_qt6 PREFIX=%{_prefix} VERSION=%{version}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :

%postun
glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :

%files
%license LICENSE LICENSES/GPL-3.0-or-later.txt LICENSES/LGPL-3.0-or-later.txt LICENSES/MIT.txt LICENSES/CC-BY-4.0.txt LICENSES/CC0-1.0.txt
%doc README.md CHANGELOG.md
%{_bindir}/deepin-screen-recorder
%{_bindir}/deepin-pin-screenshots
%{_prefix}/lib/dde-dock/plugins/*.so
%{_datadir}/dde-dock/icons/dcc-setting/dcc-shot-start-plugin.dci
%{_datadir}/dde-dock/icons/dcc-setting/dcc-shot-start-record-plugin.dci
%{_datadir}/glib-2.0/schemas/com.deepin.dde.dock.module.shot-start-plugin.gschema.xml
%{_datadir}/glib-2.0/schemas/com.deepin.dde.dock.module.shot-start-record-plugin.gschema.xml
%{_datadir}/applications/deepin-screen-recorder.desktop
%{_datadir}/icons/hicolor/scalable/apps/deepin-screen-recorder.svg
%{_datadir}/icons/hicolor/scalable/apps/deepin-screenshot.svg
%{_datadir}/deepin-screen-recorder/
%{_datadir}/deepin-manual/manual-assets/application/deepin-screen-recorder/
%{_datadir}/dbus-1/services/com.deepin.ScreenRecorder.service
%{_datadir}/dbus-1/services/com.deepin.Screenshot.service
%{_datadir}/dbus-1/services/com.deepin.PinScreenShots.service
%{_datadir}/dsg/configs/org.deepin.screen-recorder/
%{_datadir}/dsg/configs/overrides/org.deepin.dde.treeland/

%changelog
* Mon Nov 23 2026 mozixun <mozixun@fedoraproject.org> - 6.7.2-1
- Initial Fedora package for DDE 25/Treeland.
- Use qmake6 and Qt host tools from the Fedora Qt6 installation.
