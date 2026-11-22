Name:           deepin-font-manager
Version:        6.5.44
Release:        1%{?dist}
Summary:        Font manager for the Deepin desktop environment

License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/deepin-font-manager
Source0:        %{url}/archive/%{version}/deepin-font-manager-%{version}.tar.gz
Patch0:         https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/deepin-font-manager/01-qt6-moc-iid.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  qt6-linguist
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Dtk6Widget)
BuildRequires:  cmake(Dtk6Gui)
BuildRequires:  cmake(dfm6-base)
BuildRequires:  dde-file-manager-devel
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)

Requires:       dde-file-manager
Requires:       dtk6widget
Requires:       hicolor-icon-theme
Recommends:     deepin-manual

%description
Deepin Font Manager is a font management tool for the Deepin desktop.  It
can search, install, enable, disable and delete fonts, preview fonts with
custom text and sizes, and provides a preview plugin for the file manager.

%prep
%autosetup -n deepin-font-manager-%{version} -p1

%build
%cmake -GNinja
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/deepin-font-manager
%{_libdir}/dde-file-manager/plugins/previews/libdeepin-font-preview-plugin.so
%{_datadir}/applications/deepin-font-manager.desktop
%{_datadir}/deepin-font-manager/
%{_datadir}/deepin-manual/manual-assets/application/deepin-font-manager/
%{_datadir}/icons/hicolor/scalable/apps/deepin-font-manager.svg

%changelog
* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 6.5.44-1
- Initial Fedora package.
