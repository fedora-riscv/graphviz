# Note: graphviz requires gd with gif support, hence use internal one for now.

Summary: 	Graph Visualization Tools
Name: 		graphviz
Version: 	1.12
Release: 	2
Epoch:		0
Group: 		Applications/Multimedia
License: 	AT&T open source (see COPYING)
URL:  		http://www.graphviz.org/
Source: 	http://www.graphviz.org/pub/graphviz/ARCHIVE/graphviz-1.12.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-root
BuildRequires:	zlib-devel libpng-devel libjpeg-devel XFree86-devel expat-devel
BuildRequires:	bison m4 flex tk tcl >= 0:8.3
BuildRequires:	/usr/include/tcl.h /usr/include/tk.h

%package devel
Summary: 	Development package for %{name}
Group: 		Development/Libraries
Requires: 	%{name} = %{epoch}:%{version}-%{release}

%description
A collection of tools and tcl packages for the manipulation and layout
of graphs (as in nodes and edges, not as in barcharts).

%description devel
A collection of tools and tcl packages for the manipulation and layout
of graphs (as in nodes and edges, not as in barcharts).
This package contains development files for %{name}


%prep
%setup -q


%build
# XXX ix86 only used to have -ffast-math, let's use everywhere
%{expand: %%define optflags %{optflags} -ffast-math}
%configure --with-x
make docdir=%{_docdir}/%{name} %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make \
    DESTDIR=$RPM_BUILD_ROOT \
    docdir=$RPM_BUILD_ROOT%{_docdir}/%{name} \
    transform='s,x,x,' \
	install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%doc AUTHORS COPYING MINTERMS.txt NEWS README
%doc doc/*.html doc/*.pdf doc/*.ref
%{_bindir}/*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/pkgIndex.tcl
%{_libdir}/%{name}/*.so.*
%{_mandir}/man1/*.1*
%{_mandir}/mann/*.n*
%{_datadir}/%{name}

%files devel
%defattr(-,root,root,-)
%{_includedir}/%{name}
%{_libdir}/%{name}/*.la
%{_libdir}/%{name}/*.so
%{_mandir}/man3/*.3*


%changelog
* Thu Jun  3 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.12-0.fdr.2
- BuildRequire m4 to work around https://bugzilla.redhat.com/108655 on FC1.

* Tue May 25 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.12-0.fdr.1
- Update to 1.12.

* Tue Nov 11 2003 Dams <anvil[AT]livna.org> 0:1.10-0.fdr.3
- Applied patch to fix build on FC1

* Sat Aug 23 2003 Dams <anvil[AT]livna.org> 0:1.10-0.fdr.2
- Hopefully fixed BuildRequires

* Sun Aug 17 2003 Dams <anvil[AT]livna.org> 0:1.10-0.fdr.2
- Added some BuildRequires to satisfy build conditions on severn.

* Sat Aug 16 2003 Dams <anvil[AT]livna.org> 0:1.10-0.fdr.1
- Added _smp_mflags
- Removed "transform='s,x,x,'" configure arg

* Tue Jul 29 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.10-0.fdr.1
- Update to 1.10.
- BuildRequires expat-devel.
- Include *.la (uses ltdl).
- %%configure in %%build.

* Thu Jul 10 2003 Dams <anvil[AT]livna.org> 0:1.9-0.fdr.1
- Updated to 1.9
- Split devel package

* Tue Jul  8 2003 Dams <anvil[AT]livna.org> 0:1.7.14-0.fdr.1
- Applied fedora spec file look&feel

* Tue Jan  1 2002 Jeff Johnson <jbj@redhat.com>
- update to 1.7.14.

* Wed Apr 25 2001 Jeff Johnson <jbj@redhat.com>
- repackage for powertools.
- simplify spec file.
- add -ffast-math for all arch's, not just ix86.
- remove Requires: webfonts.
