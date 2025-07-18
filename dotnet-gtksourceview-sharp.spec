Summary:	.NET language bindings for GtkSourceView
Summary(pl.UTF-8):	Wiązania GtkSourceView dla .NET
Name:		dotnet-gtksourceview-sharp
Version:	0.5
Release:	11
License:	LGPL
Group:		Libraries
Source0:	http://mono2.ximian.com/archive/1.0/gtksourceview-sharp-%{version}.tar.gz
# Source0-md5:	b82e767e42a542e185a534048db3078d
Patch0:		%{name}-install.patch
Patch1:		%{name}-mint.patch
URL:		http://www.mono-project.com/
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.7
BuildRequires:	dotnet-gtk-sharp-gnome-devel >= 0.93
BuildRequires:	gtksourceview-devel >= 1.0.1
BuildRequires:	libtool
BuildRequires:	monodoc >= 0.16
BuildRequires:	mono-csharp >= 1.1.7
BuildRequires:	pkgconfig
Requires:	dotnet-gtk-sharp >= 0.93
Requires:	gtksourceview >= 1.0.1
Requires:	mono >= 1.1.7
Provides:	dotnet-gtksourceview
Provides:	gtksourceview-sharp
Obsoletes:	dotnet-gtksourceview
Obsoletes:	gtksourceview-sharp
ExcludeArch:	i386
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides .NET bindings for GtkSourceView library.

%description -l pl.UTF-8
Pakiet ten dostarcza wiązania .NET do biblioteki GtkSourceView.

%package devel
Summary:	Development part of GtkSourceView#
Summary(pl.UTF-8):	Część GtkSourceView# przeznaczona dla programistów
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dotnet-gtk-sharp-devel >= 0.93
Provides:	dotnet-gtksourceview-devel
Provides:	gtksourceview-sharp-devel
Obsoletes:	dotnet-gtksourceview-devel
Obsoletes:	gtksourceview-sharp-devel

%description devel
Development part of GtkSourceView#.

%description devel -l pl.UTF-8
Część GtkSourceView# przeznaczona dla programistów.

%prep
%setup -q -n gtksourceview-sharp-%{version}
%patch -P0 -p1
%patch -P1 -p1
sed -i -e 's/`monodoc --get-sourcesdir`/$(DESTDIR)&/' doc/Makefile.am
sed -i -e 's/apidir = $(DESTDIR)@gtk/apidir = @gtk/' gtksourceview/makefile.am

%build
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
rm -f $RPM_BUILD_ROOT%{_datadir}/gtksourceview-1.0/language-specs/{csharp,nemerle,vbnet}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%{_prefix}/lib/mono/gac/*
%{_datadir}/mime-info/*

%files devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gtk-sharp/*
%{_datadir}/gapi/*
%{_pkgconfigdir}/*
%{_libdir}/monodoc/sources/gtksourceview-sharp-docs.*
