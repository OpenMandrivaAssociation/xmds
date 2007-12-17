%define name xmds
%define realversion 1.5-3
%define version %( echo %realversion | sed 's/-/_/g' )
%define release %mkrel 1

Summary: eXtensible multi-dimensional Simulator 
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{realversion}.tar.bz2
Patch0: xmds-stupid-configure.patch
License:GPL 
Group:Sciences/Other 
Url: http://www.xmds.org/  
BuildRequires: fftw2-devel
Requires:fftw2-devel
 
%description
XMDS is a code generator that integrates equations. You write them down in
human readable form in an XML file, and it goes away and writes and compiles
a C++ program that integrates those equations as fast as it can possibly be
done in your architecture.
 
%prep
%setup -q -n %name-%realversion
%patch -p0

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog AUTHORS INSTALL NEWS README
%doc examples
%_bindir/*
%_includedir/*.h
%_libdir/*.a
%_mandir/man?/*

