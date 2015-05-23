Summary: Library implementing the Unicode Bidirectional Algorithm
Name: fribidi
Version: 0.19.6
Release: 1%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://fribidi.org/

Source: http://fribidi.org/download/fribidi-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool

%description
A library to handle bidirectional scripts (eg. hebrew, arabic), so that
the display is done in the proper way; while the text data itself is
always written in logical order.

%package devel
Summary: Libraries and include files for fribidi
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
Include files and libraries needed for developing applications which use
fribidi.

%prep
%setup

%build
#aclocal
autoconf
autoreconf -f -i
automake
#autoreconf -i
%configure --disable-static
%{__make} #%{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README THANKS TODO
%{_bindir}/fribidi
%{_libdir}/libfribidi.so.*
%exclude %{_libdir}/libfribidi.la

%files devel
%defattr(-, root, root, 0755)
#%{_bindir}/fribidi-config
%{_includedir}/fribidi
%{_libdir}/libfribidi.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/man/man3/*

%changelog
* Thu Apr 30 2015 Johnny Wang <johnnywang1991@msn.com> - 0.19.6
- Updated to 0.19.6

* Mon Dec 06 2010 Dag Wieers <dag@wieers.com> - 0.10.9-1
- Initial package. (using DAR)
