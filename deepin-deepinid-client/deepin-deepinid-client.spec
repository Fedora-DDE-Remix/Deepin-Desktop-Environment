Name:           deepin-deepinid-client
Version:        7.0.9
Release:        1%{?dist}
Summary:        Deepin ID account client
License:        LGPL-3.0-or-later
URL:            https://github.com/linuxdeepin/deepin-deepinid-client
Source0:        %{url}/archive/%{version}/deepin-deepinid-client-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6WebChannel)
BuildRequires:  cmake(Qt6WebEngineCore)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Dtk6Widget)
BuildRequires:  qt6-linguist

Requires:       qt6-qtwebengine

%description
Deepin ID client provides the account login UI and the D-Bus client used by
the Deepin Control Center and Deepin Home.

%prep
%autosetup -n deepin-deepinid-client-%{version} -p1

%build
%cmake -GNinja -DENABLE_QT6=ON
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/deepin-deepinid-client
%{_datadir}/dbus-1/services/com.deepin.deepinid.Client.service
%{_datadir}/deepin-deepinid-client/
%{_datadir}/icons/hicolor/128x128/apps/deepin-id.png

%changelog
* Sat Nov 21 2026 mozixun <mozixun@fedoraproject.org> - 7.0.9-1
- Initial Fedora package (Qt 6).
