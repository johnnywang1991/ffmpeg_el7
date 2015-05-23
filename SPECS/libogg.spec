Name:		libogg
Version:	1.3.2
Release:	4
Summary:	Ogg Bitstream Library.

Group:		System Environment/Libraries
License:	BSD
URL:		http://www.xiph.org/
Vendor:		Xiph.org Foundation <team@xiph.org>
Source:		http://www.vorbis.com/files/1.0.1/unix/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

# We're forced to use an epoch since both Red Hat and Ximian use it in their
# rc packages
Epoch:		2
# Dirty trick to tell rpm that this package actually provides what the
# last rc and beta was offering
Provides:	%{name} = %{version}

%description
Libogg is a library for manipulating ogg bitstreams.  It handles
both making ogg bitstreams and getting packets from ogg bitstreams.

%package devel
Summary: 	Ogg Bitstream Library Development
Group: 		Development/Libraries
Requires: 	libogg = %{version}
# Dirty trick to tell rpm that this package actually provides what the
# last rc and beta was offering
Provides:	%{name}-devel = %{version}

%description devel
The libogg-devel package contains the header files, static libraries
and documentation needed to develop applications with libogg.

%prep
%setup -q -n %{name}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{_prefix} --enable-static
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS CHANGES COPYING README
%{_exec_prefix}/lib/libogg.so.*

%files devel
%defattr(-,root,root)
%doc %{_datadir}/doc/libogg/*.html
%doc %{_datadir}/doc/libogg/*.txt
%doc %{_datadir}/doc/libogg/*.png
%doc %{_datadir}/doc/libogg/libogg/*.html
%doc %{_datadir}/doc/libogg/libogg/style.css
%dir %{_includedir}/ogg
%{_includedir}/ogg/ogg.h
%{_includedir}/ogg/os_types.h
%{_includedir}/ogg/config_types.h
%{_exec_prefix}/lib/libogg.a
%{_exec_prefix}/lib/libogg.la
%{_exec_prefix}/lib/libogg.so
%{_exec_prefix}/lib/pkgconfig/ogg.pc
%{_datadir}/aclocal/ogg.m4

%changelog
* Sat May 23 2015 Johnny Wang <johnnywang1991@msn.com>
- update to release 1.3.2-3

* Thu Nov 08 2007 Conrad Parker <conrad@metadecks.org>
- update doc dir (reported by thosmos on #vorbis)

* Thu Jun 10 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- autogenerate from configure
- fix download location
- remove Prefix
- own include dir
- move ldconfig runs to -p scripts
- change Release tag to include xiph

* Tue Oct 07 2003 Warren Dukes <shank@xiph.org>
- update for 1.1 release

* Sun Jul 14 2002 Thomas Vander Stichele <thomas@apestaart.org>
- update for 1.0 release
- conform Group to Red Hat's idea of it
- take out case where configure doesn't exist; a tarball should have it

* Tue Dec 18 2001 Jack Moffitt <jack@xiph.org>
- Update for RC3 release

* Sun Oct 07 2001 Jack Moffitt <jack@xiph.org>
- add support for configurable prefixes

* Sat Sep 02 2000 Jack Moffitt <jack@icecast.org>
- initial spec file created
