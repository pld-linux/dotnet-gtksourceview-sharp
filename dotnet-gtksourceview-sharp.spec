Summary:	.NET language bindings for GtkSourceView
Summary(pl):	Wi±zania GtkSourceView dla .NET
Name:		gtksourceview-sharp
Version:	0.1.0
Release:	2
License:	LGPL
Group:		Development/Libraries
Source0:	http://www.go-mono.com/archive/%{name}-%{version}.tar.gz
# Source0-md5:	c7bf339a41c80934a31f79f0717e2f0f
BuildRequires:	autoconf
BuildRequires:	automake >= 1.7
BuildRequires:	gtk-sharp-devel >= 0.17
BuildRequires:	gtksourceview-devel >= 0.1.0
BuildRequires:	libtool
BuildRequires:	mono-csharp
BuildRequires:  mono-devel
Requires:	gtksourceview >= 0.1.0
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

%description devel
Development part of GtkSourceView#.

%description devel -l pl
Czê¶æ GtkSourceView# przeznaczona dla programistów.

%prep
%setup -q

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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/*.dll
%{_datadir}/mime-info/*

%files devel
%defattr(644,root,root,755)
%doc ChangeLog AUTHORS
%{_datadir}/gapi/*
%{_pkgconfigdir}/*
