%define name xmds
%define realversion 1.6.6
%define version %( echo %realversion | sed 's/-/_/g' )
%define release %mkrel 2

Summary: eXtensible multi-dimensional Simulator 
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{realversion}.tar.gz
License:GPL 
Group:Sciences/Other 
Url: http://www.xmds.org/  
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: fftw-devel
#Requires:fftw2-devel
 
%description
XMDS is a code generator that integrates equations. You write them down in
human readable form in an XML file, and it goes away and writes and compiles
a C++ program that integrates those equations as fast as it can possibly be
done in your architecture.
 
%prep
%setup -q -n %name-%realversion

%build
%configure2_5x --enable-fftw3
	     
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog AUTHORS INSTALL NEWS README
%doc examples
%_bindir/*
%_includedir/*.h
%_libdir/*.a
%_mandir/man?/*

