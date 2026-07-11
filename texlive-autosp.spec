%global tl_name autosp
%global tl_revision 77851

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A Preprocessor that generates note-spacing commands for MusiXTeX scores
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/autosp
License:	gpl2+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/autosp.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/autosp.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(autosp.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This program simplifies the creation of MusiXTeX scores by converting
(non-standard) commands of the form \anotes ... \en into one or more
conventional note-spacing commands, as determined by the note values
themselves, with \sk spacing commands inserted as necessary. The coding
for an entire measure can be entered one part at a time, without concern
for note-spacing changes within the part or spacing requirements of
other parts. For example, \anotes\qa J\qa K&\ca l\qa m\ca n\en generates
\Notes\qa J\sk\qa K\sk&\ca l\qa m\sk\ca n\en .

