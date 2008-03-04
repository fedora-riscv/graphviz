# $Id: graphviz.spec.in,v 1.135 2007/12/12 19:26:17 ellson Exp $ $Revision: 1.135 $
# graphviz.spec.  Generated from graphviz.spec.in by configure.

# Note: pre gd-2.0.34 graphviz uses its own gd tree with gif support and other fixes

#-- Global graphviz rpm and src.rpm tags-------------------------------------
Name:    graphviz
Summary: Graph Visualization Tools
Version: 2.16.1

%define truerelease 0.4
%{?distroagnostic: %define release %{truerelease}}
%{!?distroagnostic: %define release %{truerelease}%{?dist}}

Release: %{?release}

Group:   Applications/Multimedia
License: CPL
URL:     http://www.graphviz.org/
Source0: http://www.graphviz.org/pub/graphviz/ARCHIVE/%{name}-%{version}.tar.gz
Patch0:  %{name}-tk8.5.patch
Patch1:  %{name}-gcc43.patch
Patch2:  %{name}-multilib.patch

# graphviz is relocatable - Caution: this feature is used in AT&T,
#   but probably will not be supported in Redhat/Fedora/Centos distros
#Prefix: /usr

#-- feature and package selection -------------------------------------------
#   depends on %dist and %fedora (or %rhl or %rhel) which are set
#   in .rpmmacros on each build host

# Define a default set of features incase none of the conditionals apply
%define SHARP  0
%define GUILE  0
%define _IO    0
%define JAVA   0
%define LUA    0
%define OCAML  0
%define PERL   0
%define PHP    0
%define PYTHON 0
%define RUBY   0
%define R_LANG 0
%define TCL    1
%define IPSEPCOLA --without-ipsepcola
%define MYLIBGD --with-mylibgd
%define PANGOCAIRO --without-pangocairo
%define DEVIL 0
%define MING 0
%define GDK_PIXBUF --without-gdk-pixbuf

# SuSE uses a different mechanism to generate BuildRequires
# norootforbuild
# neededforbuild  expat freetype2 freetype2-devel gcc libjpeg libpng-devel-packages tcl tcl-devel tk tk-devel x-devel-packages

BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: zlib-devel libpng-devel libjpeg-devel expat-devel freetype-devel >= 2
BuildRequires: /bin/ksh bison m4 flex tk tcl >= 8.3 swig

# This just indicates the requirement for tcl.h, tk.h, but doesn't identify
# where to get them from. In RH9 and earlier they were in the tcl, tk,
# base packages which are always BR'd anyway (above).
BuildRequires:  /usr/include/tcl.h /usr/include/tk.h

#-- Red Hat Linux specific Build Requirements -------------------------------
%if 0%{?rhl}
%define TCL    1
BuildRequires: XFree86-devel
%endif

#-- Red Hat Enterprise Linux specific Build Requirements --------------------
%if 0%{?rhel}
%define TCL    1
%if "%rhel" < "4"
BuildRequires:  XFree86-devel
%endif
%if "%rhel" >= "3"
%define IPSEPCOLA --with-ipsepcola
BuildRequires: fontconfig-devel tcl-devel tk-devel
%endif
%if "%rhel" == "4"
BuildRequires: xorg-x11-devel
%endif
%if "%rhel" >= "4"
# PERL is available earlier, but a suitable SWIG isn't
%define PERL   1
%define RUBY   1
%define GUILE  1
%define PYTHON 1
BuildRequires: perl ruby-devel guile-devel python-devel
%endif
%if "%rhel" >= "5"
%define JAVA   1
%define PANGOCAIRO --with-pangocairo
BuildRequires: libtool-ltdl libtool-ltdl-devel libXaw-devel libSM-devel libICE-devel libXpm-devel libXt-devel libXmu-devel libXext-devel libX11-devel java-devel
BuildRequires: cairo-devel >= 1.1.10 pango-devel gmp-devel gtk2-devel libgnomeui-devel
%endif
%if "%rhel" >= "6"
%define PHP    1
%define MYLIBGD --without-mylibgd
%define GDK_PIXBUF --with-gdk-pixbuf
BuildRequires: gd gd-devel perl-devel php-devel
%endif
%endif

#-- Fedora specific Build Requirements --------------------------------------
%if 0%{?fedora}
%define PERL   1
%define TCL    1
BuildRequires: fontconfig-devel tcl-devel tk-devel 
%if "%fedora" < "3"
BuildRequires: XFree86-devel
%endif
%if "%fedora" == "3"
BuildRequires: xorg-x11-devel
%endif
%if "%fedora" == "4"
BuildRequires: xorg-x11-devel
%endif
%if "%fedora" >= "3"
%define IPSEPCOLA --with-ipsepcola
%endif
%if "%fedora" >= "4"
%define RUBY   1
%define GUILE  1
%define PYTHON 1
BuildRequires: libtool-ltdl libtool-ltdl-devel ruby ruby-devel guile-devel python-devel
%endif
%if "%fedora" >= "5"
%define PHP    1
%define JAVA   1
BuildRequires: libXaw-devel libSM-devel libICE-devel libXpm-devel libXt-devel libXmu-devel libXext-devel libX11-devel java-devel php-devel
%ifnarch ppc64
%define SHARP  1
%define OCAML  1
BuildRequires: mono-core ocaml
%endif
%endif
%if "%fedora" >= "6"
%define LUA    1
%define PANGOCAIRO --with-pangocairo
BuildRequires: cairo-devel >= 1.1.10 pango-devel gmp-devel lua-devel gtk2-devel libgnomeui-devel
%endif
%if "%fedora" >= "7"
%define DEVIL 1
%define MYLIBGD --without-mylibgd
%define GDK_PIXBUF --with-gdk-pixbuf
BuildRequires: gd gd-devel perl-devel DevIL-devel
%endif
%if "%fedora" >= "8"
#define R_LANG 1
#BuildRequires: R-devel swig >= 1.3.33
%endif
%if "%fedora" >= "9"
%define MING 0
#BuildRequires: ming ming-devel
%endif
%endif

#-- main graphviz rpm ------------------------------------------------
Requires:         urw-fonts
Requires(post):   /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
A collection of tools for the manipulation and layout
of graphs (as in nodes and edges, not as in barcharts).

# run "dot -c" to generate plugin config in %{_libdir}/graphviz/config
%post
/sbin/ldconfig
%{_bindir}/dot -c

# if there is no dot after everything else is done, then remove config
%postun
if [ $1 -eq 0 ]; then
        rm -f %{_libdir}/graphviz/config || :
fi
/sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/*
%dir %{_libdir}/graphviz
%{_libdir}/*.so.*
%{_libdir}/graphviz/*.so.*
%{_mandir}/man1/*.1*
%{_mandir}/man7/*.7*
%dir %{_datadir}/graphviz
%{_datadir}/graphviz/lefty
%exclude %{_libdir}/graphviz/*/*
%exclude %{_libdir}/graphviz/libgvplugin_gd.*
%if %{DEVIL}
%exclude %{_libdir}/graphviz/libgvplugin_devil.*
%endif
%if %{MING}
%exclude %{_libdir}/graphviz/libgvplugin_ming.*
%exclude %{_libdir}/graphviz/*fdb
%endif

#-- graphviz-gd rpm --------------------------------------------------
%package gd
Group:            Applications/Multimedia
Summary:          Graphviz plugin for renderers based on gd
Requires:         graphviz = %{version}-%{release}
Requires(post):   %{_bindir}/dot /sbin/ldconfig
Requires(postun): %{_bindir}/dot /sbin/ldconfig

%description gd
Graphviz plugin for renderers based on gd.  (Unless you absolutely have
to use GIF, you are recommended to use the PNG format instead because
of the better quality anti-aliased lines provided by the cairo+pango
based renderer.)

# run "dot -c" to generate plugin config in %{_libdir}/graphviz/config
%post gd
/sbin/ldconfig
%{_bindir}/dot -c

%postun gd
/sbin/ldconfig
[ -x %{_bindir}/dot ] && %{_bindir}/dot -c || :

%files gd
%{_libdir}/graphviz/libgvplugin_gd.so.*

#-- graphviz-devil rpm --------------------------------------------------
%if %{DEVIL}
%package devil
Group:            Applications/Multimedia
Summary:          Graphviz plugin for renderers based on DevIL
Requires:         graphviz = %{version}-%{release}

%description devil
Graphviz plugin for renderers based on DevIL.  (Unless you absolutely have
to use BMP, TIF, or TGA, you are recommended to use the PNG format instead
supported directly by the cairo+pango based renderer in the base graphviz rpm.)

# run "dot -c" to generate plugin config in %{_libdir}/graphviz/config
%post devil
%{_bindir}/dot -c

%postun devil
[ -x %{_bindir}/dot ] && %{_bindir}/dot -c || :

%files devil
%{_libdir}/graphviz/libgvplugin_devil.so.*
%endif

#-- graphviz-ming rpm --------------------------------------------------
%if %{MING}
%package ming
Group:            Applications/Multimedia
Summary:          Graphviz plugin for flash renderer based on ming
Requires:         graphviz = %{version}-%{release}

%description ming
Graphviz plugin for -Tswf (flash) renderer based on ming.

# run "dot -c" to generate plugin config in %{_libdir}/graphviz/config
%post ming
%{_bindir}/dot -c

%postun ming
[ -x %{_bindir}/dot ] && %{_bindir}/dot -c || :

%files ming
%{_libdir}/graphviz/libgvplugin_ming.so.*
%{_libdir}/graphviz/*fdb
%endif

#-- graphviz-sharp rpm --------------------------------------------
%if %{SHARP}
%package sharp
Group:          Applications/Multimedia
Summary:        C# extension for graphviz
Requires:       graphviz = %{version}-%{release} mono-core

%description sharp
C# extension for graphviz.

%files sharp
%defattr(-,root,root,-)
%dir %{_libdir}/graphviz/sharp
%{_libdir}/graphviz/sharp/*
%{_mandir}/mann/gv_sharp.n*
%endif

#-- graphviz-guile rpm --------------------------------------------
%if %{GUILE}
%package guile
Group:          Applications/Multimedia
Summary:        Guile extension for graphviz
Requires:       graphviz = %{version}-%{release} guile

%description guile
Guile extension for graphviz.

%files guile
%defattr(-,root,root,-)
%dir %{_libdir}/graphviz/guile
%{_libdir}/graphviz/guile/*
%{_mandir}/mann/gv_guile.n*
%endif

#-- graphviz-io rpm -----------------------------------------------
%if %{_IO}
%package io
Group:          Applications/Multimedia
Summary:        Io extension for graphviz
Requires:       graphviz = %{version}-%{release} io

%description io
Io extension for graphviz.

%files io
%defattr(-,root,root,-)
%dir %{_libdir}/graphviz/io
%{_libdir}/graphviz/io/*
%{_mandir}/mann/gv_io.n*
%endif

#-- graphviz-java rpm ---------------------------------------------
%if %{JAVA}
%package java
Group:          Applications/Multimedia
Summary:        Java extension for graphviz
Requires:       graphviz = %{version}-%{release} java

%description java
Java extension for graphviz.

%files java
%defattr(-,root,root,-)
%dir %{_libdir}/graphviz/java
%{_libdir}/graphviz/java/*
%{_mandir}/mann/gv_java.n*
%endif

#-- graphviz-lua rpm ----------------------------------------------
%if %{LUA}
%package lua
Group:          Applications/Multimedia
Summary:        Lua extension for graphviz
Requires:       graphviz = %{version}-%{release} lua

%description lua
Lua extension for graphviz.

%files lua
%defattr(-,root,root,-)
%dir %{_libdir}/graphviz/lua
%{_libdir}/graphviz/lua/*
%{_mandir}/mann/gv_lua.n*
%endif

#-- graphviz-ocaml rpm --------------------------------------------
%if %{OCAML}
%package ocaml
Group:          Applications/Multimedia
Summary:        Ocaml extension for graphviz
Requires:       graphviz = %{version}-%{release} ocaml

%description ocaml
Ocaml extension for graphviz.

%files ocaml
%defattr(-,root,root,-)
%dir %{_libdir}/graphviz/ocaml
%{_libdir}/graphviz/ocaml/*
%{_mandir}/mann/gv_ocaml.n*
%endif

#-- graphviz-perl rpm ---------------------------------------------
%if %{PERL}
%package perl
Group:          Applications/Multimedia
Summary:        Perl extension for graphviz
Requires:       graphviz = %{version}-%{release} perl

%description perl
Perl extension for graphviz.

%files perl
%defattr(-,root,root,-)
%dir %{_libdir}/graphviz/perl
%{_libdir}/graphviz/perl/*
%{_mandir}/mann/gv_perl.n*
%endif

#-- graphviz-php rpm ----------------------------------------------
%if %{PHP}
%package php
Group:          Applications/Multimedia
Summary:        PHP extension for graphviz
Requires:       graphviz = %{version}-%{release} php

%description php
PHP extension for graphviz.

%files php
%defattr(-,root,root,-)
%dir %{_libdir}/graphviz/php
%{_libdir}/graphviz/php/*
%{_mandir}/mann/gv_php.n*
%endif

#-- graphviz-python rpm -------------------------------------------
%if %{PYTHON}
%package python
Group:          Applications/Multimedia
Summary:        Python extension for graphviz
Requires:       graphviz = %{version}-%{release} python

%description python
Python extension for graphviz.

%files python
%defattr(-,root,root,-)
%dir %{_libdir}/graphviz/python
%{_libdir}/graphviz/python/*
%{_mandir}/mann/gv_python.n*
%endif

#-- graphviz-r rpm ---------------------------------------------
%if %{R_LANG}
%package r
Group:          Applications/Multimedia
Summary:        R extension for graphviz
Requires:       graphviz = %{version}-%{release} r

%description r
R extension for graphviz.

%files r
%defattr(-,root,root,-)
%dir %{_libdir}/graphviz/r
%{_libdir}/graphviz/r/*
%{_mandir}/mann/gv_r.n*
%endif

#-- graphviz-ruby rpm ---------------------------------------------
%if %{RUBY}
%package ruby
Group:          Applications/Multimedia
Summary:        Ruby extension for graphviz
Requires:       graphviz = %{version}-%{release} ruby

%description ruby
Ruby extension for graphviz.

%files ruby
%defattr(-,root,root,-)
%dir %{_libdir}/graphviz/ruby
%{_libdir}/graphviz/ruby/*
%{_mandir}/mann/gv_ruby.n*
%endif

#-- graphviz-tcl rpm ----------------------------------------------
%if %{TCL}
%package tcl
Group:          Applications/Multimedia
Summary:        Tcl extension & tools for graphviz
Requires:       graphviz = %{version}-%{release} tcl >= 8.3 tk

%description tcl
Various tcl packages (extensions) for the graphviz tools.

%files tcl
%defattr(-,root,root,-)
%dir %{_libdir}/graphviz/tcl
%{_libdir}/graphviz/tcl/*
%{_libdir}/graphviz/pkgIndex.tcl
%{_datadir}/graphviz/demo
# hack to include gv_tcl.n only if available
#  always includes tcldot.n, gdtclft.n
%{_mandir}/mann/*tcl*.n*
%{_mandir}/mann/tkspline.n*
%endif

#-- graphviz-devel rpm --------------------------------------------
%package devel
Group:          Development/Libraries
Summary:        Development package for graphviz
Requires:       graphviz = %{version}-%{release} pkgconfig

%description devel
A collection of tools for the manipulation and layout
of graphs (as in nodes and edges, not as in barcharts).
This package contains development files for graphviz.

%files devel
%defattr(-,root,root,-)
%{_includedir}/graphviz
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*.3*
%exclude %{_libdir}/graphviz/*/*
%exclude %{_libdir}/graphviz/libgvplugin*
%exclude %{_libdir}/graphviz/*.so

#-- graphviz-graphs rpm -------------------------------------------
%package graphs
Group:          Applications/Multimedia
Summary:        Demo graphs for graphviz

%description graphs
Some demo graphs for graphviz.

%files graphs
%defattr(-,root,root,-)
%dir %{_datadir}/graphviz
%{_datadir}/graphviz/graphs

#-- graphviz-doc rpm ----------------------------------------------
%package doc
Group:          Documentation
Summary:        PDF and HTML documents for graphviz

%description doc
Provides some additional PDF and HTML documentation for graphviz.

%files doc
%defattr(-,root,root,-)
%doc __doc/*

#-- building --------------------------------------------------

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%if ! %{SHARP}
%define NO_SHARP --disable-sharp
%endif
%if ! %{GUILE}
%define NO_GUILE --disable-guile
%endif
%if ! %{_IO}
%define NO_IO --disable-io
%endif
%if ! %{JAVA}
%define NO_JAVA --disable-java
%endif
%if ! %{LUA}
%define NO_LUA --disable-lua
%endif
%if ! %{OCAML}
%define NO_OCAML --disable-ocaml
%endif
%if ! %{PERL}
%define NO_PERL --disable-perl
%endif
%if ! %{PHP}
%define NO_PHP --disable-php
%endif
%if ! %{PYTHON}
%define NO_PYTHON --disable-python
%endif
%if ! %{R_LANG}
%define NO_R_LANG --disable-r
%endif
%if ! %{RUBY}
%define NO_RUBY --disable-ruby
%endif
%if ! %{TCL}
%define NO_TCL --disable-tcl
%endif
%if ! %{DEVIL}
%define NO_DEVIL --without-devil
%endif
%if ! %{MING}
%define NO_MING --without-ming
%endif

# XXX ix86 only used to have -ffast-math, let's use everywhere
%{expand: %%define optflags %{optflags} -ffast-math}

# %%configure is broken in RH7.3 rpmbuild
CFLAGS="$RPM_OPT_FLAGS" \
./configure \
        --prefix=%{_prefix} \
        --bindir=%{_bindir} \
        --libdir=%{_libdir} \
        --includedir=%{_includedir} \
        --datadir=%{_datadir} \
        --mandir=%{_mandir} \
        --with-x \
	--disable-static \
        --disable-dependency-tracking \
	%{MYLIBGD} %{IPSEPCOLA} %{PANGOCAIRO} %{GDK_PIXBUF} \
        %{?NO_SHARP} %{?NO_GUILE} %{?NO_IO} %{?NO_JAVA} %{?NO_LUA} %{?NO_OCAML} %{?NO_PERL} %{?NO_PHP} %{?NO_PYTHON} %{?NO_R_LANG} %{?NO_RUBY} %{?NO_TCL} %{?NO_DEVIL} %{?NO_MING}
make %{?_smp_mflags}

%install
rm -rf %{buildroot} __doc
make DESTDIR=%{buildroot} \
        docdir=%{buildroot}%{_docdir}/%{name} \
        pkgconfigdir=%{_libdir}/pkgconfig \
        install
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
chmod -x %{buildroot}%{_datadir}/%{name}/lefty/*
cp -a %{buildroot}%{_datadir}/%{name}/doc __doc
rm -rf %{buildroot}%{_datadir}/%{name}/doc

%clean
# regression test
cd rtest
make rtest
# clean up temporary installation
rm -rf %{buildroot}

#-- changelog --------------------------------------------------

%changelog
* Tue Mar 04 2008 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.16.1-0.4
- Disable R support

* Mon Mar 03 2008 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.16.1-0.2
- New upstream release (fixes BZ#433205, BZ#427376)
- Merged spec changes in from upstream
- Added patch from BZ#432683

* Tue Feb 12 2008 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.16-3.3
- Added upstream-provided patch for building under GCC 4.3 (thanks John!)

* Thu Jan  3 2008 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.16-3.2
- Re-added tcl/tk 8.5 patch
- Tweaked ming stuff

* Thu Jan  3 2008 Alex Lancaster <alexlan[AT]fedoraproject.org> - 2.16-3.1
- Rebuild against new Tcl 8.5

* Wed Dec 12 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.16-2
- What the heck?  Can't BR stuff that hasn't even gotten reviewed yet.

* Wed Nov 28 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.16-1
- New upstream release
- Remove arith.h patch

* Tue Sep 04 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.14.1-3
- Patch to resurrect arith.h

* Thu Aug 23 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 2.14.1-2
- Added perl-devel to BR for F7+

* Wed Aug 15 2007 John Ellson <ellson@research.att.com>
- release 2.14.1 - see ChangeLog for details
* Wed Aug 2 2007 John Ellson <ellson@research.att.com>
- release 2.14 - see ChangeLog for details
* Fri Mar 16 2007 Stephen North <north@research.att.com>
- remove xorg-X11-devel from rhel >= 5
* Mon Dec 11 2006 John Ellson <john.ellson@comcast.net>
- fix graphviz-lua description (Fedora BZ#218191)
* Tue Sep 13 2005 John Ellson <ellson@research.att.com>
- split out language bindings into their own rpms so that 
  main rpm doesn't depend on (e.g.) ocaml

* Sat Aug 13 2005 John Ellson <ellson@research.att.com>
- imported various fixes from the Fedora-Extras .spec by Oliver Falk <oliver@linux-kernel.at>

* Wed Jul 20 2005 John Ellson <ellson@research.att.com>
- release 2.4
