%define		_status		beta
%define		_pearname	Text_Highlighter
%include	/usr/lib/rpm/macros.php
Summary:	%{_pearname} - syntax highlighting
Summary(pl.UTF-8):	%{_pearname} - podświetlanie składni
Name:		php-pear-%{_pearname}
Version:	0.8.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	0eb11e9588ad5c7a1046ffad3ca2aed8
URL:		http://pear.php.net/package/Text_Highlighter/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 5.4.0
Requires:	php-pear
Requires:	php-pear-Console_Getopt >= 1.4.1
Requires:	php-pear-PEAR-core >= 1:1.10.3
Requires:	php-pear-XML_Parser >= 1.3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text_Highlighter is a package for syntax highlighting.

It provides a base class providing all the functionality, and a
descendent classes geneator class.

The main idea is to simplify creation of subclasses implementing
syntax highlighting for particular language. Subclasses do not
implement any new functionality, they just provide syntax highlighting
rules. The rules sources are in XML format.

To create a highlighter for a language, there is no need to code a new
class manually. Simply describe the rules in XML file and use
Text_Highlighter_Generator to create a new class.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Text_Highlighter to pakiet do podświetlania składni.

Zawiera klasę bazową dostarczającą całą funkcjonalność i klasę
generującą klasy dziedziczące.

Główną ideą jest uproszczenie tworzenia podklas implementujących
podświetlanie składni dla danego języka. Podklasy nie implementują
żadnej nowej funkcjonalności, a jedynie dostarczają reguły
podświetlania składni. Źródła reguł są w formacie XML.

Aby stworzyć podświetlanie dla języka, nie trzeba kodować ręcznie
nowej klasy. Wystarczy opisać reguły w pliku XML i użyć
Text_Highlighter_Generator, aby utworzyć nową klasę.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{php_pear_dir}}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Text/*.php
%{php_pear_dir}/Text/Highlighter

%{php_pear_dir}/data/%{_pearname}
