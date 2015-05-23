# el7

Summary: Open-source, patent-free speech codec
Name: speex
Version: 1.0.5
Release: 1%{?dist}
License: BSD
Group: System Environment/Libraries
URL: http://www.speex.org/

Source: http://www.speex.org/download/speex-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Provides: libspeex = %{version}-%{release}
Obsoletes: libspeex <= 1.0.0
BuildRequires: libogg-devel, gcc-c++

%description
Speex is a patent-free audio codec designed especially for voice (unlike 
Vorbis which targets general audio) signals and providing good narrowband 
and wideband quality. This project aims to be complementary to the Vorbis
codec.


%package devel
Summary: Speex development files
Group: Development/Libraries
Provides: libspeex-devel = %{version}-%{release}
Requires: %{name} = %{version}

%description devel
Speex development files.


%prep
%setup

%build
export CFLAGS='%{optflags} -DRELEASE'
%configure \
	--enable-shared \
	--enable-static \
	--with-ogg-libraries="%{_libdir}"
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} DESTDIR=%{buildroot} install


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc COPYING AUTHORS ChangeLog NEWS README doc/manual.pdf
%{_bindir}/speexdec
%{_bindir}/speexenc
%{_libdir}/libspeex.so.*
#%{_libdir}/libspeexdsp.so.*
%{_mandir}/man1/speexdec.1*
%{_mandir}/man1/speexenc.1*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/speex/
%{_includedir}/speex.h
%{_includedir}/speex_bits.h
%{_includedir}/speex_callbacks.h
%{_includedir}/speex_header.h
%{_includedir}/speex_stereo.h
%{_libdir}/libspeex.a
%{_libdir}/libspeex.la
%{_libdir}/libspeex.so
%{_libdir}/pkgconfig/speex.pc
%{_datadir}/aclocal/speex.m4
#%exclude %{_libdir}/libspeexdsp.la
#%{_libdir}/libspeexdsp.so
#%{_libdir}/libspeexdsp.a
#%{_libdir}/pkgconfig/speexdsp.pc

%changelog
* Sat May 23 2015 Johnny Wang <johnnywang1991@msn.com>
- Initial rutweb version
