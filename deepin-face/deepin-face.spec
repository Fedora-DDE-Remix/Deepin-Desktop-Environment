Name:           deepin-face
Version:        2.0.18
Release:        1%{?dist}
Summary:        Face recognition service for Deepin authentication
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/deepin-face
Source0:        %{url}/archive/%{version}/deepin-face-%{version}.tar.gz
Patch0:         https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/deepin-face/01-fedora-paths.patch

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtmultimedia-devel
BuildRequires:  qt6-linguist
BuildRequires:  dtk6core-devel
BuildRequires:  dtk6widget-devel
BuildRequires:  seetaface-open-role-zoo-devel
BuildRequires:  seetaface-tennis-devel
BuildRequires:  seetaface-authorize-devel
BuildRequires:  seetaface-boxes-devel
BuildRequires:  seetaface-landmarker-devel
BuildRequires:  seetaface-anti-spoofing-x-devel
BuildRequires:  seetaface-tracker-devel
BuildRequires:  seetaface-recognizer-devel
BuildRequires:  seetaface-pose-estimation-devel
BuildRequires:  seetaface-quality-assessor-devel

Requires:       dde-api
Requires:       seetaface-models
Requires:       seetaface-boxes
Requires:       seetaface-landmarker
Requires:       seetaface-anti-spoofing-x
Requires:       seetaface-tracker
Requires:       seetaface-recognizer
Requires:       seetaface-pose-estimation
Requires:       seetaface-quality-assessor
Requires:       seetaface-authorize
Requires:       seetaface-tennis
Requires:       seetaface-open-role-zoo

%description
deepin-face is the facial recognition service used by the Deepin
authentication stack.  It exposes org.deepin.dde.Face1 and uses the
SeetaFace engine and models.

%prep
%autosetup -n deepin-face-%{version} -p1
sed -i 's|systemd.path = /lib/systemd/system/|systemd.path = /usr/lib/systemd/system/|' deepin-face.pro

%build
%qmake_qt6
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}
install -Dm644 debian/tmpfiles %{buildroot}%{_tmpfilesdir}/deepin-face.conf

%post
%systemd_post deepin-face.service

%preun
%systemd_preun deepin-face.service

%postun
%systemd_postun_with_restart deepin-face.service

%files
%license LICENSE
%doc README.md
%{_libexecdir}/deepin-face
%{_datadir}/dbus-1/system.d/org.deepin.dde.Face1.conf
%{_datadir}/dbus-1/system-services/org.deepin.dde.Face1.service
%{_datadir}/deepin-authentication/interfaces/deepin-face-driver.json
%{_unitdir}/deepin-face.service
%{_tmpfilesdir}/deepin-face.conf
%ghost %{_localstatedir}/log/deepin-face.log

%changelog
* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 2.0.18-1
- Initial Fedora package.
