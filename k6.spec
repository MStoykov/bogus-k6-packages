Name: k6
Version: 0.31.1
Release: 2.changerepo
License: LICENSE
Url: https://k6.io/
Summary: Load testing for the 21st century

%description
k6 is a developer centric open source load testing tool for testing the performance of your backend infrastructure. It’s built with Go and JavaScript to integrate well into your development workflow, so you can stay on top of performance without fuzz.

%pre -p /bin/sh
echo -e "\e[32mThe repo you are using for installing k6 is being depracated as a result bintray sunsetting it's service on 1st of May 2021.\e[0m
As a result of that there is now a new repository. In order to upgrade we recommend that you:
1. removing this repo which if you've followed the old installation instructions should be done with 'sudo rm /etc/yum.repos.d/bintray-loadimpact-rpm.repo' if not you shoudl just delete the repo file you created when installing
2. install the new repo 'sudo dnf install https://dl.k6.io/rpm/repo.rpm' as said in https://k6.io/docs/getting-started/installation/#fedora-centos
3(optional). reinstall the package with 'dnf reinstall k6'"
exit 1

%install

%files

%changelog
* Thu Apr 22 2021 Load Impact 
 - package to mention we need to move
