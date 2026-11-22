Name:           deepin-voice-note
Version:        6.6.7
Release:        1%{?dist}
Summary:        Voice and text note application for the Deepin desktop

License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/deepin-voice-note
Source0:        %{url}/archive/%{version}/deepin-voice-note-%{version}.tar.gz
Patch0:         https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/deepin-voice-note/01-fedora-build-fixes.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  qt6-linguist
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6WebEngineQuick)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(Dtk6Widget)
BuildRequires:  cmake(Dtk6Gui)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libvlc)
BuildRequires:  pkgconfig(gstreamer-1.0)

Requires:       dtk6widget
Requires:       gstreamer1-plugins-good
Requires:       qt6-qtmultimedia
Requires:       qt6-qtwebengine
Requires:       vlc
Requires:       hicolor-icon-theme
Recommends:     deepin-manual

%description
Deepin Voice Notes is a lightweight memo application that combines text
notes with voice recordings.  Recordings can be saved as audio files and
the notes can be searched from the main window.

%prep
%autosetup -n deepin-voice-note-%{version} -p1

%build
%cmake -GNinja
%cmake_build

%install
%cmake_install
# These are browser assets, not command-line tools; drop their node shebangs
# so rpmlint does not treat the data files as non-executable scripts.
sed -i '1{/^#!/d}' \
  %{buildroot}%{_datadir}/deepin-voice-note/tiptap/validate-envelope.mjs \
  %{buildroot}%{_datadir}/deepin-voice-note/web/css/createfont/createfont.js

%files
%license LICENSE
%doc README.md
%{_bindir}/deepin-voice-note
%{_datadir}/applications/deepin-voice-note.desktop
%{_datadir}/dbus-1/services/org.deepin.voicenote.service
%{_datadir}/deepin-voice-note/
%{_datadir}/deepin-manual/manual-assets/application/deepin-voice-note/
%{_datadir}/dsg/configs/org.deepin.voice-note/
%{_datadir}/icons/hicolor/scalable/apps/deepin-voice-note.svg

%changelog
* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 6.6.7-1
- Initial Fedora package.
