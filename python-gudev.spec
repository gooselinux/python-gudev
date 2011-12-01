%if 0%{?fedora} > 12 || 0%{?rhel} > 6
%global with_python3 1
%else
%{!?python_sitearch: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print (get_python_lib(1))")}
%endif

%global srcname nzjrs-python-gudev-5fac65a

Summary:        Python (PyGObject) bindings to the GUDev library
Name:           python-gudev
URL:            http://github.com/nzjrs/python-gudev
# Tar.gz can be downloaded from
# http://github.com/nzjrs/python-gudev/tarball/%{version}
Source0:        %{srcname}.tar.gz
Version:        147.1
Release:        4%{?dist}
Group:          Development/Libraries
License:        LGPLv3+
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       libgudev1 >= 147
Requires:       pygobject2
BuildRequires:  python-devel
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  libgudev1-devel >= 147
BuildRequires:  pygobject2-devel

%description
python-gudev is a Python (PyGObject) binding to the GUDev UDEV library.

%prep
%setup -q -n %{srcname}

%build
sh autogen.sh --prefix %{_prefix} --disable-static
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
find $RPM_BUILD_ROOT -name gudev.la | xargs rm

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING README NEWS
%doc test.py
%{python_sitearch}/*
%{_datadir}/*

%changelog
* Mon Mar 15 2010 Miroslav Suchý <msuchy@redhat.com> 147.1-4
- 572609 - do not strip all debuginfo

* Mon Feb  8 2010 Miroslav Suchý <msuchy@redhat.com> 147.1-3
- initial release
