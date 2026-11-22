Name:           ddm
Version:        0.5.0
Release:        4%{?dist}
Summary:        Deepin Display Manager
License:        GPL-2.0-or-later
URL:            https://github.com/linuxdeepin/ddm
Source0:        %{url}/archive/%{version}/ddm-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/ddm/90-ddm.preset

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(Dtk6Tools)
BuildRequires:  cmake(TreelandProtocols) >= 0.5.3
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  systemd-devel
BuildRequires:  pam-devel
BuildRequires:  libXau-devel
BuildRequires:  wayland-devel

Requires:       accountsservice
Requires:       systemd
Requires:       systemd-pam
Requires:       pam

%description
DDM is the Deepin Display Manager, a Wayland greeter and session manager used
with the Treeland compositor.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains development files for %{name}.

%prep
%autosetup -n ddm-%{version} -p1

%build
%cmake -GNinja -DBUILD_MAN_PAGES=OFF -DWERROR=OFF
%cmake_build

%install
%cmake_install
install -Dm644 %{SOURCE1} %{buildroot}%{_presetdir}/90-ddm.preset

%post
%systemd_post ddm.service

%preun
%systemd_preun ddm.service

%postun
%systemd_postun_with_restart ddm.service

%files
%license LICENSES/
%doc README.md
%{_bindir}/ddm
%{_libexecdir}/ddm-helper
%{_unitdir}/ddm.service
%{_presetdir}/90-ddm.preset
%{_sysusersdir}/dde.conf
%{_tmpfilesdir}/ddm.conf
%config(noreplace) %{_sysconfdir}/pam.d/ddm
%config(noreplace) %{_sysconfdir}/pam.d/ddm-autologin
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.DisplayManager.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.deepin.DisplayManager.conf
%{_datadir}/ddm/
%{_datadir}/dsg/configs/org.deepin.dde.ddm/
%{_libdir}/libddm-common.so.0*

%files devel
%{_includedir}/ddm/
%{_libdir}/libddm-common.so
%{_libdir}/cmake/DDM/

%changelog
* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 0.5.0-4
- Use a raw URL for the systemd preset so COPR spec builds work.

* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 0.5.0-3
- Enable ddm.service from the ddm package preset.

* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 0.5.0-2
- Require systemd-pam for pam_systemd.so.

* Sat Nov 21 2026 mozixun <mozixun@fedoraproject.org> - 0.5.0-1
- Initial Fedora package.
