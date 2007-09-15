%define module  Class-DBI-AutoLoader
%define name    perl-%{module}
%define version 0.12
%define release %mkrel 4

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Generates Class::DBI subclasses dynamically
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Class/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl(DBI)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
Class::DBI::AutoLoader scans the tables in a given database, and auto-generates
the Class::DBI classes. These are loaded into your package when you import
Class::DBI::AutoLoader, as though you had created the Data::FavoriteFilms class
and "use"d that directly.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Class
%{_mandir}/*/*

