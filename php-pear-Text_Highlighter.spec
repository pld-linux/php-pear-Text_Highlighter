# ToDo:
# - think about renaming generate script
%include	/usr/lib/rpm/macros.php
%define		_class		Text
%define		_subclass	Highlighter
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Syntax highlighting
Summary(pl):	%{_pearname} - Pod�wietlanie sk�adni
Name:		php-pear-%{_pearname}
Version:	0.6.5
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	a8c7b53efbc023f4f02b178a06b27960
URL:		http://pear.php.net/package/Text_Highlighter/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text_Highlighter is a package for syntax highlighting.

It provides a base class providing all the functionality, and a
descendent classes geneator class.

The main idea is to simplify creation of subclasses implementing
syntax highlighting for particular language. Subclasses do not
implement any new functionality, they just provide syntax
highlighting rules. The rules sources are in XML format.

To create a highlighter for a language, there is no need to code a new
class manually. Simply describe the rules in XML file and use
Text_Highlighter_Generator to create a new class.

In PEAR status of this package is: %{_status}.

%description -l pl
Text_Highlighter to pakiet do pod�wietlania sk�adni.

Zawiera klas� bazow� dostarczaj�c� ca�� funkcjonalno�� i klas�
generuj�c� klasy dziedzicz�ce.

G��wn� ide� jest uproszczenie tworzenia podklas implementuj�cych
pod�wietlanie sk�adni dla danego j�zyka. Podklasy nie implementuj�
�adnej nowej funkcjonalno�ci, a jedynie dostarczaj� regu�y
pod�wietlania sk�adni. �r�d�a regu� s� w formacie XML.

Aby stworzy� pod�wietlanie dla j�zyka, nie trzeba kodowa� r�cznie
nowej klasy. Wystarczy opisa� regu�y w pliku XML i u�y�
Text_Highlighter_Generator, aby utworzy� now� klas�.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%build
sed -i -e 's,@php_bin@,%{_bindir}/php,' %{_pearname}-%{version}/generate

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{php_pear_dir}/%{_class}/%{_subclass}/Renderer}

install %{_pearname}-%{version}/generate $RPM_BUILD_ROOT%{_bindir}
install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/*.xml $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}
install %{_pearname}-%{version}/%{_subclass}/Renderer/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Renderer

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/README
%attr(755,root,root) %{_bindir}/*
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
