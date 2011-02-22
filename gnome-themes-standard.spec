Summary:	Default themes for GNOME environment
Summary(pl.UTF-8):	Domyślne motywy dla środowiska GNOME
Name:		gnome-themes-standard
Version:	2.91.90
Release:	1
License:	LGPL
Group:		Themes
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-themes-standard/2.91/%{name}-%{version}.tar.bz2
# Source0-md5:	e2f2817ba34b7a3c3609bf4431ff50b6
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	intltool >= 0.36.1
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
Requires:	gnome-icon-theme >= 2.91.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Default themes for GNOME environment.

%description -l pl.UTF-8
Domyślne motywy dla środowiska GNOME.

%prep
%setup -q

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gtk-3.0/3.0.0/theming-engines/libadwaita.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-3.0/3.0.0/theming-engines/libadwaita.so
%{_datadir}/themes/Adwaita
%{_datadir}/gnome-background-properties/adwaita.xml
%{_iconsdir}/Adwaita
