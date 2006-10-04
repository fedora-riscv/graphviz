# $Id: graphviz.spec,v 1.28 2006/10/04 21:35:44 jima Exp $ $Revision: 1.28 $
# graphviz.spec.  Generated from graphviz.spec.in by configure.

# Io is disabled because it's not (yet?) found in Fedora.
# http://www.iolanguage.com/about/
# - Jima
%define _IO 0

# Note: graphviz requires gd with gif support (and other fixes), hence use
# internal one for now.

Summary:	Graph Visualization Tools
Name:		graphviz
Version:	2.8
Release:	5%{?dist}
Group:		Applications/Multimedia
License:	CPL
URL:		http://www.graphviz.org/
Source:		http://www.graphviz.org/pub/graphviz/ARCHIVE/%{name}-%{version}.tar.gz
Requires:	urw-fonts

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	libpng-devel libjpeg-devel expat-devel ksh bison flex 
BuildRequires:	libtool-ltdl-devel fontconfig-devel swig libXaw-devel 
BuildRequires:	libSM-devel libXpm-devel libXext-devel libXt-devel
BuildRequires:	mono-core guile-devel libgcj-devel java-1.4.2-gcj-compat-devel
BuildRequires:	lua-devel ocaml php-devel python-devel ruby-devel tk-devel

%description
A collection of tools for the manipulation and layout
of graphs (as in nodes and edges, not as in barcharts).

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.so.*
%{_mandir}/man1/*.1*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/lefty
%exclude %{_libdir}/%{name}/*/*

#------------------------------------------------------------------
%package sharp
Group:	Applications/Multimedia
Summary:	C# extension for %{name}
Requires:	%{name} = %{version}-%{release}

%description sharp
C# extensions for %{name}.

%files sharp
%defattr(-,root,root,-)
%dir %{_libdir}/%{name}/sharp
%{_libdir}/%{name}/sharp/*

#------------------------------------------------------------------
%package guile
Group:		Applications/Multimedia
Summary:	Guile extension for %{name}
Requires:	%{name} = %{version}-%{release}

%description guile
Guile extensions for %{name}.

%files guile
%defattr(-,root,root,-)
%dir %{_libdir}/%{name}/guile
%{_libdir}/%{name}/guile/*

#------------------------------------------------------------------
%if %{_IO}
%package io
Group:		Applications/Multimedia
Summary:	Io extension for %{name}
Requires:	%{name} = %{version}-%{release}

%description io
Java extensions for %{name}.

%files io
%defattr(-,root,root,-)
%dir %{_libdir}/%{name}/io
%{_libdir}/%{name}/io/*
%endif

#------------------------------------------------------------------
%package java
Group:		Applications/Multimedia
Summary:	Java extension for %{name}
Requires:	%{name} = %{version}-%{release}

%description java
Java extensions for %{name}.

%files java
%defattr(-,root,root,-)
%dir %{_libdir}/%{name}/java
%{_libdir}/%{name}/java/*

#------------------------------------------------------------------
%package lua
Group:		Applications/Multimedia
Summary:	Lua extension for %{name}
Requires:	%{name} = %{version}-%{release}

%description lua
Java extensions for %{name}.

%files lua
%defattr(-,root,root,-)
%dir %{_libdir}/%{name}/lua
%{_libdir}/%{name}/lua/*

#------------------------------------------------------------------
%package ocaml
Group:		Applications/Multimedia
Summary:	Ocaml extension for %{name}
Requires:	%{name} = %{version}-%{release}

%description ocaml
Ocaml extensions for %{name}.

%files ocaml
%defattr(-,root,root,-)
%dir %{_libdir}/%{name}/ocaml
%{_libdir}/%{name}/ocaml/*

#------------------------------------------------------------------
%package perl
Group:		Applications/Multimedia
Summary:	Perl extension for %{name}
Requires:	%{name} = %{version}-%{release}

%description perl
Perl extensions for %{name}.

%files perl
%defattr(-,root,root,-)
%dir %{_libdir}/%{name}/perl
%{_libdir}/%{name}/perl/*

#------------------------------------------------------------------
%package php
Group:		Applications/Multimedia
Summary:	PHP extension for %{name}
Requires:	%{name} = %{version}-%{release}

%description php
PHP extensions for %{name}.

%files php
%defattr(-,root,root,-)
%dir %{_libdir}/%{name}/php
%{_libdir}/%{name}/php/*

#------------------------------------------------------------------
%package python
Group:		Applications/Multimedia
Summary:	Python extension for %{name}
Requires:	%{name} = %{version}-%{release}

%description python
Python extensions for %{name}.

%files python
%defattr(-,root,root,-)
%dir %{_libdir}/%{name}/python
%{_libdir}/%{name}/python/*

#------------------------------------------------------------------
%package ruby
Group:		Applications/Multimedia
Summary:	Ruby extension for %{name}
Requires:	%{name} = %{version}-%{release}

%description ruby
Ruby extensions for %{name}.

%files ruby
%defattr(-,root,root,-)
%dir %{_libdir}/%{name}/ruby
%{_libdir}/%{name}/ruby/*

#------------------------------------------------------------------
%package tcl
Group:		Applications/Multimedia
Summary:	Tcl extension & tools for %{name}
Requires:	%{name} = %{version}-%{release} tcl >= 8.3 tk

%description tcl
Various tcl packages (extensions) for the %{name} tools.

%files tcl
%defattr(-,root,root,-)
%dir %{_libdir}/%{name}/tcl
%{_libdir}/%{name}/tcl/*
%{_libdir}/%{name}/pkgIndex.tcl
%{_datadir}/%{name}/demo
%{_mandir}/mann/*.n*

#------------------------------------------------------------------
%package devel
Group:		Development/Libraries
Summary:	Development package for %{name}
Requires:	%{name} = %{version}-%{release} pkgconfig

%description devel
A collection of tools for the manipulation and layout
of graphs (as in nodes and edges, not as in barcharts).
This package contains development files for %{name}.

%files devel
%defattr(-,root,root,-)
%{_includedir}/%{name}
%{_libdir}/%{name}/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*.3*
%exclude %{_libdir}/%{name}/*/*

#------------------------------------------------------------------
%package graphs
Group:		Applications/Multimedia
Summary:	Demo graphs for %{name}

%description graphs
Some demo graphs for %{name}.

%files graphs
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/graphs

#------------------------------------------------------------------
%package doc
Group:		Documentation
Summary:	PDF and HTML documents for %{name}

%description doc
Provides some additional PDF and HTML documentation for %{name}.

%files doc
%defattr(-,root,root,-)
%doc __doc/*

#------------------------------------------------------------------
%prep
%setup -q

%build
%configure --disable-static --with-mylibgd --disable-io
%__make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT __doc
%{__make} \
    DESTDIR=$RPM_BUILD_ROOT \
    docdir=$RPM_BUILD_ROOT%{_docdir}/%{name} \
    pkgconfigdir=%{_libdir}/pkgconfig \
    install
find ${RPM_BUILD_ROOT} -type f -name "*.la" -exec rm -f {} ';'
#find ${RPM_BUILD_ROOT} -type f -name "*.a" -exec rm -f {} ';'
chmod -x $RPM_BUILD_ROOT%{_datadir}/%{name}/lefty/*
cp -a $RPM_BUILD_ROOT%{_datadir}/%{name}/doc __doc
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/doc

%clean
rm -rf $RPM_BUILD_ROOT

# run "dot -c" to generate plugin config in %{_libdir}/%{name}/config
%post
%{_bindir}/dot -c

# if there is not dot after everything else is done, the remove config
%postun
if ! test -x %{_bindir}/dot; then rm -f %{_libdir}/%{name}/config; fi

%changelog
* Wed Oct 04 2006 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.8-5
- Bump-n-build

* Thu Sep 14 2006 Patrick "Jima" Laughton <jima@beer.tclug.org>	- 2.8-4
- Fixing BZ#188148 & BZ#184171
- Dropped the unified spec file logic; it complicated matters unnecessarily
- Removed VERY broken fc5/fc4/fc3 conditionals
- Removed redundant BuildReqs
- Disabled io support due to not knowing what it was
- General cleanup
- Lots of help from Alex Lancaster on this package! Thanks!

* Wed Mar 01 2006 Oliver Falk <oliver@linux-kernel.at>		- 2.8-3
- Add libtool-ltdl, libtool-ltdl-devel
- Fix fixes

* Fri Feb 24 2006 Oliver Falk <oliver@linux-kernel.at>		- 2.8-2
- Fix unpackaged files on x86_64

* Wed Feb 22 2006 Oliver Falk <oliver@linux-kernel.at>		- 2.8-1
- Merge with specfile from Paul F. Johnson
- Update

* Mon Feb 13 2006 Oliver Falk <oliver@linux-kernel.at>		- 2.6-4
- BR: ruby-devel

* Mon Nov 21 2005 Oliver Falk <oliver@linux-kernel.at>		- 2.6-3
- Rebuild

* Fri Nov 04 2005 Oliver Falk <oliver@linux-kernel.at>		- 2.6-2
- BuildRequires fixes for "Modular X"; Thanks to John Ellson

* Mon Aug 29 2005 Oliver Falk <oliver@linux-kernel.at>		- 2.6-1
- Update

* Mon Aug 22 2005 Oliver Falk <oliver@linux-kernel.at>		- 2.4-2
- Bug #163840

* Thu Aug 11 2005 Oliver Falk <oliver@linux-kernel.at>		- 2.4-1
- Update
- Took over maintainership
- Merge with spec provided within source tarball

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 2.2.1-2
- rebuild on all arches

* Fri Apr  7 2005 John Ellson <ellson@research.att.com> - 2.2.1-1
- update to graphviz-2.2.1

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Sun Jan 23 2005 John Ellson <ellson@research.att.com> - 0:2.2-3
- change BuildRequires to /bin/ksh, since ksh doesn't provide a /usr/bin/ksh
- change devel exclude to also exclude libtcl*.la

* Sat Jan 22 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:2.2-2
- Move -doc back to %%{__docdir}, remove unused docdir=... from build.
- Own %%{_datadir}/%%{name} in -graphs.
- Require tcl and tk in -tcl.
- Require pkgconfig in -devel, fix *.pc install location.
- Build without dependency tracking.
- Honor $RPM_OPT_FLAGS again.
- Move dotneato-config to -devel.
- Fix lefty/* permissions.

* Sat Jan 22 2005 John Ellson <ellson@research.att.com> - 0:2.2-1
- Updated to 2.2
- split out:
    graphviz-docs    - optional and large
    graphviz-graphs  - optional demo graphs
    graphviz-tcl     - optional, of interest only to tcl users, requires tcl
- avoid use of %%configure which breaks on RH73
- add some pkgconfigs - probably in wrong place they're a bit experimental
  so OK for now
- add BuildRequires /usr/bin/ksh  (either pdksh or the real one)

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
