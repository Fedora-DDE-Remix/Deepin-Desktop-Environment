# Fedora DDE / Deepin RPM specs

This directory contains one RPM spec directory per upstream source repository.
The directory name always matches the upstream Git repository name; the spec
file name follows the Fedora binary/source package name.

## Conventions

- Target: Fedora 45, x86_64 and aarch64, COPR (`mozixun/Fedora-DDE-Remix`).
- 71 source packages in total, plus the dde-desktop comps group, including
the SeetaFace stack used by
  `deepin-face`, the OCR engine and the Deepin applications.
- Qt 6 only. DTK 5 (Qt 5) builds are explicitly disabled with `-DDTK5=OFF`.
- Package names follow Fedora where Fedora already has a package
  (`dtk6core`, `dtk6gui`, `dtk6widget`, `dtk6declarative`, `dtk6log`,
  `deepin-terminal`, `deepin-desktop-base`, `deepin-desktop-schemas`).
- New packages follow the upstream project / DDE Debian binary names
  (`dde-*`, `treeland`, `ddm`, `dtk6systemsettings`, ...).
- DTK modules are never merged into one package.  `dtkcore`, `dtkdeclarative`,
  `dtkgui`, `dtkwidget` etc. each have their own directory and spec.
- Build-time compatibility fixes are kept in the spec (`%build` flags) or in
  `*.patch` files next to the spec.  No behavioural DDE source change is
  carried by the resulting packages.
- Every `PatchN:` tag points at the raw GitHub URL of the patch in this
  repository (`.../refs/heads/main/<repo>/<patch>`); the same `.patch` file is
  kept next to the spec for local builds and `spectool -g`.
- Fedora 45 provides newer Qt (6.11.2) than the Fedora 44 DTK specs; the DTK
  specs here are therefore newer upstream releases (6.7.54) and supersede the
  older Fedora 44/rawhide `dtk6*` builds by EVR in COPR.

## Build order

The dependency order is:

```text
dtkcommon
dtk6log
dtk6core
treeland-protocols
deepin-wayland-protocols
dtk6gui
dtk6widget
dtk6declarative
dtk6systemsettings
gsettings-qt
openssl-compat
dareader
deepin-pw-check
dde-seatd
ddm
dde-desktop-comps
treeland
dde-api
dde-session
deepin-service-manager
dde-app-services
dde-services
dde-application-manager
dde-tray-loader
dde-shell
dde-launchpad
dde-polkit-agent
dde-appearance
dde-clipboard
udisks2-qt6
deepin-pdfium
deepin-ocr-plugin-manager
util-dfm
dde-file-manager
dde-control-center
deepin-fcitx5configtool-plugin
dde-qtintegration (deepin-qt6integration)
deepin-terminal
deepin-editor
dde-calendar
deepin-system-monitor
deepin-voice-note
deepin-font-manager
deepin-image-viewer
deepin-draw
deepin-reader
deepin-scanner
deepin-compressor
deepin-deepinid-client
deepin-account-faces
deepin-desktop-schemas
deepin-icon-theme
deepin-gtk-theme
deepin-sound-theme
deepin-desktop-base
deepin-default-settings
deepin-authenticate-compat
seetaface-open-role-zoo
seetaface-tennis
seetaface-authorize
seetaface-boxes
seetaface-landmarker
seetaface-anti-spoofing-x
seetaface-tracker
seetaface-recognizer
seetaface-pose-estimation
seetaface-quality-assessor
seetaface-models
deepin-face
```

`dde-control-center` build-depends on `deepin-pw-check-devel` and
`dareader-devel` for the accounts/authentication plugins, and on
`dde-shell-devel` for the Treeland integration.  Build those first.

`dde-desktop` is a comps group, not an RPM package.  It installs the complete
DDE Wayland desktop, including DDM, the session, the shell and the standard
applications.  It uses VLC for music, GNOME Logs for journal viewing and
Fedora Media Writer for USB image writing.

COPR's Pulp storage cannot publish comps metadata, so `dde-desktop-comps`
carries a small local comps repository and enables it.  Install the metadata
package first, then the group:

```text
sudo dnf copr enable mozixun/Fedora-DDE-Remix
sudo dnf install dde-desktop-comps
sudo dnf groupinstall dde-desktop
```

The group has no versioned package entries; components such as `dde-shell`
and `dde-tray-loader` can be updated independently.

## Source archives

Every `SourceN` and `PatchN` entry is a fully qualified https URL.  Upstream
tarballs come from the GitHub/GitLab tag archives; the small local helper files
(systemd presets, sysusers config, compat shims) are fetched from this spec
repository itself.  COPR can therefore build each package directly from its
online spec URL, with `%_disable_source_fetch` set to 0, without a prebuilt
SRPM.

`fcitx5-dde-integration` is intentionally not packaged as an RPM because it
replaces files owned by the Fedora `fcitx5` / `fcitx5-configtool` packages.
Apply it from the ISO kickstart or as a local integration step.

## Known Fedora-specific build workarounds

- `dde-api` rewrites its installed `DDEAPIConfig.cmake` so it does not add
  `/usr/include` as an explicit `-isystem` path.
- `dde-shell` carries two small CMake build patches: optional example plugins
  and removal of the redundant `/usr/include` from Fedora's
  `FindOpenGL`/`FindX11` imported targets.  It also builds with `-fPIE` and
  without deprecation-as-error.  These are Fedora build adaptations, not
  behavioural DDE changes.
- `deepin-fcitx5configtool-plugin` carries a build patch for Fedora fcitx5
  5.1.23 (C++20, Fcitx5 Utils include and `stringutils.h`) because upstream
  hard-codes C++17 in several subdirectories.
- `deepin-ocr-plugin-manager` and `deepin-image-viewer` build against the
  Fedora `opencv4.pc`/`ncnn` instead of the Debian `opencv_mobile` bundle.
  The OCR manager also drops the ncnn per-extractor Vulkan switch that
  current ncnn releases removed.
- `deepin-reader` builds against the system `deepin-pdfium`; the spec
  backports `fileIdentifier()`/`imageObjectRects()` into `deepin-pdfium`
  1.5.8-2.  OFD support is disabled because Fedora has no `rofd-ffi`.
  DOCX conversion uses Fedora's `pandoc-cli`.
- `deepin-scanner` rewrites the hard-coded `/lib/qt6/bin` `lupdate`/`lrelease`
  fallback to `%{_qt6_bindir}`.
- `deepin-system-monitor` uses the shipped translated polkit policy and
  desktop file; Fedora does not ship the Deepin `*-ts-convert` helpers.
- `deepin-voice-note` builds with Qt 6/DTK 6 and VLC; its translation script
  now finds Fedora's `lupdate-qt6`/`lrelease-qt6`, and a missing
  `<QJsonDocument>` include is fixed.
- `deepin-font-manager` needs the plugin factory IIDs defined in the
  translation unit for Qt 6.8+ moc and installs its preview plugin with
  `CMAKE_INSTALL_LIBDIR` so it lands in `/usr/lib64`.

See `UPSTREAM-ISSUES.md` for the corresponding upstream fixes.

## Notes

- `dde-daemon` is built unmodified.  Its `Makefile` already installs the real
  binaries to `/usr/libexec/deepin` and the upstream wrapper to
  `/usr/lib/deepin-daemon`; the spec only removes Fedora-incompatible GRUB and
  LightDM data from the buildroot.
- `treeland` vendors waylib and wlroots as git subtrees, so the normal GitHub
  archive is self-contained.  The generated `waylib-wlroots` and
  `waylibserver` libraries are declared as `bundled(...)`.
- OpenSSL 4 removed the legacy SM3/SM4 helper symbols.  `openssl-compat`
  provides provider-backed `EVP_sm3`, `EVP_sm4_cbc` and `EVP_sm4_ecb` with
  `OPENSSL_3.0.0` symbol versions, plus a build-time SM3 header.  `util-dfm` uses a one-line OpenSSL 3/4 API patch; the proprietary
  `deepin-authenticate` binaries use the library.
- `deepin-default-settings` is packaged as a Fedora-safe data subset: skel
  Desktop symlinks and `user-dirs.dirs`.  Distribution-wide files such as
  `/etc/lsb-release`, PAM, sudoers, X11 and sysctl configuration are not
  installed by the RPM.
- `deepin-desktop-base` intentionally does not ship `/etc/lsb-release`; Fedora
  owns that file.
