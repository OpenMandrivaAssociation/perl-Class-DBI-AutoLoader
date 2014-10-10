%define upstream_name    Class-DBI-AutoLoader
%define upstream_version 0.12

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Generates Class::DBI subclasses dynamically
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(DBI)
BuildArch:	noarch

%description
Class::DBI::AutoLoader scans the tables in a given database, and auto-generates
the Class::DBI classes. These are loaded into your package when you import
Class::DBI::AutoLoader, as though you had created the Data::FavoriteFilms class
and "use"d that directly.

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
%{perl_vendorlib}/Class
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.120.0-2mdv2011.0
+ Revision: 680788
- mass rebuild

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.120.0-1mdv2011.0
+ Revision: 403008
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.12-6mdv2009.0
+ Revision: 241177
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.12-4mdv2008.0
+ Revision: 86087
- rebuild


* Mon Aug 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.12-3mdv2007.0
- Rebuild

* Wed Dec 28 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.12-2mdk
- fix buildrequires

* Mon Dec 05 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.12-1mdk
- initial Mandriva package

