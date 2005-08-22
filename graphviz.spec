Summary:			Graph Visualization Tools
Name:				graphviz

Version:			2.4
Release:			1

Group:				Applications/Multimedia
License:			CPL

URL:				http://www.graphviz.org/
Source0:			http://www.graphviz.org/pub/graphviz/ARCHIVE/%{name}-%{version}.tar.gz

BuildRoot:			%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:		zlib-devel libpng-devel libjpeg-devel expat-devel freetype-devel >= 2
BuildRequires:		/bin/ksh bison m4 flex
BuildRequires:		tcl-devel >= 8.3
BuildRequires:		tk-devel
BuildRequires:		fontconfig-devel xorg-x11-devel
BuildRequires:		php-devel guile-devel
Requires(post):		%{_bindir}/dot
Requires(postun):	%{_bindir}/d

%package			tcl
Summary:			Tcl extension tools for %{name}
Group:				Applications/Multimedia
Requires:			%{name} = %{version}-%{release} tcl >= 8.3 tk

%package			devel
Summary:			Development package for %{name}
Group:				Development/Libraries
Requires:			%{name} = %{version}-%{release} pkgconfig

%package			doc
Summary:			PDF and HTML documents for %{name}
Group:				Documentation

%package			graphs
Summary:			Demo graphs for %{name}
Group:				Applications/Multimedia

%description
A collection of tools and tcl packages for the manipulation and layout
of graphs (as in nodes and edges, not as in barcharts).

%description tcl
Various tcl packages (extensions) for the %{name} tools.

%description devel
A collection of tools and tcl packages for the manipulation and layout
of graphs (as in nodes and edges, not as in barcharts).
This package contains development files for %{name}.

%description doc
Provides some additional PDF and HTML documentation for %{name}.

%description graphs
Some demo graphs for %{name}.

%prep
%setup -q

%build
# XXX ix86 only used to have -ffast-math, let's use everywhere
%{expand: %%define optflags %{optflags} -ffast-math}

%configure	--with-x \
			--with-mylibgd \
			--disable-dependency-tracking \
			--disable-static

%{__make} %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT __doc

%{__make} \
    DESTDIR=$RPM_BUILD_ROOT \
    docdir=$RPM_BUILD_ROOT%{_docdir}/%{name} \
    pkgconfigdir=%{_libdir}/pkgconfig \
    transform='s,x,x,' \
    install

chmod -x $RPM_BUILD_ROOT%{_datadir}/%{name}/lefty/*
cp -a $RPM_BUILD_ROOT%{_datadir}/%{name}/doc __doc
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.so.*
%{_mandir}/man1/*.1*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/lefty
%exclude %{_libdir}/%{name}/lib*tcl*.so.*
%exclude %{_libdir}/%{name}/libtk*.so.*
%exclude %{_includedir}/ltdl*
%exclude %{_libdir}/libltdl*

%files tcl
%defattr(-,root,root,-)
%{_libdir}/%{name}/lib*tcl*.so.*.*
%{_libdir}/%{name}/libtk*.so.*.*
%{_libdir}/%{name}/pkgIndex.tcl
%{_datadir}/%{name}/demo
%{_mandir}/mann/*.n*

%files devel
%defattr(-,root,root,-)
%{_includedir}/%{name}
%{_libdir}/%{name}/*.la
%{_libdir}/%{name}/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*.3*
%exclude %{_libdir}/%{name}/lib*tcl*.*
%exclude %{_libdir}/%{name}/libtk*.*

%files graphs
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/graphs

%files doc
%defattr(-,root,root,-)
%doc __doc/*

# run "dot -V" to generate plugin config in %{_libdir}/%{name}/config
%post
%{_bindir}/dot -V 2>/dev/null

%post tcl
%{_bindir}/dot -V 2>/dev/null

%post devel
%{_bindir}/dot -V 2>/dev/null

%changelog
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
