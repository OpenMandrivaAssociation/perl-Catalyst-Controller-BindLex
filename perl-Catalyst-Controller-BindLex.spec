%define realname Catalyst-Controller-BindLex
%define name	perl-%{realname}
%define	modprefix Catalyst

%define version	0.05

%define release	%mkrel 1

Summary:	Stash your lexical goodness
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}/
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{realname}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel >= 5.8.1
%endif
BuildRequires:	perl(Array::RefElem)
BuildRequires:	perl(Catalyst)
BuildRequires:	perl(Devel::Caller)
BuildRequires:	perl(Devel::LexAlias)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(PadWalker)
BuildRequires:	perl(Test::use::ok)
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}

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
%setup -q -n %{realname}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/*/*
%{perl_vendorlib}/%{modprefix}

%clean
rm -rf %{buildroot}

