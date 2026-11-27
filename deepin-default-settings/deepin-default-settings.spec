Name:           deepin-default-settings
Version:        1.0.0
Release:        3%{?dist}
Summary:        Fedora-safe Deepin skel and XDG defaults
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/deepin-default-settings
Source0:        %{url}/archive/%{version}/deepin-default-settings-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/02e1bdb0b632479ff9d20479982c5abbba7abf84/deepin-default-settings/40-fedora-treeland-background.json
Source2:        https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/02e1bdb0b632479ff9d20479982c5abbba7abf84/deepin-default-settings/40-fedora-appearance-background.json
BuildArch:      noarch

BuildRequires:  make

Requires:       dde-file-manager-desktop
Requires:       xdg-user-dirs
Requires:       desktop-backgrounds-basic

%description
This package installs the Fedora-safe subset of the Deepin default settings:
the skel Desktop symlinks for Computer and Trash, the XDG user directory
configuration and the Deepin font configuration metadata. It also selects
a Fedora-packaged default wallpaper for Treeland and DDE appearance without
resetting existing users' wallpaper choices.

Distribution-wide files (PAM, sudoers, X11, sysctl, /etc/lsb-release and
LightDM) are intentionally not installed by this package.

%prep
%autosetup -n deepin-settings-default-%{version} -p1

%build
# Data-only package; make build is not needed on Fedora.

%install
install -d %{buildroot}%{_sysconfdir}/skel/Desktop
cp -a skel/Desktop/. %{buildroot}%{_sysconfdir}/skel/Desktop/
install -Dm644 skel/.config/user-dirs.dirs %{buildroot}%{_sysconfdir}/skel/.config/user-dirs.dirs
install -Dm644 usr.share.d/deepin-default-settings/fontconfig.json \
  %{buildroot}%{_datadir}/deepin-default-settings/fontconfig.json

install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/dsg/configs/overrides/org.deepin.dde.treeland/org.deepin.dde.treeland.user/40-fedora-dde-background.json
install -Dm644 %{SOURCE2} %{buildroot}%{_datadir}/dsg/configs/overrides/org.deepin.dde.appearance/org.deepin.dde.appearance/40-fedora-dde-background.json

%files
%license LICENSE
%doc README.md
%config(noreplace) %{_sysconfdir}/skel/Desktop/
%config(noreplace) %{_sysconfdir}/skel/.config/user-dirs.dirs
%{_datadir}/deepin-default-settings/fontconfig.json

%dir %{_datadir}/dsg
%dir %{_datadir}/dsg/configs
%dir %{_datadir}/dsg/configs/overrides
%dir %{_datadir}/dsg/configs/overrides/org.deepin.dde.treeland
%dir %{_datadir}/dsg/configs/overrides/org.deepin.dde.treeland/org.deepin.dde.treeland.user
%{_datadir}/dsg/configs/overrides/org.deepin.dde.treeland/org.deepin.dde.treeland.user/40-fedora-dde-background.json
%dir %{_datadir}/dsg/configs/overrides/org.deepin.dde.appearance
%dir %{_datadir}/dsg/configs/overrides/org.deepin.dde.appearance/org.deepin.dde.appearance
%{_datadir}/dsg/configs/overrides/org.deepin.dde.appearance/org.deepin.dde.appearance/40-fedora-dde-background.json

%changelog
* Fri Nov 27 2026 Fedora DDE Remix contributors - 1.0.0-3
- Select a packaged JPEG wallpaper for Treeland and DDE appearance defaults.
- Preserve existing user choices through distribution DConfig overrides.

* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 1.0.0-2
- Match the upstream archive top-level directory (deepin-settings-default).

* Sat Nov 21 2026 mozixun <mozixun@fedoraproject.org> - 1.0.0-1
- Initial Fedora package (Fedora-safe data subset).
