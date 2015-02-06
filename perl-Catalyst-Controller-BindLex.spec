%define upstream_name    Catalyst-Controller-BindLex
%define upstream_version 0.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Stash your lexical goodness
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Array::RefElem)
BuildRequires:	perl(Catalyst)
BuildRequires:	perl(Devel::Caller)
BuildRequires:	perl(Devel::LexAlias)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(PadWalker)
BuildRequires:	perl(Test::use::ok)
BuildArch:	noarch

%description
This plugin lets you put your lexicals on the stash and elsewhere very
easily.

It uses some funky modules to get it's job done: PadWalker,
Array::RefElem, Devel::Caller, Devel::LexAlias and attributes. In some
people's opinion this hurts this plugin's reputation ;-).

If you use the same name for two variables with the same storage
binding attribute they will be aliased to each other, so you can use
this for reading as well as writing values across controller
subs. This is almost like sharing your lexical scope.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/*/*
%{perl_vendorlib}/Catalyst


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.50.0-2mdv2011.0
+ Revision: 680718
- mass rebuild

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2011.0
+ Revision: 406259
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.05-2mdv2009.0
+ Revision: 268391
- rebuild early 2009.0 package (before pixel changes)

* Wed May 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-1mdv2009.0
+ Revision: 212791
- new version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-2mdv2008.0
+ Revision: 85924
- rebuild


* Mon May 29 2006 Scott Karns <scottk@mandriva.org> 0.03-1mdv2007.0
- Version 0.03

* Mon May 08 2006 Scott Karns <scottk@mandriva.org> 0.02-1mdk
- Version 0.02
- Updated BuildRequires to include perl(Module::Build)

* Sun Mar 12 2006 Scott Karns <scott@karnstech.com> 0.01-1mdk
- First Mandriva release

