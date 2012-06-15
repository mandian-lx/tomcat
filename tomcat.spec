# Copyright (c) 2000-2008, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%global jspspec 2.2
%global major_version 7
%global minor_version 0
%global micro_version 27
%global packdname apache-tomcat-%{version}-src
%global servletspec 3.0
%global elspec 2.2
%global tcuid 91

# FHS 2.3 compliant tree structure - http://www.pathname.com/fhs/2.3/
%global basedir %{_var}/lib/%{name}
%global appdir %{basedir}/webapps
%global homedir %{_datadir}/%{name}
%global bindir %{homedir}/bin
%global confdir %{_sysconfdir}/%{name}
%global libdir %{_javadir}/%{name}
%global logdir %{_var}/log/%{name}
%global cachedir %{_var}/cache/%{name}
%global tempdir %{cachedir}/temp
%global workdir %{cachedir}/work
%global _initrddir %{_sysconfdir}/init.d
%global _systemddir /lib/systemd/system

Name:          tomcat
Version:       %{major_version}.%{minor_version}.%{micro_version}
Release:       1
Summary:       Apache Servlet/JSP Engine, RI for Servlet %{servletspec}/JSP %{jspspec} API

Group:         Networking/WWW
License:       ASL 2.0
URL:           http://tomcat.apache.org/
Source0:       http://www.apache.org/dist/tomcat/tomcat-%{major_version}/v%{version}/src/%{packdname}.tar.gz
Source1:       %{name}-%{major_version}.%{minor_version}.conf
Source2:       %{name}-%{major_version}.%{minor_version}.init
Source3:       %{name}-%{major_version}.%{minor_version}.sysconfig
Source4:       %{name}-%{major_version}.%{minor_version}.wrapper
Source5:       %{name}-%{major_version}.%{minor_version}.logrotate
Source6:       %{name}-%{major_version}.%{minor_version}-digest.script
Source7:       %{name}-%{major_version}.%{minor_version}-tool-wrapper.script
Source8:       servlet-api-OSGi-MANIFEST.MF
Source9:       jsp-api-OSGi-MANIFEST.MF
Source10:      %{name}-%{major_version}.%{minor_version}-log4j.properties
Source11:      %{name}-%{major_version}.%{minor_version}.service
Patch0:        %{name}-%{major_version}.%{minor_version}-bootstrap-MANIFEST.MF.patch
Patch1:        %{name}-%{major_version}.%{minor_version}-tomcat-users-webapp.patch

BuildArch:     noarch

BuildRequires: ant
BuildRequires: ant-nodeps
BuildRequires: ecj
BuildRequires: findutils
BuildRequires: apache-commons-collections
BuildRequires: apache-commons-daemon
BuildRequires: apache-commons-dbcp
BuildRequires: apache-commons-pool
BuildRequires: jakarta-taglibs-standard
BuildRequires: java-devel >= 0:1.6.0
BuildRequires: jpackage-utils >= 0:1.7.0
BuildRequires: junit
BuildRequires: log4j
BuildRequires: geronimo-jaxrpc
BuildRequires: wsdl4j
Requires:      apache-commons-daemon
Requires:      apache-commons-logging
Requires:      apache-commons-collections
Requires:      apache-commons-dbcp
Requires:      apache-commons-pool
Requires:      java >= 0:1.6.0
Requires:      procps
Requires:      %{name}-lib = %{version}-%{release}
Requires(pre):    shadow-utils
Requires(post):   chkconfig
Requires(preun):  chkconfig
Requires(post):   jpackage-utils
Requires(postun): jpackage-utils

%description
Tomcat is the servlet container that is used in the official Reference
Implementation for the Java Servlet and JavaServer Pages technologies.
The Java Servlet and JavaServer Pages specifications are developed by
Sun under the Java Community Process.

Tomcat is developed in an open and participatory environment and
released under the Apache Software License version 2.0. Tomcat is intended
to be a collaboration of the best-of-breed developers from around the world.

%package admin-webapps
Group: Networking/WWW
Summary: The host-manager and manager web applications for Apache Tomcat
Requires: %{name} = %{version}-%{release}

%description admin-webapps
The host-manager and manager web applications for Apache Tomcat.

%package docs-webapp
Group: Networking/WWW
Summary: The docs web application for Apache Tomcat
Requires: %{name} = %{version}-%{release}

%description docs-webapp
The docs web application for Apache Tomcat.

%package javadoc
Group: Development/Java
Summary: Javadoc generated documentation for Apache Tomcat
Requires: jpackage-utils

%description javadoc
Javadoc generated documentation for Apache Tomcat.

%package jsp-%{jspspec}-api
Group: Development/Java
Summary: Apache Tomcat JSP API implementation classes
Provides: jsp = %{jspspec}
Provides: jsp22
Requires: %{name}-servlet-%{servletspec}-api = %{version}-%{release}
Requires(post): chkconfig
Requires(postun): chkconfig

%description jsp-%{jspspec}-api
Apache Tomcat JSP API implementation classes.


%package lib
Group: Development/Java
Summary: Libraries needed to run the Tomcat Web container
Requires: %{name}-jsp-%{jspspec}-api = %{version}-%{release}
Requires: %{name}-servlet-%{servletspec}-api = %{version}-%{release}
Requires: %{name}-el-%{elspec}-api = %{version}-%{release}
Requires: ecj
Requires: apache-commons-collections
Requires: apache-commons-dbcp
Requires: apache-commons-pool
Requires(preun): coreutils

%description lib
Libraries needed to run the Tomcat Web container.

%package servlet-%{servletspec}-api
Group: Development/Java
Summary: Apache Tomcat Servlet API implementation classes
Provides: servlet = %{servletspec}
Provides: servlet6
Provides: servlet3
Requires(post): chkconfig
Requires(postun): chkconfig

%description servlet-%{servletspec}-api
Apache Tomcat Servlet API implementation classes.

%package el-%{elspec}-api
Group: Development/Java
Summary: Expression Language v1.0 API
Provides: el_1_0_api = %{version}-%{release}
Provides: el_api = %{elspec}
Requires(post): chkconfig
Requires(postun): chkconfig

%description el-%{elspec}-api
Expression Language 1.0.

%package webapps
Group: Networking/WWW
Summary: The ROOT and examples web applications for Apache Tomcat
Requires: %{name} = %{version}-%{release}
Requires: jakarta-taglibs-standard >= 0:1.1

%description webapps
The ROOT and examples web applications for Apache Tomcat.

%prep
%setup -q -n %{packdname}
# remove pre-built binaries and windows files
find . -type f \( -name "*.bat" -o -name "*.class" -o -name Thumbs.db -o -name "*.gz" -o \
   -name "*.jar" -o -name "*.war" -o -name "*.zip" \) -delete

%patch0 -p0
%patch1 -p0
%{__ln_s} $(build-classpath jakarta-taglibs-core) webapps/examples/WEB-INF/lib/jstl.jar
%{__ln_s} $(build-classpath jakarta-taglibs-standard) webapps/examples/WEB-INF/lib/standard.jar

%build
export OPT_JAR_LIST="xalan-j2-serializer"
   # we don't care about the tarballs and we're going to replace
   # tomcat-dbcp.jar with apache-commons-{collections,dbcp,pool}-tomcat5.jar
   # so just create a dummy file for later removal
   touch HACK
   %{__mkdir_p} HACKDIR
   touch HACKDIR/build.xml
   # who needs a build.properties file anyway
   %{ant} -Dbase.path="." \
      -Dbuild.compiler="modern" \
      -Dcommons-collections.jar="$(build-classpath apache-commons-collections)" \
      -Dcommons-daemon.jar="$(build-classpath apache-commons-daemon)" \
      -Dcommons-daemon.native.src.tgz="HACK" \
      -Djasper-jdt.jar="$(build-classpath ecj)" \
      -Djdt.jar="$(build-classpath ecj)" \
      -Dtomcat-dbcp.jar="$(build-classpath apache-commons-dbcp)" \
      -Dtomcat-native.tar.gz="HACK" \
      -Dtomcat-native.dll.win32="HACK" \
      -Dtomcat-native.dll.x64="HACK" \
      -Dtomcat-native.dll.i64="HACK" \
      -Dcommons-daemon.native.win.mgr.exe="HACK" \
      -Dnsis.exe="HACK" \
      -Djaxrpc-lib.jar="$(build-classpath jaxrpc)" \
      -Dwsdl4j-lib.jar="$(build-classpath wsdl4j)" \
      -Dcommons-pool.home="HACKDIR" \
      -Dcommons-dbcp.home="HACKDIR" \
      -Dno.build.dbcp=true \
      -Dversion="%{version}" \
      -Dversion.build="%{micro_version}" \
      deploy dist-prepare dist-source javadoc

    # remove some jars that we'll replace with symlinks later
   %{__rm} output/build/bin/commons-daemon.jar \
           output/build/lib/ecj.jar
    # remove the cruft we created
   %{__rm} output/build/bin/tomcat-native.tar.gz
pushd output/dist/src/webapps/docs/appdev/sample/src
%{__mkdir_p} ../web/WEB-INF/classes
%{javac} -cp ../../../../../../../../output/build/lib/servlet-api.jar -d ../web/WEB-INF/classes mypackage/Hello.java
pushd ../web
%{jar} cf ../../../../../../../../output/build/webapps/docs/appdev/sample/sample.war *
popd
popd

# inject OSGi manifests
mkdir -p META-INF
cp -p %{SOURCE8} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u output/build/lib/servlet-api.jar META-INF/MANIFEST.MF
cp -p %{SOURCE9} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u output/build/lib/jsp-api.jar META-INF/MANIFEST.MF

%install
# build initial path structure
%{__install} -d -m 0755 %{buildroot}%{_bindir}
%{__install} -d -m 0755 %{buildroot}%{_sbindir}
%{__install} -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
%{__install} -d -m 0755 %{buildroot}%{_initrddir}
%{__install} -d -m 0755 %{buildroot}%{_systemddir}
%{__install} -d -m 0755 %{buildroot}%{_sysconfdir}/logrotate.d
%{__install} -d -m 0755 %{buildroot}%{_sysconfdir}/sysconfig
%{__install} -d -m 0755 %{buildroot}%{appdir}
%{__install} -d -m 0755 %{buildroot}%{bindir}
%{__install} -d -m 0775 %{buildroot}%{confdir}
%{__install} -d -m 0775 %{buildroot}%{confdir}/Catalina/localhost
%{__install} -d -m 0755 %{buildroot}%{libdir}
%{__install} -d -m 0775 %{buildroot}%{logdir}
/bin/touch %{buildroot}%{logdir}/catalina.out
/bin/echo "%{name}-%{major_version}.%{minor_version}.%{micro_version} RPM installed" >> %{buildroot}%{logdir}/catalina.out
%{__install} -d -m 0775 %{buildroot}%{homedir}
%{__install} -d -m 0775 %{buildroot}%{tempdir}
%{__install} -d -m 0775 %{buildroot}%{workdir}

# move things into place
# First copy supporting libs to tomcat lib
pushd output/build
    cp -a bin/*.{jar,xml} %{buildroot}%{bindir}
    cp %{SOURCE10} conf/log4j.properties
    cp -a conf/*.{policy,properties,xml} %{buildroot}%{confdir}
    cp -a lib/*.jar %{buildroot}%{libdir}
    cp -a webapps/* %{buildroot}%{appdir}
popd
# javadoc
cp -a output/dist/webapps/docs/api/* %{buildroot}%{_javadocdir}/%{name}

%{__sed} -e "s|\@\@\@TCHOME\@\@\@|%{homedir}|g" \
   -e "s|\@\@\@TCTEMP\@\@\@|%{tempdir}|g" \
   -e "s|\@\@\@LIBDIR\@\@\@|%{_libdir}|g" %{SOURCE1} \
    > %{buildroot}%{confdir}/%{name}.conf
%{__sed} -e "s|\@\@\@TCHOME\@\@\@|%{homedir}|g" \
   -e "s|\@\@\@TCTEMP\@\@\@|%{tempdir}|g" \
   -e "s|\@\@\@LIBDIR\@\@\@|%{_libdir}|g" %{SOURCE3} \
    > %{buildroot}%{_sysconfdir}/sysconfig/%{name}
%{__install} -m 0644 %{SOURCE2} \
    %{buildroot}%{_initrddir}/%{name}
%{__install} -m 0644 %{SOURCE4} \
    %{buildroot}%{_sbindir}/%{name}
%{__install} -m 0644 %{SOURCE11} \
    %{buildroot}%{_systemddir}/%{name}.service
%{__ln_s} %{name} %{buildroot}%{_sbindir}/d%{name}
%{__sed} -e "s|\@\@\@TCLOG\@\@\@|%{logdir}|g" %{SOURCE5} \
    > %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
%{__sed} -e "s|\@\@\@TCHOME\@\@\@|%{homedir}|g" \
   -e "s|\@\@\@TCTEMP\@\@\@|%{tempdir}|g" \
   -e "s|\@\@\@LIBDIR\@\@\@|%{_libdir}|g" %{SOURCE6} \
    > %{buildroot}%{_bindir}/%{name}-digest
%{__sed} -e "s|\@\@\@TCHOME\@\@\@|%{homedir}|g" \
   -e "s|\@\@\@TCTEMP\@\@\@|%{tempdir}|g" \
   -e "s|\@\@\@LIBDIR\@\@\@|%{_libdir}|g" %{SOURCE7} \
    > %{buildroot}%{_bindir}/%{name}-tool-wrapper
# create jsp and servlet API symlinks
pushd %{buildroot}%{_javadir}
   %{__mv} %{name}/jsp-api.jar %{name}-jsp-%{jspspec}-api.jar
   %{__ln_s} %{name}-jsp-%{jspspec}-api.jar %{name}-jsp-api.jar
   %{__mv} %{name}/servlet-api.jar %{name}-servlet-%{servletspec}-api.jar
   %{__ln_s} %{name}-servlet-%{servletspec}-api.jar %{name}-servlet-api.jar
   %{__mv} %{name}/el-api.jar %{name}-el-%{elspec}-api.jar
   %{__ln_s} %{name}-el-%{elspec}-api.jar %{name}-el-api.jar
popd

pushd output/build
    %{_bindir}/build-jar-repository lib apache-commons-collections \
                                        apache-commons-dbcp apache-commons-pool ecj 2>&1
    # need to use -p here with b-j-r otherwise the examples webapp fails to
    # load with a java.io.IOException
    %{_bindir}/build-jar-repository -p webapps/examples/WEB-INF/lib \
    taglibs-core.jar taglibs-standard.jar 2>&1
popd

pushd %{buildroot}%{libdir}
    # symlink JSP and servlet API jars
    %{__ln_s} ../%{name}-jsp-%{jspspec}-api.jar .
    %{__ln_s} ../%{name}-servlet-%{servletspec}-api.jar .
    %{__ln_s} ../%{name}-el-%{elspec}-api.jar .
    %{__ln_s} $(build-classpath apache-commons-collections) commons-collections.jar
    %{__ln_s} $(build-classpath apache-commons-dbcp) commons-dbcp.jar
    %{__ln_s} $(build-classpath log4j) log4j.jar
    %{__ln_s} $(build-classpath ecj) jasper-jdt.jar

    # Link the juli jar here from /usr/share/java/tomcat
    %{__ln_s} %{bindir}/tomcat-juli.jar .
popd

# symlink to the FHS locations where we've installed things
pushd %{buildroot}%{homedir}
    %{__ln_s} %{appdir} webapps
    %{__ln_s} %{confdir} conf
    %{__ln_s} %{libdir} lib
    %{__ln_s} %{logdir} logs
    %{__ln_s} %{tempdir} temp
    %{__ln_s} %{workdir} work
popd

# install sample webapp
%{__mkdir_p} %{buildroot}%{appdir}/sample
pushd %{buildroot}%{appdir}/sample
%{jar} xf %{buildroot}%{appdir}/docs/appdev/sample/sample.war
popd
%{__rm} %{buildroot}%{appdir}/docs/appdev/sample/sample.war


# Generate a depmap fragment javax.servlet:servlet-api pointing to
# tomcat-servlet-3.0-api for backwards compatibility
%add_to_maven_depmap javax.servlet servlet-api %{servletspec} JPP %{name}-servlet-%{servletspec}-api
# also provide jetty depmap (originally in jetty package, but it's cleaner to have it here)
%add_to_maven_depmap org.mortbay.jetty servlet-api %{servletspec} JPP %{name}-servlet-%{servletspec}-api
mv %{buildroot}%{_mavendepmapfragdir}/%{name} %{buildroot}%{_mavendepmapfragdir}/%{name}-servlet-api

# Install the maven metadata
%{__install} -d -m 0755 %{buildroot}%{_mavenpomdir}
pushd output/dist/src/res/maven
for pom in *.pom; do
    # fix-up version in all pom files
    sed -i 's/@MAVEN.DEPLOY.VERSION@/%{version}/g' $pom
done

# we won't install dbcp, juli-adapters and juli-extras pom files
for pom in tomcat-annotations-api.pom tomcat-catalina.pom tomcat-jasper-el.pom tomcat-jasper.pom \
           tomcat-catalina-ha.pom ; do
    cp -a $pom %{buildroot}%{_mavenpomdir}/JPP.$pom
    base=`basename $pom .pom`
    %add_to_maven_depmap org.apache.tomcat $base %{version} JPP/%{name} $base
done

# servlet-api jsp-api and el-api are not in tomcat subdir, since they are widely re-used elsewhere
for pom in tomcat-jsp-api.pom tomcat-servlet-api.pom tomcat-el-api.pom;do
    cp -a $pom %{buildroot}%{_mavenpomdir}/JPP-%{name}-$pom
    base=`basename $pom .pom`
    %add_to_maven_depmap org.apache.tomcat $base %{version} JPP %{name}-$base
done

# two special pom where jar files have different names
cp -a tomcat-tribes.pom %{buildroot}%{_mavenpomdir}/JPP.%{name}-catalina-tribes.pom
%add_to_maven_depmap org.apache.tomcat tribes %{version} JPP/%{name} catalina-tribes

cp -a tomcat-juli.pom %{buildroot}%{_mavenpomdir}/JPP.%{name}-tomcat-juli.pom
%add_to_maven_depmap org.apache.tomcat juli %{version} JPP/%{name} tomcat-juli

cp -a tomcat-util.pom %{buildroot}%{_mavenpomdir}/JPP.%{name}-tomcat-util.pom
%add_to_maven_depmap org.apache.tomcat util %{version} JPP/%{name} tomcat-util

cp -a tomcat-api.pom %{buildroot}%{_mavenpomdir}/JPP.%{name}-tomcat-api.pom
%add_to_maven_depmap org.apache.tomcat api %{version} JPP/%{name} tomcat-api

%pre
# add the tomcat user and group
%{_sbindir}/groupadd -g %{tcuid} -r tomcat 2>/dev/null || :
%{_sbindir}/useradd -c "Apache Tomcat" -u %{tcuid} -g tomcat \
    -s /bin/nologin -r -d %{homedir} tomcat 2>/dev/null || :

%post
# install but don't activate
/sbin/chkconfig --add %{name}
%update_maven_depmap

%post jsp-%{jspspec}-api
%{_sbindir}/update-alternatives --install %{_javadir}/jsp.jar jsp \
    %{_javadir}/%{name}-jsp-%{jspspec}-api.jar 20100

%post servlet-%{servletspec}-api
%{_sbindir}/update-alternatives --install %{_javadir}/servlet.jar servlet \
    %{_javadir}/%{name}-servlet-%{servletspec}-api.jar 20500
%update_maven_depmap

%post el-%{elspec}-api
%{_sbindir}/update-alternatives --install %{_javadir}/elspec.jar elspec \
   %{_javadir}/%{name}-el-%{elspec}-api.jar 20250

%preun
# clean tempdir and workdir on removal or upgrade
%{__rm} -rf %{workdir}/* %{tempdir}/*
if [ "$1" = "0" ]; then
    %{_initrddir}/%{name} stop >/dev/null 2>&1
    /sbin/chkconfig --del %{name}
fi


%postun
%update_maven_depmap

%postun jsp-%{jspspec}-api
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove jsp \
        %{_javadir}/%{name}-jsp-%{jspspec}-api.jar
fi

%postun servlet-%{servletspec}-api
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove servlet \
        %{_javadir}/%{name}-servlet-%{servletspec}-api.jar
    %update_maven_depmap
fi

%postun el-%{elspec}-api
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove elspec \
        %{_javadir}/%{name}-el-%{elspec}-api.jar
fi

%files
%defattr(0664,root,tomcat,0755)
%doc {LICENSE,NOTICE,RELEASE*}
%attr(0755,root,root) %{_bindir}/%{name}-digest
%attr(0755,root,root) %{_bindir}/%{name}-tool-wrapper
%attr(0755,root,root) %{_sbindir}/d%{name}
%attr(0755,root,root) %{_sbindir}/%{name}
%attr(0755,root,root) %{_initrddir}/%{name}
%attr(0644,root,root) %{_systemddir}/%{name}.service
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%attr(0765,root,tomcat) %dir %{basedir}
%attr(0755,root,tomcat) %dir %{confdir}
%defattr(0664,root,tomcat,0770)
%attr(0770,root,tomcat) %dir %{logdir}
%attr(0660,tomcat,tomcat) %{logdir}/catalina.out
%attr(0770,root,tomcat) %dir %{cachedir}
%attr(0770,root,tomcat) %dir %{tempdir}
%attr(0770,root,tomcat) %dir %{workdir}
%defattr(0664,root,tomcat,0775)
%attr(0775,root,tomcat) %dir %{appdir}
%attr(0775,root,tomcat) %dir %{confdir}/Catalina
%attr(0775,root,tomcat) %dir %{confdir}/Catalina/localhost
%attr(0664,tomcat,tomcat) %config(noreplace) %{confdir}/%{name}.conf
%attr(0664,tomcat,tomcat) %config(noreplace) %{confdir}/*.policy
%attr(0664,tomcat,tomcat) %config(noreplace) %{confdir}/*.properties
%attr(0664,tomcat,tomcat) %config(noreplace) %{confdir}/context.xml
%attr(0664,tomcat,tomcat) %config(noreplace) %{confdir}/server.xml
%attr(0660,tomcat,tomcat) %config(noreplace) %{confdir}/tomcat-users.xml
%attr(0664,tomcat,tomcat) %config(noreplace) %{confdir}/web.xml
%dir %{homedir}
%dir %{bindir}
%{bindir}/bootstrap.jar
%{bindir}/catalina-tasks.xml
%{homedir}/lib
%{homedir}/temp
%{homedir}/webapps
%{homedir}/work
%{homedir}/logs
%{homedir}/conf

%files admin-webapps
%defattr(0664,root,tomcat,0755)
%{appdir}/host-manager
%{appdir}/manager

%files docs-webapp
%defattr(-,root,root,-)
%{appdir}/docs

%files javadoc
%defattr(-,root,root,-)
%{_javadocdir}/%{name}

%files jsp-%{jspspec}-api
%defattr(-,root,root,-)
%{_javadir}/%{name}-jsp-%{jspspec}*.jar
%{_javadir}/%{name}-jsp-api.jar
%{_mavenpomdir}/JPP-%{name}-tomcat-jsp-api.pom

%files lib
%defattr(-,root,root,-)
%{libdir}
%{bindir}/tomcat-juli.jar
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/JPP.%{name}-annotations-api.pom
%{_mavenpomdir}/JPP.%{name}-catalina-ha.pom
%{_mavenpomdir}/JPP.%{name}-catalina-tribes.pom
%{_mavenpomdir}/JPP.%{name}-catalina.pom
%{_mavenpomdir}/JPP.%{name}-jasper-el.pom
%{_mavenpomdir}/JPP.%{name}-jasper.pom
%{_mavenpomdir}/JPP.%{name}-tomcat-api.pom
%{_mavenpomdir}/JPP.%{name}-tomcat-juli.pom
%{_mavenpomdir}/JPP.%{name}-tomcat-util.pom
%exclude %{libdir}/%{name}-el-%{elspec}-api.jar

%files servlet-%{servletspec}-api
%defattr(-,root,root,-)
%doc LICENSE
%{_javadir}/%{name}-servlet-%{servletspec}*.jar
%{_javadir}/%{name}-servlet-api.jar
%{_mavendepmapfragdir}/%{name}-servlet-api
%{_mavenpomdir}/JPP-%{name}-tomcat-servlet-api.pom

%files el-%{elspec}-api
%defattr(-,root,root,-)
%doc LICENSE
%{_javadir}/%{name}-el-%{elspec}-api.jar
%{_javadir}/%{name}-el-api.jar
%{libdir}/%{name}-el-%{elspec}-api.jar
%{_mavenpomdir}/JPP-%{name}-tomcat-el-api.pom

%files webapps
%defattr(0644,tomcat,tomcat,0755)
%{appdir}/ROOT
%{appdir}/examples
%{appdir}/sample

