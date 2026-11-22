Name:           deepin-default-settings
Version:        1.0.0
Release:        2%{?dist}
Summary:        Fedora-safe Deepin skel and XDG defaults
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/deepin-default-settings
Source0:        %{url}/archive/%{version}/deepin-default-settings-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make

Requires:       dde-file-manager-desktop
Requires:       xdg-user-dirs

%description
This package installs the Fedora-safe subset of the Deepin default settings:
the skel Desktop symlinks for Computer and Trash, the XDG user directory
configuration and the Deepin font configuration metadata.

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

%files
%license LICENSE
%doc README.md
%config(noreplace) %{_sysconfdir}/skel/Desktop/
%config(noreplace) %{_sysconfdir}/skel/.config/user-dirs.dirs
%{_datadir}/deepin-default-settings/fontconfig.json

%changelog
* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 1.0.0-2
- Match the upstream archive top-level directory (deepin-settings-default).

* Sat Nov 21 2026 mozixun <mozixun@fedoraproject.org> - 1.0.0-1
- Initial Fedora package (Fedora-safe data subset).
