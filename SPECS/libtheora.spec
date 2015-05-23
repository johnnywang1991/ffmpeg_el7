Name:       libtheora
Summary:    Theora Video Compression Codec
Version:    1.1.1
Release:    1
Group:      System/Libraries
License:    BSD
URL:        http://www.theora.org/
Source0:    http://downloads.xiph.org/releases/theora/%{name}-%{version}.tar.bz2
Requires(post):  /sbin/ldconfig
Requires(postun):  /sbin/ldconfig

BuildRoot:  %{_tmppath}/%{name}-%{version}-build

%description
Description: %{summary}


%package devel
Summary:    Development tools for Theora applications
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Description: %{summary}

%prep
%setup -q -n %{name}-%{version}

%build
./autogen.sh
%configure --disable-static \
    --enable-shared \
    --disable-examples

# Call make instruction with smp support
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install
rm -rf %{buildroot}/usr/share/doc/libtheora

%clean
rm -rf %{buildroot}



%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig



%files
%defattr(-,root,root,-)
%doc README COPYING
%{_libdir}/libtheora.so.*
%{_libdir}/libtheoradec.so.*
%{_libdir}/libtheoraenc.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/theora
%{_libdir}/*.so
%{_libdir}/pkgconfig/theora.pc
%{_libdir}/pkgconfig/theoraenc.pc
%{_libdir}/pkgconfig/theoradec.pc
%{_libdir}/libtheora.la
%{_libdir}/libtheoradec.la
%{_libdir}/libtheoraenc.la

%changelog
* Sat May 23 2015 Johnny Wang <johnnywang1991@msn.com>
- update to 1.1.1
