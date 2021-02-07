Summary:	Window manager
Name:		awesome
Version:	4.3
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		https://awesomewm.org/
Source0:	https://github.com/awesomeWM/awesome-releases/raw/master/%{name}-%{version}.tar.xz
#Patch0:		awesome-3.5.2-link.patch
Patch1:   3065.patch
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	gperf
BuildRequires:	imagemagick
BuildRequires:	asciidoc xmlto doxygen
BuildRequires:	docbook-dtd45-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	lua-lgi
BuildRequires:	luadoc
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(cairo-xcb)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(imlib2)
BuildRequires:	pkgconfig(libev)
BuildRequires:	pkgconfig(libstartup-notification-1.0) >= 0.10
BuildRequires:	pkgconfig(libxdg-basedir)
#BuildRequires:	pkgconfig(lua)
BuildRequires:	lua5.3-devel
BuildRequires:	lua5.3
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
# for wallpaper setting handling
Requires:	feh
Requires:	lua-lgi
Requires:	typelib(cairo)
Requires:	typelib(Pango)
Requires:	typelib(PangoCairo)
Requires:	xterm

%description
awesome is a tiling window manager initialy based on a dwm code rewriting.
It's extremely fast, small, dynamic and awesome.

Windows can be managed in several layouts: tiled, maximized and floating.
Each layout can be applied on the fly, optimizing the environment for
the application in use and the task performed.

Managing windows in tiled mode assures that no space will be wasted on
your screen. No gaps, no overlap.

%files -f %{name}.lang
%doc LICENSE AUTHORS README build/awesomerc.lua
%{_bindir}/aw*
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*
%{_datadir}/%{name}
%{_datadir}/xsessions/awesome.desktop
%config(noreplace) %{_sysconfdir}/X11/wmsession.d/19awesome
%config(noreplace) %{_sysconfdir}/xdg/awesome/rc.lua

#----------------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1
%cmake -DXDG_CONFIG_DIR:PATH=%{_sysconfdir}/xdg -G Ninja

%build
%ninja -C build

%install
%ninja_install -C build

mkdir -p %{buildroot}%{_sysconfdir}/X11/wmsession.d/
cat > %{buildroot}%{_sysconfdir}/X11/wmsession.d/19awesome << EOF
NAME=awesome
EXEC=/usr/bin/awesome
DESC=awesome window manager
SCRIPT:
exec /usr/bin/awesome
EOF

%find_lang %{name} --with-man --all-name

