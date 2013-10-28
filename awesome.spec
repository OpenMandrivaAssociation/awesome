Name:		awesome
#fwang: 2.4 requires cairo-xcb which does not exist any more
Version:	3.5.2
Release:	1
Source0:	http://awesome.naquadah.org/download/%{name}-%{version}.tar.bz2
URL:		http://awesome.naquadah.org/
Summary:	Window manager
License:	GPLv2+
Group:		Graphical desktop/Other
BuildRequires:	cmake
BuildRequires:	gperf
BuildRequires:	imagemagick
BuildRequires:	asciidoc xmlto doxygen
BuildRequires:	docbook-dtd45-xml
BuildRequires:	luadoc
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(imlib2)
BuildRequires:	pkgconfig(pangocairo)
BuildRequires:	pkgconfig(lua)
BuildRequires:	lua-lgi
BuildRequires:	pkgconfig(xcb-keysyms) >= 0.3.4
BuildRequires:	pkgconfig(xcb-icccm) >= 0.3.8
BuildRequires:	pkgconfig(xcb-image) >= 0.3.0
BuildRequires:	pkgconfig(xcb-cursor)
BuildRequires:	pkgconfig(libxdg-basedir) >= 1.0.0
BuildRequires:	pkgconfig(libstartup-notification-1.0) >= 0.10
BuildRequires:	pkgconfig(libev)

%description
awesome is a tiling window manager initialy based on a dwm code rewriting.
It's extremely fast, small, dynamic and awesome.

Windows can be managed in several layouts: tiled, maximized and floating.
Each layout can be applied on the fly, optimizing the environment for
the application in use and the task performed.

Managing windows in tiled mode assures that no space will be wasted on
your screen. No gaps, no overlap.

%prep
%setup -q
%apply_patches

%build
#configure2_5x
%cmake -DXDG_CONFIG_DIR:PATH=%{_sysconfdir}/xdg
%make

%install
pushd build
%makeinstall_std
popd

%{__mkdir_p} %{buildroot}%{_sysconfdir}/X11/wmsession.d/
cat > %{buildroot}%{_sysconfdir}/X11/wmsession.d/19awesome << EOF
NAME=awesome
EXEC=/usr/bin/awesome
DESC=awesome window manager
SCRIPT:
exec /usr/bin/awesome
EOF

%find_lang %{name} --all-name --with-man

%files -f %{name}.lang
%doc LICENSE AUTHORS README build/awesomerc.lua
%{_bindir}/aw*
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*
%{_datadir}/%{name}
%{_datadir}/xsessions/awesome.desktop
%config(noreplace) %{_sysconfdir}/X11/wmsession.d/19awesome
%config(noreplace) %{_sysconfdir}/xdg/awesome/rc.lua


%changelog
* Sun Mar 13 2011 Funda Wang <fwang@mandriva.org> 2.3.6-2mdv2011.0
+ Revision: 644124
- BR dtd45
- add warning on new versions

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.0 packages

* Wed May 27 2009 Funda Wang <fwang@mandriva.org> 2.3.6-1mdv2010.0
+ Revision: 380044
- New version 2.3.6

* Fri Jan 02 2009 Jérôme Soyer <saispo@mandriva.org> 2.3.5-1mdv2009.1
+ Revision: 323483
- Add files'
- New upstream update

* Tue Aug 26 2008 Jérôme Soyer <saispo@mandriva.org> 2.3.4-1mdv2009.0
+ Revision: 276165
- New release 2.3.4

* Sun Jul 27 2008 Funda Wang <fwang@mandriva.org> 2.3.3-1mdv2009.0
+ Revision: 250392
- update to new version 2.3.3

* Wed Jun 25 2008 Funda Wang <fwang@mandriva.org> 2.3.2-1mdv2009.0
+ Revision: 228839
- New version 2.3.2

* Wed Jun 04 2008 Funda Wang <fwang@mandriva.org> 2.3.1-1mdv2009.0
+ Revision: 214955
- update to new version 2.3.1

* Wed May 07 2008 Funda Wang <fwang@mandriva.org> 2.3-1mdv2009.0
+ Revision: 202713
- BR imlib2-devel
- BR doxygen
- BR pango
- New version 2.3

* Fri Feb 15 2008 Nicolas Vigier <nvigier@mandriva.com> 2.1-1mdv2008.1
+ Revision: 169011
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - fix summary-not-capitalized
    - fix no-buildroot-tag

* Mon Dec 17 2007 Nicolas Vigier <nvigier@mandriva.com> 2.0-1mdv2008.1
+ Revision: 124705
- import awesome


