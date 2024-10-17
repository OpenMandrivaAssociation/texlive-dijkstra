Name:		texlive-dijkstra
Version:	64580
Release:	2
Summary:	Dijkstra algorithm for LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/dijkstra
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dijkstra.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dijkstra.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This small package uses the Dijkstra algorithm for weighted
graphs,directed or not: the search table of the shortest path
can be displayed, the minimum distance between two vertices and
the corresponding path are stored in macros. This packages
depends on simplekv.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/dijkstra
%doc %{_texmfdistdir}/doc/latex/dijkstra

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
