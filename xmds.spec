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



%changelog
* Wed Aug 26 2009 Emmanuel Andry <eandry@mandriva.org> 1.6.6-2mdv2010.0
+ Revision: 421581
- build against fftw3

* Tue Aug 12 2008 Olivier Thauvin <nanardon@mandriva.org> 1.6.6-1mdv2009.0
+ Revision: 271013
- 1.6.6

* Sat Feb 09 2008 Olivier Thauvin <nanardon@mandriva.org> 1.6.4-1mdv2008.1
+ Revision: 164446
- 1.6.4

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 1.5_3-1mdv2008.0
+ Revision: 20039
- 1.5-3


* Thu Aug 10 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/10/06 10:44:04 (55344)
- 1.5-2

* Thu Aug 10 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/10/06 10:39:37 (55339)
Import xmds

* Sun Mar 05 2006 Olivier Thauvin <nanardon@mandriva.org> 1.5_1-1mdk
- 1.5-1

* Fri Jan 21 2005 Sylvie Terjan <erinmargault@zarb.org> 1.3_5-1mdk
- make spec file

