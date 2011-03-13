Name:		awesome
#fwang: 2.4 requires cairo-xcb which does not exist any more
Version:	2.3.6
Release:	%mkrel 2
Source:		http://awesome.naquadah.org/download/awesome-%{version}.tar.bz2
URL:		http://awesome.naquadah.org/
Summary:	Window manager
License:	GPLv2+
Group:		Graphical desktop/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libx11-devel libxext-devel libxrandr-devel libxinerama-devel
BuildRequires:	confuse-devel libxft-devel zlib-devel freetype2-devel
BuildRequires:	libcairo-devel asciidoc xmlto pango-devel doxygen imlib2-devel
BuildRequires:	docbook-dtd45-xml

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

%build
%configure2_5x
%make

%install
%{__rm} -Rf %{buildroot}
%makeinstall_std

%{__mkdir_p} %{buildroot}%{_sysconfdir}/X11/wmsession.d/
cat > %{buildroot}%{_sysconfdir}/X11/wmsession.d/19awesome << EOF
NAME=awesome
EXEC=/usr/bin/awesome
DESC=awesome window manager
SCRIPT:
exec /usr/bin/awesome
EOF

%post
%make_session

%postun
%make_session

%files
%doc LICENSE AUTHORS README awesomerc
%{_bindir}/%{name}
%{_bindir}/%{name}-client
%{_bindir}/%{name}-menu
%{_bindir}/%{name}-message
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/%{name}rc.5*
%{_mandir}/man1/%{name}-client.1*
%{_mandir}/man1/%{name}-menu.1*
%{_mandir}/man1/%{name}-message.1*
%{_datadir}/%{name}/icons/layouts/*
%{_datadir}/%{name}/icons/*.png
%config(noreplace) %{_sysconfdir}/X11/wmsession.d/19awesome
