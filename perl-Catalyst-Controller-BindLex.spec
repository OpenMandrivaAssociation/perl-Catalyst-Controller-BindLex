%define upstream_name    Catalyst-Controller-BindLex
%define upstream_version 0.05

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Stash your lexical goodness
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.bz2

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
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

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
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/*/*
%{perl_vendorlib}/Catalyst
