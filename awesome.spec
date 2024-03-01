%global lua_version 5.3

Summary:	Window manager
Name:		awesome
Version:	4.3
Release:	2
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		https://awesomewm.org/
Source0:	https://github.com/awesomeWM/awesome-releases/raw/master/%{name}-%{version}.tar.xz
Source1:    19awesome
Source2:    theme.lua
# Upstream patch, from here https://github.com/awesomeWM/awesome/pull/3065 rebased by OpenSUSE for current stable

Patch0:   awesome-om-branding.patch
Patch1:   awesome-enable-xcompmgr.patch
# Fix for duplicate symbol #GCC10
Patch2:   001-extern-vars-declaration-fix-gcc10.patch

BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	gperf
BuildRequires:	imagemagick
BuildRequires:	asciidoc
BuildRequires:  xmlto
BuildRequires:  doxygen
BuildRequires:  asciidoctor
BuildRequires:	docbook-dtd45-xml
BuildRequires:	docbook-style-xsl
# Make sure to use always same Lua version to build awesome and lua-lgi.
BuildRequires:	lua%{lua_version}-devel
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(cairo-xcb)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(imlib2)
BuildRequires:	pkgconfig(libev)
BuildRequires:	pkgconfig(libstartup-notification-1.0) >= 0.10
BuildRequires:	pkgconfig(libxdg-basedir)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(pangocairo)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(xcb-cursor)
BuildRequires:	pkgconfig(xcb-icccm)
BuildRequires:	pkgconfig(xcb-image)
BuildRequires:	pkgconfig(xcb-keysyms)
BuildRequires:	pkgconfig(xcb-randr)
BuildRequires:	pkgconfig(xcb-shape)
BuildRequires:	pkgconfig(xcb-util)
BuildRequires:	pkgconfig(xcb-xinerama)
BuildRequires:	pkgconfig(xcb-xtest)
BuildRequires:  pkgconfig(xcb-xrm)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(zlib)

Requires:	lua%{lua_version}-lgi
Requires:   luadoc
Requires:	typelib(cairo)
Requires:	typelib(Pango)
Requires:	typelib(PangoCairo)
Requires: typelib(GLib)
Requires: typelib(Gio)
Requires:	xterm
Requires: xcompmgr

# for wallpaper setting handling
Suggests:	feh

%description
awesome is a tiling window manager initialy based on a dwm code rewriting.
It's extremely fast, small, dynamic and awesome.

Windows can be managed in several layouts: tiled, maximized and floating.
Each layout can be applied on the fly, optimizing the environment for
the application in use and the task performed.

Managing windows in tiled mode assures that no space will be wasted on
your screen. No gaps, no overlap.

%files
%doc LICENSE build/awesomerc.lua 00-authors.md 01-readme.md 02-contributing.md
%{_bindir}/aw*
%{_mandir}/*/man1/*
%{_mandir}/*/man5/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_datadir}/%{name}
%{_datadir}/xsessions/awesome.desktop
%config(noreplace) %{_sysconfdir}/X11/wmsession.d/19awesome
%config(noreplace) %{_sysconfdir}/xdg/awesome/rc.lua

#----------------------------------------------------------------------------

%prep
%autosetup -p1
%cmake -G Ninja \
        -DXDG_CONFIG_DIR:PATH=%{_sysconfdir}/xdg \
        -DCMAKE_BUILD_TYPE=Release

%build
%ninja_build -C build

%install
%ninja_install -C build

mkdir -p %{buildroot}%{_sysconfdir}/X11/wmsession.d/
install -D -m644 %{S:2} %{buildroot}%{_sysconfdir}/X11/wmsession.d
mkdir -p %{buildroot}%{_datadir}/awesome/themes/OpenMandriva
cp -R %{buildroot}%{_datadir}/awesome/themes/default/* %{buildroot}%{_datadir}/awesome/themes/OpenMandriva
install -D -m644 %{S:1} %{buildroot}%{_datadir}/awesome/themes/OpenMandriva

