Name:           dde-polkit-agent
Version:        6.0.25
Release:        2%{?dist}
Summary:        PolicyKit authentication agent for DDE
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dde-polkit-agent
Source0:        %{url}/archive/%{version}/dde-polkit-agent-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(Dtk6Widget)
BuildRequires:  cmake(Dtk6Tools)
BuildRequires:  cmake(DDEShell)
BuildRequires:  pkgconfig(polkit-qt6-1)

Requires:       polkit
Requires:       dde-shell
Requires:       dde-session

%description
dde-polkit-agent is the PolicyKit authentication agent used by the DDE
session and by privileged DDE applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the dde-polkit-agent extension headers.

%prep
%autosetup -n dde-polkit-agent-%{version} -p1

%build
%cmake -GNinja
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_prefix}/lib/polkit-1-dde/dde-polkit-agent
%{_datadir}/dde-polkit-agent/

%files devel
%{_includedir}/dpa/

%changelog
* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 6.0.25-2
- Add Qt6Qml/Qt6Quick required by DDEShellConfig.

* Sat Nov 21 2026 mozixun <mozixun@fedoraproject.org> - 6.0.25-1
- Initial Fedora package.
