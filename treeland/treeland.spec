%global debug_package %{nil}

Name:           treeland
Version:        0.12.0
Release:        10%{?dist}
Summary:        Wayland compositor for the Deepin desktop environment
License:        (Apache-2.0 OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only) AND MIT AND CC0-1.0
URL:            https://github.com/linuxdeepin/treeland
Source0:        %{url}/archive/%{version}/treeland-%{version}.tar.gz
Patch0:         https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/treeland/01-relax-pixman.patch
Patch1:         https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/treeland/02-pnpids-no-heredoc.patch

Provides:       bundled(waylib) = 0.20.2
Provides:       bundled(wlroots) = 0.20.2

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6ShaderTools)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6RemoteObjects)
BuildRequires:  cmake(Qt6HttpServer)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6QuickPrivate)
BuildRequires:  cmake(Qt6GuiPrivate)
BuildRequires:  cmake(Qt6CorePrivate)
BuildRequires:  cmake(Qt6QuickTemplates2Private)
BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(Dtk6Declarative)
BuildRequires:  cmake(Dtk6SystemSettings)
BuildRequires:  cmake(DDM) >= 0.2.0
BuildRequires:  cmake(TreelandProtocols) >= 0.9.0
BuildRequires:  pkgconfig(libseat) >= 0.2.0
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcb-errors)
BuildRequires:  pkgconfig(xcb-dri3)
BuildRequires:  pkgconfig(xcb-present)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcb-xinput)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-res)
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xwayland)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  mpv-devel
BuildRequires:  pkgconfig(systemd)
BuildRequires:  glslang
BuildRequires:  pkgconfig(libliftoff)
BuildRequires:  libdisplay-info-devel
BuildRequires:  pkgconfig(hwdata)
BuildRequires:  hwdata
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(wlr-protocols)
BuildRequires:  systemd-devel
BuildRequires:  pam-devel
BuildRequires:  libXau-devel
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  mesa-libgbm-devel
BuildRequires:  libdrm-devel
BuildRequires:  libinput-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  pixman-devel
BuildRequires:  vulkan-loader-devel
BuildRequires:  lcms2-devel
BuildRequires:  libliftoff-devel

Requires:       ddm
Requires:       dde-session
Requires:       deepin-wayland-protocols
Requires:       treeland-protocols

%description
Treeland is the Wayland compositor and window manager of the Deepin desktop
environment.  It integrates with DDM for the greeter and lock screen.

%prep
%autosetup -n treeland-%{version} -p1

%build
%cmake -GNinja \
  -DWITH_SUBMODULE_WAYLIB=ON \
  -DDISABLE_DDM=OFF \
  -DDISABLE_XWAYLAND=OFF \
  -DEXT_SESSION_LOCK_V1=ON \
  -DBUILD_TREELAND_PROTOCOL_TESTS=OFF \
  -DBUILD_TREELAND_EXAMPLES=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSES/
%doc README.md
%{_bindir}/treeland
%{_bindir}/treeland-debug
%{_bindir}/treeland.sh
%{_bindir}/treeland-user-wrapper
%{_bindir}/treeland-wallpaper-factory
%{_libexecdir}/treeland-screensaver
%{_libexecdir}/treeland-sd
%{_libexecdir}/treeland-session-helper
%{_libexecdir}/treeland-xwayland
%{_libdir}/libtreeland.so.0*
%{_libdir}/libtreeland-protocol-capture-v1.so.0*
%{_libdir}/libwaylib-wlroots.so.0*
%{_libdir}/libwaylibserver.so.0*
%{_libdir}/treeland/plugins/liblockscreen.so
%{_libdir}/treeland/plugins/libmultitaskview.so
%{_datadir}/treeland/
%{_datadir}/wayland-sessions/treeland.desktop
%{_datadir}/wayland-sessions/treeland-user.desktop
%{_datadir}/dsg/configs/org.deepin.dde.treeland/
%{_datadir}/dbus-1/interfaces/org.freedesktop.ScreenSaver.xml
%{_datadir}/polkit-1/actions/org.deepin.dde.treeland-debug.policy
%{_datadir}/dbus-1/system.d/org.deepin.compositor1.conf
%{_unitdir}/treeland.service
%{_userunitdir}/treeland.service
%{_userunitdir}/treeland.service.d/xwayland.conf
%{_userunitdir}/treeland-session-helper.service
%{_userunitdir}/treeland-screensaver.service
%{_userunitdir}/treeland-sd.socket
%{_userunitdir}/treeland-sd.service
%{_userunitdir}/treeland-xwayland.socket
%{_userunitdir}/treeland-xwayland.service
%{_userunitdir}/treeland-session-shutdown.service
%{_userunitdir}/dde-session-pre.target.wants/treeland-sd.service
%{_userunitdir}/dde-session-pre.target.wants/treeland-sd.socket
%{_userunitdir}/dde-session-pre.target.wants/treeland-xwayland.service
%{_userunitdir}/dde-session-pre.target.wants/treeland-xwayland.socket
%{_userunitdir}/dde-session-pre.target.wants/treeland.service
%{_userunitdir}/dde-session-shutdown.target.wants/treeland-session-shutdown.service
%{_userunitdir}/treeland.service.wants/

%post
%systemd_post treeland.service
%systemd_user_post treeland.service treeland-sd.socket treeland-xwayland.socket

%preun
%systemd_preun treeland.service
%systemd_user_preun treeland.service treeland-sd.socket treeland-xwayland.socket

%postun
%systemd_postun_with_restart treeland.service
%systemd_user_postun_with_restart treeland.service

%changelog
* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 0.12.0-10
- Avoid the gen_pnpids.sh here-document, which fails under the mock
  build shell.

* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 0.12.0-9
- Require the hwdata package for pnp.ids.

* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 0.12.0-8
- Add mpv-devel and pkgconfig(systemd).

* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 0.12.0-7
- Add Qt6HttpServer for treeland-debug.

* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 0.12.0-6
- Add Qt6GuiPrivate/Qt6CorePrivate.

* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 0.12.0-5
- Add the Xwayland xcb module set.

* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 0.12.0-4
- Add glslang for the Vulkan renderer.

* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 0.12.0-3
- Add the full XCB dependency set and xwayland for the X11 backend.

* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 0.12.0-2
- Require libdisplay-info-devel and hwdata-devel.

* Sat Nov 21 2026 mozixun <mozixun@fedoraproject.org> - 0.12.0-1
- Initial Fedora package.