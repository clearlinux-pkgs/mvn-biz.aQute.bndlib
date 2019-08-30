#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-biz.aQute.bndlib
Version  : 3.0.0
Release  : 10
URL      : https://repo1.maven.org/maven2/biz/aQute/bnd/biz.aQute.bndlib/3.0.0/biz.aQute.bndlib-3.0.0.jar
Source0  : https://repo1.maven.org/maven2/biz/aQute/bnd/biz.aQute.bndlib/3.0.0/biz.aQute.bndlib-3.0.0.jar
Source1  : https://repo1.maven.org/maven2/biz/aQute/bnd/biz.aQute.bndlib/2.4.1/biz.aQute.bndlib-2.4.1.jar
Source2  : https://repo1.maven.org/maven2/biz/aQute/bnd/biz.aQute.bndlib/2.4.1/biz.aQute.bndlib-2.4.1.pom
Source3  : https://repo1.maven.org/maven2/biz/aQute/bnd/biz.aQute.bndlib/3.0.0/biz.aQute.bndlib-3.0.0.jar
Source4  : https://repo1.maven.org/maven2/biz/aQute/bnd/biz.aQute.bndlib/3.0.0/biz.aQute.bndlib-3.0.0.pom
Source5  : https://repo1.maven.org/maven2/biz/aQute/bnd/biz.aQute.bndlib/3.2.0/biz.aQute.bndlib-3.2.0.jar
Source6  : https://repo1.maven.org/maven2/biz/aQute/bnd/biz.aQute.bndlib/3.2.0/biz.aQute.bndlib-3.2.0.pom
Source7  : https://repo1.maven.org/maven2/biz/aQute/bnd/biz.aQute.bndlib/3.4.0/biz.aQute.bndlib-3.4.0.jar
Source8  : https://repo1.maven.org/maven2/biz/aQute/bnd/biz.aQute.bndlib/3.4.0/biz.aQute.bndlib-3.4.0.pom
Source9  : https://repo1.maven.org/maven2/biz/aQute/bnd/biz.aQute.bndlib/4.0.0/biz.aQute.bndlib-4.0.0.jar
Source10  : https://repo1.maven.org/maven2/biz/aQute/bnd/biz.aQute.bndlib/4.0.0/biz.aQute.bndlib-4.0.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-biz.aQute.bndlib-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-biz.aQute.bndlib package.
Group: Data

%description data
data components for the mvn-biz.aQute.bndlib package.


%prep
%setup -q -n META-INF

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/biz/aQute/bnd/biz.aQute.bndlib/3.0.0
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/biz/aQute/bnd/biz.aQute.bndlib/3.0.0/biz.aQute.bndlib-3.0.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/biz/aQute/bnd/biz.aQute.bndlib/2.4.1
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/biz/aQute/bnd/biz.aQute.bndlib/2.4.1/biz.aQute.bndlib-2.4.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/biz/aQute/bnd/biz.aQute.bndlib/2.4.1
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/biz/aQute/bnd/biz.aQute.bndlib/2.4.1/biz.aQute.bndlib-2.4.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/biz/aQute/bnd/biz.aQute.bndlib/3.0.0
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/biz/aQute/bnd/biz.aQute.bndlib/3.0.0/biz.aQute.bndlib-3.0.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/biz/aQute/bnd/biz.aQute.bndlib/3.0.0
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/biz/aQute/bnd/biz.aQute.bndlib/3.0.0/biz.aQute.bndlib-3.0.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/biz/aQute/bnd/biz.aQute.bndlib/3.2.0
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/biz/aQute/bnd/biz.aQute.bndlib/3.2.0/biz.aQute.bndlib-3.2.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/biz/aQute/bnd/biz.aQute.bndlib/3.2.0
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/biz/aQute/bnd/biz.aQute.bndlib/3.2.0/biz.aQute.bndlib-3.2.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/biz/aQute/bnd/biz.aQute.bndlib/3.4.0
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/biz/aQute/bnd/biz.aQute.bndlib/3.4.0/biz.aQute.bndlib-3.4.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/biz/aQute/bnd/biz.aQute.bndlib/3.4.0
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/biz/aQute/bnd/biz.aQute.bndlib/3.4.0/biz.aQute.bndlib-3.4.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/biz/aQute/bnd/biz.aQute.bndlib/4.0.0
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/biz/aQute/bnd/biz.aQute.bndlib/4.0.0/biz.aQute.bndlib-4.0.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/biz/aQute/bnd/biz.aQute.bndlib/4.0.0
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/biz/aQute/bnd/biz.aQute.bndlib/4.0.0/biz.aQute.bndlib-4.0.0.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/biz/aQute/bnd/biz.aQute.bndlib/2.4.1/biz.aQute.bndlib-2.4.1.jar
/usr/share/java/.m2/repository/biz/aQute/bnd/biz.aQute.bndlib/2.4.1/biz.aQute.bndlib-2.4.1.pom
/usr/share/java/.m2/repository/biz/aQute/bnd/biz.aQute.bndlib/3.0.0/biz.aQute.bndlib-3.0.0.jar
/usr/share/java/.m2/repository/biz/aQute/bnd/biz.aQute.bndlib/3.0.0/biz.aQute.bndlib-3.0.0.pom
/usr/share/java/.m2/repository/biz/aQute/bnd/biz.aQute.bndlib/3.2.0/biz.aQute.bndlib-3.2.0.jar
/usr/share/java/.m2/repository/biz/aQute/bnd/biz.aQute.bndlib/3.2.0/biz.aQute.bndlib-3.2.0.pom
/usr/share/java/.m2/repository/biz/aQute/bnd/biz.aQute.bndlib/3.4.0/biz.aQute.bndlib-3.4.0.jar
/usr/share/java/.m2/repository/biz/aQute/bnd/biz.aQute.bndlib/3.4.0/biz.aQute.bndlib-3.4.0.pom
/usr/share/java/.m2/repository/biz/aQute/bnd/biz.aQute.bndlib/4.0.0/biz.aQute.bndlib-4.0.0.jar
/usr/share/java/.m2/repository/biz/aQute/bnd/biz.aQute.bndlib/4.0.0/biz.aQute.bndlib-4.0.0.pom
