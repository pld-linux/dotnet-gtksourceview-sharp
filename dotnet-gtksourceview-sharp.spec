Summary:	.NET language bindings for GtkSourceView
Summary(pl):	Wi±zania GtkSourceView dla .NET
Name:		dotnet-gtksourceview-sharp
Version:	0.5
Release:	1
License:	LGPL
Group:		Development/Libraries
Source0:	http://mono2.ximian.com/archive/1.0/gtksourceview-sharp-%{version}.tar.gz
# Source0-md5:	b82e767e42a542e185a534048db3078d
Patch0:		%{name}-install.patch
BuildRequires:	autoconf
BuildRequires:	automake >= 1.7
BuildRequires:	dotnet-gtk-sharp-devel >= 0.93
BuildRequires:	gtksourceview-devel >= 1.0.1
BuildRequires:	libtool
BuildRequires:	monodoc >= 0.16
BuildRequires:	mono-csharp
BuildRequires:	mono-devel >= 0.95
Requires:	gtksourceview >= 1.0.1
Requires:	dotnet-gtk-sharp
Provides:	gtksourceview-sharp
Obsoletes:	gtksourceview-sharp
Provides:	dotnet-gtksourceview
Obsoletes:	dotnet-gtksourceview
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides bindings for .NET to Gtk+2 and GNOME2 libraries.

%description -l pl
Pakiet ten dostarcza wi±zania dla .NET do bibliotek z Gtk+2 oraz
GNOME2.

%package devel
Summary:	Development part of GtkSourceView#
Summary(pl):	Czê¶æ GtkSourceView# przeznaczona dla programistów
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	gtksourceview-sharp-devel
Obsoletes:	gtksourceview-sharp-devel
Provides:	dotnet-gtksourceview-devel
Obsoletes:	dotnet-gtksourceview-devel

%description devel
Development part of GtkSourceView#.

%description devel -l pl
Czê¶æ GtkSourceView# przeznaczona dla programistów.

%prep
%setup -q -n gtksourceview-sharp-%{version}
%patch0 -p1
sed -i -e 's/`monodoc --get-sourcesdir`/$(DESTDIR)&/' doc/Makefile.am
sed -i -e 's/apidir = $(DESTDIR)@gtk/apidir = @gtk/' gtksourceview/makefile.am

%build
rm -rf autom4te.cache
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT`monodoc --get-sourcesdir`

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
# already in main package
rm -f $RPM_BUILD_ROOT%{_datadir}/gtksourceview-1.0/language-specs/csharp.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/mono/gac/*
%{_datadir}/mime-info/*
%{_datadir}/gtksourceview-1.0/language-specs/*

%files devel
%defattr(644,root,root,755)
%doc ChangeLog AUTHORS
%{_libdir}/mono/gtk-sharp/*
%{_datadir}/gapi/*
%{_pkgconfigdir}/*
%{_libdir}/monodoc/sources/gtksourceview-sharp-docs.*
