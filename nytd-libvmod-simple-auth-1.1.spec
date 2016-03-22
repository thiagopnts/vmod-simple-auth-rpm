Summary: Varnish Vmod for simple url signing
Name: libvmod-simple-auth
Version: 1.2
Release: 1%{?dist}
Packager: NYTimes
Group: Development/Libraries
License: FreeBSD
URL: https://github.com/thiagopnts/vmod-simple-auth
Source: libvmod-simple-auth.tar.gz
BuildRequires: make
BuildRequires: automake
BuildRequires: libtool
BuildRequires: mhash-devel
BuildRequires: python-docutils

%description
Varnish Vmod for simple url signing

%prep
pwd
%setup -n vmod-simple-auth-0.0.2

%build
./autogen.sh
VMODDIR=%{buildroot}/usr/lib64/varnish/vmods VARNISHSRC=../varnish-3.0.3/ ./configure --prefix %{buildroot}
make

%install
make install

%files
/usr/lib64/varnish/vmods/libvmod_simple_auth.la
/usr/lib64/varnish/vmods/libvmod_simple_auth.so
/share/man/man3/vmod_simple_auth.3
/share/doc/libvmod-simple-auth/LICENSE
/share/doc/libvmod-simple-auth/README.rst
