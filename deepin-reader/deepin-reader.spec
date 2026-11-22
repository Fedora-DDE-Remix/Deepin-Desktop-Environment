Name:           deepin-reader
Version:        6.6.4
Release:        2%{?dist}
Summary:        Document viewer for the Deepin desktop environment

License:        GPL-3.0-or-later AND LGPL-3.0-or-later
URL:            https://github.com/linuxdeepin/deepin-reader
Source0:        %{url}/archive/%{version}/deepin-reader-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  qt6-linguist
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(Dtk6Widget)
BuildRequires:  cmake(Dtk6Gui)
BuildRequires:  deepin-pdfium-devel >= 1.5.8-2
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(ddjvuapi)
BuildRequires:  pkgconfig(deepin-pdfium)
BuildRequires:  pkgconfig(libgxps)
BuildRequires:  cups-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(freetype2)

Requires:       deepin-pdfium >= 1.5.8-2
Requires:       pandoc-cli
Requires:       qt6-qtwebengine
Requires:       qt6-qt5compat
Requires:       hicolor-icon-theme
Requires:       shared-mime-info
Recommends:     deepin-manual

%description
Deepin Document Viewer reads PDF, DjVu, XPS, OXPS, DOCX and plain-text
documents.  PDF rendering is provided by the Deepin PDF library.

%prep
%autosetup -n deepin-reader-%{version} -p1

%build
%cmake -GNinja \
  -DVERSION=%{version} \
  -DQT_VERSION_MAJOR=6 \
  -DDTK_VERSION_MAJOR=6 \
  -DUSE_PDFIUM_BUNDLE=OFF \
  -DOFD_SUPPORT=OFF \
  -DXPS_SUPPORT=ON \
  -DBUILD_TESTS=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/deepin-reader
%{_bindir}/deepin-reader-batchprint
%{_libdir}/deepin-reader/htmltopdf
%{_datadir}/applications/deepin-reader.desktop
%{_datadir}/applications/context-menus/deepin-reader-batchprint.conf
%{_datadir}/deepin-log-viewer/deepin-log.conf.d/org.deepin.reader.json
%{_datadir}/deepin-manual/manual-assets/application/deepin-reader/
%{_datadir}/deepin-reader/
%{_datadir}/dsg/configs/org.deepin.reader/
%{_datadir}/icons/hicolor/scalable/apps/deepin-reader.svg
%{_datadir}/mime/packages/xps.xml

%changelog
* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 6.6.4-2
- Add cups-devel for the batch print helper.

* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 6.6.4-1
- Initial Fedora package.
