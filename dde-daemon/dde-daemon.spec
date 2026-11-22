%global debug_package %{nil}

Name:           dde-daemon
Version:        6.2.1
Release:        3%{?dist}
Summary:        Daemon handling the DDE session settings
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dde-daemon
Source0:        %{url}/archive/%{version}/dde-daemon-%{version}.tar.gz
Patch0:         https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/dde-daemon/01-skip-policy-regeneration.patch
Source1:        https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/dde-daemon/90-dde-daemon.preset

BuildRequires:  golang
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  gettext
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(ddcutil)
BuildRequires:  librsvg2-tools
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libgudev-1.0)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xi)

Requires:       deepin-desktop-base
Requires:       deepin-desktop-schemas
Requires:       dde-api
Requires:       dde-session
Requires:       dde-polkit-agent
Requires:       gvfs
Requires:       bluez
Requires:       rfkill
Recommends:     lshw
Recommends:     iso-codes
Recommends:     mobile-broadband-provider-info

%description
dde-daemon handles session and system settings for the Deepin desktop
environment: accounts, audio, Bluetooth, display, input devices, power,
timedate, tray icons and related D-Bus services.

%prep
%autosetup -n dde-daemon-%{version} -p1

%build
for f in misc/polkit-action/*.policy.in; do cp "$f" "${f%.in}"; done
export GO111MODULE=on
export GOFLAGS="-mod=mod"
export GOPATH=%{_builddir}/gopath
%make_build BUILD_TAGS=noscheduler GOBUILD_OPTIONS=

%install
export GO111MODULE=on
export GOFLAGS="-mod=mod"
export GOPATH=%{_builddir}/gopath
%make_install BUILD_TAGS=noscheduler GOBUILD_OPTIONS=
install -Dm644 %{SOURCE1} %{buildroot}%{_presetdir}/90-dde-daemon.preset
mkdir -p %{buildroot}%{_unitdir} %{buildroot}%{_userunitdir}
mv %{buildroot}/lib/systemd/system/* %{buildroot}%{_unitdir}/ 2>/dev/null || :
mv %{buildroot}/lib/systemd/user/* %{buildroot}%{_userunitdir}/ 2>/dev/null || :

# Fedora does not use the Debian/Deepin GRUB helpers or LightDM.
rm -rf %{buildroot}%{_sysconfdir}/grub.d
rm -rf %{buildroot}%{_sysconfdir}/default/grub.d
rm -f  %{buildroot}%{_prefix}/lib/deepin-daemon/grub2
rm -f  %{buildroot}%{_datadir}/lightdm/lightdm.conf.d/60-deepin.conf
rm -f  %{buildroot}%{_unitdir}/deepin-grub2.service

%files
%license LICENSE
%doc README.md
%{_prefix}/lib/deepin-daemon/
%{_libexecdir}/deepin/dde-session-daemon
%{_libexecdir}/deepin/langselector
%{_datadir}/dde-daemon/
%{_datadir}/deepin/scheduler/
%{_datadir}/dde/
%{_datadir}/dbus-1/services/org.deepin.*.service
%{_datadir}/dbus-1/system-services/org.deepin.*.service
%{_datadir}/dbus-1/system.d/org.deepin.*.conf
%{_datadir}/polkit-1/actions/org.deepin.*.policy
%{_datadir}/polkit-1/rules.d/org.deepin.*.rules
%{_datadir}/dsg/configs/org.deepin.dde.daemon/
%{_datadir}/dsg/configs/org.deepin.dde.lightdm-deepin-greeter/
%{_datadir}/glib-2.0/schemas/com.deepin.dde.display.gschema.xml
%{_datadir}/icons/hicolor/
%{_datadir}/locale/*/LC_MESSAGES/dde-daemon.mo
%config(noreplace) %{_sysconfdir}/pam.d/deepin-auth-keyboard
%config(noreplace) %{_sysconfdir}/deepin/
%config(noreplace) %{_sysconfdir}/pulse/daemon.conf.d/
%{_unitdir}/dde-backlight-helper.service
%{_unitdir}/dde-greeter-setter.service
%{_unitdir}/dde-lock-service.service
%{_unitdir}/dde-system-daemon.service
%{_presetdir}/90-dde-daemon.preset
%{_userunitdir}/org.dde.session.Daemon1.service
%{_userunitdir}/org.deepin.dde.SoundEffect1.service
%{_userunitdir}/dde-display-task-refresh-brightness.service
%{_userunitdir}/dde-session-initialized.target.wants/dde-display-task-refresh-brightness.service
%{_userunitdir}/dde-session-pre.target.wants/org.dde.session.Daemon1.service

%post
%systemd_post dde-system-daemon.service dde-lock-service.service dde-greeter-setter.service dde-backlight-helper.service
glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :

%preun
%systemd_preun dde-system-daemon.service dde-lock-service.service dde-greeter-setter.service dde-backlight-helper.service

%postun
%systemd_postun_with_restart dde-system-daemon.service dde-lock-service.service dde-greeter-setter.service dde-backlight-helper.service
glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :

%changelog
* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 6.2.1-3
- Use a raw URL for the systemd preset so COPR spec builds work.

* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 6.2.1-2
- Enable dde-system-daemon.service from the dde-daemon package preset.

* Sat Nov 21 2026 mozixun <mozixun@fedoraproject.org> - 6.2.1-1
- Initial Fedora package.
